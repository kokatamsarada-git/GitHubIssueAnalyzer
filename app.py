import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from graph.graph_builder import graph

st.title("GIT Hub Analysis - AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "display_history" not in st.session_state:
    st.session_state.display_history = []



for role, content in st.session_state.display_history:
    with st.chat_message(role):
        st.write(content)


async def run_agent_stream(messages):
    """Stream tokens from the graph using astream_events."""
    full_response = ""
    placeholder = st.empty()

    async for event in graph.astream_events(
        {"messages": messages},
        version="v2",
    ):
        kind = event["event"]

        # Token-level streaming from the LLM inside the agent node
        if kind == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            content = chunk.content

            # content can be str or list of content blocks
            if isinstance(content, list):
                text = "".join(
                    block.get("text", "") if isinstance(block, dict) else str(block)
                    for block in content
                )
            else:
                text = content or ""

            # Skip tool-call-only chunks (no text)
            if text:
                full_response += text
                placeholder.markdown(full_response + "▌")

        # Show tool execution status
        elif kind == "on_tool_start":
            tool_name = event.get("name", "tool")
            placeholder.markdown(full_response + f"\n\n⏳ *Running {tool_name}...*")

    placeholder.markdown(full_response)
    return full_response


if prompt := st.chat_input("Ask about GIT Hub name or repository name, email etc..."):
    st.chat_message("user").write(prompt)
    st.session_state.display_history.append(("user", prompt))

    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant"):
        full_response = asyncio.run(run_agent_stream(st.session_state.messages))

        answer_lower = full_response.lower()

    st.session_state.messages.append(AIMessage(content=full_response))

