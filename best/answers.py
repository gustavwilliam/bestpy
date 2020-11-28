import platform

from typing import List


def language() -> List[str]:
    return [
        "Python",
    ]


def package() -> List[str]:
    return [
        "Bestpy",
    ]


def os() -> List[str]:
    name = platform.system()

    # Replacing "Darwin", since it might be confusing for macOS users
    if name == "Darwin":
        name = "macOS"

    return [
        name,
    ]


def year() -> List[int]:
    return list(range(2100))
