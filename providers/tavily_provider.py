"""
==========================================================
Jarvis-X Tavily Provider
Version : 1.0.0
==========================================================
"""

import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

API_KEY = os.getenv("TAVILY_API_KEY")

if not API_KEY:
    raise RuntimeError("TAVILY_API_KEY not found.")

client = TavilyClient(api_key=API_KEY)


def search(query: str, max_results: int = 5):
    """
    Search the web using Tavily.

    Returns:
        dict
    """

    try:

        result = client.search(
            query=query,
            max_results=max_results,
            search_depth="advanced",
        )

        return result

    except Exception as e:

        return {
            "error": str(e)
        }


if __name__ == "__main__":

    while True:

        q = input("\nSearch : ")

        if q.lower() == "exit":
            break

        result = search(q)

        print(result)