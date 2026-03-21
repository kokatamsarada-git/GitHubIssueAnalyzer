from agents.analyzer import analyze_issue
from tools.github_tool import fetch_issue
from tools.gmail_tool import send_email


tools = [
    analyze_issue,
    fetch_issue,
    send_email
    ]