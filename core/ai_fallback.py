"""
==========================================================
Jarvis-X AI Fallback Engine
Version : 1.0.0
==========================================================

Purpose:
Handles AI failures gracefully.

If Gemini is unavailable, rate-limited,
or returns an error, this module formats
the available web search results instead
of exposing raw API errors.
"""

import re


def _clean(text: str) -> str:
    """
    Clean extra whitespace.
    """

    if not text:
        return ""

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def _extract_title(web_results: str) -> str:
    """
    Extract first result title.
    """

    match = re.search(
        r"Title:\s*(.+)",
        web_results,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(1).strip()

    return "Live Search Result"


def _extract_url(web_results: str) -> str:
    """
    Extract source URL.
    """

    match = re.search(
        r"URL:\s*(.+)",
        web_results,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(1).strip()

    return ""


def _extract_content(web_results: str) -> str:
    """
    Extract article preview.
    """

    match = re.search(
        r"Content:\s*(.*)",
        web_results,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if match:
        return _clean(match.group(1))

    return _clean(web_results)


def fallback_response(
    ai_response: str,
    web_results: str,
) -> str:
    """
    Return AI response if successful.

    Otherwise generate a clean
    response using web search.
    """

    if ai_response:

        lower = ai_response.lower()

        failures = (
            "429",
            "resource_exhausted",
            "quota",
            "rate limit",
            "ai error",
            "timed out",
            "connection",
            "network",
        )

        if not any(item in lower for item in failures):
            return ai_response

    title = _extract_title(web_results)

    url = _extract_url(web_results)

    content = _extract_content(web_results)

    if len(content) > 1200:
        content = content[:1200] + "..."

    response = f"""
{title}

{content}

Source:
{url}
"""

    return response.strip()


if __name__ == "__main__":

    sample_ai = "AI Error: 429 RESOURCE_EXHAUSTED"

    sample_web = """
Title:
Jana Nayagan Box Office Collection Day 6

URL:
https://example.com

Content:
Worldwide collection crossed ₹246 Cr.
India gross reached ₹167 Cr.
Day 6 collection ₹8 Cr.
"""

    print(
        fallback_response(
            sample_ai,
            sample_web,
        )
    )