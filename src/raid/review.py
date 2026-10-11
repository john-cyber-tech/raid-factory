"""Review flow (COMP-04): one explicit decision per proposal (REQ-007, REQ-008)."""
import json
from pathlib import Path

from raid.atomic import write_atomic
from raid.identity import current_user

PENDING_NAME = "pending.json"
QUESTION = "Accept or reject? (a/r): "


def review(project_dir, store, *, stdin, stdout, now):
    """Show each pending proposal and take accept or reject. Returns the exit code."""
    pending_path = Path(project_dir) / PENDING_NAME
    proposals = _read_pending(pending_path)
    if not proposals:
        print("Nothing to review.", file=stdout)
        return 0

    total = len(proposals)
    while proposals:
        proposal = proposals[0]
        _show(proposal, total - len(proposals) + 1, total, stdout)
        answer = _ask(stdin, stdout)
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


def _read_pending(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))["proposals"]


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


def _ask(stdin, stdout):
    """Return 'a' or 'r', or None when the input ends. Anything else asks again."""
    while True:
        stdout.write(QUESTION)
        stdout.flush()
        line = stdin.readline()
        if line == "":
            return None
        answer = line.strip().lower()
        if answer in ("a", "r"):
            return answer
