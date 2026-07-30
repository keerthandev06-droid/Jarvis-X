"""
==========================================================
Jarvis-X Screenshot Manager
Version : 2.0.0
==========================================================
"""

import os
from datetime import datetime
from PIL import ImageGrab


SCREENSHOT_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Pictures",
    "Jarvis Screenshots",
)


def take_screenshot():
    """
    Capture full screen and save it.
    Returns True on success.
    """

    try:

        os.makedirs(
            SCREENSHOT_FOLDER,
            exist_ok=True,
        )

        filename = datetime.now().strftime(
            "Screenshot_%Y%m%d_%H%M%S.png"
        )

        filepath = os.path.join(
            SCREENSHOT_FOLDER,
            filename,
        )

        image = ImageGrab.grab(all_screens=True)

        image.save(filepath)

        print(f"✅ Screenshot saved:\n{filepath}")

        return True

    except Exception as e:

        print(f"❌ Screenshot Error: {e}")

        return False


if __name__ == "__main__":

    take_screenshot()