"""
Jarvis-X Resource Resolver
Version: 2.0.0
"""

from core.config.apps import APPS


def resolve(resource: str) -> str:
    """
    Resolve a generic resource into an actual application.
    """

    resource = resource.lower().strip()

    # ----------------------------
    # Browser
    # ----------------------------

    if resource == "browser":
        return APPS["browser"]["personal"]

    if resource == "work_browser":
        return APPS["browser"]["work"]

    if resource == "personal_browser":
        return APPS["browser"]["personal"]

    # ----------------------------
    # Office
    # ----------------------------

    if resource in APPS["office"]:
        return APPS["office"][resource]

    # ----------------------------
    # Direct Keys
    # ----------------------------

    if resource in APPS:
        return APPS[resource]

    # ----------------------------
    # Already an App Name
    # ----------------------------

    return resource