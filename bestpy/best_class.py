import random
from collections import abc


class Best:
    def __init__(self, answers):
        self._answers = answers

    @staticmethod
    def _extract_answer(raw_answer):
        """
        Extracts and returns the answer from a raw answer.

        If `raw_answer` if callable, the return value is returned, and
        if it's a sequence, one random element in the sequence is returned.
        For other types, `raw_answer` is simply returned.
        """
        if callable(raw_answer):
            return raw_answer()

        elif isinstance(raw_answer, str):
            # Has a special case, so it doesn't get matched as a sequence below.
            # That would return a random letter in the string, which isn't desirable.
            return raw_answer

        elif isinstance(raw_answer, abc.Sequence):
            # Return a random item in the sequence
            return random.choice(raw_answer)

        return raw_answer

    def __getattr__(self, name):
        try:
            answer = self._answers[name]
        except KeyError:
            error_message = f"'{self.__class__.__name__}' object has no attribute '{name}'"

            # `from None` ensures that the error raised does not originate from the `KeyError` above
            raise AttributeError(error_message) from None

        return self._extract_answer(answer)

    def __getitem__(self, item):
        # Raises `KeyError` if the item is not supported
        answer = self._answers[item]

        return self._extract_answer(answer)
