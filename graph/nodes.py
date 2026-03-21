
import os
from langchain_aws import ChatBedrock
from langchain_core.tools import tool

from agents.analyzer import analyze_issue
from agents import tools as all_tools
from graph.prompt import SYSTEM_PROMPT
from tools.github_tool import fetch_issue
from tools.gmail_tool import send_email
from graph.state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage

_llm = ChatBedrock(
    model="global.anthropic.claude-haiku-4-5-20251001-v1:0"
)

_llm_with_tools = _llm.bind_tools(all_tools)


def agent_node(state):
    messages = state["messages"]

    messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = _llm_with_tools.invoke(messages)

    return {"messages": [response]}

# def fetch_issue_node(state: AgentState) -> AgentState:
#     issue_text = fetch_issue(
#         owner=state["owner"],
#         repo=state["repo"],
#         issue_number=state["issue_number"]
#     )

#     return {
#         **state,
#         "issue": issue_text
#     }


# def analyze_node(state: AgentState) -> AgentState:
#     analysis = analyze_issue(state["issue"])

#     return {
#         **state,
#         "analysis": analysis
#     }


# def email_node(state: AgentState) -> AgentState:
#     subject = "GitHub Issue Analysis Report"
#     body = f"""
#             Issue:
#             {state['issue']}

#             Analysis:
#             {state['analysis']}
#             """

#     status = send_email(
#         subject=subject,
#         body=body
#     )

#     return {
#         **state,
#         "email_status": status
#     }
