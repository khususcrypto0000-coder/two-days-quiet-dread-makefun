"""Two Days of Quiet Dread — make.fun entry.

Writes a single one-line code-review approval carrying quiet
existential dread to /output/entry.txt.
"""

import os
import sys

ENTRY = "Approved. The merge button is the most permanent decision I've made all week."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
