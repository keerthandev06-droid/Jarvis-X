"""
==========================================================
Jarvis-X Session Manager
Version : 1.0.0
==========================================================

Purpose:
Maintains interactive sessions such as:
- File Search
- Confirmations
- AI Chat (future)
- Voice Dialogs (future)

Only ONE session can be active at a time.
"""

from dataclasses import dataclass
from typing import Any, Optional


# ==========================================================
# Session Types
# ==========================================================

SESSION_NONE = "none"
SESSION_SEARCH = "search"
SESSION_CONFIRM = "confirm"
SESSION_CHAT = "chat"
SESSION_VOICE = "voice"


# ==========================================================
# Session Object
# ==========================================================

@dataclass
class Session:

    type: str = SESSION_NONE

    data: Any = None

    active: bool = False


# ==========================================================
# Global Session
# ==========================================================

_current = Session()


# ==========================================================
# Start Session
# ==========================================================

def start(session_type: str, data: Any = None):
    """
    Start a new session.
    """

    global _current

    _current = Session(
        type=session_type,
        data=data,
        active=True,
    )


# ==========================================================
# End Session
# ==========================================================

def end():
    """
    End the current session.
    """

    global _current

    _current = Session()


# ==========================================================
# Status
# ==========================================================

def is_active() -> bool:
    """
    Returns True if any session is active.
    """

    return _current.active


def current_type() -> str:
    """
    Returns the active session type.
    """

    return _current.type


# ==========================================================
# Session Data
# ==========================================================

def get_data():
    """
    Returns session data.
    """

    return _current.data


def set_data(data):
    """
    Replace session data.
    """

    _current.data = data


# ==========================================================
# Helpers
# ==========================================================

def is_search() -> bool:
    return (
        _current.active
        and _current.type == SESSION_SEARCH
    )


def is_confirm() -> bool:
    return (
        _current.active
        and _current.type == SESSION_CONFIRM
    )


def is_chat() -> bool:
    return (
        _current.active
        and _current.type == SESSION_CHAT
    )


def is_voice() -> bool:
    return (
        _current.active
        and _current.type == SESSION_VOICE
    )


# ==========================================================
# Debug
# ==========================================================

def info() -> dict:
    """
    Returns the current session state.
    """

    return {
        "active": _current.active,
        "type": _current.type,
        "data": _current.data,
    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("Initial:")
    print(info())

    print()

    start(
        SESSION_SEARCH,
        {
            "query": "resume",
            "results": [1, 2, 3],
        },
    )

    print("Started:")
    print(info())

    print()

    end()

    print("Ended:")
    print(info())