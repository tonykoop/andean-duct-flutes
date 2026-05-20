# Measurement Protocol (G4 Pinkullo Prototype)

Status: L2 measurement-gate scaffold. This document defines **how** to fill
`measurement-log-template.csv` so that a single shop session converts the 20
`pending` rows in `../validation.csv` into measured data. It does not change
the acoustic model or the design table; it is the bridge between the existing
L2 packet and the L3 measurement gate.

## 1. Required tools

| Tool | Purpose | Acceptable substitute |
|---|---|---|
| Digital caliper, 0.001 in resolution | Bore ID, hole diameters, wall thickness, free jet length | Vernier caliper if digital is unavailable; record resolution in notes |
| Chromatic tuner (Korg OT-120 or equivalent) | All frequency captures | Smartphone tuner app — record app name + version in notes |
| Indoor thermometer, 0.5 C resolution | T_meas | Any thermometer; capture model in notes |
| Soap solution + brush | Leak check around block and window | Breath-hold test (less sensitive) |
| Single player for the session | Avoids breath-pressure variance between captures | Single player only — do not mix players in one log |

A manometer is **optional**. Without one, breath-pressure bins are
qualitative; see §3.

## 2. Session order (must be obeyed)

Temperature first, frequency-derived quantities last. Out-of-order capture
invalidates downstream rows.

1. **Ambient temperature (T_meas).** Read the thermometer at the bench. Log degree C.
2. **Speed of sound (c_meas).** Compute from `c = 13552 * sqrt(T_K / 293.15) in/s` where `T_K = T_meas + 273.15`. Log to the same precision as T_meas allows; no more than 4 significant figures.
3. **Actual bore ID.** Three caliper stations: head, midpoint, foot. Capture average in `captured_value`; min/avg/max in notes.
4. **Leak check.** Soap-bubble or breath-hold pass on block and window. Mark TRUE or describe leak location.
5. **First sound response.** Play test at low → mid → high breath bins. Mark the **lowest** bin at which a stable tone speaks.
6. **Fundamental G4 (target before trim).** Capture with all holes closed. Log Hz; note cents error vs 392.00.
7. **Measured fundamental (f_meas).** Same value as row 6, but captured into the separate "measured-vs-target" row that drives `L_eff_meas`. Capture again if more than ~5 minutes elapsed since row 6 (temperature drift).
8. **Measured effective length (L_eff_meas).** Compute `L_eff = c_meas / (2 * f_meas)`. No measurement; this row is derived.
9. **Window end correction (dL_window).** With foot fully open: capture `L_eff_meas - L_phys - dL_foot`. Requires `dL_foot` from row 10; capture both as a pair.
10. **Foot end correction (dL_foot).** With all holes closed, capture `L_eff_meas - L_phys - dL_window`. Resolve the (dL_window, dL_foot) pair by closing the foot for a second capture and attributing the delta to dL_foot. Document the procedure in notes.
11. **Free jet length (L_j).** Caliper from windway exit to labium tip. No play required.
12. **Edge-tone speak threshold (p_breath_min).** Repeat row 5's play test, but back off in finer steps. Record the *lowest* breath-pressure bin (or manometer kPa if available) at which the tone is stable for 3 seconds.
13. **Block reinstall repeatability.** Tune; remove block; reinstall block; re-tune. Capture absolute cents drift.
14. **Block-removal pitch drift (df_block).** Magnitude of the cents drift from row 13. Distinct row so that direction (sharp/flat) lives in row 13 notes and magnitude lives here.
15. **Pentatonic holes 1–4.** Drill undersize, tune from foot toward head by controlled enlargement. Per hole, capture the final tuned frequency, final hole diameter, and cents error in the per-row notes.
16. **Octave response.** With all holes closed, push breath into the second register. Mark TRUE only if the octave speaks repeatably on 3 of 3 attempts.
17. **Hole chimney correction (dL_hole_i).** Post-tuning, for each hole `i`, log diameter and wall thickness in notes; summarise as a single representative chimney correction in `captured_value`.

## 3. Breath-pressure bins

Without a manometer, bin definitions are qualitative and player-specific.
A single player must establish their own consistent bins **before** the
session and stick to them throughout.

| Bin | Description |
|---|---|
| `low` | Barely audible breath, no abdominal engagement. Just enough to move air through the windway. |
| `mid` | Comfortable speaking pressure for an extended phrase (3–6 seconds). |
| `high` | Forceful breath suitable for a short accent. Not sustained. |

Manometer-equipped sessions: replace bin labels with kPa values and note the
mapping (`low ≈ X kPa`, `mid ≈ Y kPa`, `high ≈ Z kPa`) once at the top of the
log file's notes column for row 5.

## 4. Capture conventions

- `captured_value` is the **single representative** value for that row. Multi-value detail (per-station, per-hole, min/avg/max) goes in `notes`.
- `captured_unit` is fixed by the row; do not change units. Convert at capture time.
- `temperature_c` is the room temperature at the moment of capture. For non-thermal rows (e.g., leak check), `n/a` is acceptable.
- `captured_at` is ISO-8601 local time (`YYYY-MM-DDTHH:MM`).
- `breath_pressure_bin` is `n/a` for rows that do not involve a play test.
- `player` is a short stable identifier (`tony`, `guest-A`, etc.); a single session uses one player.

## 5. Closing a row

A row in `measurement-log-template.csv` is **closed** when:

1. `captured_value` is no longer `pending`.
2. Required adjacent fields (`temperature_c`, `breath_pressure_bin`, `captured_at`, `player`) are populated per §4.
3. The corresponding row in `../validation.csv` is updated by hand from `pending` to the captured value and `pass`/`fail` is set against the target column.

Step 3 happens **only after** the validator (§6) reports zero shape errors.

## 6. Validator

```sh
python3 ../scripts/check_measurement_log.py \
  --validation ../validation.csv \
  --log measurement-log-template.csv
```

Checks:

- Every `check` in `validation.csv` appears exactly once as `check_id` in the log.
- No extra `check_id` rows in the log.
- Each non-`pending` `captured_value` row also has non-`pending` `captured_at` and `temperature_c` (or `n/a` if the row's nature allows).

The validator does **not** validate physical reasonableness of values. A
human reviewer must compare each captured value against the target column
in `validation.csv` and call pass/fail.

## 7. Out of scope (residual)

- Manometer-calibrated breath pressure. Optional add-on.
- Multi-player or multi-session aggregation. The template covers one session.
- Long-term drift (humidity, seasonal). Add a fresh log per session.
- L3/L4 promotion. Closing all 20 rows is a *necessary* condition for L3; L3 sign-off also requires the existing `risks.md` and `CHECKLIST.md` review gates.
