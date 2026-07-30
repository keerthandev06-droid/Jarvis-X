"""
==========================================================
Jarvis-X Conversation Memory
Version : 2.0.0
==========================================================
"""

from config import MAX_CONVERSATION_MESSAGES


# ==========================================================
# Memory Storage
# ==========================================================

_conversation = []


# ==========================================================
# Add Message
# ==========================================================

def add_message(role: str, content: str):
    """
    Add a message to the conversation history.
    """

    if not content:
        return

    role = role.lower().strip()

    if role == "assistant":
        role = "model"

    if role not in ("user", "model"):
        raise ValueError(f"Invalid role: {role}")

    content = str(content).strip()

    if not content:
        return

    # Avoid duplicate consecutive messages
    if _conversation:

        last = _conversation[-1]

        if (
            last["role"] == role
            and last["content"] == content
        ):
            return

    _conversation.append(
        {
            "role": role,
            "content": content,
        }
    )

    if len(_conversation) > MAX_CONVERSATION_MESSAGES:
        _conversation.pop(0)


# ==========================================================
# Get Messages
# ==========================================================

def get_messages():
    """
    Return conversation history.
    """

    return _conversation.copy()


# ==========================================================
# Clear Memory
# ==========================================================

def clear_memory():
    """
    Remove every stored message.
    """

    _conversation.clear()


# ==========================================================
# Count
# ==========================================================

def message_count():
    """
    Return total stored messages.
    """

    return len(_conversation)