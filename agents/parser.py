
import json
import re
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


_llm = ChatBedrock(
    model="global.anthropic.claude-haiku-4-5-20251001-v1:0"
)

def parse_query(query: str) -> dict:
        """ You are an expert software issue parser.
        """        
        response= _llm.invoke([
            HumanMessage(content=(
                f"""Extract the following from the user query:

                - owner (GitHub username/org)
                - repo (repository name)
                - issue_number (integer)
                Query:
                {query}

                Return ONLY JSON:
                {{
                "owner": "...",
                "repo": "...",
                "issue_number": ...
                }}"""
            ))
        ])
        # Extract JSON from markdown code blocks if present
        content = response.content.strip()
        json_match = re.search(r'```(?:json)?\s*({.*?})\s*```', content, re.DOTALL)
        if json_match:
            content = json_match.group(1)
        return json.loads(content)