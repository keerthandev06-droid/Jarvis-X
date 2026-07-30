"""
Jarvis-X Application Scanner
Scans:
- Windows Start Menu shortcuts (.lnk)
- Windows Store / UWP Apps (Get-StartApps)
"""

import os
import subprocess

from modules.app_database import save_app

START_MENU_PATHS = (
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    ),
)


def scan_start_menu():
    """
    Scan Windows Start Menu shortcuts.
    """

    total = 0

    for base in START_MENU_PATHS:

        if not os.path.exists(base):
            continue

        print(f"Scanning Start Menu: {base}")

        for root, _, files in os.walk(base):

            for file in files:

                if not file.lower().endswith(".lnk"):
                    continue

                name = os.path.splitext(file)[0]

                save_app(
                    name=name,
                    path=os.path.join(root, file),
                    app_type="lnk",
                )

                total += 1

    print(f"Indexed {total} Start Menu shortcuts.")


def scan_store_apps():
    """
    Scan Windows Store (UWP/MSIX) applications.
    """

    print("Scanning Windows Store apps...")

    total = 0

    try:

        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-StartApps | Select-Object Name,AppID"
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        lines = result.stdout.splitlines()

        for line in lines:

            line = line.strip()

            if (
                not line
                or line.startswith("Name")
                or line.startswith("----")
            ):
                continue

            parts = line.rsplit(maxsplit=1)

            if len(parts) != 2:
                continue

            name, appid = parts

            if "!" not in appid:
                continue

            save_app(
                name=name.strip(),
                path=appid.strip(),
                app_type="store",
            )

            total += 1

    except Exception as e:
        print(f"Store app scan failed: {e}")

    print(f"Indexed {total} Store apps.")


def scan_apps():
    """
    Main application scanner.
    """

    scan_start_menu()
    scan_store_apps()