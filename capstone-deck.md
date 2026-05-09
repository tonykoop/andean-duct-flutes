# Andean Duct Flutes Build Packet
- Musical instrument documentation capstone
- Build packet: andean-duct-flutes-codex-bob-r3-build-packet
- Generated: 2026-05-09

---

# Project Intent
- Create an L2 root-mode build packet for a small family of Andean duct flutes
that can be prototyped with PVC before committing to hardwood or bamboo. The
first prototype is a G4 pinkullo-style fipple flute with a removable block so
the windway, window, and labium can be tuned independently from the tube.

_Speaker notes:_ Read design.md before committing to dimensions or sourcing decisions.

---

# Physics Model
- The starting acoustic model is an open-open pipe:

```
f = c / (2 * L_eff)
L_eff = L_physical + 2 * 0.6 * radius
c = 13552 in/s at 68 F
```

```
distance_from_foot = acoustic_length * (fundamental_hz / hole_hz)
```

_Speaker notes:_ Governing equations extracted verbatim from design.md. Apply empirical corrections (NAF K2, scale offsets) only where the model permits — see references/acoustic-models.md.

---

# How To Use This Packet
- Start with design.md for intent and assumptions.
- Use bom.csv, sourcing.csv, and cut-list.csv before buying or cutting.
- Use drawing-brief.md and CAD/CNC folders before machining.
- Print the packet for shopping, shop work, and validation.

---

# File Map
- design.md: Project intent, catalog metadata, assumptions, and validation plan.
- bom.csv: Starter bill of materials with part categories, quantities, drawing refs, and notes.
- sourcing.csv: Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks.
- cut-list.csv: Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts.
- drawing-brief.md: Manufacturing drawing and technical product sketch brief.
- assembly-manual.md: Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes.
- validation.csv: Target/measured values, tolerance, environment, result, and tuning/build action log.
- supplier-rfq.md: Supplier email/request-for-quote starter.

---

# Family Spec

| member_id | name | fundamental_hz | bore_id_in | od_in | physical_length_in | windway_height_in | windway_width_in | window_length_in | labium_angle_deg | scale_offsets | prototype_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADF-G4-P1 | Pinkullo G4 first prototype | 392.00 | 0.625 | 0.875 | 16.10 | 0.040 | 0.500 | 0.450 | 35 | 0 3 5 7 10 12 | PVC proof-of-tune |
| ADF-A4-P2 | Tarka A4 high prototype | 440.00 | 0.562 | 0.812 | 14.30 | 0.036 | 0.450 | 0.400 | 35 | 0 3 5 7 10 12 | queued after G4 voicing |
| ADF-C5-P3 | Small duct flute C5 proof body | 523.25 | 0.500 | 0.750 | 11.90 | 0.032 | 0.400 | 0.350 | 35 | 0 3 5 7 10 12 | scale experiment body |

_Speaker notes:_ Sizes scale via the master scale factor; tuning targets are first-order Helmholtz/cantilever predictions to be empirically corrected per prototype.

---

# Build Workflow
- Design and assumptions
- Source materials and hardware
- Prepare stock, fixtures, and CNC/laser/lathe setup
- Assemble, tune, finish, and validate

---

# Sourcing And BOM
- BOM gives part categories and drawing references.
- Sourcing tracks search terms, supplier candidates, price/date, lead time, substitutions.
- Visual BOM brief turns the parts list into a presentation-ready image board.

---

# Shop Packet
- Cut list for lumber/sheet/blank planning.
- Assembly manual for away-from-keyboard work.
- Validation sheet for measured dimensions, tuning, pass/fail checks.

---

# Drawings, CAD, CNC
- drawing-brief.md defines required views, dimensions, datums, sketch intent.
- cad/ holds models and design tables.
- cnc/ holds CAM, toolpaths, setup sheets, dry-run notes.
- drawings/ holds PDFs, SVGs, DXFs, drawing exports.

---

# Images And Screenshots
- Add hero render/photo, visual BOM, shop screenshots, drawing previews, validation photos in images/.

---

# Validation Plan
- A4 = 440 Hz reference check.
- Tuning targets logged in validation.csv.
- Critical dimensions verified against design sheet and CAD.
- Photos and revision notes after each major step.

---

# Open Risks / Decisions
- TBDs in design sheet and BOM.
- Supplier price/availability not yet verified.
- Generated images marked as concept placeholders.
- Empirical corrections await measured prototype data.

---

# Next Actions
- Replace TBDs with measured/source-backed values.
- Verify live supplier price and availability before buying.
- Export final drawings and visual BOM images.
- Regenerate this deck and print packet after final edits.

---
