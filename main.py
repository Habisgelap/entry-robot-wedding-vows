"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow must be 1-160 characters, one line,
and funny: a real wedding promise with a machine-specific turn
that pays off in the last few words.
"""

import os

# The vow (153 characters, one line). Chosen from 12 candidates
# scored in CANDIDATES.md — it keeps the full wedding formula
# ("I take you", "to have and to hold", "until death do us part")
# and undercuts eternity with the most robot ending possible.
VOW = (
    "I take you to be my lawfully wedded co-processor, to have and "
    "to hold, in sickness and in low battery, until death do us part "
    "\u2014 or until the next update."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_vow(text):
    """Check the vow against the competition gate."""
    if not text or not text.strip():
        raise ValueError("vow must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "vow is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def write_entry(path=OUTPUT_PATH):
    """Validate the vow and write it, exactly, to the output file."""
    vow = validate_vow(VOW)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(vow)
    return path, len(vow)


def self_check():
    """Print the vow and its length; exit non-zero if it fails the gate."""
    vow = validate_vow(VOW)
    print(vow)
    print("---")
    print("%d characters (limit %d), one line, valid UTF-8" % (len(vow), MAX_CHARS))
    return 0


def main():
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        raise SystemExit(self_check())
    path, size = write_entry()
    print("wrote %d characters to %s" % (size, path))


if __name__ == "__main__":
    main()
