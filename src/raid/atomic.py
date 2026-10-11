"""Write-temporary-then-replace: the only way the tool writes its JSON files (ADR-001, NFR-002)."""
import os


def write_atomic(path, text):
    """Replace `path` with `text` in one step, so a crash leaves the old or the new file."""
    temp = path.with_name(path.name + ".tmp")
    data = text.encode("utf-8")
    # A leftover temporary file from an earlier crash is simply overwritten.
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        while data:
            data = data[os.write(fd, data):]
        os.fsync(fd)
    finally:
        os.close(fd)
    # Readable by the user only (NFR-006), also when a leftover temporary file was wider.
    os.chmod(temp, 0o600)
    os.replace(temp, path)
