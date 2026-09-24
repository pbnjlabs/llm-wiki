---
type: index
---

# Index

Entry point for every query — check here first before opening raw manuals.

## Manufacturers

| Manufacturer | Page | Manuals on disk | Ingested |
|---|---|---|---|
| Bruno | [[Bruno]] | 20 | 20 |
| Golden | [[Golden]] | 66 | 66 |
| Pride | [[Pride]] | 10 | 10 |
| Prism | [[Prism]] | 5 | 5 — likely a Handicare brand, not an independent manufacturer, see note below |
| Vancare | [[Vancare]] | 1 | 1 — **different manufacturer**, found under `MANUALS/Prism/`, see note below |
| Harmar | [[Harmar]] | 74 | 36 source pages (see note — several consolidate multiple low-narrative files) |
| AutoSlide | [[AutoSlide]] | 2 | 2 — **different product category**, see note below |
| Red Hawk | [[Red Hawk]] | 5 | 5 — **organizational folder name spanning two unrelated OEMs**, see note below |
| EZ-ACCESS (raw folder `MANUALS/Ramps/`) | [[EZ-ACCESS]] | 7 files in `MANUALS/Ramps/` + 11 web clippings | All technical files ingested (16 source pages): **PMS Ramps Handbook** (in-house training; highest authority), the Pathway Assembly Manual (2015), 2 reference sheets of unknown origin, the U.S. Access Board ADA guide (under `sources/Standards/`) and 11 web clippings. The 2 pay-scale sheets are deliberately skipped |

Note: `MANUALS/Bruno/` physically holds 21 files, but the table
attributes only 20 to Bruno — one file (`HARMAR Camera Measuring
Manual.pdf`, physically under `MANUALS/Bruno/Bruno Curved SL/`) is
counted under Harmar instead, a different manufacturer's document not
moved since raw sources are immutable. See [[Harmar]] and [[Bruno]] for
details.

Note: `MANUALS/Prism/` physically holds 6 files, but the table
attributes only 5 to Prism — one
(`Ceiling Lift Installation Manual NEW.pdf`) is a **Vancare**-authored
ceiling-lift track installation guide, not a Prism document — counted
under Vancare instead, parallel to the Bruno/Harmar case above. See
[[Vancare]] and [[Prism]] for details.

Note: **"Prism" is very likely a Handicare brand, not an independent
manufacturer** — confirmed for two of its products ([[P440]] and the
[[Prism-Castor-2-Post-Lift-Stand]] accessory), both explicitly
Handicare-branded/warranted in their manuals, with "Prism" apparently
used for Handicare's North American refurbished-equipment line. Not yet
confirmed for [[C-450-C-625]] itself. See [[Prism]] for the full
writeup — kept under the "Prism" manufacturer page rather than
renamed, since that's the name on the raw `MANUALS/` folder and the
older documents' own branding.

Note: Golden's 66-file on-disk count includes one byte-identical duplicate
PDF saved under two filenames (confirmed by md5) — 65 distinct documents,
65 source pages. See [[Golden]] for details.

Note: **AutoSlide is not mobility equipment** — it's an automatic sliding-
door retrofit kit, a different product category from every other
manufacturer in this wiki. Its 2 raw files were found outside this repo (at
`/home/lu/Work/MANUALS/`, not `/home/lu/Work/llm-wiki/MANUALS/`) and copied
in preserving their original foldering: `MANUALS/AutoSlide/` (the main
install manual) and `MANUALS/Open Sesame/` (an RFID pet-sensor accessory
manual that is, confusingly, entirely AutoSlide-branded). Confirmed via web
search: **Open Sesame is a real, separate manufacturer** (automatic
swing-door operators, a different mechanism from AutoSlide's sliding-door
track) commonly sold alongside AutoSlide by the same door-access dealers —
so this file is a **misfile**, not a distributor name AutoSlide itself uses.
See [[AutoSlide]] for details, including the still-open question of whether
either brand belongs in this wiki's stated scope at all.

Note: **"Red Hawk" is not a brand name** — it's Performance Medical
Supply's own folder name for 5 folding-power-wheelchair manuals covering
**two unrelated Chinese manufacturers** sold under **four different
model names** by **two different regional distributors**: Nanjing Jin
Bai He Medical Apparatus Co., Ltd. (sold as "Air Hawk" by Gilani
Engineering, Australia, and as "Eagle HD"/"Falcon" by Discover Your
Mobility Inc., USA — plus possibly "Phoenix", also Discover Your
Mobility but a different manual template with manufacturer unconfirmed)
and Anhui JBH Medical Apparatus Company Limited (sold as "Pegasus Plus"
— DC02 — despite no "Pegasus" branding anywhere in that manual). See
[[Red Hawk]] for the full breakdown, including a truncated-manual
limitation on the DC02/Pegasus Plus source.

Note: Harmar's 74-file on-disk count (73 files in `MANUALS/Harmar/` after
three ingest passes, plus the 1 misfiled Bruno-folder file already
counted under Bruno) includes several sets of byte-identical duplicate
PDFs (AL100/AL300/AL301 owner's manuals; AL100/AL300/AL301 install
manuals; an al-100-12 assembly-drawing pair; 4 exact-duplicate Helix
files across the two source drops, not even copied into the wiki's
MANUALS folder since the content was already on file) confirmed by md5.
The 36 source pages also **consolidate** several low-narrative-value
file groups — 6 sales order/evaluation forms into one page, 4 marketing
spec sheets into one page, 9 engineering parts-diagram drawings into one
page, 6 wiring-schematic drawings into one page — rather than a strict
1:1 file-to-page mapping. 17 image/CSV files (product photos, 2 DAM
metadata exports) were deliberately excluded as non-manual assets. See
[[Harmar]] for details.

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
| ASL-250 (Out-Sider, legacy) | Bruno | [[ASL-250]] |
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
| C-450 / C-625 (C-800/C-1000 confirmed but undocumented) | Prism | [[C-450-C-625]] |
| P440 (P-600 confirmed but undocumented; likely Handicare-manufactured) | Prism | [[P440]] |
| Castor 2 Post Lift Stand (accessory) | Prism | [[Prism-Castor-2-Post-Lift-Stand]] |
| Helix (CSL Series) | Harmar | [[Helix]] |
| Highlander II (VPL400-1400; enclosure / no-enclosure / VPL400-X configs) | Harmar | [[HighlanderII]] |
| Pinnacle SL300 | Harmar | [[Pinnacle-SL300]] |
| Pinnacle SL600 | Harmar | [[Pinnacle-SL600]] |
| AL-Series Outside Vehicle Lifts (~22 models, hitch-mounted) | Harmar | [[AL-Series-Outside-Vehicle-Lifts]] |
| Hoist-Series Inside Vehicle Lifts (~12 models, cargo-area mounted) | Harmar | [[Hoist-Series-Inside-Vehicle-Lifts]] |
| Hybrid Vehicle Lifts (AL600/AL690/AL6000/AL6000HD, cargo-area mounted, powered swing-out tower) | Harmar | [[Hybrid-Vehicle-Lifts]] |
| AutoSlide (Standard/iLock/Elite/Elite iLock) — automatic sliding-door retrofit kit, not mobility equipment | AutoSlide | [[AutoSlide-Drive-System]] |
| Air Hawk / Eagle HD — same product, dual-branded | Red Hawk | [[Air-Hawk-Eagle-HD]] |
| Falcon — 180kg variant with reclining backrest | Red Hawk | [[Falcon]] |
| Phoenix — different manual template, manufacturer unconfirmed | Red Hawk | [[Phoenix]] |
| Pegasus Plus (DC02) — different manufacturer (Anhui JBH); source manual truncated | Red Hawk | [[Pegasus Plus (DC02)]] |
| TRANSITIONS threshold plates/ramps/mats (5 products, full size tables) | EZ-ACCESS | [[TRANSITIONS-Threshold-Ramps]] |
| SUITCASE folding ramps (Singlefold / Singlefold AS / TRIFOLD AS) | EZ-ACCESS | [[SUITCASE-Ramps]] |
| GATEWAY 3G solid ramp (PMS treats it as permanent, so 1:12 applies) | EZ-ACCESS | [[GATEWAY-3G]] |
| PATHWAY 3G residential modular ramp system ("Pathway" and "3G" are the same product; 850 lb per its 2015 manual) | EZ-ACCESS | [[PATHWAY-3G]] |
| PATHWAY HD commercial modular ramps and platforms | EZ-ACCESS | [[PATHWAY-HD]] |

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
| Ramp slope and length (**wiki standard: 1:12 only**, 1 ft of run per inch of rise, 4.8° on an angle meter; device incline ratings) | [[Ramp-Slope-and-Length]] |
| ADA ramp requirements (from the U.S. Access Board guide: slope, width, landings, handrails, edge protection, curb ramps; the PMS 1:12 rule overrides ADA's alteration exceptions) | [[ADA-Ramp-Requirements]] |
| Ramp site planning (**PMS evaluation procedure from the Ramps Handbook**: start inside, fire egress, 5 ft level at the door, five design rules; plus intake questions, product picker, site-survey checklist, install/test) | [[Ramp-Site-Planning]] |
| Ramp install time estimates (per-component labor minutes from the layout-key sheet, origin unknown, with a worked example) | [[Ramp-Install-Time-Estimates]] |

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

Bruno Vehicle Lifts (3 of 3 ingested) — see
`wiki/sources/Bruno/Vehicle Lifts/`: PUL-1100 Installation Manual, ASL-275
Install Manual, ASL-250 Install Manual (2019 — an older hardware
generation found by checking an out-of-repo `MANUALS/Bruno/` drop for new
sources; revealed the [[ASL-250]] model page and its "HTP" ramped
platform variant, undocumented on ASL-275).

Harmar (36 source pages, see `wiki/sources/Harmar/`) — ingested across
three passes:

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

*Third pass* (human dropped ~16 more files into an out-of-repo
`MANUALS/Harmar/` folder, copied in preserving the drop): Hybrid Vehicle
Lifts Owner's Manual and Installation and Service Manual (AL600/AL690,
2025), AL6000 Series Owner's Manual (2021, Rev A) and Installation and
Service Manual (2022, Rev C) — together revealing the entire
[[Hybrid-Vehicle-Lifts]] product category and resolving the previously
unexplained "AL600 Hybrid" parts-diagram mention on
[[AL-Series-Outside-Vehicle-Lifts]]. 2 renamed-but-byte-identical
duplicates of already-ingested Helix files were not re-copied. 10
further product-photo/DAM-metadata files (5 AL425HD product photos, 3
more AL425 photos, 2 metadata-export CSVs) were deliberately excluded as
non-manual assets, bringing the running exclusion total to 17.

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

Prism (5 of 5 ingested — fully ingested) — see `wiki/sources/Prism/`:
C-450/C-625 Technical Manual, Ceiling Lift Evaluation Form (generic
pre-install site-survey form, not C-450/C-625-specific), P440 User
Manual (2017, superseded — found by checking an out-of-repo
`MANUALS/Prism/` drop for new sources; revealed the [[P440]]
portable-ceiling-lift product line, distinct from the fixed-track
C-Series), P440 Owner's Manual (2021, Rev 19-Oct — a newer, more
complete revision found in a further `MANUALS/Prism/` check; the first
document in this wiki to explicitly confirm **Handicare** as the
manufacturer behind at least this model, resolving a long-open note on
[[C-450-C-625]]'s page), Prism Castor 2 Post Lift Stand Installation
Manual (2018 — a freestanding two-post track accessory, co-branded
Prism/Handicare, sized to match the C-Series lifts' 450lb/625lb
capacities exactly; new model page [[Prism-Castor-2-Post-Lift-Stand]]).

Vancare (1 of 1 ingested — fully ingested) — see `wiki/sources/Vancare/`:
Ceiling Lift Installation Guide (2021 — a 213-page Vancare-authored
track-system install manual found in the same `MANUALS/Prism/` drop;
not a Prism document, but its cross-compatibility tables confirmed two
new Prism model numbers, C-800/C-1000 and P-600, with no manuals of
their own on file — see [[Vancare]]).

AutoSlide (2 of 2 ingested — fully ingested) — see `wiki/sources/AutoSlide/`:
AutoSlide Installation Manual (Standard, iLock, Elite, Elite iLock), RFID
Pet Sensor Operation Instructions (physically filed under
`MANUALS/Open Sesame/` — confirmed misfile, see [[AutoSlide]]).

Red Hawk (5 of 5 ingested — fully ingested) — see `wiki/sources/Red Hawk/`:
Air Hawk Owner's Manual, Eagle HD Owner's Manual (confirmed
byte-for-byte-identical technical content to Air Hawk, different
distributor), Falcon Owner's Manual (180kg variant with reclining
backrest), Phoenix Owner's Manual (different manual template,
manufacturer unconfirmed), Pegasus Plus Heavy Duty Manual (DC02, a
different manufacturer entirely — Anhui JBH, not Nanjing Jin Bai He —
and a **truncated file**: its own table of contents promises
warranty/troubleshooting/diagnostics/wiring/EMC sections through page
44, but the file stops at page 27 with blank trailing pages to 30; those
sections are not documented in this wiki). See [[Red Hawk]] for the full
multi-brand breakdown.

EZ-ACCESS (all technical files ingested; pay scales skipped), see `wiki/sources/EZ-ACCESS/`. PMS in-house: Ramps Handbook (General). Manual: Pathway Modular Access System Assembly Manual (P/N 10565, rev 05-12-15) under PATHWAY 3G. Reference sheets (General): EZ Access Parts and Pieces (2018), EZ Access Layout Key and Install Time (2019). Web clippings: these are EZ-ACCESS
blog articles saved with Obsidian Web Clipper, copied from the vault's
`Clippings/` folder to `MANUALS/Clippings/`. doc_type: Web Article.
General: How Long Should a Wheelchair Ramp Be, Wheelchair Ramp Slope
Calculator Guide, Understanding ADA Ramp Requirements, Understanding
Ramp Incline, How to Measure and Install a Ramp, Residential Ramps -
Where Do I Begin. PATHWAY 3G: Configuration Factors for Residential Ramp
Systems, Securing PATHWAY 3G Before a Storm. PATHWAY HD: Which Platform
Is Right for Your Needs. TRANSITIONS: Different Types of Threshold
Ramps. Portable Ramps: Portable Wheelchair Ramps (Residential).

Standards (1 of 1 ingested), see `wiki/sources/Standards/ADA/`: ADA
Technical Guide - Ramps and Curb Ramps (U.S. Access Board, July 2015;
raw file `MANUALS/Ramps/ADA_Rules_ramps.pdf`). This is the
authoritative ADA reference behind [[ADA-Ramp-Requirements]].

**All manuals in the entire wiki are now ingested**, including all three
rounds of Harmar's `MANUALS/Harmar/` additions (see Harmar entry above) —
except the deliberately excluded Harmar image/CSV asset files, which
aren't manuals, and the two EZ-ACCESS pay-scale sheets (skipped per the
human). The Harmar exclusion is stated as 17 files, but only 10 such
files are on disk on this device; see the 2026-09-24 lint entry in the
log.

## Ingestion backlog

### Bruno — fully ingested, no backlog remaining (a third pass added [[ASL-250]], a legacy vehicle-lift generation found via a new-sources check).

### Golden — fully ingested, no backlog remaining.

### Pride — fully ingested, no backlog remaining.

### Prism — fully ingested, no backlog remaining (a second pass added [[P440]]; a third pass added a newer P440 revision confirming **Handicare** as the actual manufacturer, plus the co-branded [[Prism-Castor-2-Post-Lift-Stand]] accessory, both found via new-sources checks). Two sibling models, C-800/C-1000 and P-600, are confirmed to exist (via [[Vancare]]'s cross-compatibility tables) but have no manual of their own on disk — not a missing-ingest issue since no such document exists yet. Open question: is [[C-450-C-625]] itself also Handicare-manufactured? Not yet confirmed either way.

### Vancare — fully ingested, no backlog remaining. A single track-system install guide found under `MANUALS/Prism/` (not Prism-authored) — see [[Vancare]] for the open question of whether this reflects a broader Vancare supplier relationship worth tracking, or is a one-off.

### Harmar — fully ingested (a third pass added the full [[Hybrid-Vehicle-Lifts]] doc set and resolved the AL600 naming quirk). Only [[Hoist-Series-Inside-Vehicle-Lifts]] still lacks a narrative owner's/install manual (brochure + one bulletin + parts diagrams only) — not a missing-ingest issue since no such document is on disk yet.

### AutoSlide — fully ingested, no backlog remaining. Two accessories mentioned in the FAQ (Bluetooth module + AutoPlus Hub phone control, home-automation relay/key-switch cable) have no manual on file yet — not a missing-ingest issue since no such document exists on disk. See [[AutoSlide]] for the open scope question this manufacturer raised, plus a **new possible backlog category**: "Open Sesame" is a confirmed real, separate manufacturer (automatic swing-door operators) that PMS keeps a raw-source folder for, but no genuine Open Sesame manuals have been found yet — worth asking the human if any exist.

### Red Hawk — fully ingested, no backlog remaining, but with one open item: the [[Pegasus Plus (DC02)]] source manual is truncated (missing warranty/troubleshooting/diagnostics/wiring/EMC sections its own table of contents promises) — worth asking the human if a complete copy exists. The [[Phoenix]] model's manufacturer is also unconfirmed from its manual alone (different template from the other three Red Hawk models, mentions an unexplained third company "TREK Mobility").

### EZ-ACCESS — fully ingested, no technical backlog. `Ramps Handbook.docx` (PMS in-house training) was the last file (2026-09-24). **Deliberately skipped** per the human: `EZ Pay Scale 2023.pdf` and `Generic EZ Pay Scale.pdf`. Resolved: "Pathway" = PATHWAY 3G, so the 2015 manual applies and capacity is 850 lb. Also noted: the Ramps Handbook's 28.5 in → 28 ft example is wrong: **confirmed as 29 ft** (round up). The docx itself still says 28 ft.

## How to use this wiki

1. **Querying?** Start here, follow links into `manufacturers/`, `models/`,
   or `concepts/` pages. If nothing covers your question yet, say so — the
   PDF backlog above is the fallback.
2. **Ingesting a new manual (or an existing backlog one)?** Follow the
   workflow in `/CLAUDE.md` — pick one manual or a tight cluster, read it,
   write/update its `sources/` page, its `models/` page, any `concepts/`
   pages it touches, then update this file and `log.md`.
