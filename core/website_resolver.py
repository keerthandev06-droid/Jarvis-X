"""
Jarvis-X Website Resolver
Version: 1.0.0
"""

from core.config.websites import WEBSITES


def resolve_website(name: str):
    """
    Resolve a website name.

    Returns:
        dict | None
    """

    name = name.lower().strip()

    # Exact match
    if name in WEBSITES:
        return WEBSITES[name]

    # Partial match
    for website, details in WEBSITES.items():
        if website in name:
            return details

    return None