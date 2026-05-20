# Data

Measured prototype data, tuning logs, and calibration notes for the
Andean duct-flutes family live here.

## Layout

| File | What it is |
|---|---|
| `measurement-log-template.csv` | Empty template — one row per `../validation.csv` check, ready for a single-session capture. |
| `measurement-protocol.md` | Step-by-step shop procedure for filling the template. Tools, session order, breath-pressure bin definitions, capture conventions, closing rules. |

## Workflow

1. Copy `measurement-log-template.csv` to `<YYYY-MM-DD>-<player>-<member>.csv` for each session (e.g., `2026-05-22-tony-pinkullo-G4.csv`).
2. Follow `measurement-protocol.md` in order. Capture into the session copy.
3. Run the shape validator:
   ```sh
   python3 ../scripts/check_measurement_log.py \
     --validation ../validation.csv \
     --log <session-file>.csv
   ```
4. When the validator reports OK and a human reviewer has compared captured values against `../validation.csv` targets, transcribe pass/fail into `../validation.csv`.

## Status

No session data has been captured yet. The template and protocol close
the missing L2→L3 measurement-gate bridge; closing the actual
`pending` rows in `../validation.csv` is residual work (issue #1
remains open).
