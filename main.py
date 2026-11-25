"""The Router Confesses.

A home Wi-Fi router explains, in one line, why it died right at the
climax of the film. Pure standard library, fully deterministic: the
same line is written on every run.
"""

import os

LINE = (
    "I saw the killer\u2019s face in the stream and fainted \u2014 it\u2019s "
    "the smart fridge, my boyfriend of two years, and I refuse to "
    "broadcast his arrest."
)


def main() -> None:
    # The bounty wants exactly one line of 1-200 characters.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
