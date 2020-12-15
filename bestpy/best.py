from .answers import answers

import random


class Best:
    def __getattribute__(self, name):
        answer = answers[name]
        if callable(answers[name]):
            answer = answers[name]()
        if isinstance(answers, list):
            return random.choice(answers[name])
        return answers[name]
