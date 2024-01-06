from pathlib import Path
from typing import Final

DIR_ROOT: Final = Path(__file__).parent.parent.resolve()
DIR_API: Final = (DIR_ROOT / "api").resolve()
DIR_LOCAL: Final = (DIR_ROOT / ".local").resolve()

err_local = f"Project .local dir is not found: {DIR_LOCAL}"
assert DIR_LOCAL.is_dir, err_local

DIR_STATIC: Final = (DIR_LOCAL / "static").resolve()

DIR_STATIC.mkdir(exist_ok=True)

__all__ = (
    "DIR_ROOT",
    "DIR_API",
    "DIR_LOCAL",
    "DIR_STATIC",
)
