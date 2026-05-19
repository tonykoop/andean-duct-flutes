# Duct Flute Acoustic Law (L1/L2 Scaffold)

Status: validation scaffold. This document makes the governing acoustic model
explicit so that future measurements have a place to land. It does **not**
create build-ready tuning. Final fundamental, hole positions, windway, and
labium dimensions are decided by measurement on a physical prototype, not by
the equations below.

## Scope

Applies to the duct flutes in this family (pinkullo G4, tarka A4, small duct
flute C5). Each member is treated as a **duct + window + open tube** acoustic
system. The equations here size the air column and a first-pass tone-hole
schedule. Voicing (windway height, window length, labium angle, breath
pressure) is empirical and is captured in `validation.csv`, not in this doc.

## Boundary Conditions

The duct flute behaves as three coupled elements. Each element has a stated
boundary condition that must be true for the next stage to apply.

| Element | Boundary condition | Why it matters |
| --- | --- | --- |
| Duct (flue/windway) | Air jet exits the windway as a flat sheet of width `w_w` and height `h_w`, aimed at the labium. The block is airtight enough that the only meaningful air path is through the windway. | If the block leaks or the windway is uneven, jet formation fails and the rest of the model does not apply. |
| Edge tone | Jet impinges on the labium at angle `theta_l` with a free jet length `L_j` between windway exit and labium tip. Edge-tone oscillation seeds the pipe. | If edge-tone is absent (no sound) or unstable (multiphonics, breathy hiss), the pipe selection law below is meaningless. |
| Open tube (pipe) | Acoustic pressure node at the open foot **and** at the window opening (open-open boundary, first approximation). Effective length is the physical column plus end corrections at each open end. | This is the equation that turns geometry into a predicted fundamental. It is only valid once the duct and edge-tone elements are working. |

The open-open assumption is a **first-pass simplification**. Real fipple flutes
sit between open-open and open-closed depending on window size, labium geometry,
and player technique. The true effective length is measured, not assumed.

## Governing Equation (Air Column, First Pass)

```text
f_n   = n * c / (2 * L_eff)         # n = 1, 2, ... for open-open
L_eff = L_phys + dL_foot + dL_window
c     = c0 * sqrt(T_K / T0_K)       # speed of sound vs. absolute temperature
c0    = 13552 in/s at T0 = 293.15 K (20 C / 68 F) in dry air
```

`dL_foot` is the end correction at the open foot. `dL_window` is the end
correction at the window. Both are **unknown until measured** for this family.
A textbook starting estimate is `dL ≈ 0.6 * r` per open end for an unflanged
circular opening, but the window is rectangular and the foot may have a chamfer
or wall thickness that shifts the value. Treat 0.6r as a seed, not a fact.

## Tone Hole First-Pass Equation

```text
x_hole = L_eff * (f_fundamental / f_hole)
```

`x_hole` is the distance from the foot to the center of a tone hole that would
produce `f_hole` if it were the new effective foot of the pipe. This ignores
finite hole diameter, wall thickness, cross-fingering, and chimney correction.
Holes are drilled **undersize** and tuned by controlled enlargement from foot
toward head, with each measured value logged in `validation.csv`.

## Unknown Measurement Fields

The following values are unknown until a physical prototype is measured. They
are listed here so that future builds have an unambiguous place to capture
them. Until each field has a measured value, downstream geometry derived from
that field is provisional.

| Field | Symbol | Unit | Status | Capture location |
| --- | --- | --- | --- | --- |
| Ambient temperature at measurement | T_meas | C (or F) | unknown | validation.csv |
| Speed of sound at T_meas | c_meas | in/s | unknown (derive from T_meas) | validation.csv |
| Measured fundamental | f_meas | Hz | unknown | validation.csv |
| Measured effective length | L_eff_meas | in | unknown | validation.csv |
| Window end correction | dL_window | in | unknown | validation.csv |
| Foot end correction | dL_foot | in | unknown | validation.csv |
| Free jet length (windway exit to labium) | L_j | in | unknown | validation.csv |
| Edge-tone speak threshold (low breath bin) | p_breath_min | qualitative | unknown | validation.csv |
| Hole chimney correction (per hole) | dL_hole_i | in | unknown | validation.csv |
| Block-removal pitch drift | df_block | cents | unknown | validation.csv |

Empty rows in `validation.csv` for these fields are intentional. They are not
TODOs to be filled by analysis; they require a first physical prototype.

## What This Doc Does Not Do

- It does **not** declare any geometry in this repo build-ready.
- It does **not** set a final speed-of-sound value. `c` depends on T_meas.
- It does **not** replace voicing skill. Windway geometry, labium edge
  quality, and player breath are empirical.
- It does **not** transfer between members of the family. A measurement on
  the G4 prototype releases the G4 prototype only.

## Refs

- Issue #1
- `design.md` (governing model summary)
- `validation.csv` (measurement log placeholders)
- `family-spec.csv` (per-member starter geometry)
