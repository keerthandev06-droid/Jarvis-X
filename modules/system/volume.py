"""
==========================================================
Jarvis-X Volume Manager
Version : 3.0.0
==========================================================
"""

from pycaw.pycaw import AudioUtilities


def _endpoint():

    speakers = AudioUtilities.GetSpeakers()

    return speakers.EndpointVolume


def mute():

    _endpoint().SetMute(1, None)

    print("✅ Muted")

    return True


def unmute():

    _endpoint().SetMute(0, None)

    print("✅ Unmuted")

    return True


def volume_up(step=5):

    volume = _endpoint()

    current = volume.GetMasterVolumeLevelScalar()

    current = min(1.0, current + (step / 100))

    volume.SetMasterVolumeLevelScalar(current, None)

    print(f"✅ Volume : {int(current*100)}%")

    return True


def volume_down(step=5):

    volume = _endpoint()

    current = volume.GetMasterVolumeLevelScalar()

    current = max(0.0, current - (step / 100))

    volume.SetMasterVolumeLevelScalar(current, None)

    print(f"✅ Volume : {int(current*100)}%")

    return True


def set_volume(level):

    level = max(0, min(100, int(level)))

    _endpoint().SetMasterVolumeLevelScalar(
        level / 100,
        None,
    )

    print(f"✅ Volume : {level}%")

    return True