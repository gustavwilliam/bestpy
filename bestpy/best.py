from .answers import answers

import random


class Best:
    def __getattribute__(self, name):
        answer = answers[name]
        if callable(answer):
            answer = answer()
            
        if isinstance(answers, list):
            return random.choice(answer)
        return answer
