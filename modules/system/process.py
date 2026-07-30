"""
==========================================================
Jarvis-X Process Manager
Version : 2.0.0
==========================================================
"""

import subprocess
import psutil


def list_processes():

    return sorted(
        {
            p.info["name"]
            for p in psutil.process_iter(["name"])
            if p.info["name"]
        }
    )


def close_process(name: str):

    if not name:
        return False

    name = name.lower().replace(".exe", "")

    closed = False

    for proc in psutil.process_iter(["name"]):

        try:

            proc_name = (
                proc.info["name"] or ""
            ).lower().replace(".exe", "")

            if proc_name == name:

                proc.terminate()

                try:
                    proc.wait(timeout=3)
                except Exception:
                    proc.kill()

                closed = True

        except Exception:
            pass

    if closed:
        print(f"✅ Closed {name}")
    else:
        print(f"❌ {name} is not running")

    return closed


def kill_process(name: str):

    if not name:
        return False

    name = name.lower().replace(".exe", "")

    killed = False

    for proc in psutil.process_iter(["name"]):

        try:

            proc_name = (
                proc.info["name"] or ""
            ).lower().replace(".exe", "")

            if proc_name == name:

                proc.kill()

                killed = True

        except Exception:
            pass

    return killed


def task_manager():

    subprocess.Popen("taskmgr")

    return True


if __name__ == "__main__":

    print(list_processes()[:20])