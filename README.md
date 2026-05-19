# Andean Duct Flutes

> L2 root-mode build packet for a small Andean duct-flute family: pinkullo,
> tarka, and related fipple flutes.

![Hero photo placeholder](images/README-placeholder.txt)

## What This Is

This repository documents a contemporary workshop build packet for Andean
duct flutes: block-and-window flutes where a windway directs the player's air
jet across a labium. The first build target is a **G4 pinkullo-style
prototype** because it is large enough to make the duct geometry forgiving,
short enough for common stock, and useful as a reference before lower tarka
members are attempted.

The packet is intentionally **L2, not L3**. It is ready for review as a
shop-packet candidate, but it is not build-ready until the windway, window,
breath pressure, and tuning data are measured on a physical prototype.

The acoustic model in this repo is an **L1/L2 validation scaffold only**. See
[`reference/duct-flute-acoustic-law.md`](reference/duct-flute-acoustic-law.md)
for the explicit duct/flue/edge-tone/pipe boundary conditions, end-correction
treatment, and the list of measurement fields that are still unknown. The
scaffold does **not** create build-ready tuning. Final fundamental, hole
positions, and voicing are decided by measurement on a first prototype, not by
the equations.

Refs #1.

## Design Overview

| Topic | Packet decision |
| --- | --- |
| Governing model | Open-open pipe first pass: `f = c / (2 * L_eff)` |
| Voicing model | Duct windway plus window/labium; empirical breath-pressure validation required |
| First prototype | G4 pinkullo-style duct flute |
| Scale options | Pentatonic minor first, hexatonic/diatonic variant after tone-hole validation |
| Materials | PVC proof-of-tune body first; hardwood or bamboo second |
| Manufacturing path | Drill/ream bore, cut fipple window, fit block, drill undersize holes, tune by controlled enlargement |

## Why Duct Geometry Is The Center Of The Packet

The tube length equation only sizes the air column. The instrument will not
speak cleanly unless the duct and labium are tuned together:

- windway height starts near 0.040 in for the G4 prototype and is adjusted for
  response, not volume;
- window length starts at 0.45 in and is filed after first-sound tests;
- labium ramp angle starts near 35 degrees, with a crisp edge and no torn grain;
- block fit must be airtight enough that breath energy exits through the
  windway, not around the plug;
- breath pressure is logged as low/medium/high subjective bins until a manometer
  test is added.

## Packet Map

| Path | Purpose |
| --- | --- |
| `design.md` | Governing model, duct geometry, scale options, and assumptions |
| `family-spec.csv` | G4/A4/C5 starter family with bore, length, window, and hole schedule summary |
| `bom.csv` | Materials and tooling for PVC proof-of-tune plus hardwood follow-up |
| `sourcing.csv` | Source/spec tracker; current prices still require live purchasing checks |
| `cut-list.csv` | Body, block, test coupons, and jig blanks |
| `assembly-manual.md` | Shop sequence from blank prep through first tuning |
| `validation.csv` | Pitch, response, leak, and breath-pressure checks |
| `drawing-brief.md` | Required drawing sheets and datum scheme |
| `visual-bom-brief.md` | Visual BOM plate plan |
| `jig-decision.md` | Drill V-block, fipple-window guide, and hole-layout fixture choices |
| `resources.md` | Cultural and engineering reference plan |
| `risks.md` | Acoustic, structural, ergonomic, sourcing, and finish risks |
| `wolfram-starter.wl` | Parametric frequency and hole-position starter |
| `reference/duct-flute-acoustic-law.md` | Explicit duct/flue/edge-tone/pipe model, end-correction treatment, and unknown-measurement fields |

## Build Order

1. Build PVC G4 proof-of-tune body and keep the duct block removable.
2. Establish repeatable first sound at low and medium breath pressure.
3. Drill tone holes undersize and tune from foot to head.
4. Record frequency and response data in `validation.csv`.
5. Transfer only the measured duct/window geometry to hardwood or bamboo.

## Status

| Area | Status |
| --- | --- |
| Packet docs | L2 root-mode candidate |
| Drawings/CAD | Drawing brief and starter fixture plan included |
| Photos | Placeholder only |
| Validation | Planned, no measured prototype yet |
| Issue linkage | Refs #1, does not close #1 |

## License

[CC BY 4.0](LICENSE) - engineering documentation only. This packet is a
contemporary workshop interpretation and is not a claim of cultural ownership.
