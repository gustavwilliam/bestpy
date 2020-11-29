import random

from bestpy import answers


def _get_answer(category):
    options = answers.answers.get(category)

    if callable(options):
        options = options()

    if isinstance(options, list):
        return random.choice(options)

    return options
