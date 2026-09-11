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
- **GP1xx/GP6xx Compass / Alante / LiteRider Envy / Ally** — power
  wheelchairs. **Fully ingested.**
  - [[GP162-LiteRider-Envy]] — sold under one model number with **two
    different controller families**: PTC/PG VR2 (10-bar
    [[TruCharge-Diagnostics]], wheelchair-adapted) and LiNX (7-code
    [[LiNX-Diagnostics]], plus OONAPU power-up interlock).
  - [[GP204-Alante-DX]] — thin coverage, one ELR install doc; shares
    legrest hardware with Alante GP201 and Compass Sport GP605.
  - [[GP6xx-Compass]] (GP600/605/615/620) — GP605 "Compass Sport" uses a
    **"SHARK"**-branded controller, a fourth Golden controller family
    beyond PG VR2/LiNX and Dynamics R-Series, with no diagnostic table on
    file yet.
  - [[GP303-Ally]] — **not** a Compass variant despite the "GP" prefix; a
    distinct foldable-frame power wheelchair. Was misfiled by number
    during initial clustering, corrected after reading content.
  - GP160 battery replacement doc was already covered under
    [[GL110-140-LiteRider]] (cross-listed there).
- **Chargers**: HP8204B, MRC24-4LX. **Fully ingested** — see
  [[Golden-Battery-Charging]].

## Cross-cutting / all-models docs — Fully ingested.

22 documents that aren't model-specific, filed as 8 concept pages by
actual topic rather than one page per document:

- [[Golden-Accessory-Installs]] — accessory receiver, adjustable depth
  seat, cane/crutch holder, cup holder, oxygen/walker holder, universal
  mirror mount, flag installation, seat belt (8 docs, all short universal
  install sheets)
- [[Golden-Battery-Charging]] — HP8204B and MRC24-4LX charger operation,
  plus general battery care guidance (4 docs)
- [[Golden-Seating-Systems]] — seat size-code catalog/fitment matrix
  (SM4/SM5/SM9/SMP/SMV etc.), measuring procedure, and the physical
  Proflex seating base behind the "SMP" code (4 docs) — surfaces several
  models with no manuals on file yet: GR575 (Patriot), GP205, GP207, GP208
- [[Golden-Dealer-Tips]] — general reminders (incl. the only mention of
  **lift chairs** anywhere in this collection — no lift chair manuals on
  file) and cosmetic touch-up paint tips (2 docs)
- [[Golden-Key-Switch-Replacement]] — universal key/key-switch swap
- [[Golden-Joystick-Side-Conversion]] — Shark-controller joystick
  right-to-left conversion, ties to [[GP6xx-Compass]]'s SHARK controller
- [[Golden-Transaxle-Replacement]] — cross-model doc explicitly naming
  [[GL110-140-LiteRider]] and [[GB1xx-Buzzaround-XL]], mandatory paired
  controller swap
- [[Golden-Power-Seat-Operation]] — speed/height interlock on power-
  elevating seats, ties to [[GP6xx-Compass]]'s GP600

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
- [[LiNX-Diagnostics]] — a third scheme (7-code), confirmed on GP162's
  LiNX-controller variant only so far.
- [[Golden-Wheelchair-Warranty]] — a **separate** warranty policy from
  [[Golden-Scooter-Warranty]], confirmed by the GP162 LiNX owner's manual:
  Golden maintains distinct warranty documents for scooters vs. power
  wheelchairs (GP162, GP205, GP207, GP605, GP620 named).

Golden uses at least four controller brands (PG S-Drive/VR2, LiNX,
Dynamics R-Series, and GP605's "SHARK") and three diagnostic schemes
across scooters and wheelchairs — always check the controller before
assuming any scheme or warranty applies to a model without checking its
own documentation.

## Not yet ingested

Nothing — **all 66 Golden manuals on disk have been ingested.**
