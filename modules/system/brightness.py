"""
==========================================================
Jarvis-X Brightness Manager
Version : 1.0.0
==========================================================
"""

try:
    import screen_brightness_control as sbc
except ImportError:
    sbc = None


def _check():

    if sbc is None:
        raise RuntimeError(
            "screen_brightness_control is not installed.\n"
            "Run:\n"
            "python -m pip install screen-brightness-control"
        )


def get_brightness():

    _check()

    return sbc.get_brightness()[0]


def set_brightness(level):

    _check()

    level = max(
        0,
        min(
            100,
            int(level),
        ),
    )

    sbc.set_brightness(level)

    return level


def increase(step=10):

    current = get_brightness()

    return set_brightness(current + step)


def decrease(step=10):

    current = get_brightness()

    return set_brightness(current - step)


if __name__ == "__main__":

    print(
        get_brightness()
    )