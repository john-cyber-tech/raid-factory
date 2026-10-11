import sys
from pathlib import Path

# Tests import the package from src/ without needing an install.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
