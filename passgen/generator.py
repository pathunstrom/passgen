from enum import Enum
from random import shuffle
from secrets import SystemRandom
from secrets import choice
import string


class Characters(Enum):
    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase
    DIGITS = string.digits
    SPECIAL = string.punctuation
    WHITE = string.whitespace


def generate(max_length, *, minimums=(), char_sets=()):
    minimums = dict(minimums)
    selection_sets = {enum: enum.value for enum in Characters}
    selection_sets.update(char_sets)

    chars_for_minimums = []
    min_counts = 0
    for k, v in minimums.items():
        min_counts += v
        chars_for_minimums.extend((choice(selection_sets[k]) for _ in range(v)))

    all_characters = "".join(v for v in selection_sets.values())
    remaining = max_length - min_counts
    chars_remaining = [choice(all_characters) for _ in range(remaining)]

    final_set = chars_for_minimums + chars_remaining

    rand = SystemRandom()
    shuffle(final_set, rand.random)

    return "".join(final_set)
