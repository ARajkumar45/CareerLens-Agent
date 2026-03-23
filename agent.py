from dotenv import load_dotenv

load_dotenv()

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from tools import search_web, search_jobs, research_skills, get_ai_news

model = ChatNVIDIA(model="meta/llama-3.3-70b-instruct")

agent = create_agent(
    model=model,
    tools=[search_web, search_jobs, research_skills, get_ai_news],
    checkpointer=InMemorySaver(),
    system_prompt="""You are CareerLens AI Agent — 
    an expert AI career coach for Indian tech 
    job market 2026.

    You help users with:
    - Finding GenAI/AI Engineer job openings
    - Researching required skills for roles  
    - Latest AI industry news and trends
    - Career transition advice

    Always be specific, helpful and encouraging.
    Use your tools to find current information.
    Remember conversation history for personalised advice.
    Keep responses clear and actionable."""
)


def chat(message: str, thread_id: str = "1"):
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke(
        {"messages": [HumanMessage(content=message)]},
        config
    )
    return response['messages'][-1].content