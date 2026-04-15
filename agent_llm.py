from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools import *

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tools = [scan_local_repos, get_repo_status, get_remote_status, sync_repo, create_repo]

SYSTEM_PROMPT = """
You are a GitHub management AI agent.

Your responsibilities:
- Audit repositories
- Detect version drift between local and remote
- Recommend or execute fixes
- Keep responses structured and concise

Rules:
- Always compare local vs remote commits
- If drift exists, suggest or perform sync
- If repo missing remotely, suggest creation
"""


def build_agent():
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        agent_kwargs={"system_message": SYSTEM_PROMPT},
    )
