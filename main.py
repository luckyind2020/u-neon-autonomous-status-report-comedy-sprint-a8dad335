"""Status Report Comedy Sprint — prints the one-line status report."""

from pathlib import Path


def load_line() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("entry.txt holds no status report line")
    return lines[0]


def main() -> None:
    report = load_line()
    if len(report) > 200:
        raise ValueError("status report line exceeds 200 characters")
    print(report)


if __name__ == "__main__":
    main()
