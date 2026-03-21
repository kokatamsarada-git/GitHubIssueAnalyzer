from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


_llm = ChatBedrock(
    model="global.anthropic.claude-haiku-4-5-20251001-v1:0"
)

@tool
def analyze_issue(issue: str) -> str:
        """ You are an expert software issue analyzer.
        Analyze the given GitHub issue and provide insights or suggestions.
        """        
        response= _llm.invoke([
            HumanMessage(content=(
                f"""Analyze the following GitHub issue
                {issue} ::\n\n
                    Return output in this format:
                    Classification: (bug/feature/enhancement)
                    Priority: (low/medium/high)
                    Summary: (concise summary) """
            ))
        ])      
        return response.content