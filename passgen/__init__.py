import argparse

from passgen.generator import generate
from passgen.generator import Characters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", "-m", type=int, default=25, dest="max_length")
    for character_set in Characters:
        flag = character_set.name.lower()
        short_flag = flag[0]
        parser.add_argument(f"--{flag}", f"-{short_flag}", dest=flag)
        parser.add_argument(f"--{flag}min", dest=f"{flag}min", type=int)

    args = parser.parse_args()
    mins = []
    char_sets = []
    for character_set in Characters:
        name = character_set.name.lower()
        c_set = getattr(args, name, None)
        if c_set is not None:
            char_sets.append((character_set, c_set))
        elif character_set is Characters.WHITE:
            char_sets.append((character_set, ""))  # Default to no white space.
        minimum = getattr(args, f"{name}min", None)
        if minimum is not None:
            mins.append((character_set, minimum))

    print(generate(args.max_length, char_sets=char_sets, minimums=mins))
