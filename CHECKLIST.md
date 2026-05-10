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
