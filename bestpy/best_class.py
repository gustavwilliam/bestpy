from .answers import answers

import random


class Best:
    def __getattribute__(self, name):
        answer = answers[name]
        if callable(answer):
            answer = answer()

        if isinstance(answer, list):
            return random.choice(answer)
        return answer
