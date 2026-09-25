#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys

root = Path(__file__).resolve().parents[1]
manifest = root / "FREEZE_MANIFEST.sha256"
if not manifest.exists():
    print("No FREEZE_MANIFEST.sha256 found.", file=sys.stderr)
    sys.exit(2)

bad = []
for line in manifest.read_text().splitlines():
    if not line.strip(): continue
    expected, rel = line.split("  ", 1)
    p = root / rel
    if not p.exists():
        bad.append((rel, "MISSING"))
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != expected:
        bad.append((rel, "HASH_MISMATCH"))

if bad:
    for x in bad: print(*x)
    sys.exit(1)
print("Freeze manifest verified.")
