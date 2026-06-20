#!/usr/bin/env python3
"""Copy minisimmy_orbital_ship_v2.html to the local GrokBuildProjects play folder."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "minisimmy_orbital_ship_v2.html"
DEST_DIR = Path(r"C:\Users\itreb\GrokBuildProjects\ModularLifeSim-Website")
LATEST_NAME = "minisimmy_orbital_ship_v2.html"


def read_build_tag(html: str) -> str:
    m = re.search(r"const MINISIMMY_BUILD = '([^']+)'", html)
    if m:
        return m.group(1)
    m = re.search(r'content="[^"]*-([^"]+)"', html)
    return m.group(1) if m else "unknown-build"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    text = SOURCE.read_text(encoding="utf-8")
    build = read_build_tag(text)
    snapshot = DEST_DIR / f"minisimmy_orbital_ship_v2-{build}.html"
    latest = DEST_DIR / LATEST_NAME

    shutil.copy2(SOURCE, latest)
    shutil.copy2(SOURCE, snapshot)

    print(f"Published build: {build}")
    print(f"  latest   -> {latest}")
    print(f"  snapshot -> {snapshot}")


if __name__ == "__main__":
    main()