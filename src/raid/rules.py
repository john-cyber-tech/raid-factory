"""Field rules: one set, matching the pending.json contract exactly (ADR-004).

Used for edits during review and for changes made through the log store. The
values here are compared with pending.schema.json by a test, so they cannot drift.
"""
import re
from datetime import date

TYPES = ("Risk", "Assumption", "Issue", "Dependency")
SEVERITIES = ("High", "Medium", "Low")
TITLE_LIMIT = 80
# No control character, line or paragraph separator, or text-direction control.
FORBIDDEN_IN_ONE_LINE = re.compile(
    r"[\u0000-\u001f\u007f-\u009f\u2028\u2029\u202a-\u202e\u2066-\u2069]"
)
# The same, but a tab, a line break and a carriage return followed by a line break are allowed.
FORBIDDEN_IN_LONG_TEXT = re.compile(
    r"[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f-\u009f\u2028\u2029\u202a-\u202e\u2066-\u2069]|\r(?!\n)"
)
DATE_FORMAT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


class RuleError(Exception):
    """A value breaks a field rule. The message states the rule and never repeats the value."""


def is_real_date(text):
    """True for a real calendar date written exactly as YYYY-MM-DD."""
    if not isinstance(text, str) or not DATE_FORMAT.fullmatch(text):
        return False
    try:
        date(int(text[:4]), int(text[5:7]), int(text[8:]))
    except ValueError:
        return False
    return True


def check(field, value):
    """Return `value` if it is allowed for `field`; otherwise raise RuleError."""
    if field == "type":
        _one_of(field, value, TYPES)
    elif field == "severity":
        _one_of(field, value, SEVERITIES)
    elif field == "title":
        _text(field, value, FORBIDDEN_IN_ONE_LINE)
        if not value:
            raise RuleError("title cannot be empty")
        if len(value) > TITLE_LIMIT:
            raise RuleError(f"title is {len(value)} characters; the limit is {TITLE_LIMIT}")
    elif field == "owner":
        if value is not None:
            _text(field, value, FORBIDDEN_IN_ONE_LINE)
    elif field == "description":
        _text(field, value, FORBIDDEN_IN_LONG_TEXT)
    elif field in ("due_date", "source_date"):
        if value is not None and not is_real_date(value):
            raise RuleError(f"{field} must be a real date written as YYYY-MM-DD")
    else:
        raise RuleError(f"{field} cannot be changed")
    return value


def _one_of(field, value, allowed):
    if value not in allowed:
        raise RuleError(f"{field} must be {', '.join(allowed[:-1])} or {allowed[-1]}")


def _text(field, value, forbidden):
    if not isinstance(value, str):
        raise RuleError(f"{field} must be text")
    if forbidden.search(value):
        raise RuleError(f"{field} contains a control or text-direction character")
