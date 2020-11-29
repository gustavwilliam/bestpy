import platform

from typing import Type


def add_from_class(cls: Type, target_dict: dict) -> None:
    """Adds the methods of the specified class to the target dict, if it doesn't start with '_'."""
    method_names = [name for name in dir(cls) if not name.startswith("_")]  # Only methods that don't start with _
    answer_methods = {name: getattr(cls, name) for name in method_names}
    target_dict.update(answer_methods)


class CodeAnswers:
    """Class for answers that require code execution on every access"""

    def __init__(self):
        pass

    @staticmethod
    def os() -> str:
        name = platform.system()

        # Replacing "Darwin", since it might be confusing for macOS users
        if name == "Darwin":
            name = "macOS"

        return name


answers = {
    # region: Tech
    "language": "Python",
    "package": "Bestpy",
    "phone": ["iPhone", "Nokia", "OnePlus", "Huawei", "Samsung Galaxy", "BlackBerry", "Google Pixel", "Sony Experia"],
    # endregion

    # region: Time
    "year": list(range(2100)),
    "month": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"],
    # endregion
}


add_from_class(CodeAnswers, answers)
