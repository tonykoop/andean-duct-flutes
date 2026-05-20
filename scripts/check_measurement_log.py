#!/usr/bin/env python3
"""Shape-check a measurement log against validation.csv.

Usage:
    python3 scripts/check_measurement_log.py \
        --validation validation.csv \
        --log data/measurement-log-template.csv

Exit codes:
    0  every validation.csv check has exactly one matching log row,
       and any non-`pending` captured_value also has captured_at and
       (where applicable) temperature_c populated.
    1  shape mismatch (missing/extra rows, or partial captures).

This is a SHAPE validator only. It does not judge whether captured
values meet their targets — a human reviewer does that.
"""
from __future__ import annotations

import argparse
import csv
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--validation", required=True)
    p.add_argument("--log", required=True)
    args = p.parse_args()

    with open(args.validation, newline="") as f:
        v_rows = list(csv.DictReader(f))
    with open(args.log, newline="") as f:
        l_rows = list(csv.DictReader(f))

    v_checks = [r["check"] for r in v_rows]
    l_checks = [r["check_id"] for r in l_rows]

    errors: list[str] = []

    # 1. Set equality.
    missing = set(v_checks) - set(l_checks)
    extra = set(l_checks) - set(v_checks)
    if missing:
        errors.append(f"log is missing {len(missing)} validation check(s): {sorted(missing)}")
    if extra:
        errors.append(f"log has {len(extra)} extra check_id(s) not in validation.csv: {sorted(extra)}")

    # 2. No duplicate check_id rows in the log.
    seen: dict[str, int] = {}
    for cid in l_checks:
        seen[cid] = seen.get(cid, 0) + 1
    dups = {k: v for k, v in seen.items() if v > 1}
    if dups:
        errors.append(f"log has duplicate check_id row(s): {dups}")

    # 3. Partial-capture check: if captured_value != 'pending', captured_at
    #    must also be set, and temperature_c must be set or 'n/a'.
    for r in l_rows:
        cv = (r.get("captured_value") or "").strip().lower()
        if cv and cv != "pending":
            ca = (r.get("captured_at") or "").strip().lower()
            tc = (r.get("temperature_c") or "").strip().lower()
            if not ca or ca == "pending":
                errors.append(f"row {r['check_id']!r} has captured_value but captured_at is pending")
            if not tc or tc == "pending":
                errors.append(f"row {r['check_id']!r} has captured_value but temperature_c is pending (use 'n/a' if not applicable)")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(l_rows)} rows match validation.csv check set; no partial captures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
