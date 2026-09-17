---
type: index
---

# Index

Entry point for every query — check here first before opening raw manuals.

## Manufacturers

| Manufacturer | Page | Manuals on disk | Ingested |
|---|---|---|---|
| Bruno | [[Bruno]] | 19 | 19 |
| Golden | [[Golden]] | 66 | 66 |
| Pride | [[Pride]] | 10 | 10 |
| Prism | [[Prism]] | 1 | 1 |
| Harmar | [[Harmar]] | 60 | 32 source pages (see note — several consolidate multiple low-narrative files) |
| AutoSlide | [[AutoSlide]] | 2 | 2 — **different product category**, see note below |
| Ramps | *(not yet ingested)* | 6 | 0 — new backlog category, see Ingestion backlog below |

Note: Bruno's on-disk count dropped from 20 to 19 because one file
(`HARMAR Camera Measuring Manual.pdf`, physically under
`MANUALS/Bruno/Bruno Curved SL/`) is counted under Harmar instead — a
different manufacturer's document, not moved since raw sources are
immutable. See [[Harmar]] and [[Bruno]] for details.

Note: Golden's 66-file on-disk count includes one byte-identical duplicate
PDF saved under two filenames (confirmed by md5) — 65 distinct documents,
65 source pages. See [[Golden]] for details.

Note: **AutoSlide is not mobility equipment** — it's an automatic sliding-
door retrofit kit, a different product category from every other
manufacturer in this wiki. Its 2 raw files were found outside this repo (at
`/home/lu/Work/MANUALS/`, not `/home/lu/Work/llm-wiki/MANUALS/`) and copied
in preserving their original foldering: `MANUALS/AutoSlide/` (the main
install manual) and `MANUALS/Open Sesame/` (an RFID pet-sensor accessory
manual that is, confusingly, entirely AutoSlide-branded — folder name
doesn't match content, not confirmed whether this is a misfile or a real
second brand/reseller name). See [[AutoSlide]] for the open questions this
raised, including whether it belongs in this wiki's stated scope at all.

Note: Harmar's 60-file on-disk count (59 files in `MANUALS/Harmar/` after
two ingest passes, plus the 1 misfiled Bruno-folder file already counted
under Bruno) includes several sets of byte-identical duplicate PDFs
(AL100/AL300/AL301 owner's manuals; AL100/AL300/AL301 install manuals;
an al-100-12 assembly-drawing pair; 2 exact-duplicate Helix files not
even copied into the wiki's MANUALS folder since the content was already
on file) confirmed by md5. The 32 source pages also **consolidate**
several low-narrative-value file groups — 6 sales order/evaluation forms
into one page, 4 marketing spec sheets into one page, 9 engineering
parts-diagram drawings into one page, 6 wiring-schematic drawings into
one page — rather than a strict 1:1 file-to-page mapping. 7 image/CSV
files (product photos, a DAM metadata export) were deliberately excluded
as non-manual assets. See [[Harmar]] for details.

## Models

| Model | Manufacturer | Page |
|---|---|---|
| SRE-2010 (Elite) | Bruno | [[SRE-2010]] |
| SRE-3000 (Elan, legacy) | Bruno | [[SRE-3000]] |
| SRE-3050 (Elan) | Bruno | [[SRE-3050]] |
| VPL-3100B | Bruno | [[VPL-3100B]] |
| VPL-3200B (VPL-3210B) | Bruno | [[VPL-3200B]] |
| CRE-2110 (Elite Curve) | Bruno | [[CRE-2110]] |
| PUL-1100 (Out-Rider) | Bruno | [[PUL-1100]] |
| ASL-275 (Out-Sider) | Bruno | [[ASL-275]] |
| GA541 Avenger | Golden | [[GA541-Avenger]] |
| Buzzaround XL / Lite (GB106/116/146/147) | Golden | [[GB1xx-Buzzaround-XL]] |
| Buzzaround Extreme/EX (GB118/148) | Golden | [[GB118-148-Buzzaround-EX]] |
| Buzzaround Carry On (GB120) | Golden | [[GB120-Buzzaround-CarryOn]] |
| Companion GC221/321/421 (older gen) | Golden | [[GC221-321-421-Companion]] |
| Companion GC240/340/440/540 HD | Golden | [[GC240-340-440-540-Companion]] |
| LiteRider GL110/140 (older gen) | Golden | [[GL110-140-LiteRider]] |
| LiteRider GL111/141 (current gen) | Golden | [[GL111-141-LiteRider]] |
| LiteRider Envy GP162 (PTC/VR2 + LiNX variants) | Golden | [[GP162-LiteRider-Envy]] |
| Alante DX GP204 | Golden | [[GP204-Alante-DX]] |
| Compass GP600/605/615/620 | Golden | [[GP6xx-Compass]] |
| Ally GP303 | Golden | [[GP303-Ally]] |
| J6 (J6 / J6 VA) | Pride | [[J6]] |
| Q6 Edge 3 Stretto | Pride | [[Q6-Edge-3-Stretto]] |
| C-450 / C-625 | Prism | [[C-450-C-625]] |
| Helix (CSL Series) | Harmar | [[Helix]] |
| Highlander II (VPL400-1400; enclosure / no-enclosure / VPL400-X configs) | Harmar | [[HighlanderII]] |
| Pinnacle SL300 | Harmar | [[Pinnacle-SL300]] |
| Pinnacle SL600 | Harmar | [[Pinnacle-SL600]] |
| AL-Series Outside Vehicle Lifts (~22 models, hitch-mounted) | Harmar | [[AL-Series-Outside-Vehicle-Lifts]] |
| Hoist-Series Inside Vehicle Lifts (~12 models, cargo-area mounted) | Harmar | [[Hoist-Series-Inside-Vehicle-Lifts]] |
| AutoSlide (Standard/iLock/Elite/Elite iLock) — automatic sliding-door retrofit kit, not mobility equipment | AutoSlide | [[AutoSlide-Drive-System]] |

## Concepts

| Concept | Page |
|---|---|
| Overspeed safety governor (Bruno field-resettable + Prism motor-replacement variant) | [[Overspeed-Safety-Brake]] |
| Folding rail (manual/power) | [[Folding-Rail]] |
| Rail mounting/anchoring guidance | [[Rail-Mounting-Guidance]] |
| Top landing gate installation (VPL) | [[Top-Landing-Gate-Installation]] |
| Battery charger LED diagnostics (VPL) | [[Battery-Charger-LED-Diagnostics]] |
| Diagnostic codes (SRE-2010/3000, CRE-2110) | [[Diagnostic-Codes]] |
| Bruno warranty (stairlift + vehicle lift variants) | [[Warranty]] |
| Staircase measuring system (Picture Perfect) | [[Staircase-Measuring-System]] |
| Vehicle lift power wiring (PUL-1100, ASL-275) | [[Vehicle-Lift-Power-Wiring]] |
| Golden scooter warranty (BUZZaround/LiteRider/Companion/Avenger/Patriot; VA contract variant confirmed same text) | [[Golden-Scooter-Warranty]] |
| TruCharge battery/fault diagnostics (10-bar, PG S-Drive/VR2 controllers: GA541 + GP162 PTC variant) | [[TruCharge-Diagnostics]] |
| Flash/beep code diagnostics (9-code, Dynamics R-Series controller: Companion + both LiteRider generations) | [[Flash-Beep-Diagnostics]] |
| LiNX controller diagnostics (7-code, GP162 LiNX variant so far) | [[LiNX-Diagnostics]] |
| Golden wheelchair warranty (separate from scooter warranty: GP162/GP205/GP207/GP605/GP620) | [[Golden-Wheelchair-Warranty]] |
| Golden battery charging (HP8204B, MRC24-4LX + general care) | [[Golden-Battery-Charging]] |
| Golden accessory installs (8 universal accessory docs) | [[Golden-Accessory-Installs]] |
| Golden seating systems (size-code catalog, Proflex base) | [[Golden-Seating-Systems]] |
| Golden dealer tips (general reminders, touch-up paint) | [[Golden-Dealer-Tips]] |
| Golden key/key-switch replacement | [[Golden-Key-Switch-Replacement]] |
| Golden joystick side conversion (Shark controller) | [[Golden-Joystick-Side-Conversion]] |
| Golden transaxle replacement (LiteRider + Buzzaround XL) | [[Golden-Transaxle-Replacement]] |
| Golden power seat operation (speed/height interlock) | [[Golden-Power-Seat-Operation]] |
| Golden brake replacement (3 model families, complexity ranges from 5-step puck swap to 28-step full drive-assembly pull) | [[Brake-Replacement]] |
| Joystick controllers (Q-Logic + Q-Logic 3: end-user ops, error codes, full provider programming) | [[Joystick-Controllers]] |
| TRU-Balance 3 power positioning (tilt/recline/elevate, iLevel, inhibit matrix) | [[Tru-Balance-3-Power-Positioning]] |
| Harmar warranty (6 product lines/SKU groups, each with its own distinct term) | [[Harmar-Warranty]] |
| Harmar stairlift beep codes (Helix/SL300/SL600, near-identical major-fault scheme) | [[Harmar-Stairlift-Beep-Codes]] |

Golden uses at least 4 controller brands (PG S-Drive/VR2, LiNX, Dynamics
R-Series, GP605's "SHARK") and 3 diagnostic schemes across scooters and
wheelchairs — always verify the controller before assuming a scheme
applies to an un-ingested model. Pride's Q-Logic/Q-Logic 3 controllers
(see [[Joystick-Controllers]]) are a separate scheme again — don't assume
Golden's error codes apply to a Pride chair or vice versa.

[[Overspeed-Safety-Brake]] now spans three manufacturers and **four**
distinct mechanisms (Bruno centrifugal/field-resettable, Prism
motor-replacement, Harmar HighlanderII's OSG switch, and Harmar Helix's
own mechanical rack/sprocket jammer — Harmar alone contributes two
unrelated mechanisms across its own product lines) — always check which
manufacturer's *and which product's* variant applies before assuming a
reset procedure carries over.

Other candidates flagged but not yet written: Seat-Systems
(general/cross-manufacturer — Golden and Pride each have their own seating
concept page instead, which now looks like the settled pattern rather than
backlog); Troubleshooting (general, non-Bruno-specific — Pride's
[[Q6 Edge Basic Troubleshooting]] and all of Prism's
[[C-450 C-625 Technical Manual]] are candidate sources if this gets
written).

## Sources

Bruno Straight SL (6 of 6 ingested) — see `wiki/sources/Bruno/Bruno Straight SL/`:
2010-TS Tech Support Guide, 3050-I Install Manual, 3050-O Operator Manual,
3050-TS Tech Support Guide, SRE-2010 Folding Rail Install Manual,
SRE-3000 Installation Manual.

Bruno VPL (4 of 4 ingested) — see `wiki/sources/Bruno/VPL/`: VPL-3100B
Install Manual, VPL-3100B Operator Manual, VPL-3200B Install Manual,
VPL-3200B Operator Manual.

Bruno Curved SL (7 of 7 Bruno-authored files ingested) — see
`wiki/sources/Bruno/Bruno Curved SL/`: 2110-TS Tech Support Guide, CRE-2110
Install Manual, Bruno Elite 2010 Conversion (SRE-2010) [misfiled — actually
SRE-2010 content], Bruno Stair Lift Warranty, Picture Perfect Camera
Overview (2020, superseded), Picture Perfect Instructions (2022 Rev 5),
Picture Perfect Staircase Target Placement.

Bruno Vehicle Lifts (2 of 2 ingested) — see
`wiki/sources/Bruno/Vehicle Lifts/`: PUL-1100 Installation Manual, ASL-275
Install Manual.

Harmar (32 source pages, see `wiki/sources/Harmar/`) — ingested across two
passes:

*First pass:* CSL Series Photo Measuring Manual (physically located under
`MANUALS/Bruno/Bruno Curved SL/HARMAR Camera Measuring Manual.pdf` — a
different manufacturer's document, not moved since raw sources are
immutable), Helix Owner's Manual, Helix Photo Measuring Manual (2023, Rev
C), Highlander II with Enclosure Owner's Manual, Highlander II with
Enclosure Installation and Service Manual, Outside Vehicle Lifts Owner's
Manual (covers AL100/AL300/AL301, byte-identical files), Outside Vehicle
Lifts Installation and Service Manual (covers AL100/AL300/AL301,
byte-identical files), Pinnacle SL300 Owner's Manual, Pinnacle SL600
Owner's Manual, Vehicle Lift Phone Interview Form (internal PMS sales
form, not a Harmar technical manual).

*Second pass* (human added ~46 more files to `MANUALS/Harmar/`): Helix
Install Manual; Pinnacle SL300 Install Manual (2026, Rev L) plus its
superseded 2024 Rev K; Pinnacle SL600 Install Manual; Pinnacle Power
Swivel and Power Footrest Install Supplement; Highlander II Install
Manual (no enclosure — a genuinely different configuration from the
Enclosure version); VPL400-X Install Manual; Outside Vehicle Lifts
Install Manual (2025, Rev D); 9 technical bulletins (Worm Gear Clicking
Noise, Boom Lift Strap Replacement, Pinnacle Seat Swivel Modifications,
New Harmar Interlock Introduction, Pinnacle Seat/Footrest Supply Chain
Changes, Highlander II PCB Moisture Protection Plate, AL1232 Hitch
Adapter Cold Welds, Pinnacle Rail Length Change, License Plate Riser
Installation); Hoist Vehicle Lift Brochure (revealed the entire
[[Hoist-Series-Inside-Vehicle-Lifts]] product category); and four
consolidated reference pages — Harmar Evaluation and Order Forms (6
files), Harmar Product Spec Sheets (4 files), Harmar Parts Diagrams (9
files), Harmar Wiring Schematics (6 files) — each covering multiple
low-narrative-value engineering/marketing documents in one page rather
than one page per file. 7 product-photo/DAM-metadata files were
deliberately excluded as non-manual assets (see [[Harmar]]).

Golden (66 of 66 ingested — fully ingested) — see `wiki/sources/Golden/`: GA541 Avenger IPB,
GA541 Avenger Operator Manual, GA541 Avenger Mirror Installation,
2-Piece Brake Replacement, Frame Lock Adjustment (GB116/146), Field
Alignment Procedure (GB147), Rental Bumper Kit (GB118), Charging Dock
(GB118/148), Tie Down Kit (GB118/148), Rental Bumper Kit (GB148),
BuzzAround CarryOn Transportation Guide, GB120 Kickstand Installation
Guide, GB120 Tiller Replacement Instructions, Potentiometer Replacement
(GC221/321/421), Head Set Bearing Assembly (All Companions/LiteRiders),
Front Basket Installation, Seat Pedestal Replacement, Tiller Bolt
Replacement, Tiller Cable Replacement, Seat Lock Mechanism Operating
Instructions, Companion Service Guide, Companion & Companion HD IPB,
Companion Owner's Manual (VA Contract Variant), Battery Replacement
(GL110/140/GP160), Brake Replacement (GL110/140), LiteRider Service Guide
(GL110/140), LiteRider IPB (GL111/141), LiteRider Owner's Manual
(GL111/141), Alante DX ELR Installation (GP204), Compass Battery
Replacement Power Elevating Seat (GP600), Compass Caster Wheel Mounting
(GP600/605/615/620), Compass ELR Swing-Away Installation and Adjustment,
Compass Footrest Extension (GP600), Compass Sport Battery Connections
(GP605), Compass Sport Brake Replacement (GP605), Compass Sport Circuit
Breaker Wire Routing Upgrade (GP605), Compass Sport ELR Installation
(GP605), GP303 Ally Main Wiring Harness Replacement, LiteRider Envy IPB
(GP162), LiteRider Envy LiNX Supplemental Insert (GP162), LiteRider Envy
Seat Belt Installation (GP162), LiteRider PTC Service Guide (GP162, PG
VR2 Controller), LiteRider Envy LiNX Owner's Manual (GP162), Accessory
Receiver Installation, Adjustable Depth Seat Instructions, Battery
Charging Insert, Cane and Crutch Holder Installation, Connecting the
Batteries, Cup Holder Installation, Golden Tips, HP8204B Charger
Operation, Key and Key Switch Change, LiteRider and Buzzaround Transaxle
Change, Measuring Seats, Mobility All Models Flag Installation, Mobility
Seating Matrix, MRC24-4LX Charger Operation, Oxygen Holder and Walker
Holder Installation, Power Seat Operation, Proflex Seat Instructions,
Right to Left Side Joystick Conversion, Seat Belt Instructions, Touch Up
Paint Tips, Universal Mirror Mount, Mobility Seats.

Pride (10 of 10 ingested — fully ingested) — see `wiki/sources/Pride/`: J6
Specifications, J6 VA Specifications, J6 Operator Manual, Q6 Edge 3 Stretto
Specifications, Q6 Edge Basic Troubleshooting, Q6 Edge 3 Stretto Operator
Manual, Q-Logic Controller Basic Operation Instructions, Q-Logic 3 Basic
Operation Instructions, Q-Logic 3 Programming Guide, Tru-Balance 3 Power
Positioning Systems BOI.

Prism (1 of 1 ingested — fully ingested) — see `wiki/sources/Prism/`:
C-450/C-625 Technical Manual.

AutoSlide (2 of 2 ingested — fully ingested) — see `wiki/sources/AutoSlide/`:
AutoSlide Installation Manual (Standard, iLock, Elite, Elite iLock), RFID
Pet Sensor Operation Instructions (physically filed under the mismatched
`MANUALS/Open Sesame/` folder — see [[AutoSlide]] for the filing-naming
open question).

**All manuals in the entire wiki are now ingested**, including both
rounds of Harmar's `MANUALS/Harmar/` additions (see Harmar entry above) —
except the 7 deliberately-excluded image/CSV asset files, which aren't
manuals.

## Ingestion backlog

### Bruno — fully ingested, no backlog remaining.

### Golden — fully ingested, no backlog remaining.

### Pride — fully ingested, no backlog remaining.

### Prism — fully ingested, no backlog remaining.

### Harmar — fully ingested (install manuals for Helix/SL300/SL600 closed the previous pass's backlog). Only [[Hoist-Series-Inside-Vehicle-Lifts]] still lacks a narrative owner's/install manual (brochure + one bulletin + parts diagrams only) — not a missing-ingest issue since no such document is on disk yet.

### AutoSlide — fully ingested, no backlog remaining. Two accessories mentioned in the FAQ (Bluetooth module + AutoPlus Hub phone control, home-automation relay/key-switch cable) have no manual on file yet — not a missing-ingest issue since no such document exists on disk. See [[AutoSlide]] for the open scope/filing questions this manufacturer raised.

### Ramps — **new backlog category found by the 2026-09-12 lint pass, nothing ingested yet.** `MANUALS/Ramps/` (6 files, no manufacturer stub, no wiki mention anywhere before this lint) — appears to be "EZ Access"-brand modular ramps: `EZ Access Pathway-Assembly-Manual.pdf` (49pp, an install guide), `EZ Access Layout Key and Install Time.pdf` (1pp), `EZ Access parts and pieces.pdf` (1pp), `Ramps Handbook.docx`, plus two pricing sheets (`EZ Pay Scale 2023.pdf`, `Generic EZ Pay Scale.pdf` — likely not technical content, similar to the sales/pricing paperwork already excluded elsewhere in the wiki). Not ingested as part of this lint pass — flagging for the human to prioritize.

## How to use this wiki

1. **Querying?** Start here, follow links into `manufacturers/`, `models/`,
   or `concepts/` pages. If nothing covers your question yet, say so — the
   PDF backlog above is the fallback.
2. **Ingesting a new manual (or an existing backlog one)?** Follow the
   workflow in `/CLAUDE.md` — pick one manual or a tight cluster, read it,
   write/update its `sources/` page, its `models/` page, any `concepts/`
   pages it touches, then update this file and `log.md`.
