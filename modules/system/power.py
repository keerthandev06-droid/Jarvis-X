"""
==========================================================
Jarvis-X Power Manager
Version : 1.0.0
==========================================================
"""

import ctypes
import os


def shutdown(delay: int = 0):
    """
    Shutdown Windows.
    """
    os.system(f"shutdown /s /t {delay}")


def restart(delay: int = 0):
    """
    Restart Windows.
    """
    os.system(f"shutdown /r /t {delay}")


def cancel_shutdown():
    """
    Cancel scheduled shutdown/restart.
    """
    os.system("shutdown /a")


def lock():
    """
    Lock Windows.
    """
    ctypes.windll.user32.LockWorkStation()


def logoff():
    """
    Log off current user.
    """
    os.system("shutdown /l")


def sleep():
    """
    Put Windows to sleep.
    """
    ctypes.windll.powrprof.SetSuspendState(
        False,
        True,
        False,
    )


POWER_COMMANDS = {
    "shutdown": shutdown,
    "restart": restart,
    "cancel_shutdown": cancel_shutdown,
    "lock": lock,
    "sleep": sleep,
    "logoff": logoff,
}


if __name__ == "__main__":

    print("Jarvis-X Power Manager")

    print()

    print(POWER_COMMANDS.keys())