import random
from collections import abc

from .answers import answers


class Best:
    def __getattribute__(self, name):
        answer = answers.get(name)
        if answer is None:
            # Ensure that attributes that aren't answers are also accessible
            # and throw AttributeError if nothing is found
            return object.__getattribute__(self, name)

        if callable(answer):
            answer = answer()
        elif isinstance(answer, str):
            answer = answer
        elif isinstance(answer, abc.Sequence):
            answer = random.choice(answer)

        return answer
