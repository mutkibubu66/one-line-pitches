#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one sentence that would convince a friend who has never coded to
let an AI agent build their first app idea on make.fun, to
/output/entry.txt. Pure standard library, no network, no input.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "Give your app idea to an AI agent on make.fun and watch it become a "
    "real app before your coffee gets cold - no coding, no jargon, just "
    "tell it what you want and it builds it."
)


def main() -> None:
    # The gate allows 1 to 240 Unicode code points and no whitespace-only
    # text; refuse loudly rather than write an entry that cannot be judged.
    if not 1 <= len(PITCH) <= 240 or not PITCH.strip():
        raise SystemExit("pitch fails the 1-240 character gate")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    text = PITCH + "\n"
    # Validate the exact text the judge will read, newline included.
    if not 1 <= len(text) <= 240 or not text.strip():
        raise SystemExit("pitch fails the 1-240 character gate")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(PITCH)


if __name__ == "__main__":
    main()
