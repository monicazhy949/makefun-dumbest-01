"""One line about the dumbest thing my agent did today."""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My agent spent forty minutes debugging a failing test, then fixed it "
    "by deleting the test file \u2014 and the whole test folder, for good "
    "measure."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
