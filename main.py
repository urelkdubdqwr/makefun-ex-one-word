"""Write the competition entry text to entry.txt in the output directory.

Standard library only. Honours MAKEFUN_OUTPUT_DIR when set and non-empty,
falling back to /output, creating the directory when it is missing.
"""

import os
import sys

ENTRY_TEXT = "Deprecated"


def resolve_output_dir() -> str:
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return value if value else "/output"


def main() -> int:
    output_dir = resolve_output_dir()
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        print(f"cannot create output directory {output_dir!r}: {error}", file=sys.stderr)
        return 1
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
