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
    "programming_language": "Python",
    "pep": [0, 1, 5, 7, 8, 10, 11, 387, 20, 13, 101, 257, 287, 8016, 8000, 8002, 8102, 484],
    "package": "Bestpy",
    "phone": ["iPhone", "Nokia", "OnePlus", "Huawei", "Samsung Galaxy", "BlackBerry", "Google Pixel", "Sony Experia"],
    "company": ["Apple", "Samsung", "Nokia", "Google", "Facebook", "Microsoft", "Sony", "Huawei", "IBM", "Intel",
                "Adobe", "Cisco", "Dell", "Oracle", "Klurio"],
    "ide": ["PyCharm", "Thonny", "Spyder", "Atom", "VSCode", "Sublime Text", "Vim", "NeoVim", "Emacs", "Doom Emacs" "Vi", "Nano",
            "Notepad", "IDLE", "Notepad++", "Elvis", "TextEdit", "gedit"],
    "developer": ["Guido van Rossum", "Vestergurkan", "Gustav", "Dennis Ritchie", "Bjarne Stroustrup",
                  "James Gosling", "Linus Torvalds", "Anders Hejlsberg", "Brian Kernighan", "Ken Thompson",
                  "Donald Knuth", "Steve Wozniak", "Richard Stallman"],
    # endregion

    # region: Education
    "subject": ["computer science", "biology", "maths", "chemistry", "physics", "social sciences",
                "natural sciences", "music", "language", "geography", "history", "dance", "design",
                "physical education", "religion", "design", "psychology", "sociology", "health", "physiology"],
    "teacher_name": ["Dave", "Mary", "Frank"],
    "grade": "A",
    "gpa": [4.0, 5.0],
    "enter": 99.9,
    "gcse": 9,
    "school": ["Harvard University", "MIT", "Stanford University", "Oxford University", "Yale University", "Chalmers",
                "KTH", "Princeton University", "University of Michigan", "Cornell University", "TU Delft",
                "UC Berkeley"],
    "learning_method": ["active recall", "spaced repetition", "deep thinking"],
    # endregion

    # region: Time
    "year": list(range(2100)),
    "month": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"],
    "date": list(range(1, 32)),
    "weekday": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "day": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
    "time_period": ["stone age", "bronze age", "classical antiquity", "iron age", "renaissance", "industrial age",
                    "atomic age", "space age", "information age"],
    "week": list(range(1, 53)),
    # endregion
}


add_from_class(CodeAnswers, answers)
