"""
==========================================================
Jarvis-X Command Result
Version : 1.0.0
==========================================================

Purpose:
Provides a standard result object returned by every
Jarvis-X command handler.
"""

from dataclasses import dataclass
from typing import Any


# ==========================================================
# Command Result
# ==========================================================

@dataclass(slots=True)
class CommandResult:
    """
    Standard return object for all handlers.
    """

    success: bool
    message: str = ""
    data: Any = None

    @classmethod
    def ok(cls, message: str = "", data: Any = None):
        """
        Successful result.
        """
        return cls(
            success=True,
            message=message,
            data=data,
        )

    @classmethod
    def fail(cls, message: str = "", data: Any = None):
        """
        Failed result.
        """
        return cls(
            success=False,
            message=message,
            data=data,
        )

    def __bool__(self):
        """
        Allows:

        if result:
            ...
        """

        return self.success


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    success = CommandResult.ok(
        "Opened Chrome"
    )

    failure = CommandResult.fail(
        "Chrome not found"
    )

    print(success)
    print(failure)

    if success:
        print("Success")

    if not failure:
        print("Failure")