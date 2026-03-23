from dotenv import load_dotenv

load_dotenv()

from langchain.tools import tool
from tavily import TavilyClient

tavily = TavilyClient()


# ── Tool 1: Web Search ────────────────────────────────────────
@tool
def search_web(query: str) -> str:
    """Search the web for current information
    about jobs, skills, companies and AI trends."""

    results = tavily.search(
        query=query,
        max_results=3
    )
    output = []
    for r in results['results']:
        output.append(f"Title: {r['title']}")
        output.append(f"Content: {r['content'][:200]}")
        output.append("---")
    return "\n".join(output)


# ── Tool 2: Job Search ────────────────────────────────────────
@tool
def search_jobs(role: str, location: str = "India") -> str:
    """Search for current job openings for a
    specific role and location."""

    query = f"{role} jobs {location} 2026 hiring"
    results = tavily.search(query=query, max_results=3)
    output = []
    for r in results['results']:
        output.append(f"• {r['title']}")
        output.append(f"  {r['content'][:150]}")
        output.append("")
    return "\n".join(output)


# ── Tool 3: Skills Research ───────────────────────────────────
@tool
def research_skills(role: str) -> str:
    """Research what skills are required
    for a specific job role in 2026."""

    query = f"skills required {role} India 2026"
    results = tavily.search(query=query, max_results=3)
    output = []
    for r in results['results']:
        output.append(r['content'][:300])
        output.append("---")
    return "\n".join(output)


# ── Tool 4: AI News ───────────────────────────────────────────
@tool
def get_ai_news(topic: str = "GenAI") -> str:
    """Get latest AI industry news and trends."""

    query = f"latest {topic} news India 2026"
    results = tavily.search(query=query, max_results=3)
    output = []
    for r in results['results']:
        output.append(f"• {r['title']}")
        output.append(f"  {r['content'][:200]}")
        output.append("")
    return "\n".join(output)