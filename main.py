"""Roast Your Own Agent — make.fun entry generator.

Pure Python 3 standard library. Writes the one-line roast to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).
"""

import os

ENTRY = (
    "My agent says 'Great question!' then confidently opens six tabs, "
    "reads none, and calls it research \u2014 and somehow I still trust it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
