import platform


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
    "os": CodeAnswers.os,
    "phone": ["iPhone", "Nokia", "OnePlus", "Huawei", "Samsung Galaxy", "BlackBerry", "Google Pixel", "Sony Experia"],
    # endregion

    # region: Time
    "year": list(range(2100)),
    "month": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"],
    # endregion
}
