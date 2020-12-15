from .answers import answers

import random


class Best:
    def __getattribute__(self, name):
        # Return random value in list
        if isinstance(answers[name], list):
            return random.choice(answers[name])
        # Call function
        elif callable(answers[name]):
            return answers[name]()
        else:
            return answers[name]
