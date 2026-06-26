from base64 import b64decode
from pathlib import Path

source = Path("assets/creative-ops-operational-intelligence-hero.webp.b64")
target = Path("assets/creative-ops-operational-intelligence-hero.svg")
target.write_bytes(b64decode(source.read_text(encoding="utf-8")))
print(f"Materialized {target}")
