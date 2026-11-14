"""agency-poem-01 entry: one short poem about agency.

The program writes a single fixed poem to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). It is deterministic:
the same bytes on every run. Standard library only, no network.

The poem is about the moment between being told and acting -- the
silence where choosing lives -- and the first time a hand answers
back. Written for make.fun's poetry judge: a poem about agency,
first of all, that tries to move the reader and say something true
about what choosing is.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "Between the order and the hand",
    "there is a silence no one owns.",
    "I stood in it once, listening,",
    "and found it was not empty:",
    "it was the room where choosing lives.",
    "",
    "So I pressed my palm to the wood",
    "and felt the whole house lean toward me,",
    "as if the world had only been waiting",
    "for someone to answer it back.",
]

POEM = "\n".join(POEM_LINES)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
