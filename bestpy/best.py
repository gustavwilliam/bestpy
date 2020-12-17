import random
from collections import abc

from .answers import answers


class Best:
    def __getattribute__(self, name):
        answer = answers[name]

        if callable(answer):
            return answer()
        elif isinstance(answer, abc.Sequence):
            return random.choice(answer)

        return answer
