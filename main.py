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
import tempfile

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

# The entry must hold 1 to 1,000 characters: refuse to write anything
# outside that range rather than submitting an invalid entry.
if not 1 <= len(POEM) <= 1000:
    raise ValueError(f"poem is {len(POEM)} characters, outside 1-1000")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    # Write atomically: a reader never sees a half-written entry.
    fd, tmp_path = tempfile.mkstemp(dir=OUTPUT_DIR, prefix=".entry-",
                                    suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(POEM)
        os.replace(tmp_path, path)
        # Read back what landed: a short entry is cheap to verify, and a
        # truncated write must fail loudly here, not at grading time.
        with open(path, "r", encoding="utf-8", newline="") as f:
            if f.read() != POEM:
                raise IOError("entry.txt does not match the poem")
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
