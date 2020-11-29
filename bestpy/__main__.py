import random

from bestpy.answers import answers


def _get_answer(category):
    options = answers.get(category)

    if callable(options):
        options = options()

    if isinstance(options, list):
        return random.choice(options)

    return options


class Best:
    def __init__(self):
        pass

    def __getattr__(self, item):
        return _get_answer(item.lower())


best = Best()
