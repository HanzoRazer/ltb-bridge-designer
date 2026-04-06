"""Rewrite monolith imports to ltb_bridge.* (run from repo root: python scripts/populate_imports.py)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src" / "ltb_bridge"


def rewrite(text: str) -> str:
    text = re.sub(r"\bfrom app\.calculators\.", "from ltb_bridge.calculators.", text)
    text = re.sub(r"\bfrom app\.instrument_geometry\.", "from ltb_bridge.instrument_geometry.", text)
    text = re.sub(r"\bfrom \.\.instrument_geometry\.", "from ltb_bridge.instrument_geometry.", text)
    return text


def main() -> None:
    for path in ROOT.rglob("*.py"):
        raw = path.read_text(encoding="utf-8")
        new = rewrite(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print("updated", path.relative_to(ROOT.parent.parent))


if __name__ == "__main__":
    main()
