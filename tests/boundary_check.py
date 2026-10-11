"""Import check for src/ (NFR-004): no network module, no model client, no way to start another program."""
import ast

FORBIDDEN = {
    "socket", "urllib", "http", "requests", "httpx", "subprocess", "anthropic",
    "asyncio", "ssl", "smtplib", "ftplib", "urllib3", "aiohttp", "openai",
}
FORBIDDEN_OS_CALLS = {"system", "popen"}


def forbidden_imports(path):
    """Return one line per forbidden import or shell call in the Python file at `path`."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    problems = []

    def flag(node, what):
        problems.append(f"{path.name}:{node.lineno}: {what}")

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top in FORBIDDEN:
                    flag(node, f"imports {top} ({alias.name})")
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            top = node.module.split(".")[0]
            if top in FORBIDDEN:
                flag(node, f"imports {top} ({node.module})")
            elif node.module == "os":
                for alias in node.names:
                    if alias.name in FORBIDDEN_OS_CALLS:
                        flag(node, f"imports os.{alias.name}")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr in FORBIDDEN_OS_CALLS
        ):
            flag(node, f"calls os.{node.func.attr}")
    return problems
