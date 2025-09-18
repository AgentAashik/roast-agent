"""
roast_agent.py
LangChain-based AI agent that roasts users using their own social media data
(provided by the company). 

This is a fun, entertainment-only agent:
- Pulls mock user data (bio, posts, likes)
- Generates a playful roast
- Keeps tone humorous but not offensive

Usage:
    python roast_agent.py --user_id 12345
"""

import argparse
import json
import random
from typing import Dict

from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


# ----------------------------
# Mock API / Data Loader
# ----------------------------
def fetch_user_data(user_id: str) -> Dict:
    """
    Simulate fetching open social media data for the user.
    In production: call the company's API instead of loading static data.
    """
    # Mock dataset for demo
    data = {
        "id": user_id,
        "bio": "Tech enthusiast. Gym once a month. Coffee is my personality.",
        "posts": [
            "Just did a 5K run… took 3 hours but worth it.",
            "Why do I always burn toast?",
            "Can’t believe I stayed up till 4am watching cat videos.",
        ],
        "likes": ["meme pages", "coffee shops", "crypto gurus"],
    }
    return data


def format_user_data(user_data: Dict) -> str:
    """Convert user data dict into roast-friendly text context."""
    return json.dumps(user_data, indent=2)


# ----------------------------
# Roast Tool
# ----------------------------
def roast_user(user_id: str) -> str:
    """Fetch user data and let the LLM roast them playfully."""
    data = fetch_user_data(user_id)
    context = format_user_data(data)

    roast_prompt = PromptTemplate(
        input_variables=["context"],
        template="""
You are a witty stand-up comedian. Roast the person below in a lighthearted,
sarcastic but safe way. Avoid anything offensive — keep it playful and clever.

Here’s their social media data:
{context}

Now write a roast (3–5 sentences, max 100 words). Make it personal, funny, and creative.
""",
    )

    llm = OpenAI(temperature=0.9)  # Or Gemini via LangChain
    roast_text = llm(roast_prompt.format(context=context))
    return roast_text


# ----------------------------
# LangChain Agent Setup
# ----------------------------
def build_agent():
    """Create a LangChain agent with the roast tool."""
    llm = OpenAI(temperature=0.9)
    roast_tool = Tool(
        name="RoastTool",
        func=roast_user,
        description="Use this to roast a user given their social media data.",
    )
    agent = initialize_agent(
        tools=[roast_tool],
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    return agent


# ----------------------------
# CLI Runner
# ----------------------------
def run(user_id: str):
    agent = build_agent()
    print("🔥 Generating roast...\n")
    result = agent.run(f"Roast the user with ID {user_id}")
    print("\n--- Roast Result ---\n")
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roast Agent (LangChain)")
    parser.add_argument("--user_id", required=True, help="User ID to roast")
    args = parser.parse_args()
    run(args.user_id)
