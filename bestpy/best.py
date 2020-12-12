from .answers import answers

import random


class Best:
    def __getattr__(self, name):
        # Return random value in list
        if type(answers[name]) != list:
            return answers[name]
        else:
            return random.choice(answers[name])
