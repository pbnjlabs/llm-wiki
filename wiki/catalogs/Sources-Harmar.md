---
type: catalog
---

# Sources: Harmar

Part of the source catalog split out of [[index]] (2026-10-25). Lists every `sources/` page for this group with ingest history and counts.

Harmar (47 source pages, see `wiki/sources/Harmar/`) — ingested across
five passes:

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
Install Manual (2025, Rev D); 10 technical bulletins (Worm Gear Clicking
Noise, Boom Lift Strap Replacement, Pinnacle Seat Swivel Modifications,
New Harmar Interlock Introduction, Pinnacle Seat/Footrest Supply Chain
Changes, Highlander II PCB Moisture Protection Plate, AL1232 Hitch
Adapter Cold Welds, Pinnacle Rail Length Change, License Plate Riser
Installation, AL1235U Universal Drop Hitch Adapter); [[Vehicle Lift Workflow]] (PMS estimate
workflow: lift by device, swing-away, hitch adapter on every estimate;
phone number and login omitted); Hoist Vehicle Lift Brochure (revealed the entire
[[Hoist-Series-Inside-Vehicle-Lifts]] product category); and four
consolidated reference pages — Harmar Evaluation and Order Forms (6
files), Harmar Product Spec Sheets (4 files), Harmar Parts Diagrams (10
files), Harmar Wiring Schematics (6 files) — each covering multiple
low-narrative-value engineering/marketing documents in one page rather
than one page per file. Product-photo/DAM-metadata files were
deliberately excluded as non-manual assets. This pass logged them as "7";
the true count is 10 (see the correction below).

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
non-manual assets. **Correction (2026-09-24 lint):** these are the *same*
files the second pass had already excluded. All 10 have been in the drop
folder since 2026-09-11, before either pass. The earlier "running total
of 17" double-counted them. **The true exclusion total is 10.**

*Fourth pass* (2026-10-06, 11 new one-page files in the human's
`MANUALS/Harmar/`): [[Harmar Product Insights (2021-2023)]], consolidated: lift selection, docking
devices, hitch adapters, AL015 travel-scooter lift, Highlander II
Guardian System / install prep / Q4 2022 changes, Pinnacle drive system
and zero-overrun install, Helix remotes, threshold ramps. Dealer sheets,
ranked below the manuals; two conflicts flagged (AL1235U 4 in drop,
Highlander II Service Mode timer).

*Fifth pass* (2026-10-06, 4 files): [[Inside Lifts Installation and Owner's Manual (2017, Rev F)]], [[Truck Lifts Installation and Owner's Manual (AL800 Series, 2017)]], [[AL625-AL625HD Installation and Owner's Manual (2012, Rev B)]] (legacy
"Tracker") and [[Harmar Mobility Solutions Chart (2026, Rev F)]]. Closes three Missing manuals items (hoist lifts,
truck lifts, AL-625HD). Flagged: AL815CC/AL825 capacity, 2022 FSS list
150/225 lb vs manual and 2026 chart 135/210 lb.

*Sixth pass* (2026-10-23, training videos): all **47 Harmar training
videos** from `~/Downloads/Col_ID8949-original` (one, the AL-100
actuator video, was already in), in `MANUALS/Harmar/Videos/` with
transcripts, frames and caption OCR in `Videos/_work/<slug>/`. 34
`Video - …` source pages (the 13 Pinnacle install clips and the 4
dumbwaiter clips are one page each). Stairlifts: Pinnacle install
series and full-length version (SL300), folding-rail hand change, rail
jig, hand-control side swap, remote pairing, batteries, board, seat
harness, beep tones, sales demo kit; Helix install, measuring, lower
roller, diagnostic software, batteries, board, sales demo kit. Platform
lifts (older RPL/CPL): electrical components, safety pan, call
station, top landing gate, door operator. Vehicle lifts: actuator,
AL100 hold-down foot, AL560 arm, hitch adapters, AL701 7-pin harness,
Hybrid RF remote, AL800 limit switch, AL425HD truck install.
Dumbwaiter: 110→220 V conversion. **Conflicts flagged (manual wins):**
SL300 footplate torque 25 vs **46 ft-lb**; Pinnacle rail clearance 2–3
vs **3 in minimum**; folding-rail foot wrench 9/16 vs ½ in; AL560 arm
lowered 1–2 vs **2–3 in**; beep-tone count 5 vs **4** for top+bottom
obstruction; Pinnacle demo kit's 350 lb vs SL300 **300 lb**; hitch
video's 6 in drop at 21 in vs **3 in** on the AL1235U chart.

*Seventh pass* (2026-10-27, 2 screenshots from `~/Downloads`):
[[Actuator Drawing 310-00005 (Rev C)]], both sheets of Harmar's actuator drawing (`310-00005.msd2.webp`
sheet 1, `310-00005.msd.webp` sheet 2, in `MANUALS/Harmar/`). Rev A
says "formerly PN ALA10010"; specs, connector, ball nut. No torques.

*Seventh pass, continued* (2026-10-27, from the Mobility Scooters Direct pull): [[Hybrid Electrical Kit Drawings (AL412, 140-00023, 140-00030, 380-00099)]], four Harmar drawings (five sheets) from the retailer's product galleries, and the retailer part-number catalog [[Parts Catalog - Mobility Scooters Direct (Harmar)]] (121 parts, 29 with a drawing image).
