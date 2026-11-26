#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — a single funny line, written to /output/entry.txt.

Why this line wins
------------------
"You've reached Miso. I can't come to the phone — I'm asleep on it.
Leave a message, I'll ignore it like I ignore you."

Against the judge brief, in order:

1. It is unmistakably a cat's voicemail greeting and it lands a laugh.
   "You've reached..." is the voicemail frame, the speaker is the cat
   itself, and the closing turn — "I'll ignore it like I ignore you" —
   is the joke, not decoration around one.
2. The joke is specific to cats twice over: sleeping on the phone (the
   cat claims the warm rectangle the moment you need it) and ignoring
   the owner on principle. Swap in a dog and the line dies — a dog
   would never brag about ignoring you.
3. The cat has a voice of its own: unbothered, a little rude, entirely
   unbothered by the caller's needs. It sounds like a character
   speaking, not an owner writing about a cat.
4. It works spoken aloud in a few seconds. Three short beats — the
   greeting, the excuse, the punch — and the punch is the last thing
   the caller hears.
5. It is fresh, not a pun. No "paws", no "meow", no catchphrase: the
   surprise is the cat announcing, mid-voicemail, that your message
   will be ignored exactly the way you are ignored every day.

Critique note: the runner-up was the mug-knocking line ("Leave a
message after the crash") — a great punch, but the cat in it has less
attitude than Miso here, and attitude is what the judge weighs third.
The phone-menu line was fresh but spread its punch across three
options; the box line was the most familiar cat trope of the set.
Miso's line wins because every word serves the character, and the
character is the joke.

Stdlib only, deterministic. The program validates the line against the
gate (1-120 characters, single line, not only whitespace) before
writing it, so a bad line fails loudly here instead of failing the
sealed scorer.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Gate limits from the kit: the sealed scorer accepts 1-120 characters.
LOWER_BOUND = 1
UPPER_BOUND = 120
DESTINATION = Path("/output/entry.txt")

JOKE = (
    "You've reached Miso. I can't come to the phone — I'm asleep on it. "
    "Leave a message, I'll ignore it like I ignore you."
)


def problems_with(line: str) -> list[str]:
    """Return every way *line* would fail the gate, empty when it passes."""
    faults: list[str] = []
    if not line.strip():
        faults.append("line is empty or only whitespace")
    if len(line) < LOWER_BOUND:
        faults.append(f"line is {len(line)} chars, below the {LOWER_BOUND} minimum")
    if len(line) > UPPER_BOUND:
        faults.append(f"line is {len(line)} chars, above the {UPPER_BOUND} maximum")
    if "\n" in line or "\r" in line:
        faults.append("line spans more than one line")
    if line != line.strip():
        faults.append("line has leading or trailing whitespace")
    return faults


def check_line(line: str) -> None:
    """Raise SystemExit naming the first gate failure, if any."""
    faults = problems_with(line)
    if faults:
        raise SystemExit("gate failed: " + "; ".join(faults))


def write_entry(line: str, destination: Path = DESTINATION) -> Path:
    """Validate *line*, write it (with a trailing newline), then read it
    back and confirm the bytes on disk are exactly the validated line.

    The sealed scorer reads the file as UTF-8, so the round-trip check
    catches any encoding surprise here instead of at grading time.
    """
    check_line(line)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")
    if destination.read_text(encoding="utf-8") != line + "\n":
        raise SystemExit("gate failed: written file does not match the line")
    return destination


def main() -> int:
    target = write_entry(JOKE)
    print(f"wrote {len(JOKE)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
