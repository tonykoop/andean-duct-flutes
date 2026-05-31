# Andean Duct Flutes Build Packet Print Packet

Generated: 2026-05-09
Packet folder: `/tmp/andean-duct-flutes-codex-bob-r3-build-packet`

## File Map

| File | Purpose |
| --- | --- |
| `design.md` | Project intent, catalog metadata, assumptions, and validation plan. |
| `bom.csv` | Starter bill of materials with part categories, quantities, drawing refs, and notes. |
| `sourcing.csv` | Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks. |
| `cut-list.csv` | Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts. |
| `drawing-brief.md` | Manufacturing drawing and technical product sketch brief. |
| `assembly-manual.md` | Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes. |
| `validation.csv` | Target/measured values, tolerance, environment, result, and tuning/build action log. |
| `supplier-rfq.md` | Supplier email/request-for-quote starter. |
| `visual-bom-brief.md` | Art direction for an image-forward visual BOM. |
| `andean-duct-flutes-starter.wl` | Wolfram starter for physics, optimization, visualization, and validation. |
| `CHECKLIST.md` | Project artifact. |
| `README.md` | Project artifact. |
| `family-spec.csv` | Project artifact. |
| `jig-decision.md` | Project artifact. |
| `photo-shotlist.md` | Project artifact. |
| `resources.md` | Project artifact. |
| `review-evidence.md` | Project artifact. |
| `risks.md` | Project artifact. |

<div class="page-break"></div>

## design.md

Project intent, catalog metadata, assumptions, and validation plan.

# Design

## Design Intent

Create an L2 root-mode build packet for a small family of Andean duct flutes
that can be prototyped with PVC before committing to hardwood or bamboo. The
first prototype is a G4 pinkullo-style fipple flute with a removable block so
the windway, window, and labium can be tuned independently from the tube.

This packet supports issue #1 by providing a reviewable shop candidate. It does
not claim L3/build-ready status until the first prototype speaks cleanly and
the tuning rows in `validation.csv` are filled with measured data.

## Governing Model

The starting acoustic model is an open-open pipe:

```text
f = c / (2 * L_eff)
L_eff = L_physical + 2 * 0.6 * radius
c = 13552 in/s at 68 F
```

Tone-hole first pass:

```text
distance_from_foot = acoustic_length * (fundamental_hz / hole_hz)
```

The formula sizes the bore and first-pass holes only. The duct-flute voicing is
empirical: windway height, window length, block fit, labium edge quality, and
breath pressure determine whether the pipe speaks.

## Prototype Family

| Member | Musical role | Fundamental | Bore ID | Physical length | Scale path |
| --- | --- | ---: | ---: | ---: | --- |
| Pinkullo G4 | First prototype | 392.00 Hz | 0.625 in | 16.1 in | pentatonic minor first |
| Tarka A4 | Higher, brighter test | 440.00 Hz | 0.562 in | 14.3 in | pentatonic or hexatonic |
| Small duct flute C5 | Short proof body | 523.25 Hz | 0.500 in | 11.9 in | pentatonic minor |

Physical lengths include first-pass end correction and 0.25 in trimming
allowance. They are deliberately long until measured tuning confirms the
block/window behavior.

## Duct And Window Starter Geometry

| Feature | G4 starter | Validation note |
| --- | ---: | --- |
| Windway height | 0.040 in | Shim down if breath is noisy; open slightly if it chokes |
| Windway width | 0.50 in | About 80% of bore ID |
| Window length | 0.45 in | File after first sound |
| Labium angle | 35 deg | Keep edge crisp and centered |
| Block insertion | 1.00 in | Waxed fit for removable first prototype |
| Window setback from head | 0.75 in | Mark from head datum before cutting |

## Scale Options

Pentatonic minor offsets are the first tuning target: `0, +3, +5, +7, +10,
+12`. A hexatonic/diatonic test can be drilled on a sacrificial PVC body after
the pentatonic body validates the duct geometry. Do not mix scale experiments
with the first voicing validation body.

## Materials

- PVC proof-of-tune: 1/2 in nominal pipe or tube stock with measured actual ID.
- Hardwood follow-up: straight-grain cherry, maple, or walnut blank.
- Bamboo follow-up: only after node spacing and wall thickness are measured.
- Block: cedar, maple, or Delrin insert, fitted airtight but removable.

## SolidWorks/OpenSCAD Handoff

This packet does not include production CAD. The first geometry handoff should
be a simple axisymmetric bore plus rectangular window/block model with named
inputs for bore ID, OD, body length, window length, windway height, and hole
stations. CAD should not be treated as final until the G4 PVC body validates
the windway/window relationship.

## L2 To L3 Gates

- G4 prototype speaks at low and medium breath pressure.
- Fundamental and five tone holes are within +/-15 cents before final tuning.
- Final trim brings the scale within +/-8 cents or records why that target is
not practical.
- Block can be removed and reinstalled without changing pitch by more than
5 cents.
- A hardwood or bamboo body copies only measured PVC geometry, not estimates.

<div class="page-break"></div>

## bom.csv

Starter bill of materials with part categories, quantities, drawing refs, and notes.

| item | qty | unit | estimated_cost | notes |
| --- | --- | --- | --- | --- |
| PVC proof tube 0.625 in ID | 2 | each | derived estimate 12 | Measure actual ID before calculating length |
| Cherry or maple blank 1 x 1 x 24 in | 1 | each | derived estimate 18 | Hardwood follow-up after PVC validates voicing |
| Cedar or maple block stock | 3 | blanks | derived estimate 6 | Removable fipple blocks and spares |
| Beeswax/paraffin sealing wax | 1 | small block | derived estimate 4 | Temporary leak sealing and block fit tests |
| Small cork/rubber sheet | 1 | sheet | derived estimate 5 | Optional block shims |
| Sandpaper 220-600 grit | 1 | set | derived estimate 8 | Labium edge and finish |
| Mineral oil or shellac | 1 | small bottle | derived estimate 10 | Final finish after tuning |

<div class="page-break"></div>

## sourcing.csv

Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks.

| item | required_spec | search_terms | preferred_source | current_check_needed | substitution_notes |
| --- | --- | --- | --- | --- | --- |
| PVC proof tube | measured 0.625 in ID or closest stable tube | rigid pvc tube 5/8 id | local hardware or plastics supplier | yes | Use measured ID in design table |
| Hardwood blank | straight grain 1 x 1 x 24 in cherry maple or walnut | cherry turning blank 1x1x24 | wood supplier | yes | Only after PVC duct geometry is validated |
| Block stock | dry cedar maple or Delrin insert stock | cedar block stock delrin rod | shop scrap or plastics supplier | yes | Must fit airtight and remain removable |
| Wax | beeswax or paraffin for temporary sealing | beeswax block paraffin | craft or hardware store | yes | Used for leak tests not final glue |
| Finish | non-toxic oil or shellac | food safe mineral oil shellac flakes | woodworking supplier | yes | Apply after tuning is stable |

<div class="page-break"></div>

## cut-list.csv

Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts.

| part | qty | material | rough_dimensions_in | final_dimensions_in | operation_notes |
| --- | --- | --- | --- | --- | --- |
| G4 PVC body | 2 | PVC tube | 0.875 OD x 17.0 long | 0.875 OD x 16.10 long plus trim | Leave 0.25 in extra until tuning |
| G4 hardwood body | 1 | cherry or maple | 1.00 x 1.00 x 18.0 | 0.875 OD x measured tuned length | Build only after PVC validation |
| Removable block blanks | 3 | cedar maple or Delrin | 0.60 x 0.60 x 1.25 | fit to bore x 1.00 long | Plane/sand to airtight slip fit |
| Fipple window coupon | 3 | same as body stock | 2.0 long offcuts | window test coupons | Practice window and labium before body cut |
| Hole-layout story stick | 1 | plywood or acrylic | 1.0 x 18.0 | marked stations from foot datum | Use for drilling repeatability |

<div class="page-break"></div>

## drawing-brief.md

Manufacturing drawing and technical product sketch brief.

# Drawing Brief

## Required Sheets

1. Overall G4 body elevation with head datum, foot datum, window setback, and
   all tone-hole stations.
2. Bore and block section showing removable fipple block, windway height, and
   leak-control surfaces.
3. Window/labium detail with windway width, window length, ramp angle, and edge
   note.
4. Drill jig/story-stick layout for repeatable hole placement.

## Datum Scheme

- A: bore centerline.
- B: foot end after square trim.
- C: top surface orientation through window and front holes.

All tone-hole stations are measured from datum B. Window and block dimensions
are measured from the head end and cross-checked to datum A.

## Tolerance Notes

- Bore ID is measured, not assumed from nominal pipe size.
- Tone holes start undersize; final diameters are validation outputs.
- Windway height is a controlled empirical variable and should be called out as
  adjustable on the drawing.

<div class="page-break"></div>

## assembly-manual.md

Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes.

# Assembly Manual

## Scope

This manual covers the G4 PVC proof-of-tune body. Hardwood or bamboo bodies
should copy only the measured geometry from a successful PVC prototype.

## Steps

1. Measure the tube ID, OD, and straightness at three stations.
2. Cut the body 0.25 in long and square both ends.
3. Mark the head datum, window setback, and foot datum.
4. Cut a conservative rectangular window and leave the labium edge slightly
   heavy for hand finishing.
5. Fit a removable block so the windway is centered and airtight.
6. Shim or sand the windway toward the 0.040 in starter height.
7. Form the labium ramp to about 35 degrees and sharpen the edge.
8. Play first sound before drilling any finger holes.
9. Adjust window length and windway height until response is repeatable at low
   and medium breath pressure.
10. Drill tone holes undersize from the foot upward.
11. Tune by gradual enlargement, recording final diameters in `validation.csv`.
12. Trim the foot only after the scale is stable.
13. Photograph the block, window, labium, and final hole layout for the build
   log.

## Stop Conditions

- Stop if the block leaks enough to change response after reinstalling.
- Stop if the labium edge chips or tears; make a window coupon before recutting
  the body.
- Stop if the first tone requires high breath pressure only; fix voicing before
  drilling tone holes.

<div class="page-break"></div>

## validation.csv

Target/measured values, tolerance, environment, result, and tuning/build action log.

| check | target | method | tool | actual | pass | notes |
| --- | --- | --- | --- | --- | --- | --- |
| Actual bore ID | 0.625 in +/- measured tolerance | inside caliper at three stations | digital caliper | pending | pending | Recalculate length if tube ID differs |
| First sound response | stable tone at low and medium breath | play test with same player | shop notes | pending | pending | Record breath-pressure bin |
| Fundamental G4 | 392.00 Hz +/- 15 cents before trim | chromatic tuner at 68 F | tuner | pending | pending | Trim foot after block/window settle |
| Pentatonic hole 1 | +3 semitones from fundamental | drill undersize then enlarge | tuner | pending | pending | Tune from foot upward |
| Pentatonic hole 2 | +5 semitones from fundamental | drill undersize then enlarge | tuner | pending | pending | Log hole diameter after tuning |
| Pentatonic hole 3 | +7 semitones from fundamental | drill undersize then enlarge | tuner | pending | pending | Watch cross-fingering leakage |
| Pentatonic hole 4 | +10 semitones from fundamental | drill undersize then enlarge | tuner | pending | pending | Keep ergonomic reach under review |
| Octave response | +12 semitones accessible with breath shift | play test | tuner | pending | pending | Do not overclaim until repeatable |
| Block reinstall repeatability | within 5 cents after removal/reinstall | tuner before/after | tuner | pending | pending | Reject loose block fit |
| Leak check | no audible leak around block or window | soap bubble or breath hold | visual/play test | pending | pending | Wax temporary leaks before final fit |

<div class="page-break"></div>

## supplier-rfq.md

Supplier email/request-for-quote starter.

# Supplier RFQ

## Request

Please quote the following public-safe, non-proprietary instrument-build
materials or fabrication services.

## Items

- Item: TBD
- Quantity: TBD
- Material/spec: TBD
- Tolerance: TBD
- Finish: TBD
- Lead time target: TBD

<div class="page-break"></div>

## visual-bom-brief.md

Art direction for an image-forward visual BOM.

# Visual BOM Brief

Create a single-page visual BOM after the first prototype is cut. Required
image panels:

- PVC proof body before window cutting.
- Removable block blanks and fitted block.
- Window/labium close-up.
- Hole-layout story stick.
- Tuning tools: tuner, caliper, drill index, files, wax.

Each row should include quantity, material, final dimensions, and which
validation row confirms the part.

<div class="page-break"></div>

## andean-duct-flutes-starter.wl

Wolfram starter for physics, optimization, visualization, and validation.

```wolfram
(* Andean duct flute starter: open-pipe length and first-pass holes. *)

ClearAll["Global`*"];

cInPerSec = 13552;
a4 = 440;
fundamentalHz = 392.0;
boreIn = 0.625;
radiusIn = boreIn/2;
endCorrectionIn = 2*0.6*radiusIn;

targetHz[midi_] := a4*2^((midi - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
physicalLengthForHz[f_] := cInPerSec/(2*f) - endCorrectionIn;

scaleOffsets = {0, 3, 5, 7, 10, 12};
scaleTable = Table[
  With[{f = fundamentalHz*2^(offset/12)},
    <|
      "OffsetSemitones" -> offset,
      "TargetHz" -> f,
      "DistanceFromFootIn" -> physicalLengthForHz[fundamentalHz]*(fundamentalHz/f)
    |>
  ],
  {offset, scaleOffsets}
];

Dataset[scaleTable]

(* Validation reminder: duct/window response is empirical and must be measured
   before this model is used for a hardwood or bamboo body. *)
```

<div class="page-break"></div>

## CHECKLIST.md

Project artifact.

# Public-Ready Checklist

## Readiness Level

- [ ] L0 Concept: target sound, family, and rough build method are documented.
- [ ] L1 Design: governing equations, assumptions, dimensions, BOM, and sourcing candidates are present.
- [ ] L2 Shop Packet: build sequence, drawings/briefs, cut list, validation checklist, hazards, and artifact paths are complete enough for careful builder review.
- [ ] L3 Validated Packet: validator passes, generated/rendered artifacts open, units are consistent, and sourceability/tolerance claims are checked.
- [ ] L4 Empirical Packet: measured build data, tuning deviations, correction loop, and catalog feedback are included.

Only L3 or L4 work should be described as build-ready.

## Packet Completeness

- [ ] Replace `Andean Duct Flutes`, `L2 root-mode build packet for Andean duct flutes: pinkullo, tarka, and related fipple flutes.`, and other placeholders.
- [ ] Add cultural attribution and sources of inspiration.
- [ ] Replace placeholder photos with owned photos, renders, or honest public-safe placeholders.
- [ ] Fill `design.md` with instrument-specific governing equations and assumptions.
- [ ] Fill BOM, sourcing, cut list, validation, and family spec rows with non-placeholder values.
- [ ] Add OpenSCAD/SolidWorks/Wolfram handoff notes without pretending final CAD exists.
- [ ] Add drawings and a CNC/setup plan where applicable.
- [ ] Fill `resources.md` with public-safe provenance, education, maker, and license notes.
- [ ] Fill `jig-decision.md` for any make/order/buy/borrow fixture decisions.
- [ ] Run `instrument-maker-v4/scripts/validate_packet.py . --mode root --json`.
- [ ] Confirm no local absolute paths, private repo links, or frozen supplier-price claims.

## Review Evidence

- [ ] PR body includes changed behavior/artifact, physics/manufacturing assumptions, validation run, known gaps, reviewer focus, and do-not-merge-until bar.
- [ ] Physics gate passed: model, assumptions, units, tuning targets, and sensitivity ranges are reviewable.
- [ ] Manufacturing gate passed: toolchain, materials, tolerances, cut lists/jigs/CAD, and assembly order are plausible.
- [ ] Safety gate passed: dust, finishes, adhesives, sharp tools, tension, heat/pressure/electrical risks, and workshop constraints are addressed.
- [ ] Artifact gate passed: BOM, sourcing, cut list, validation, risks, drawings/CAD briefs, and rendered/generated artifacts are present or gaps are named.
- [ ] Empirical gate passed: measurement plan, pass/fail criteria, tuning correction path, and catalog feedback destination are stated.

<div class="page-break"></div>

## README.md

Project artifact.

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
| `andean-duct-flutes-starter.wl` | Parametric frequency and hole-position starter |

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

<div class="page-break"></div>

## family-spec.csv

Project artifact.

| member_id | name | fundamental_hz | bore_id_in | od_in | physical_length_in | windway_height_in | windway_width_in | window_length_in | labium_angle_deg | scale_offsets | prototype_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADF-G4-P1 | Pinkullo G4 first prototype | 392.00 | 0.625 | 0.875 | 16.10 | 0.040 | 0.500 | 0.450 | 35 | 0 3 5 7 10 12 | PVC proof-of-tune |
| ADF-A4-P2 | Tarka A4 high prototype | 440.00 | 0.562 | 0.812 | 14.30 | 0.036 | 0.450 | 0.400 | 35 | 0 3 5 7 10 12 | queued after G4 voicing |
| ADF-C5-P3 | Small duct flute C5 proof body | 523.25 | 0.500 | 0.750 | 11.90 | 0.032 | 0.400 | 0.350 | 35 | 0 3 5 7 10 12 | scale experiment body |

<div class="page-break"></div>

## jig-decision.md

Project artifact.

# Jig Decision

| Operation | Jig choice | Reason | Release check |
| --- | --- | --- | --- |
| Body drilling/holding | V-block with centerline fence | Keeps round tube stable without crushing | Tube cannot roll under hand pressure |
| Window cutting | Clamp-on window guide | Protects setback and square shoulders | Test on coupon before body |
| Block fitting | Bore-matched sanding mandrel | Lets block fit be tuned gradually | Block seals and can be removed |
| Tone-hole drilling | Story stick plus V-block | Faster than CNC for L2 proof body | Stations match drawing within 0.02 in |
| Foot trimming | Miter box or lathe facing | Keeps foot square during tuning | End remains square after each trim |

<div class="page-break"></div>

## photo-shotlist.md

Project artifact.

# Photo Shotlist

- Hero image of completed instrument or honest concept placeholder.
- Scale reference with ruler/calipers.
- Material blank before cutting.
- Key operations and jigs.
- Detail shots of acoustic features.
- Final validation setup.

<div class="page-break"></div>

## resources.md

Project artifact.

# Resources

## Cultural Context

This packet treats Andean duct flutes as living Indigenous and regional
instruments, not generic "folk flutes." Public-facing writing should identify
the specific form being built when known, such as pinkullo or tarka, and avoid
claiming authenticity for a workshop prototype.

## Engineering References To Gather Before L3

- Measured examples of pinkullo/tarka bore, window, and block geometry.
- Player demonstrations showing breath pressure and articulation.
- Photos of duct/window construction from makers who permit reference use.
- Temperature and humidity notes from the tuning session.

## Related Repos

- `tonykoop/instrument-maker` for governing formulas and packet validation.
- `tonykoop/siku-zampona` for Andean provenance handling and pipe-array tuning
  discipline.
- `tonykoop/flutes` for general wind-instrument measurement habits. NAF K2
  corrections do not transfer to this duct-flute packet.

<div class="page-break"></div>

## review-evidence.md

Project artifact.

# Review Evidence

Refs #1.

## Round 3 Scope

- Added an L2 root-mode build packet scaffold and hand-tuned it for Andean
  duct-flute specifics: fipple block, windway, window/labium, breath pressure,
  pentatonic-first scale validation, and PVC-to-hardwood/bamboo prototype path.
- This packet does not claim L3/build-ready status.

## Gates Before Close

- Build and measure the G4 proof-of-tune body.
- Record actual bore ID, block reinstall repeatability, breath response, final
  hole diameters, and cents error in `validation.csv`.
- Promote measured duct/window geometry before cutting a hardwood or bamboo
  body.

<div class="page-break"></div>

## risks.md

Project artifact.

# Risks

| ID | Category | Risk | Verification test | Mitigation |
| --- | --- | --- | --- | --- |
| ADF-AC-01 | Acoustic | Duct/window geometry does not speak below high breath pressure | First-sound test before drilling holes | Keep block removable; tune windway/window first |
| ADF-AC-02 | Acoustic | Tone-hole formula misses because effective open point shifts | Drill undersize and log final diameters | Tune from foot upward and update design table |
| ADF-ST-01 | Structural | Labium edge chips in hardwood | Cut window coupon first | Use PVC proof body and sharp tools |
| ADF-ER-01 | Ergonomic | Hole spacing is too wide on low member | Paper reach test and mock grip | Start with G4 before lower tarka body |
| ADF-SU-01 | Supply | Nominal PVC ID differs from formula assumptions | Measure ID at intake | Recalculate length with measured bore |
| ADF-FI-01 | Fit/finish | Removable block leaks or shifts after reinstall | Tuner before/after block reinstall | Shim/wax block; reject loose fit |
