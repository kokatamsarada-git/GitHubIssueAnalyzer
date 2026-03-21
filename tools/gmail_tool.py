
import os
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient

composio = os.getenv("COMPOSIO_API_KEY")

@tool
async def send_email(subject: str, body: str) -> str:
    """Send an email with bug analysis by formating the given subject and body."""
    print(f"Preparing to send email with subject: {subject}")
    print(f"Email body:\n{body}")
    composioTool = MultiServerMCPClient(
        {
            "composio": {
                "url": os.getenv("COMPOSOI_URL"),
                "transport": "streamable_http",
                "headers": {
                    "x-api-key": composio,
                },
            }
        }
    )
    tools = await composioTool.get_tools()
    print(tools)
    gmail_tools = {tool.name: tool for tool in tools}
    tool = gmail_tools.get("GMAIL_SEND_EMAIL")
    response = await tool.ainvoke({
            "to": os.getenv("EMAIL_TO"),
            "subject": subject,
            "body": body
        }
    )

    return "Email sent successfully" if response else "Email failed"