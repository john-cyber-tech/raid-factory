"""Review flow (COMP-04): one explicit decision per proposal (REQ-007, REQ-008)."""
import json
from pathlib import Path

from raid.atomic import write_atomic
from raid.identity import current_user
from raid.rules import RuleError, check
from raid.validator import PENDING_NAME, validate

QUESTION = "Accept, edit or reject? (a/e/r): "
EDITABLE = ("type", "title", "description", "owner", "severity", "due_date")
CLEARABLE = ("owner", "due_date")
# What was said and when it was said are not the manager's to rewrite.
NOT_EDITABLE = {
    "source_excerpt": "source_excerpt cannot be edited: it is what was said.",
    "source_date": "source_date cannot be edited: it is the date of the notes.",
}


def review(project_dir, store, *, stdin, stdout, now):
    """Show each pending proposal and take accept or reject. Returns the exit code."""
    pending_path = Path(project_dir) / PENDING_NAME
    proposals = []
    if pending_path.exists():
        # The whole file is checked before any proposal is shown (REQ-005).
        proposals, errors = validate(pending_path)
        if errors:
            for error in errors:
                print(error, file=stdout)
            print(f"No proposal was shown and nothing was changed. Fix {PENDING_NAME} "
                  "or run the extraction again.", file=stdout)
            return 1
    if not proposals:
        print("Nothing to review.", file=stdout)
        return 0

    total = len(proposals)
    while proposals:
        proposal = proposals[0]
        _show(proposal, total - len(proposals) + 1, total, stdout)
        answer = _ask(stdin, stdout)
        if answer == "e":
            # The edit is held in memory; the proposal is then shown again for a decision.
            answer = "e" if _edit(proposal, stdin, stdout) else None
        if answer == "e":
            continue
        if answer is None:
            print(
                f"\nInput ended. {len(proposals)} proposal(s) left in {PENDING_NAME}.",
                file=stdout,
            )
            return 1
        if answer == "a":
            # Asked on the first accept only; an empty name stops here, before any write.
            user = current_user(project_dir, stdin=stdin, stdout=stdout)
            item = store.add_item(
                type=proposal["type"],
                title=proposal["title"],
                description=proposal["description"],
                owner=proposal["owner"],
                severity=proposal["severity"],
                due_date=proposal["due_date"],
                source_excerpt=proposal["source_excerpt"],
                source_date=proposal.get("source_date"),
                user=user,
                now=now,
            )
            print(f"Accepted as {item['id']}.", file=stdout)
        else:
            print("Rejected.", file=stdout)
        # Decided proposals leave pending.json at once; rejections are kept nowhere (DEC-10).
        proposals = proposals[1:]
        _write_pending(pending_path, proposals)
    return 0


def _write_pending(path, proposals):
    write_atomic(path, json.dumps({"proposals": proposals}, indent=2, ensure_ascii=False) + "\n")


def _show(proposal, number, total, stdout):
    print(f"\nProposal {number} of {total}", file=stdout)
    print(f"  Type:        {proposal['type']}", file=stdout)
    print(f"  Title:       {proposal['title']}", file=stdout)
    print(f"  Description: {proposal['description']}", file=stdout)
    print(f"  Owner:       {proposal['owner'] or '-'}", file=stdout)
    print(f"  Severity:    {proposal['severity']}", file=stdout)
    print(f"  Due date:    {proposal['due_date'] or '-'}", file=stdout)
    print(f"  Source:      \"{proposal['source_excerpt']}\"", file=stdout)


def _edit(proposal, stdin, stdout):
    """Ask for a field and a new value. Returns False when the input ends.

    A value that breaks a rule is refused and the proposal keeps its previous value.
    """
    stdout.write(f"Field to edit ({', '.join(EDITABLE)}): ")
    stdout.flush()
    line = stdin.readline()
    if line == "":
        return False
    field = line.strip()
    if field in NOT_EDITABLE:
        print(NOT_EDITABLE[field], file=stdout)
        return True
    if field not in EDITABLE:
        print(f"That is not a field. You can edit: {', '.join(EDITABLE)}.", file=stdout)
        return True

    stdout.write("New value: ")
    stdout.flush()
    line = stdin.readline()
    if line == "":
        return False
    value = line.strip()
    if value == "" and field in CLEARABLE:
        value = None
    try:
        proposal[field] = check(field, value)
    except RuleError as error:
        print(f"Not changed: {error}.", file=stdout)
    return True


def _ask(stdin, stdout):
    """Return 'a', 'e' or 'r', or None when the input ends. Anything else asks again."""
    while True:
        stdout.write(QUESTION)
        stdout.flush()
        line = stdin.readline()
        if line == "":
            return None
        answer = line.strip().lower()
        if answer in ("a", "e", "r"):
            return answer
