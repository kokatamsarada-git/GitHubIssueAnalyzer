
import os
import json
import traceback
from langchain.tools import tool
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
#from langchain_mcp_adapters.tools import mcp_tools

import requests

_llm = ChatBedrock(
    model="global.anthropic.claude-haiku-4-5-20251001-v1:0"
)
token= os.getenv("GITHUB_PAT_TOKEN")

gitHubTool = MultiServerMCPClient(
    {
        "github": {
            "url": "https://api.githubcopilot.com/mcp/",
            "transport": "http",
            "headers": {
                "Authorization": f"Bearer {token}",
            },
        }
    }
)

#@tool
async def fetch_git_hub_tool():  
    async with gitHubTool.session("github") as session:
        #tools = await mcp_tools(session)  
        tools = await gitHubTool.get_tools()      

        github_tool = next(
            (t for t in tools if t.name == "list_issues"),
            None
        )

        if github_tool is None:
            raise RuntimeError("GitHub tool 'list_issues' not found")

        print("Tool schema:", github_tool.args)

        return github_tool


@tool
async def fetch_issue(repo_name: str) -> str: 
    """Fetch a GitHub issues (title + description).
    """

    if "/" not in repo_name:
        return "❌ Invalid repo format. Use 'owner/repo'"

    owner, repo = repo_name.split("/")
    #print(f"Fetching issues for {owner}/{repo}...")   
    async with gitHubTool.session("github") as session:
            #tools = await mcp_tools(session)
            tools = await gitHubTool.get_tools()
            github_tool = next(
                (t for t in tools if t.name == "list_issues"),
                None
            )

            if github_tool is None:
                return "GitHub tool 'list_issues' not found"

            print("TOOL ARGS:", github_tool.args)

            raw_result = await github_tool.ainvoke({
                "owner": owner,
                "repo": repo,
                "state": "OPEN",
                "perPage": 10
            })

    formatted_input = json.dumps(raw_result, indent=2)

    response = _llm.invoke([
        HumanMessage(
            content=f"Format these GitHub issues clearly:\n{formatted_input}"
        )
    ])

    return f"ISSUES_DATA:{response.content}. Use this data for email notifications."