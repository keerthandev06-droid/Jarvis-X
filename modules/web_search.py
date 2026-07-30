"""
==========================================================
Jarvis-X Web Search Module
Version : 2.0.0
==========================================================
"""

from providers.tavily_provider import search


def search_web(query: str, max_results: int = 5) -> str:
    """
    Search the web using Tavily and return formatted results.
    """

    if not query:
        return "No search query provided."

    result = search(query, max_results=max_results)

    if "error" in result:
        return f"Search Error: {result['error']}"

    results = result.get("results", [])

    if not results:
        return "No results found."

    formatted = []

    for index, item in enumerate(results, start=1):

        title = item.get("title", "No Title")
        url = item.get("url", "")
        content = item.get("content", "")

        formatted.append(
            f"""
==================================================
Result {index}

Title:
{title}

URL:
{url}

Content:
{content}
"""
        )

    return "\n".join(formatted)


def search_answer(query: str):
    """
    Return Tavily's direct answer if available.
    """

    result = search(query, max_results=5)

    if "error" in result:
        return None

    return result.get("answer")


def print_results(query: str):
    """
    Pretty-print search results.
    """

    print("\nSearching...")
    print("=" * 60)

    print(search_web(query))

    print("=" * 60)


if __name__ == "__main__":

    print("Jarvis-X Web Search")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Search : ").strip()

        if query.lower() == "exit":
            break

        print_results(query)