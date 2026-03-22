# GitHub Issue Analyzer and Email Notifier

An AI-powered application that analyzes GitHub issues using natural language processing, classifies them by priority and type, and can send email notifications. Built with LangGraph, LangChain, and AWS Bedrock.

## 🎯 Features

- **🔍 GitHub Issue Analysis**: Fetch and analyze open issues from any GitHub repository
- **🤖 AI-Powered Classification**: Automatically classify issues as bugs, features, or enhancements using Claude AI
- **⚡ Priority Assessment**: Determine priority levels (low, medium, high) for each issue
- **📧 Email Notifications**: Send analysis reports directly to your email
- **🗣️ Natural Language Interface**: Describe what you need in plain English
- **💬 Conversational CLI**: Interactive command-line interface for easy interaction
- **🎨 Streamlit Web UI**: Beautiful web interface for non-technical users

## 📋 Prerequisites

- Python 3.8+
- AWS Account with Bedrock access (Claude Haiku model)
- GitHub Personal Access Token (PAT)
- Email service configured (Gmail, SendGrid, etc.)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone repository
git clone <repository-url>
cd "GitHub Issue Analyzer and Email Notifier"

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create `.env` file in the project root:

```env
# AWS Bedrock
AWS_DEFAULT_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret

# GitHub
GITHUB_PAT_TOKEN=ghp_xxxxxxxxxxxxx
GITHUB_REPO_OWNER=your_username
GITHUB_REPO_NAME=your_repo

# Email
EMAIL_TO=your_email@gmail.com
```

### 3. Run Application

**CLI Mode:**
```bash
python cli.py
```

**Web Interface:**
```bash
streamlit run app.py
```

## 📖 Usage Examples

### Command Line

```
Github issue analyser and email notifier (type 'quit' to exit)

You: find issues from kokatamsarada-git/DellProjChatBot
Agent: [Fetches and analyzes open issues]

You: analyze all issues
Agent: [Provides classification, priority, and summary for each]

You: send email with analysis
Agent: [Sends detailed report to configured email]

You: quit
```

### Example Queries

- `"Show me all open issues in my repository"`
- `"Analyze issues from kokatamsarada-git/my-repo"`
- `"What are the critical bugs?"`
- `"Send me an email with issue summary"`

## 📁 Project Structure

```
.
├── agents/
│   ├── __init__.py
│   └── analyzer.py          # Issue analysis using Claude AI
├── graph/
│   ├── __init__.py
│   ├── graph_builder.py     # LangGraph workflow builder
│   ├── nodes.py             # Agent node definitions
│   ├── prompt.py            # System prompts for AI
│   └── state.py             # State management
├── tools/
│   ├── __init__.py
│   ├── github_tool.py       # GitHub REST API integration
│   └── gmail_tool.py        # Email sending
├── cli.py                   # Command-line interface
├── app.py                   # Streamlit web interface
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (gitignored)
└── README.md               # This file
```

## 🔧 How It Works

```
User Query
    ↓
Parse Query (extract owner, repo)
    ↓
Fetch GitHub Issues (REST API)
    ↓
Analyze with Claude AI
    ↓
Generate Report
    ↓
Send Email (optional)
```

### Key Components

**analyzer.py** - Analyzes issues and provides:
- Classification: bug | feature | enhancement
- Priority: low | medium | high
- Summary and recommendations

**github_tool.py** - Fetches data using GitHub API:
- Retrieves open issues
- Gets issue details (title, description, labels)
- Formats data for AI analysis

**gmail_tool.py** - Sends email notifications:
- Formats analysis as email
- Sends to configured recipient
- Includes detailed issue reports

## 🔑 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `AWS_DEFAULT_REGION` | AWS region for Bedrock | `us-east-1` |
| `AWS_ACCESS_KEY_ID` | AWS IAM access key | `AKIA...` |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key | `wJal...` |
| `GITHUB_PAT_TOKEN` | GitHub personal access token | `ghp_...` |
| `GITHUB_REPO_OWNER` | Default GitHub owner | `kokatamsarada-git` |
| `GITHUB_REPO_NAME` | Default repository | `DellProjChatBot` |
| `EMAIL_TO` | Recipient email address | `user@gmail.com` |

### Getting Credentials

**GitHub PAT:**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Select `repo` scope
4. Copy and save token

**AWS Credentials:**
1. Go to AWS IAM Console
2. Create IAM user with Bedrock permissions
3. Generate access keys
4. Save to `.env`

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| langgraph | >=0.2 | Agent workflow orchestration |
| langchain-aws | >=0.2 | AWS Bedrock integration |
| langchain-core | >=0.3 | LangChain core utilities |
| boto3 | >=1.34 | AWS SDK |
| python-dotenv | >=1.0 | Environment variable loading |
| streamlit | >=1.35 | Web UI framework |
| langchain | - | LLM framework |
| langchain-mcp-adapters | >=0.1 | MCP adapters |

## ⚙️ Configuration

### AWS Bedrock Setup

```bash
# Install AWS CLI
pip install awscli

# Configure credentials
aws configure
```

### GitHub API Limits

- Public repositories: 60 requests/hour (unauthenticated)
- Authenticated: 5,000 requests/hour
- Recommended: Use authenticated token for higher limits

## 📊 AI Model

- **Model**: Claude Haiku (via AWS Bedrock)
- **Region**: us-east-1
- **Vision**: Not supported (text-only)
- **Max Tokens**: Limited by model

## 🐛 Troubleshooting

### AWS Authentication Error
```
ValidationError: Could not load credentials
```
**Solution**: 
- Verify `.env` has correct AWS keys
- Check AWS IAM user has Bedrock permissions
- Ensure region is set to `us-east-1`

### GitHub 404 Error
```
GitHub API Error: 404 - Not Found
```
**Solution**:
- Verify repository name is correct
- Check owner/username spelling
- Ensure repo is accessible with your PAT token

### Email Not Sending
```
Error sending email
```
**Solution**:
- Verify `EMAIL_TO` is set in `.env`
- Check email service permissions
- Review email service logs

### ModuleNotFoundError
```
ModuleNotFoundError: No module named 'langchain_aws'
```
**Solution**:
```bash
pip install -r requirements.txt
pip install -U langchain langchain-aws langchain-core
```

## 🚀 Advanced Usage

### Custom Analysis Prompts

Edit `graph/prompt.py` to customize AI behavior:

```python
SYSTEM_PROMPT = """
Your custom instructions here...
"""
```

### Adding New Tools

Create new tool in `tools/` directory:

```python
from langchain.tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """Tool description."""
    # Implementation
    return result
```

Register in `agents/__init__.py`:

```python
from tools.my_tool import my_custom_tool

tools = [
    my_custom_tool,
    # ... other tools
]
```

## 📝 Example Workflow

1. **User Input**: "Analyze issues from my GitHub repo"
2. **Query Parsing**: Extract owner and repo name
3. **Issue Fetching**: Get all open issues via GitHub API
4. **AI Analysis**: Claude classifies each issue
5. **Report Generation**: Format results
6. **Email**: Optional send via email
7. **Response**: Display to user

## 🔐 Security Best Practices

- ✅ Never commit `.env` file (already in .gitignore)
- ✅ Use GitHub PAT sparingly
- ✅ Rotate AWS credentials regularly
- ✅ Use IAM policies with least privilege
- ✅ Keep dependencies updated

## 🤝 Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📈 Roadmap

- [ ] Slack integration for notifications
- [ ] Multiple repository support
- [ ] Custom classification rules
- [ ] Trending issues analytics
- [ ] Automated issue assignment
- [ ] GitHub webhook real-time updates
- [ ] Support for GitLab
- [ ] Database storage of analyses

## 📄 License

This project is licensed under the MIT License.

## 💬 Support

For issues or questions:
1. Check [Troubleshooting](#-troubleshooting) section
2. Review error messages carefully
3. Create an issue in the repository

## 👤 Author

Sarada - DellProjChatBot Exercise

---

**Last Updated**: March 22, 2026  
**Version**: 1.0.0
