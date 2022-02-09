import random
from collections import abc


class Best:
    def __init__(self, answers):
        self._answers = answers

    def __getattr__(self, name):
        try:
            answer = self._answers[name]
            print(answer)
        except KeyError:
            error_message = f"'{self.__class__.__name__}' object has no attribute '{name}'"

            # `from None` ensures that the error raised does not originate from the `KeyError` above
            raise AttributeError(error_message) from None

        if callable(answer):
            answer = answer()
        elif isinstance(answer, str):
            answer = answer
        elif isinstance(answer, abc.Sequence):
            answer = random.choice(answer)

        return answer
