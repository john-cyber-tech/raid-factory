"""Pending contract validator (COMP-02): pending.schema.json is the single definition of valid (ADR-004)."""
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

PENDING_NAME = "pending.json"
SCHEMA_PATH = Path(__file__).parent / "schemas" / "pending.schema.json"
DATE_FIELDS = ("due_date", "source_date")
DATE_FORMAT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
MULTI_LINE_FIELDS = ("description", "source_excerpt")


def validate(path):
    """Check the file at `path` against the contract.

    Returns (proposals, errors). `errors` is empty when the file is valid; otherwise
    every problem is listed in plain words and `proposals` is None.
    """
    try:
        text = Path(path).read_text(encoding="utf-8")
        data = json.loads(text, object_pairs_hook=_Object)  # _Object records repeated keys
    except json.JSONDecodeError as error:
        return None, [
            f"{PENDING_NAME} is not valid JSON "
            f"(line {error.lineno}, column {error.colno}: {error.msg})."
        ]
    except UnicodeDecodeError:
        return None, [f"{PENDING_NAME} is not valid JSON (it is not UTF-8 text)."]

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    found = set(_repeated_keys(data))
    for error in Draft202012Validator(schema).iter_errors(data):
        found.update(_describe(error))
    if not found:
        found.update(_impossible_dates(data["proposals"]))
    if found:
        return None, [f"{PENDING_NAME}: {text}" for _, text in sorted(found)]
    return [dict(proposal) for proposal in data["proposals"]], []


class _Object(dict):
    """A JSON object that remembers any key written more than once.

    A plain reader keeps the last value and says nothing, so what a person reads
    in the file and what the tool would use could differ.
    """

    def __init__(self, pairs):
        super().__init__(pairs)
        seen = set()
        self.repeated = sorted({key for key, _ in pairs if key in seen or seen.add(key)})


def _repeated_keys(data):
    problems = []
    if isinstance(data, _Object):
        problems += [(0, f"{_safe(key)} appears more than once") for key in data.repeated]
        proposals = data.get("proposals")
        if isinstance(proposals, list):
            for number, proposal in enumerate(proposals, start=1):
                if isinstance(proposal, _Object):
                    problems += [(number, f"proposal {number}: {_safe(key)} appears more than once")
                                 for key in proposal.repeated]
    return problems


def _describe(error):
    """Turn one schema error into (proposal number, plain message) pairs."""
    path = list(error.absolute_path)
    if len(path) < 2:
        return _describe_file(error, path)
    number = path[1] + 1
    where = f"proposal {number}"
    if len(path) == 2:
        if error.validator == "required":
            return [(number, f"{where}: {key} is missing")
                    for key in error.validator_value if key not in error.instance]
        if error.validator == "additionalProperties":
            allowed = error.schema["properties"]
            return [(number, f"{where}: {_safe(key)} is not an allowed key")
                    for key in error.instance if key not in allowed]
        return [(number, f"{where}: must be an object with the proposal's fields")]

    field = path[2]
    value = error.instance
    if error.validator == "enum":
        options = error.validator_value
        return [(number, f"{where}: {field} must be {', '.join(options[:-1])} or {options[-1]}, "
                         f"not {_safe(value)}")]
    if error.validator == "maxLength":
        return [(number, f"{where}: {field} is {len(value)} characters; "
                         f"the limit is {error.validator_value}")]
    if error.validator == "minLength":
        return [(number, f"{where}: {field} is empty")]
    if error.validator == "not":
        allowed = " other than a line break or tab" if field in MULTI_LINE_FIELDS else ""
        return [(number, f"{where}: {field} contains a control or text-direction character{allowed}")]
    if field in DATE_FIELDS:
        return [(number, f"{where}: {field} must be a date written as YYYY-MM-DD, or null")]
    if error.validator == "type":
        allowed = "text or null" if "null" in error.validator_value else "text"
        return [(number, f"{where}: {field} must be {allowed}")]
    return [(number, f"{where}: {field} is not valid")]


def _describe_file(error, path):
    if error.validator == "additionalProperties":
        return [(0, f"{_safe(key)} is not an allowed key; the only key is proposals")
                for key in error.instance if key != "proposals"]
    if path == ["proposals"]:
        return [(0, "proposals must be a list")]
    return [(0, "the file must be an object with one key, proposals")]


def _impossible_dates(proposals):
    """The check a schema cannot express: each date is a real calendar date."""
    problems = []
    for number, proposal in enumerate(proposals, start=1):
        for field in DATE_FIELDS:
            value = proposal.get(field)
            if value is None:
                continue
            try:
                if not DATE_FORMAT.fullmatch(value):
                    raise ValueError(value)
                date(int(value[:4]), int(value[5:7]), int(value[8:]))
            except ValueError:
                problems.append((number, f"proposal {number}: {field} is not a real date "
                                         f"({_safe(value)}); write it as YYYY-MM-DD"))
    return problems


def _safe(value):
    """A short, printable form of a refused value: nothing from the file reaches the terminal raw."""
    text = value if isinstance(value, str) else json.dumps(value)
    text = "".join("?" if unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp") else ch
                   for ch in text)
    if len(text) > 40:
        text = text[:40] + "..."
    return f'"{text}"' if isinstance(value, str) else text
