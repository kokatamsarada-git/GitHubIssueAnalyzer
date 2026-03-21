from langgraph.graph import START, StateGraph, END
from graph.state import AgentState
from graph.nodes import agent_node
from langgraph.prebuilt import ToolNode, tools_condition
from agents import tools as all_tools

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(all_tools))

    builder.add_edge(START, "agent")

    builder.add_conditional_edges("agent", tools_condition)

    builder.add_edge("tools", "agent")

    return builder.compile()


graph = build_graph()