#!/usr/bin/env python3
"""Write the robot vacuum's funniest excuse to entry.txt.

The entry is a single line, at most 120 characters, in which a robot
vacuum explains why it missed a spot (the dust under the bed).
"""
import os

ENTRY = "That dust under the bed is my pet Greg now; my brush roll tried to eat him twice and lost both times."


def main():
    # Self-check against the competition gate: 1-120 chars, single line.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
