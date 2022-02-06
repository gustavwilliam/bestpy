import random
from collections import abc

from .answers import answers


class Best:
    def __getattribute__(self, name):
        answer = answers[name]

        if callable(answer):
            answer = answer()
        elif isinstance(answer, str):
            answer = answer
        elif isinstance(answer, abc.Sequence):
            answer = random.choice(answer)

        return answer
