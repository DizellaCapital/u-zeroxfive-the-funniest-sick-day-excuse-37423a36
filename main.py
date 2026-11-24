"""The Funniest Sick-Day Excuse entry program.

Writes one sick-day excuse — a single line someone could send to call in
sick — to MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The line is at most
200 characters, one line, no trailing newline.
"""

import os
import sys

# One line, 159 characters / 161 bytes: morning time anchor, a concrete
# object (the snooze button), and a final clause that reframes a sore back
# as an HR case. No fever, no dog, no dead grandmother.
LINE = "At 6:40 this morning my back went out reaching for the snooze button, and it has filed a formal complaint with HR \u2014 I'm staying home until the case is settled."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
