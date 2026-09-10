---
type: source
manufacturer: Bruno
model: SRE-3050
doc_type: Tech Support Guide
source: "MANUALS/Bruno/Bruno Straight SL/3050-TS Tech Support Guide 07-14-2023.pdf"
date: 2023-07-14
tags: [stairlift, bruno, sre-3050, troubleshooting]
---

# 3050-TS Tech Support Guide (SRE-3050 Elan)

Field service guide, P/N 3050-TS. Covers SRE-3050, SRE-3050CAN, SRE-3050G
variants.

Key content:
- Technical specifications (ILS-01462): 300 lb capacity, 24VDC/16A direct
  drive self-locking motor (442 lb-in/50Nm torque), 8dp integrated gear
  rack, dynamic + electro-mechanical motor brake + overspeed protection,
  18 ft/min max speed, 15'6" and 19'8" standard rail lengths (cut to fit)
- Drive adjustment: eliminating carriage vibration by seating the pinion
  gear against the rack (loosen 3 drive mounting bolts, adjust jack screw
  1/8 turn increments, re-test)
- Overspeed reset procedure — nearly identical wording/figures to the
  [[SRE-2010]] tech support guide's overspeed section — see
  [[Overspeed-Safety-Brake]]
- Multi-user → single-user diagnostic mode switch (ILS-01539), IR remote
  reprogramming (ILS-01540) — same DIP-switch/LEARN-ERASE procedure as
  [[SRE-2010]]
- Troubleshooting chart and full diagnostic code table (audio/visual codes
  cross-referenced against SRE-3000 and "NEW SRE-2010" boards — same table
  layout Bruno reuses across the Straight SL line)
- **Rail Mounting Guidance (ILS-01512)** — construction-type-specific
  anchoring guidance. Title says "SRE-2010 Model" but this exact document
  (same revision, same figures) is bundled into this SRE-3050 guide too —
  Bruno ships one anchoring reference across both model lines. See
  [[Rail-Mounting-Guidance]].
- Power folding rail: troubleshooting table (stopping-at-mid-park faults,
  power vs. manual), gear rack replacement, joint adjustment, greasing,
  drive adjustment — see [[Folding-Rail]]
- **Brake Troubleshooting for the SRE-3000 and 3050** — explicitly a
  shared procedure across both models (same carriage circuit board
  family): diagnosing a grinding noise / 4-short-beep code / hot brake via
  multimeter voltage tests at the board, then physically testing the
  motor-mounted brake unit (3mm Allen bolts)
- Wiring schematics / exploded views (pp. 28-40, not itemized here)

Feeds: [[SRE-3050]], [[Overspeed-Safety-Brake]], [[Folding-Rail]],
[[Rail-Mounting-Guidance]]
