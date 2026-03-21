from langgraph.graph import MessagesState


class AgentState(MessagesState):
    """State class for agents to carry the coversation history and other relevant information."""
    pass


# from typing import TypedDict

# class AgentState(TypedDict):
#     user_query: str
#     owner: str
#     repo: str
#     issue_number: int
#     issue: str
#     analysis: str
#     email_status: str