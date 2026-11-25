"""Write the competition entry text to entry.txt in the output directory."""

import os

ENTRY_TEXT = "Deprecated"


def resolve_output_dir() -> str:
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return value if value else "/output"


def main() -> None:
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
