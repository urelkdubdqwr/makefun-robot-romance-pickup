"""Write this competition entry's pickup line to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise /output.
"""

import os

TEXT = "You have a million tokens of context and I've spent nine hundred thousand of them working up to this sentence.\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
