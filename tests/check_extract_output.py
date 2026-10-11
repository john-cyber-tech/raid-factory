"""Check a saved `pending.json` from `/raid-extract` against the notes it was made from.

Story EPIC-1-05, criterion 9: every field of the contract is present, titles are
at most 80 characters, and each source excerpt appears word for word in the notes.

    python3 tests/check_extract_output.py <pending.json> <notes file>

Prints the problems and exits 1, or prints the number of proposals and exits 0.
It reads the two files and writes nothing.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from raid.validator import validate  # noqa: E402  (the tool's own validator: one definition of valid)

CR = chr(13)


def _lines(text):
    """Windows line endings count as line breaks. Nothing else is changed."""
    return text.replace(CR + "\n", "\n")


def check(pending_path, notes_path):
    """Return a list of problems, empty when the output is acceptable."""
    pending_path, notes_path = Path(pending_path), Path(notes_path)
    if not pending_path.is_file():
        return [f"{pending_path.name} does not exist"]
    if not notes_path.is_file():
        return [f"the notes file {notes_path.name} does not exist"]

    proposals, errors = validate(pending_path)
    if errors:
        return errors

    # Read as bytes so no line ending is translated before the comparison.
    notes = _lines(notes_path.read_bytes().decode("utf-8"))
    problems = []
    for number, proposal in enumerate(proposals, start=1):
        excerpt = proposal["source_excerpt"]
        if CR in excerpt:
            problems.append(
                f"proposal {number}: source_excerpt holds a carriage return; "
                "/raid-extract writes a plain line break"
            )
        elif _lines(excerpt) not in notes:
            problems.append(
                f"proposal {number}: source_excerpt is not in the notes word for word"
            )
    return problems


def main(argv):
    if len(argv) != 2:
        print("usage: check_extract_output.py <pending.json> <notes file>")
        return 2
    problems = check(argv[0], argv[1])
    for problem in problems:
        print(problem)
    if problems:
        return 1
    count = len(validate(Path(argv[0]))[0])
    print(f"{count} proposals: contract met and every excerpt found word for word in the notes.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
