---
type: manufacturer
manufacturer: Golden
tags: [manufacturer, scooter, power-wheelchair]
---

# Golden (Golden Technologies)

Manufacturer of power scooters and power wheelchairs. Largest manual
collection in this wiki (~60 files), mostly flat under `MANUALS/Golden/`
rather than split into product-line subfolders.

## Model families (by part-number prefix, from filenames — unverified against manual content)

- **GA541 Avenger** — 4-wheel scooter (not a wheelchair — corrected from
  the filename-only stub). 750W rear-wheel drive, PG S-Drive controller,
  500 lb capacity. **Fully ingested** — see [[GA541-Avenger]].
- **GB1xx Buzzaround** (XL / EX / Carry On) — travel scooters.
  **Fully ingested.**
  - [[GB1xx-Buzzaround-XL]] (GB106 "Lite", GB116, GB146, GB147) —
    frame-lock folding design for 106/116/146; GB147 has a different
    tie-rod steering linkage, open question whether it still folds.
  - [[GB118-148-Buzzaround-EX]] — 3-wheel (GB118) vs. 4-wheel (GB148)
    variants of the same "Buzzaround Extreme" platform, dual removable
    battery packs on a shared charging dock.
  - [[GB120-Buzzaround-CarryOn]] — smallest/travel-focused, single
    quick-release lithium battery pack designed for airline carry-on.
  - Brake mechanism is shared with the not-yet-ingested GL110/GL140
    LiteRider (same brake body, model-specific handle).
- **GC2xx/3xx/4xx Companion** — scooters. **Fully ingested.**
  - [[GC221-321-421-Companion]] — older generation, only one document on
    file (potentiometer replacement).
  - [[GC240-340-440-540-Companion]] — current generation. GC240/GC340/
    GC440 share one platform/manual; **GC540 "Companion HD" is a
    genuinely distinct heavier-duty variant** (separate frame, battery,
    controller, seat — only shares the tiller assembly), not a color
    option.
  - The "VA" operator manual variant is Department of Veterans Affairs
    contract packaging, not a state regulatory difference — same product,
    same warranty text, plus an added VA-specific service plan. See
    [[Golden-Scooter-Warranty]].
  - Head-set bearing assembly is explicitly documented as shared across
    "All Companions and LiteRiders" — a real cross-family part.
- **GL1xx LiteRider** — scooters. **Fully ingested.**
  - [[GL110-140-LiteRider]] — older generation (GL110 3-wheel/GL140
    4-wheel), service guide only, no dedicated OM/IPB on file.
  - [[GL111-141-LiteRider]] — current generation, successor to
    GL110/140 (same drivetrain/transaxle part, mostly electronic/cosmetic
    changes). Shares its 90A Dynamics R-Series controller with the
    Companion line (GC240/340/440) — confirmed in the IPB.
  - Brake mechanism shared with Buzzaround XL/Lite (GB106/116/146) — same
    brake body, model-specific handle.
  - Battery replacement doc also covers GP160 LiteRider PTC (not yet
    ingested).
- **GP1xx/GP600s Compass / Alante / LiteRider Envy** — power wheelchairs
  and scooters.
  - GP160: battery replacement (shared w/ GL110/GL140).
  - GP162 LiteRider Envy (incl. LiNX variant): IPB, OM, PTC service guide,
    seat belt.
  - GP204 Alante DX: ELR installation.
  - GP600/GP605/GP615/GP620 Compass (incl. Sport): battery, brake, ELR,
    circuit breaker wiring, footrest, caster spacers.
  - GP303: harness replacement (referenced in a LIT-MB doc, not its own
    folder).
- **Chargers**: HP8204B, MRC24-4LX.

## Cross-cutting / all-models docs

Accessory installs and general tips that aren't model-specific: accessory
receiver, adjustable depth seat, cane/crutch holder, cup holder, oxygen &
walker holder, universal mirror mount, flag installation, seating matrix,
seat measuring, touch-up paint, key/key-switch change, joystick side
conversion, transaxle change, seat belt, Proflex seat, power seat operation,
"Golden Tips".

These are strong candidates for `concepts/` pages (e.g.
[[Battery-Charging]], [[Brake-Replacement]], [[Seat-Systems]]) once ingested,
since they apply across many Golden models and probably overlap with
Bruno/Pride procedures too.

## Cross-model concepts (confirmed so far)

- [[Golden-Scooter-Warranty]] — one warranty policy text explicitly
  covers many scooter models (BUZZaround, LiteRider, Companion, Avenger,
  Patriot), found in the GA541 operator manual and confirmed verbatim
  (under a VA-specific heading) in the Companion VA operator manual.
- [[TruCharge-Diagnostics]] — 10-bar battery/fault display, confirmed on
  GA541 only.
- [[Flash-Beep-Diagnostics]] — a *different* 9-code flash/beep scheme
  tied to the Dynamics R-Series controller, confirmed on the Companion
  line AND both LiteRider generations (GL110/140, GL111/141) — the
  controller family determines which scheme applies, not the model name.
  Golden uses more than one diagnostic scheme across its scooters — don't
  assume either applies to a model without checking its controller.

## Not yet ingested

Everything except GA541 Avenger, the GB1xx Buzzaround family, the
GC2xx/3xx/4xx/5xx Companion family, and the GL1xx LiteRider family. See
`wiki/index.md` for the backlog.
