# Log

Append-only. Newest entries at the bottom. Format: `## [YYYY-MM-DD] <ingest|query|lint> | <short description>`

## [2026-09-10] lint | initial wiki scaffold created

Set up `wiki/` (index.md, log.md, manufacturers/, models/, concepts/,
sources/) and root `CLAUDE.md` schema over the existing `MANUALS/` raw
collection (Bruno, Golden, Pride, Prism — 97 manuals total: corrected from
an initial miscount of 87). Wrote manufacturer stub pages from
filename/folder structure only — no manual content has been read yet.
Next step: ingest manuals one at a time (or by cluster) per the workflow
in `CLAUDE.md`.

## [2026-09-10] ingest | Bruno SRE-2010 — 2010-TS Tech Support Guide

## [2026-09-10] ingest | Bruno SRE-2010 — SRE-2010 Folding Rail Install Manual (also covers SRE-3050)

## [2026-09-10] ingest | Bruno SRE-3050 — 3050-I Install Manual

## [2026-09-10] ingest | Bruno SRE-3050 — 3050-O Operator Manual

## [2026-09-10] ingest | Bruno SRE-3050 — 3050-TS Tech Support Guide

## [2026-09-10] ingest | Bruno SRE-3000 — SRE-3000 Installation Manual

Ingested the full Bruno Straight SL cluster (6 manuals, all of
`MANUALS/Bruno/Bruno Straight SL/`). Created model pages [[SRE-2010]],
[[SRE-3000]], [[SRE-3050]] and concept pages
[[Overspeed-Safety-Brake]], [[Folding-Rail]], [[Rail-Mounting-Guidance]] —
all three concepts turned out to be genuinely shared across Bruno's
Straight SL line (same mechanisms, often the same document reused
verbatim across models). Updated [[Bruno]] and `index.md` accordingly.
Also corrected file-count errors in the original scaffold: Bruno has 20
manuals on disk (not 12), Golden has 66 (not 64).

## [2026-09-10] ingest | Bruno VPL-3100B — Install Manual

## [2026-09-10] ingest | Bruno VPL-3100B — Operator Manual (Trilingual)

## [2026-09-10] ingest | Bruno VPL-3200B — Install Manual

## [2026-09-10] ingest | Bruno VPL-3200B — Operator Manual (EN/FR)

Ingested the full Bruno VPL cluster (4 manuals, all of
`MANUALS/Bruno/VPL/`). Created model pages [[VPL-3100B]] and [[VPL-3200B]]
— Bruno's smaller porch-lift and larger multi-floor hoistway lift,
respectively, sharing the same Acme-screw-drive architecture but differing
sharply in install complexity (VPL-3200B ships as a two-half tower joined
on site via a coiled-spring-pin drive-screw splice) and emergency
operation (VPL-3200B adds an electrical emergency-lowering key switch
outside the hoistway; VPL-3100B has only the manual hand wheel). Created
concept pages [[Top-Landing-Gate-Installation]] (gate hardware/procedure
reused verbatim across both models) and
[[Battery-Charger-LED-Diagnostics]] (same LED table reused verbatim across
both install and both operator manuals). Updated [[Bruno]] and `index.md`
accordingly — Bruno's Straight SL and VPL product lines are now fully
ingested; Curved SL and Vehicle Lifts remain backlog.

## [2026-09-10] ingest | Bruno CRE-2110 — 2110-TS Tech Support Guide

## [2026-09-10] ingest | Bruno CRE-2110 — CRE-2110 Install Manual

## [2026-09-10] ingest | Bruno SRE-2010 — Bruno Elite 2010 Conversion (misfiled under Curved SL)

## [2026-09-10] ingest | Bruno — Stair Lift Warranty

## [2026-09-10] ingest | Bruno — Picture Perfect Camera Overview (2020, superseded)

## [2026-09-10] ingest | Bruno — Picture Perfect Instructions (2022 Rev 5)

## [2026-09-10] ingest | Bruno — Picture Perfect Staircase Target Placement

## [2026-09-10] ingest | Harmar — CSL Series Photo Measuring Manual (misfiled under Bruno Curved SL)

Ingested the Bruno Curved SL cluster (8 manuals in
`MANUALS/Bruno/Bruno Curved SL/`). Created model page [[CRE-2110]] (custom
curved-rail Elite Curve — shares [[Rail-Mounting-Guidance]] and
[[Diagnostic-Codes]] with the straight Elite/Elan line, but overspeed
brake is optional rather than standard and resets via a different
two-lever mechanism — see [[Overspeed-Safety-Brake]]). Created concept
pages [[Diagnostic-Codes]] (shared code table confirmed across SRE-2010,
SRE-3000, and CRE-2110 — not confirmed for SRE-3050), [[Warranty]] (Bruno
Gold Limited Warranty, general across the stairlift line), and
[[Staircase-Measuring-System]] (Picture Perfect / StairsChecker 3.0 camera
kit used to order custom curved rail — the three "camera" files turned out
to be one document's revision history plus a standalone diagram excerpt,
not three distinct systems).

Two filing surprises: "Bruno Elite 2010 conversion.pdf" is actually
SRE-2010 straight-rail content (folded into [[SRE-2010]] instead of
[[CRE-2110]]), and "HARMAR Camera Measuring Manual.pdf" turned out to be a
**different manufacturer's** competing product (Harmar's CSL Series /
Helix PhotoMap) — created a new manufacturer stub [[Harmar]] rather than
misrepresenting it as Bruno content. Updated [[Bruno]] and `index.md`
accordingly — only Vehicle Lifts (2 files) remains as Bruno backlog.

## [2026-09-10] ingest | Bruno PUL-1100 — Installation Manual

## [2026-09-10] ingest | Bruno ASL-275 — Install Manual

Ingested the Bruno Vehicle Lifts cluster (2 manuals, all of
`MANUALS/Bruno/Vehicle Lifts/`) — the last Bruno backlog. Created model
pages [[PUL-1100]] (truck-bed-mounted "Out-Rider" arm lift for storing an
empty mobility device) and [[ASL-275]] (hitch-mounted "Out-Sider" platform
lift, optional Swing-Away). Created concept page
[[Vehicle-Lift-Power-Wiring]] — both manuals describe an near-identical
battery-to-lift wiring pattern (fuse holder, firewall routing, hybrid/EV
12V-accessory-battery note). Also found both manuals embed the identical
"Bruno Gold Limited Warranty for Vehicle Lift" text (3yr flat, distinct
terms from the stairlift warranty) — restructured [[Warranty]] into two
sections (stairlift 5yr/2yr vs. vehicle-lift 3yr) rather than assuming one
warranty applies to both product categories. Updated [[Bruno]] and
`index.md` — **all 19 Bruno-authored manuals on disk are now ingested.**
Bruno is fully done; remaining backlog is Golden (66), Pride (10), and
Prism (1).

## [2026-09-10] ingest | Golden GA541 Avenger — IPB

## [2026-09-10] ingest | Golden GA541 Avenger — Operator Manual

## [2026-09-10] ingest | Golden GA541 Avenger — Mirror Installation

First Golden ingest. Created model page [[GA541-Avenger]] (750W
rear-wheel-drive 4-wheel scooter, PG S-Drive controller — corrects the
manufacturer stub's earlier guess that GA541 was a wheelchair). Created
two concept pages from direct textual evidence rather than speculation:
[[Golden-Scooter-Warranty]] (the Avenger operator manual's warranty
section explicitly names BUZZaround, LiteRider, Companion, and Patriot
models as covered by the same policy text) and [[TruCharge-Diagnostics]]
(a 10-code battery/fault display, confirmed on GA541 only so far —
flagged to verify against other Golden models as they get ingested).
Updated [[Golden]] and `index.md` — 3 of 66 Golden files done.

## [2026-09-10] ingest | Golden Buzzaround XL — 2-Piece Brake Replacement (also covers LiteRider)

## [2026-09-10] ingest | Golden GB116/GB146 — Frame Lock Adjustment

## [2026-09-10] ingest | Golden GB147 — Field Alignment Procedure

## [2026-09-10] ingest | Golden GB118 — Rental Bumper Kit

## [2026-09-10] ingest | Golden GB118/GB148 — Charging Dock

## [2026-09-10] ingest | Golden GB118/GB148 — Tie Down Kit

## [2026-09-10] ingest | Golden GB148 — Rental Bumper Kit

## [2026-09-10] ingest | Golden GB120 — CarryOn Transportation Guide (Battery)

## [2026-09-10] ingest | Golden GB120 — Kickstand Installation Guide

## [2026-09-10] ingest | Golden GB120 — Tiller Replacement Instructions

Ingested the GB1xx Buzzaround cluster (10 manuals). Sorted into three
model pages by actual platform, not raw filename groupings:
[[GB1xx-Buzzaround-XL]] (GB106 "Lite", GB116, GB146 share a frame-lock
folding design; GB147 has a different tie-rod steering linkage, open
question whether it still folds — no IPB/OM on file to confirm),
[[GB118-148-Buzzaround-EX]] (GB118=3-wheel, GB148=4-wheel of the same
"Buzzaround Extreme" platform — confirmed by their differing rental
bumper kit steps; dual removable battery packs on a shared charging
dock), and [[GB120-Buzzaround-CarryOn]] (single quick-release lithium
pack, airline-travel-focused, distinct tiller/steering architecture from
the other two families). Confirmed the brake mechanism is shared with the
not-yet-ingested GL110/GL140 LiteRider (noted on [[GB1xx-Buzzaround-XL]]
for that future ingest). Neither [[Golden-Scooter-Warranty]] nor
[[TruCharge-Diagnostics]] appear in these service/accessory bulletins —
expected, since full warranty/diagnostic text lives in Operator Manuals,
none of which are on file for any Buzzaround model yet. Updated [[Golden]]
and `index.md` — 13 of 66 Golden files done.

## [2026-09-10] ingest | Golden GC221/321/421 — Potentiometer Replacement

## [2026-09-10] ingest | Golden Companion/LiteRider — Head Set Bearing Assembly

## [2026-09-10] ingest | Golden GC240/340/440 — Front Basket Installation

## [2026-09-10] ingest | Golden GC240/340/440 — Seat Pedestal Replacement

## [2026-09-10] ingest | Golden GC240/340/440 — Tiller Bolt Replacement

## [2026-09-10] ingest | Golden GC240/340/440 — Tiller Cable Replacement

## [2026-09-10] ingest | Golden GC240/340/440 — Seat Lock Mechanism Operating Instructions

## [2026-09-10] ingest | Golden GC240/340/440 — Companion Service Guide

## [2026-09-10] ingest | Golden GC240/340/440/540 — Companion & Companion HD Illustrated Parts Breakdown

## [2026-09-10] ingest | Golden GC240/340/440 — Companion Owner's Manual (VA Contract Variant)

Ingested the Golden Companion cluster (10 manuals). Created
[[GC221-321-421-Companion]] (older generation, thin coverage — only one
part-replacement doc on file) and [[GC240-340-440-540-Companion]] (current
generation). Key finding from the 2024 IPB: **GC540 "Companion HD" is a
genuinely distinct heavier-duty variant**, not a color/trim option —
separate frame, battery (22NF vs. U1/50AH), controller (Rhino 2 140A vs.
90A DR90-A01), and seat, sharing only the tiller assembly with GC340/440.
No operator manual or service guide exists for GC540 specifically, only
the IPB.

Two warranty/diagnostics cross-checks, both resolved with real findings
rather than left unconfirmed: the Companion's "VA" operator manual is a
**Department of Veterans Affairs contract packaging** (not a state
regulatory variant — confirmed by a "Military Branch Patch" in the
packing list), and its warranty section is [[Golden-Scooter-Warranty]]'s
existing text verbatim under a VA-specific heading, plus an added 2-year
VA service plan — updated that concept page rather than creating a
duplicate. Separately, the Companion uses a **different diagnostic
scheme** than the GA541's TruCharge bars — a 9-code flash/beep system,
identical between the Service Guide and the VA Operator Manual — created
[[Flash-Beep-Diagnostics]] and cross-linked/clarified
[[TruCharge-Diagnostics]] so the two aren't conflated. Also confirmed the
head-set-bearing assembly is explicitly a shared Companion+LiteRider part.
Updated [[Golden]] and `index.md` — 23 of 66 Golden files done.

## [2026-09-10] ingest | Golden GL110/140/GP160 — Battery Replacement

## [2026-09-10] ingest | Golden GL110/140 — Brake Replacement

## [2026-09-10] ingest | Golden GL110/140 — LiteRider Service Guide

## [2026-09-10] ingest | Golden GL111/141 — LiteRider Illustrated Parts Breakdown

## [2026-09-10] ingest | Golden GL111/141 — LiteRider Owner's Manual

Ingested the GL1xx LiteRider cluster (5 manuals). Created
[[GL110-140-LiteRider]] (older generation) and [[GL111-141-LiteRider]]
(current generation) — the generational change looks mostly electronic/
cosmetic rather than mechanical: the transaxle part (RA11E103) is still
labeled for GL110/GL140 even in the newer IPB, and both use the same
2×22AH battery layout.

Key finding: the GL111/141 IPB explicitly names the same 90A Dynamics
R-Series controller part (3051600170) as shared with Companion
GC240/340/440 — direct textual evidence, not inferred. Combined with the
GL110/140 Service Guide's beep-code table matching
[[Flash-Beep-Diagnostics]] point-for-point, this confirms that concept
page was scoped too narrowly as "Companion-only" — broadened it to a
Dynamics-R-Series-controller-family concept and confirmed it now spans
Companion GC240/340/440 and both LiteRider generations. [[Golden-Scooter-
Warranty]] also confirmed on GL111/141 (rev. 11.17 text, though it lists
covered models as "GL109, GL111, GL141" — GL109, not GL110, another
warranty-text/raw-filename part-number mismatch). Battery replacement doc
also flagged as covering GP160 (not yet ingested) — cross-linked for that
future ingest. Updated [[Golden]] and `index.md` — 28 of 66 Golden files
done; Golden backlog is now just GP1xx/GP6xx Compass/Alante/Envy,
chargers, and cross-model accessory docs.

## [2026-09-10] ingest | Golden GP204 — Alante DX ELR Installation

## [2026-09-10] ingest | Golden GP600 — Compass Battery Replacement, Power Elevating Seat

## [2026-09-10] ingest | Golden GP6xx — Compass Caster Wheel Mounting

## [2026-09-10] ingest | Golden GP6xx — Compass ELR Swing-Away Installation and Adjustment

## [2026-09-10] ingest | Golden GP600 — Compass Footrest Extension

## [2026-09-10] ingest | Golden GP605 — Compass Sport Battery Connections

## [2026-09-10] ingest | Golden GP605 — Compass Sport Brake Replacement

## [2026-09-10] ingest | Golden GP605 — Compass Sport Circuit Breaker Wire Routing Upgrade

## [2026-09-10] ingest | Golden GP605 — Compass Sport ELR Installation

## [2026-09-10] ingest | Golden GP303 — Ally Main Wiring Harness Replacement

## [2026-09-10] ingest | Golden GP162 — LiteRider Envy Illustrated Parts Breakdown

## [2026-09-10] ingest | Golden GP162 — LiteRider Envy LiNX Supplemental Insert

## [2026-09-10] ingest | Golden GP162 — LiteRider Envy Seat Belt Installation

## [2026-09-10] ingest | Golden GP162 — LiteRider PTC Service Guide (PG VR2 Controller)

## [2026-09-10] ingest | Golden GP162 — LiteRider Envy LiNX Owner's Manual

Ingested the GP1xx/GP6xx cluster (15 manuals) — Golden's biggest and most
heterogeneous remaining cluster, covering three distinct model families
under one loose "GP" prefix. [[GP162-LiteRider-Envy]] is sold under one
model number with two different controller families (PTC/PG VR2 and
LiNX) rather than one superseding the other — confirmed directly from the
IPB's electrical parts list. [[GP204-Alante-DX]] has thin coverage (one
ELR doc) but shares legrest hardware with Alante GP201 and Compass Sport
GP605. [[GP6xx-Compass]] (GP600/605/615/620) share caster-wheel and
ELR/Swing-Away hardware, but GP605 uses its own **"SHARK"**-branded
controller — a fourth Golden controller family alongside PG VR2/LiNX
(GP162) and Dynamics R-Series (Companion/LiteRider), with no diagnostic
table on file for it yet. [[GP303-Ally]] turned out to be a **distinct,
unrelated model** despite sharing the "GP" prefix — a foldable-frame
power wheelchair misfiled into the Compass cluster by number; corrected
after reading its actual content.

Created two new concept pages from direct textual evidence: **[[LiNX-Diagnostics]]**
(7-code flash scheme confirmed on GP162's LiNX variant, plus an OONAPU
power-up interlock and drive-inhibit chasing-light sequence not present
on the PTC variant) and **[[Golden-Wheelchair-Warranty]]** — confirmed
**separate** from [[Golden-Scooter-Warranty]]: the GP162 LiNX owner's
manual's warranty section explicitly covers GP162/GP205/GP207/GP605/GP620
under different terms (5yr frame — GP605 frame is LIMITED LIFETIME — 13mo
drive train/electronics/parts, 12mo batteries), confirming Golden
maintains separate warranty policies per product category, not just per
model. Broadened [[TruCharge-Diagnostics]] to include the GP162 PTC/VR2
table (same 10-bar architecture, adapted for independent left/right drive
motors instead of one scooter motor). Updated [[Golden]] and `index.md`
— 43 of 66 Golden files done; only chargers and cross-model accessory
docs remain in the Golden backlog.

Note: this cluster was originally started by a prior session that was
interrupted by a rate limit after writing the first 14 source pages; this
entry completes it (the LiNX Owner's Manual source page, all 4 model
pages, both new concept pages, and the manufacturer/index updates).

## [2026-09-10] ingest | Golden — Accessory Receiver Installation
## [2026-09-10] ingest | Golden — Adjustable Depth Seat Instructions
## [2026-09-10] ingest | Golden — Battery Charging Insert
## [2026-09-10] ingest | Golden — Cane and Crutch Holder Installation
## [2026-09-10] ingest | Golden — Connecting the Batteries
## [2026-09-10] ingest | Golden — Cup Holder Installation
## [2026-09-10] ingest | Golden — Golden Tips
## [2026-09-10] ingest | Golden — HP8204B Charger Operation
## [2026-09-10] ingest | Golden — Key and Key Switch Change
## [2026-09-10] ingest | Golden — LiteRider and Buzzaround Transaxle Change
## [2026-09-10] ingest | Golden — Measuring Seats
## [2026-09-10] ingest | Golden — Mobility All Models Flag Installation
## [2026-09-10] ingest | Golden — Mobility Seating Matrix
## [2026-09-10] ingest | Golden — MRC24-4LX Charger Operation
## [2026-09-10] ingest | Golden — Oxygen Holder and Walker Holder Installation
## [2026-09-10] ingest | Golden — Power Seat Operation
## [2026-09-10] ingest | Golden — Proflex Seat Instructions
## [2026-09-10] ingest | Golden — Right to Left Side Joystick Conversion
## [2026-09-10] ingest | Golden — Seat Belt Instructions
## [2026-09-10] ingest | Golden — Touch Up Paint Tips
## [2026-09-10] ingest | Golden — Universal Mirror Mount
## [2026-09-10] ingest | Golden — Mobility Seats

Ingested Golden's last cluster: 22 charger and cross-model accessory docs,
filed as 8 concept pages by actual topic rather than one page per document
— [[Golden-Accessory-Installs]] (8 universal install sheets),
[[Golden-Battery-Charging]] (both chargers + general care),
[[Golden-Seating-Systems]] (seat size-code catalog + the Proflex seating
base behind the "SMP" code — surfaces GR575/Patriot, GP205, GP207, GP208
as models with no manuals on file yet), [[Golden-Dealer-Tips]] (general
reminders — the only mention of lift chairs in this whole collection, no
lift chair manuals exist — plus touch-up paint), and four narrower
single-topic pages: [[Golden-Key-Switch-Replacement]],
[[Golden-Joystick-Side-Conversion]] (names the "Shark" controller,
cross-linked to [[GP6xx-Compass]]), [[Golden-Transaxle-Replacement]]
(explicitly named cross-model doc, cross-linked to
[[GL110-140-LiteRider]] and [[GB1xx-Buzzaround-XL]]), and
[[Golden-Power-Seat-Operation]] (speed/height interlock, cross-linked to
GP600). Updated [[Golden]] and `index.md` — **all 66 Golden manuals are
now ingested.** Golden is fully done wiki-wide; only Pride (10 files) and
Prism (1 file) remain in the entire wiki.

## [2026-09-11] ingest | Pride — J6 Specifications
## [2026-09-11] ingest | Pride — J6 VA Specifications
## [2026-09-11] ingest | Pride — J6 Operator Manual
## [2026-09-11] ingest | Pride — Q6 Edge 3 Stretto Specifications
## [2026-09-11] ingest | Pride — Q6 Edge Basic Troubleshooting
## [2026-09-11] ingest | Pride — Q6 Edge 3 Stretto Operator Manual
## [2026-09-11] ingest | Pride — Q-Logic Controller Basic Operation Instructions
## [2026-09-11] ingest | Pride — Q-Logic 3 Basic Operation Instructions
## [2026-09-11] ingest | Pride — Q-Logic 3 Programming Guide
## [2026-09-11] ingest | Pride — Tru-Balance 3 Power Positioning Systems BOI

Ingested all 10 Pride manuals in one batch pass (user asked for "all the
Pride docs"), covering two models and two cross-cutting systems. Created
model pages [[J6]] (two contract variants, J6/J6 VA, sharing hardware but
governed for different speed-vs-range tradeoffs — 4mph/15mi vs.
4.7mph/10mi) and [[Q6-Edge-3-Stretto]] (newer/higher-spec platform, faster,
longer range, 8-amp vs. J6's 5-amp charger, optional iLevel elevating
seat). Created two new concept pages: [[Joystick-Controllers]], synthesizing
both the legacy Q-Logic controller (end-user operation, full error-code
table) and Q-Logic 3 (touchscreen end-user BOI plus the full provider/ATP
programming guide — hand control, alternative proportional drives, head
array, sip-n-puff, switches, iAccess, Bluetooth mouse, Combined Functions
for seat actuators); and
[[Tru-Balance-3-Power-Positioning]], the wiki's first power-seating/
positioning-system concept page (tilt/recline/elevate range of motion,
factory inhibit matrix, iLevel, four armrest styles, TRU-Comfort cushion
system). [[Q6 Edge Basic Troubleshooting]] turned out to be a
general-family document (covers Q-Logic/NE+/NE electronics, not
Stretto-specific) — cross-linked from both [[Joystick-Controllers]] and
both model pages rather than treated as Stretto-only. Noted a
cleaning/disinfection guidance gap between the J6 OM (2018 revision,
lighter guidance) and the Q6 Edge 3 Stretto OM (2022 revision, detailed
named-disinfectant list) on both model pages. Updated [[Pride]] and
`index.md` — **all 10 Pride manuals are now ingested.** Only Prism (1 file)
remains uningested in the entire wiki.

Process note: several PDF reads in this session (initially four small
2-page spec/troubleshooting sheets, then re-reads of three longer manuals)
had their page images silently stripped by a tool-side "request limit"
before any content was visible, even on solo (non-parallel) Read calls of
a single document. Caught this by noticing the literal
`[media removed: request limit]` marker in tool output instead of an actual
rendered page, and reading a document is not complete until real
content — text or image — has been seen for every page, not just a
successful-sounding page count. Recovered by re-reading in smaller batches
and, for the four small text-heavy spec/troubleshooting sheets, by shelling
out to `pdftotext -layout` directly instead of the image pipeline — worth
reaching for `pdftotext` first on any manual that's mostly text tables
(spec sheets, error-code tables) rather than diagrams.

## [2026-09-11] ingest | Prism — C-450/C-625 Technical Manual

Ingested the wiki's only Prism document (user asked specifically for "the
Prism doc"), a 45-page field-service manual for the C-450/C-625 overhead
ceiling lift — troubleshooting, step-by-step repair sheets (pneumatic/
electrical/mechanical), LCD programming-mode reference, and a full
exploded-view parts catalog. Used `pdftotext -layout` for the text-heavy
troubleshooting/repair-sheet pages (proved reliable for the Pride spec
sheets last session) and image reads only for the diagram-only parts-list
pages (35–45). Created [[C-450-C-625]] as the model page (three PCB
configurations distinguished by air-switch count: 2/4/6). Notable find:
this lift has its own centrifugal overspeed governor, the same *concept*
as Bruno's stairlift safety brake but with different recovery behavior
(motor replacement here vs. Bruno's field reset) — updated the existing
[[Overspeed-Safety-Brake]] concept page to cover both manufacturers instead
of writing a separate Prism-only page, and generalized its tags/intro
accordingly. Updated [[Prism]] and `index.md`.

**Every manual in the entire wiki (Bruno, Golden, Pride, Prism — 96 files)
is now ingested.** No backlog remains.

## [2026-09-11] lint | full wiki health check — 24 orphan pages fixed, 1 duplicate PDF found, 1 concept gap confirmed

First full lint pass since the initial scaffold. Checked all five criteria
from `/CLAUDE.md`:

- **Un-ingested manuals**: none — verified 97 raw PDFs on disk map to 96
  distinct documents (see duplicate finding below) and all 96 have a
  `wiki/sources/` page.
- **Missing model pages**: none — all 23 models in `index.md`'s Models
  table have a corresponding `wiki/models/*.md` file, 1:1.
- **Orphan pages** (fixed): 24 source pages existed but had zero inbound
  `[[wikilink]]`s — discoverable only via directory listing or plain-text
  mentions in `index.md`'s prose Sources section, not through wiki
  navigation. All were legitimately-ingested pages whose parent concept
  page described them in bold prose (e.g. "**Cup holder**: ...") without
  ever linking the actual source page. Added `Source(s): [[...]]` lines to
  8 concept pages ([[Golden-Accessory-Installs]],
  [[Golden-Battery-Charging]], [[Golden-Dealer-Tips]],
  [[Golden-Key-Switch-Replacement]], [[Golden-Joystick-Side-Conversion]],
  [[Golden-Transaxle-Replacement]], [[Golden-Power-Seat-Operation]],
  [[Golden-Seating-Systems]]) and linked two backtick-filename mentions in
  [[Staircase-Measuring-System]] and [[Harmar]] to their actual source
  pages. Re-verified afterward: zero orphans remain except `index` and
  `log` themselves (expected — they're entry points, not content pages).
- **Broken links**: none found, before or after the fixes above (every
  `[[link]]` target resolves to a real page).
- **Contradictions/superseded revisions**: none newly found — the one
  known case ([[Picture Perfect Camera Overview (2020, superseded)]] vs.
  [[Picture Perfect Instructions (2022 Rev 5)]]) was already correctly
  flagged from an earlier session and is now also properly linked (see
  above).
- **Repeated concepts lacking their own page**: confirmed
  **Brake-Replacement** is still a real gap — 3 separate Golden brake
  procedures ([[2-Piece Brake Replacement (LiteRider, Buzzaround XL, Buzzaround Lite)]],
  [[Brake Replacement (GL110, GL140)]],
  [[Compass Sport Brake Replacement (GP605)]]) live on 3 different model
  pages with no page comparing them side by side. Documented in
  `index.md`'s candidate list rather than writing it now — synthesizing
  three procedures is ingestion-level work, not a mechanical lint fix.
  Also reassessed **Seat-Systems**: no longer really "backlog" — Golden
  and Pride each settled on their own manufacturer-specific seating
  concept page instead, which looks like the intended pattern now, not a
  gap.

**New finding, not previously known**: `MANUALS/Golden/GP162 LiteRider PTC
Golden SG 05.16.2014.pdf` and `MANUALS/Golden/LITERIDER PTC_GP162_
SG_REVA_ 051614.pdf` are byte-identical (same md5 hash) — the same file
saved under two names. This is why Golden's 66-on-disk count was always
one higher than its 65 source pages, and it was already handled correctly
(one source page, not two) without anyone noticing the duplicate — no wiki
content was wrong, just previously undocumented. Added footnotes to
[[Golden]] and `index.md` explaining it, mirroring the existing Harmar
misfile footnote. Did not touch the raw file itself — `MANUALS/` is
immutable per policy; flagging for the human to decide whether to delete
the duplicate on disk.

## [2026-09-11] lint | re-verified clean, closed the Brake-Replacement gap

Re-ran all orphan/broken-link checks from the previous lint pass (0 orphans,
0 broken links — no drift since the 2026-09-11 pass). Then closed the one
confirmed-but-deferred gap from that pass: wrote
[[Brake-Replacement]], consolidating Golden's 3 scattered brake procedures
side by side — [[2-Piece Brake Replacement (LiteRider, Buzzaround XL, Buzzaround Lite)]],
[[Brake Replacement (GL110, GL140)]], and
[[Compass Sport Brake Replacement (GP605)]]. Notable finding while writing
it: the two GL110/140 documents aren't redundant/contradictory as they
might look — the earlier one (2011-03-15) is a one-time retrofit from an
old rearward-facing lever to the new upward-facing style, and the later
one (2011-11-30) is the general like-for-like replacement procedure for
that new style once installed; a field tech needs to check which lever
orientation is already on the unit before picking a procedure. Also
confirmed the real complexity spread across the three families: 5-step
puck-and-handle swap (LiteRider/Buzzaround) vs. 28-step full
drive-assembly pull (Compass Sport GP605) for the same underlying
component category. Linked the new page from [[GB1xx-Buzzaround-XL]],
[[GL110-140-LiteRider]], and [[GP6xx-Compass]], added it to `index.md`'s
Concepts table, and removed it from the candidates-not-yet-written list.

## [2026-09-11] ingest | Harmar — Helix, Highlander II, Outside Vehicle Lifts, Pinnacle SL300/SL600 (14 files, first real Harmar product-line ingest)

Ingested the human's newly created `MANUALS/Harmar/` folder in one batch
pass (14 files: 8 distinct PDFs after dedup + 1 docx, the docx via
zip/XML extraction since no docx-to-text tool was available; `pdftotext
-layout` for all PDFs). Harmar previously had exactly one document on
file — a misfiled camera-measuring manual under Bruno's folder — so this
is the wiki's first look at what Harmar actually makes.

Created five model pages: [[Helix]] (CSL500/510/511/560/570/589/590/595
curved stairlift — confirms "Helix" is the marketing name for the CSL
series, resolving a naming mystery flagged in the original Harmar stub),
[[HighlanderII]] (VPL400-1400 enclosed vertical platform lift — ACME
screw drive, 2/3hp gearmotor, optional battery backup, an extensive
4-LED/32-LED status system), [[Pinnacle-SL300]] and [[Pinnacle-SL600]]
(straight-rail stairlifts — SL300 residential-only, SL600 the first
Harmar product confirmed commercial-rated/FDA-registered), and
[[AL-Series-Outside-Vehicle-Lifts]] (hitch-mounted lifts for unoccupied
mobility devices — confirmed both manuals on file are generic across
~20+ model numbers despite being filed under `AL100-...` filenames, not
AL100-specific).

Two file-triplication findings (md5-confirmed, same pattern as Golden's
known duplicate): `AL100/AL300/AL301-OutsideLifts_Owners-Manual.pdf` are
one byte-identical file under three names, and likewise for the three
`...Installation-and-Service-Manual.pdf` files — one source page each,
not three. Also confirmed `Helix_Photo-Measuring-Manual.pdf` (Rev C,
2023) is a **newer revision** of the already-ingested
[[CSL Series Photo Measuring Manual]] (Rev B, 2019, misfiled under
Bruno's folder) — created a new source page rather than overwriting the
old one (immutable raw sources, and the old file is still on disk under
Bruno's tree), cross-linked both ways, and updated
[[Staircase-Measuring-System]] with the finding.

Created two new concept pages: [[Harmar-Warranty]] (every one of
Harmar's five product lines carries its own distinct warranty term — no
shared scooter/wheelchair- or stairlift/vehicle-lift-style split the way
Bruno and Golden have) and [[Harmar-Stairlift-Beep-Codes]] (Helix/SL300/
SL600 share a near-identical beeps-only major-fault scheme — SL300's
table stops at 8 codes vs. the other two's 9, and SL300 alone caveats
codes 3-6 as "if configured for your model"). Updated
[[Overspeed-Safety-Brake]] to add a **third** manufacturer/mechanism:
HighlanderII's Over-Speed Governor (OSG) switch on the ACME drive screw,
mechanically distinct from Bruno's centrifugal governor and Prism's
worn-shaft trigger, sharing a circuit with the VPL's pit switch. Rewrote
[[Harmar]] from a one-document stub into a full manufacturer page.

Not linked as a technical reference: [[Vehicle Lift Phone Interview Form]]
— a one-page internal Performance Medical Supply sales-intake script
(docx), not a Harmar-authored document; kept as a source page for
completeness since it's on disk, but doesn't feed any model/concept page.

No install or tech-support manual exists yet for Helix, SL300, or SL600
(owner's manuals only) — flagged as backlog on [[Harmar]] and in
`index.md`, but not a missing-ingest issue since no such document is on
disk. Updated `index.md` (manufacturer table, 5 new model rows, 2 new
concept rows, sources list, backlog section).

## [2026-09-12] ingest | Harmar — second pass: install manuals, bulletins, and a whole new Hoist-lift product category (46 new files)

The human added ~46 more files to `MANUALS/Harmar/` (copied in from a
separate master library at `/home/lu/Work/MANUALS/Harmar/` that already
existed outside this git repo — confirmed via md5 that 2 files were
exact duplicates of already-ingested content and skipped, and excluded 7
product-photo/DAM-metadata-export files as non-manual assets). Extracted
text via `pdftotext -layout` for all PDFs and a zip/XML strip for 2 docx
bulletins, same approach as the first Harmar pass.

**Closed the entire "no install manual" backlog** flagged in the previous
Harmar entry: [[Helix Install Manual]], two revisions of the SL300 install
manual ([[Pinnacle SL300 Install Manual (2026, Rev L)]], superseding
[[Pinnacle SL300 Install Manual (2024, Rev K, superseded)]]), and
[[Pinnacle SL600 Install Manual]] are all now on file. Also found a
**Power Swivel / Power Footrest install supplement**
([[Pinnacle Power Swivel and Power Footrest Install Supplement]]) that
resolves an open question from the first pass: SL600 does support both
options (SKUs SL600-PS/PF/PSPF), the owner's manual just never mentioned
them.

**Discovered Highlander II is documented as three separate configurations**,
not one: the already-known "with Enclosure" version, a previously-unknown
open-frame **"no enclosure"** version with its own non-sequential P/N
series ([[Highlander II Install Manual (no enclosure)]]), and a
residential-only **VPL400-X** trim with a shorter 2-year warranty and its
own install manual, spec sheet, and full wiring-schematic set. Restructured
[[HighlanderII]] to cover all three under one page rather than
fragmenting further, since they share the same core electronics/OSG/
troubleshooting architecture.

**Discovered a second, entirely distinct Harmar vehicle-lift category**:
[[Hoist-Series-Inside-Vehicle-Lifts]] ("Hoist" lifts — mounted inside the
cargo area, boom swings outside to load the mobility device, as opposed
to [[AL-Series-Outside-Vehicle-Lifts]]'s hitch-mounted platform) — found
via a marketing brochure and confirmed by AL425/AL435/AL825 parts
diagrams and one service bulletin. No narrative owner's/install manual is
on file yet for this line, only the brochure/bulletin/diagrams. Also
added two previously-undocumented Outside Vehicle Lift model numbers to
[[AL-Series-Outside-Vehicle-Lifts]]: AL600 ("Hybrid," from a parts
diagram) and AL901/AL904 (from a license-plate-riser bulletin).

Corrected [[Overspeed-Safety-Brake]]'s Helix entry from the first pass'
placeholder: Helix's mechanism is confirmed **a mechanical rack/sprocket
jammer, field-resettable**, not an unknown/undocumented one — genuinely
distinct from both Bruno's/Prism's governors and Harmar's own
HighlanderII OSG switch (Harmar now contributes two of the concept's four
documented mechanisms). A pair of wiring schematics complicates this
slightly — a 2014 schematic calls the same assembly a "Parachute
Centrifugal Brake," a 2021 one calls it "OSG" — flagged as unreconciled
rather than resolved. Also corroborated (via independent documents) that
"SL600HD" and SL600 "RAVE"/"LLSL" sub-variants are real, not typos.

Created 4 consolidated reference source pages (rather than one page per
file) for lower-narrative-value material: [[Harmar Evaluation and Order
Forms]] (6 sales forms), [[Harmar Product Spec Sheets]] (4 spec sheets),
[[Harmar Parts Diagrams]] (9 engineering BOM drawings), and
[[Harmar Wiring Schematics]] (6 wiring diagrams) — a deliberate scope
decision to avoid 25 near-empty source pages, each still extracting every
genuinely new fact found. 9 technical bulletins each got their own page
per existing precedent (each documents a distinct field issue).

Rewrote [[Harmar]] to reflect the full picture: 3 product categories
(stairlifts, platform lifts, two kinds of vehicle lifts), 8 model pages,
and Harmar's now-confirmed pattern of using completely different
mechanisms/terminology across its own product lines rather than one
company-wide standard. Updated [[Harmar-Warranty]] (VPL400-X's shorter
2yr term, Hoist-series' 3yr transferable term, resolved SL600 Power
Swivel/Footrest question) and [[Harmar-Stairlift-Beep-Codes]] (flagged an
unresolved SL600 owner's-manual-vs-install-manual beep-count
discrepancy, 9 codes vs. 8). Updated `index.md` throughout (manufacturer
file counts, 1 new model row, updated concept-table descriptions, full
sources list, backlog section).

## [2026-09-12] lint | found an entire un-ingested manufacturer category (Ramps), fixed 7 cosmetic broken-link line-wraps
## [2026-09-17] lint | reorganized wiki/sources/{Golden,Harmar,Pride,Prism} into product-line subdirectories, matching Bruno's existing layout (109 files moved, no content changes, no links broken — cross-references use [[wikilinks]] resolved by filename)
## [2026-09-17] ingest | AutoSlide — Installation Manual (Standard, iLock, Elite, Elite iLock): a new manufacturer and a different product category (automatic sliding-door retrofit kit, not mobility equipment). Raw files found outside the repo at /home/lu/Work/MANUALS/{AutoSlide,Open Sesame}/ and copied into MANUALS/ preserving their original foldering (gitignored, not committed). Flagged as an open question whether this belongs in the wiki's stated scope — see [[AutoSlide]].
## [2026-09-17] ingest | AutoSlide — RFID Pet Sensor Operation Instructions: physically filed under a mismatched MANUALS/Open Sesame/ folder despite being entirely AutoSlide-branded content; not confirmed whether misfile or a real second brand/reseller name (parallel to the pre-existing Harmar-doc-under-Bruno case). Confirms a second AutoSlide controller product name, "Multidrive," not otherwise documented.
## [2026-09-17] lint | post-AutoSlide-ingest health check — 0 broken wikilinks (1 line-wrap fixed in AutoSlide.md), 0 orphan pages across all 195 pages, raw-vs-source file-count deltas all already explained by existing index.md notes (Ramps backlog unchanged, AutoSlide 2-for-2 exact match). No new contradictions found.
## [2026-09-17] query | confirmed via web search that "Open Sesame" (opensesamedoor.com) is a real, separate manufacturer of automatic swing-door operators, commonly sold alongside AutoSlide by the same door-access dealers — resolves the open question raised by this week's AutoSlide ingest. The RFID pet-sensor file in MANUALS/Open Sesame/ is a confirmed misfile (100% AutoSlide-branded content), not a real Open Sesame document. Updated AutoSlide.md, the RFID source page's filing note, and index.md accordingly; flagged a new possible backlog item — real Open Sesame manuals may exist and haven't been found yet.
## [2026-09-17] lint | split wiki/sources/AutoSlide/ into product-line subdirectories (Drive System, Accessories), matching Bruno/Golden/Harmar/Pride/Prism's existing layout — grouped by actual content (install manual vs. accessory doc) rather than mirroring the raw MANUALS/AutoSlide vs. MANUALS/Open Sesame split, consistent with how the earlier reorg handled the Harmar-doc-under-Bruno-folder misfile. 2 files moved, no content changes, no links broken.

Full lint pass against all five `/CLAUDE.md` criteria.

- **Un-ingested manuals**: found a real gap — `MANUALS/Ramps/` (6 files: 4
  "EZ Access"-brand ramp PDFs/docx including a 49-page install guide, plus
  2 pricing sheets) has no manufacturer stub, no source pages, and no
  mention anywhere in the wiki or `CLAUDE.md`'s manufacturer list. This
  folder was already on disk (same 2026-09-11 13:06 timestamp as the rest
  of `MANUALS/`) but was never flagged by any prior ingest or lint pass.
  Added it to `index.md`'s manufacturer table and ingestion backlog as a
  new category; **not ingested** in this pass (lint only, per the human's
  request) — flagging for a future ingest session. Everything else
  (Bruno/Golden/Pride/Prism/Harmar) confirmed fully ingested against
  what's on disk.
- **Missing model pages**: none — every model referenced across
  manufacturer pages either has its own model page or is explicitly
  flagged as backlog with no manual on file (Golden's GR575/Patriot,
  GP205, GP207, GP208; Harmar's "Sierra IL500").
- **Orphan pages**: zero — all 191 wiki pages (excluding `index`/`log`
  themselves) have at least one inbound `[[wikilink]]`.
- **Broken links**: found and fixed **7 line-wrapped wikilinks/filenames**
  that don't resolve as real links because a literal newline splits the
  target name — 4 pre-existing (from early Bruno-ingest sessions, in the
  two Picture Perfect cross-links and one SRE-3050 install-manual link)
  and 1 pre-existing in a Harmar source page from this week's own ingest.
  Rewrapped all of them onto clean lines; left 3 similar-looking
  occurrences in `log.md` alone since those are literal example syntax
  in prose ("`[[wikilink]]`"), not real links, and `log.md` is
  append-only/historical besides.
- **Repeated concepts lacking their own page**: one soft candidate, not
  urgent enough to write now — Harmar's Pinnacle folding rail (SL300FR/
  SL600FR), including the detailed left/right handing-reversal procedure,
  is currently shared prose duplicated across
  [[Pinnacle SL300 Install Manual (2026, Rev L)]] and only summarized on
  the [[Pinnacle-SL300]]/[[Pinnacle-SL600]] model pages — only 2 models
  share it so far, thinner than the [[Brake-Replacement]] case that
  justified writing a page.
- **Contradictions/superseded revisions**: none newly found. The two
  known superseded-revision pairs (Bruno's Picture Perfect 2020→2022, and
  this week's Harmar SL300 install manual K→L) are both correctly
  cross-linked. The already-flagged SL600 beep-code count discrepancy
  (owner's manual: 9 codes; install manual: 8) and the Helix overspeed
  naming ambiguity (2014 "Parachute Centrifugal Brake" vs. 2021 "OSG")
  remain open, as previously documented — not newly discovered.

Updated `index.md` (new Ramps manufacturer-table row and backlog entry).
## [2026-09-17] ingest | Harmar — Hybrid Vehicle Lifts (AL600/AL690, 2025) Owner's Manual and Installation and Service Manual, plus AL6000 Series (2021-22) Owner's Manual and Installation and Service Manual: a third, previously-undiscovered Harmar vehicle-lift architecture (structural cargo-area leg + powered swing-out tower, no hitch, no boom) found by checking an out-of-repo MANUALS/Harmar/ drop for new sources. New model page [[Hybrid-Vehicle-Lifts]] covers both hardware generations (AL6000/AL6000HD: richer accessory set — Q'Straint retractors, hold-down arm, puddle lights, adjustable mounting brackets; AL600/AL690: simplified 2025 successor). Resolves the previously-flagged "AL600 Hybrid" parts-diagram-only mention — corrected [[AL-Series-Outside-Vehicle-Lifts]], [[Harmar Parts Diagrams]], and [[Harmar]]'s naming-quirks section accordingly. Added a Hybrid row to [[Harmar-Warranty]]. 2 renamed-but-byte-identical duplicate Helix files and 10 product-photo/DAM-metadata files (5 AL425HD photos, 3 more AL425 photos, 2 metadata CSVs) were not ingested as non-manual/duplicate content, per the wiki's existing exclusion pattern.
## [2026-09-17] ingest | Bruno — ASL-250 Install Manual (2019): an older hardware generation of the Out-Sider vehicle lift, found by checking an out-of-repo MANUALS/Bruno/ drop for new sources (all other files there were already-ingested duplicates). New model page [[ASL-250]] documents it as [[ASL-275]]'s predecessor — same branding and core architecture, but a third platform family ("HTP", ramped, FWD/RWD/MWD chock configurations) not present anywhere in the ASL-275 documentation, plus a lighter installed weight and a narrower/differently-tabled height-adjustment range. Confirms the shared [[Vehicle-Lift-Power-Wiring]] fuse is specifically an ATO 30A type (previously ambiguous from ASL-275 alone) and that the Bruno Gold vehicle-lift warranty text (see [[Warranty]]) is now confirmed identical across all three Bruno vehicle lifts (PUL-1100/ASL-275/ASL-250).
## [2026-09-17] ingest | Prism — P440 User Manual (2017), plus Vancare, Inc. — Ceiling Lift Installation Guide (2021): both found by checking an out-of-repo MANUALS/Prism/ drop for new sources. P440 is a portable ceiling lift (carried by hand, motorized up/down only) distinct from the fixed-track [[C-450-C-625]] — new model page [[P440]]. The Vancare document turned out to be a different manufacturer's 213-page track-system install guide, not Prism-authored — new manufacturer page [[Vancare]] (kept separate, not merged into Prism, since it has its own authorship/support chain). Its cross-compatibility tables revealed two further undocumented Prism model numbers, C-800/C-1000 (C-Series) and P-600 (Portable), plus confirmed Prism's portable lifts also run on three competing track brands (Mikyway, Guldman, ArjoTrack). Also fixed a pre-existing index.md undercount that omitted the already-ingested Ceiling Lift Evaluation Form from Prism's source listing.
## [2026-09-17] ingest | Red Hawk (new manufacturer folder) — 5 folding power-wheelchair manuals: Air Hawk, Eagle HD, Falcon, Phoenix, Pegasus Plus Heavy Duty. Discovered that "Red Hawk" is Performance Medical Supply's own organizational folder name, not a brand — the 5 manuals actually cover two unrelated Chinese manufacturers sold under four model names by two distributors: Nanjing Jin Bai He Medical Apparatus Co., Ltd. (sold as "Air Hawk" by Gilani Engineering PTY LTD, Australia, and as "Eagle HD"/"Falcon" by Discover Your Mobility Inc., USA — confirmed via byte-for-byte-identical technical parameter tables between Air Hawk and Eagle HD) and Anhui JBH Medical Apparatus Company Limited (sold as "Pegasus Plus Heavy Duty" for model DC02, despite no "Pegasus" branding in the manual itself). Phoenix uses a fourth, unrelated manual template with manufacturer unconfirmed and a stray "TREK Mobility" battery-charger reference. New manufacturer page [[Red Hawk]] and four model pages ([[Air-Hawk-Eagle-HD]], [[Falcon]], [[Phoenix]], [[Pegasus Plus (DC02)]]) document the full multi-brand picture. Flagged a data-quality issue: the Pegasus Plus/DC02 source PDF is truncated — its own table of contents promises warranty/troubleshooting/diagnostics/wiring/EMC content through page 44, but the file stops at page 27.
## [2026-09-17] ingest | Prism — P440 Owner's Manual (2021, Rev 19-Oct) and Prism Castor 2 Post Lift Stand Installation Manual (2018): found by re-checking the out-of-repo MANUALS/Prism/ drop for new sources. The 2021 P440 manual is a newer, more complete revision of the already-ingested 2017 [[P440 User Manual]] (now marked superseded) — adds an accessories catalog, service record forms, and per-manufacturing-year carabiner variations. Critically, it's the first document in this wiki to explicitly confirm **Handicare** as P440's actual manufacturer (nameplate branding + Handicare USA/Canada contact info + a warranty section that splits Handicare's new-equipment guarantee from Prism's refurbished-equipment guarantee) — resolving a long-open note on [[C-450-C-625]]'s page about an unexplained "Handicare" component-brand legend in the Ceiling Lift Evaluation Form. The Castor 2 Post Lift Stand (co-branded Prism/Handicare, new model page [[Prism-Castor-2-Post-Lift-Stand]]) independently corroborates the relationship, and its three part numbers match the C-Series lifts' 450lb/625lb capacities exactly. Updated [[Prism]] with a dedicated "Confirmed manufacturer relationship: Handicare" section; C-450/C-625 itself is not yet confirmed as Handicare-made.
## [2026-09-17] lint | post-Red-Hawk/Prism-Handicare-ingest health check — found and fixed 1 real defect: a wikilink literally split across a line break ([[Red\nHawk]]) in wiki/models/Phoenix.md, introduced during today's Red Hawk ingest. Full checks otherwise clean: 0 broken wikilinks (excluding log.md's own literal example syntax, left as-is per established convention), 0 orphan pages across all 219 pages (every model/manufacturer/concept page has an inbound link and an index.md table row), 0 duplicate page names. Raw MANUALS/ vs sources/ delta check found only the already-documented gaps: 10 Harmar product-photo/CSV assets and 6 un-ingested Ramps files (existing backlog item, unchanged). Confirmed the Golden GP162 LiteRider PTC duplicate pair (md5-matched) is the same one already noted in index.md's 66-vs-65 count — no new duplicates found across the whole MANUALS/ tree. All source pages carry `type: source` frontmatter, all model pages carry `manufacturer:` frontmatter, and all frontmatter blocks are well-formed. Supersession cross-links (P440 2017→2021, SL300 Rev K→L, Picture Perfect 2020→2022) all correctly linked in both directions.
## [2026-09-24] ingest | EZ-ACCESS — 11 web clippings (blog articles, 2021–2026) from the vault's Clippings/ folder
The wiki's first non-manual source type. The clippings were copied to `MANUALS/Clippings/` as the raw layer, and the originals were left in place.
- New manufacturer page: [[EZ-ACCESS]]. It resolves the "Ramps" backlog category's identity, but the 6 `MANUALS/Ramps/` files are still not ingested.
- 11 source pages under `sources/EZ-ACCESS/`, filed as General, PATHWAY 3G, PATHWAY HD, TRANSITIONS, and Portable Ramps.
- 5 product pages: [[TRANSITIONS-Threshold-Ramps]] (full size tables for all 5 threshold products), [[SUITCASE-Ramps]], [[GATEWAY-3G]], [[PATHWAY-3G]], [[PATHWAY-HD]].
- 3 concept pages: [[Ramp-Slope-and-Length]], [[ADA-Ramp-Requirements]], [[Ramp-Site-Planning]].
- Key synthesis: the slope page cross-references ramp ratios against the max-incline ratings already in the wiki. 1:12 is fine for every rated device. 1:8 exceeds the 6° rating of [[J6]] and [[Air-Hawk-Eagle-HD]]. Ramp back-links were added to 6 device model pages.
- Flagged: the articles contradict each other on residential 1:8 (acceptable vs. non-mobility only), and two articles print slightly different "1:12" rise-to-length tables. The TRANSITIONS Modular Entry Ramp's listed sizes leave 0.5 in threshold gaps. The ADA clipping is truncated before its handrail and surface sections.
## [2026-09-24] update | Ramp slope house standard: 1:12 only (4.8° on an angle meter), plus a door-transition field note
Direction from the human, recorded as a PMS house standard in CLAUDE.md.
- Rewrote [[Ramp-Slope-and-Length]] around the standard. The articles' 1:10, 1:8, 1:6 and 1:4 guidance is now marked superseded, and 4.8° angle-meter verification was added.
- Updated [[ADA-Ramp-Requirements]], [[Ramp-Site-Planning]], [[SUITCASE-Ramps]], [[EZ-ACCESS]], and two source pages.
- Added the field note to [[Ramp-Site-Planning]] and [[TRANSITIONS-Threshold-Ramps]]: the entry door transition's leveling feet can sometimes be removed to get the right height, but some entryways still won't sit flush with the transition.
## [2026-09-24] update | Ramp slope standard: SUITCASE ramps exempt from 1:12; leveling-feet note pinned to the Angled Entry Ramp
Clarification from the human.
- SUITCASE folding ramps are temporary-use only (e.g. loading a scooter into a van), so the 1:12 rule doesn't apply to them. For those ramps, the device's rated incline is the relevant limit.
- Updated CLAUDE.md, [[Ramp-Slope-and-Length]], [[SUITCASE-Ramps]], [[Ramp-Site-Planning]] and [[ADA-Ramp-Requirements]].
- The door-transition leveling-feet note is confirmed to refer to the TRANSITIONS Angled Entry Ramp. Its wording on [[Ramp-Site-Planning]] and [[TRANSITIONS-Threshold-Ramps]] now names that product.
## [2026-09-24] update | GATEWAY 3G reclassified as permanent (PMS), so 1:12 applies
Clarification from the human: the GATEWAY 3G is long-term. It can technically be moved, but PMS and this wiki treat it as permanent. It is not exempt from 1:12 the way temporary-use SUITCASE ramps are. Updated CLAUDE.md, [[GATEWAY-3G]], [[Ramp-Slope-and-Length]], [[Ramp-Site-Planning]], [[SUITCASE-Ramps]], [[EZ-ACCESS]] and index.md. The source pages still record EZ-ACCESS's own "portable/semi-permanent" marketing wording as-is.
## [2026-09-24] ingest | EZ-ACCESS — Pathway Modular Access System Assembly Manual (P/N 10565, rev 05-12-15), plus U.S. Access Board — ADA Technical Guide: Ramps and Curb Ramps (July 2015)
- **Pathway manual**: the first real EZ-ACCESS manual in the wiki. It is branded "Pathway", not "3G", and gives **850 lb, residential use only**, while a 2021 article claims 1,000 lb for modular ramps. It is probably the pre-3G generation; [[PATHWAY-3G]] now carries a generation note, and the question is flagged for the human.
- Rewrote [[PATHWAY-3G]] with the manual's content: full part-number table, installation essentials (bracing at 36 in and 72 in, at most 3 sections joined at a time, the handrail-bracket 6 in misalignment gotcha, transition anchoring), optional equipment (bridge plate 6 in max gap, tie strap ½ in ADA gap, lightning ground rod), the full tie-down procedure, maintenance, and the lifetime warranty.
- Clarified from the manual's figures (Fig. 3.19/3.20) that the transitions' "4°/8°" limits are **plan-view (horizontal) angles** between the ramp and the platform edge. They are not slope, and they don't conflict with the 1:12 (4.8°) standard.
- **ADA guide**: `ADA_Rules_ramps.pdf` was not in the repo's `MANUALS/Ramps/`. It was copied in from the out-of-repo `/home/lu/Work/MANUALS/Ramps/` drop. It is a U.S. Access Board document, not EZ-ACCESS, so it is filed under a new `sources/Standards/ADA/` convention (added to CLAUDE.md). Handrail dimensions were read from the drawings on pp. 5–6.
- Rewrote [[ADA-Ramp-Requirements]] from the guide: §-referenced slope, width, landing, handrail, edge-protection and curb-ramp rules; the "all required ramps must be permanent" rule (consistent with PMS's GATEWAY/PATHWAY classification); and three corrections to the EZ-ACCESS blog summary. Noted that ADA's 1:10/1:8 alteration exceptions are overridden by the house 1:12 standard.
- Also updated [[Ramp-Slope-and-Length]], [[Ramp-Site-Planning]], [[EZ-ACCESS]], [[Securing PATHWAY 3G Before a Storm]] and index.md.
## [2026-09-24] ingest | EZ-ACCESS — Parts and Pieces sheet (2018-09-12) and Layout Key and Install Time sheet (rev 2019-07-10)
Two one-page Visio sheets, read from rendered images because their extracted text was scrambled. Neither names an author; the part nicknames ("Moo-Abs", "Muck-Bee", "Mr. Heeber") and the install-time/prior-authorization content suggest internal PMS/dealer references. Both are filed under `sources/EZ-ACCESS/General/`.
- New concept page [[Ramp-Install-Time-Estimates]]: per-component labor minutes, with a worked example.
- [[PATHWAY-3G]] gained the full size catalog:
  - ramp sections 2–8 ft (bariatric 48 in only 2–6 ft)
  - width stack-up, 36 in usable to **44 in at the feet**
  - standard and low-profile platform part numbers; custom platforms max 5×5
  - MSTS support-tube lengths and the low-profile foot (rises under 6.5 in)
  - transition depths: MRUT 4, MRLT 6, MRGT 12 in
  - bracing counts, connector and nickname table (MRHRL end loop 12 in, matching the ADA extension)
- **850 lb capacity** is corroborated by the 2018 sheet, now the stated working figure.
- [[TRANSITIONS-Threshold-Ramps]]: TAER12/24/36 PMS working ranges (1.5–2, 2.25–3.5, 3.5–4.5 in) are narrower than the 2021 blog ranges; the PMS ranges were adopted. Added TAEM/TMEM part numbers and RT heights.
- [[SUITCASE-Ramps]]: 29.5 in width, weights by length, TLE lip 3 → 9 in.
- The odd blog rise-to-length values remain unexplained (the Layout Key doesn't cover them); that lead is closed.
- Pay-scale sheets skipped per the human.
## [2026-09-24] update | Correction: the parts and layout-key sheets are not PMS documents
The human doesn't recognize the part nicknames ("Moo-Abs", "Mr. Heeber"), so the earlier inference that [[EZ Access Parts and Pieces]] and [[EZ Access Layout Key and Install Time]] are internal PMS sheets was wrong. Both are now described as **origin unknown**.
- Removed the "PMS working range" / "PMS sheet" wording from [[TRANSITIONS-Threshold-Ramps]]. The TAER range conflict (parts sheet vs. 2021 blog) is now marked unresolved, with the narrower parts-sheet ranges noted as the conservative choice.
- Removed the nicknames from the [[PATHWAY-3G]] tables. They are mentioned only on the source page, as printed labels not used at PMS.
- Added a caution to [[Ramp-Install-Time-Estimates]]: its times aren't confirmed as PMS's own standard.
- Updated [[EZ-ACCESS]] and index.md to match.
## [2026-09-24] ingest | PMS — Ramps Handbook (Performance Medical Handbook: RAMPS, in-house training, created 2021-02-25, modified 2026-06-17)
PMS's own ramp evaluation and design training document (docx author "PMS", ends with an employee training sign-off). It is the source of the 1:12 / 4.8° house standard and now the highest-authority ramp document in the wiki. Filed as [[Ramps Handbook]] under `sources/EZ-ACCESS/General/`, following the precedent of PMS's Harmar forms.
- [[Ramp-Site-Planning]] now leads with the PMS evaluation procedure: start inside and meet the user (chair type/model, weight); fire-egress path through the house; 5 ft of level space at the exit door; five design rules; photos and cone layout.
- The house standard is refined to "slope meter 4.8° **or less**", with a new rule to round the run **up** to whole feet. The rule is in CLAUDE.md and [[Ramp-Slope-and-Length]].
- **Flag**: the handbook's own example (28.5 in rise → 28 ft, from an embedded EZ-ACCESS Incline Calculator screenshot) is 4.85°, over its own 4.8° limit. 29 ft gives 4.68°. Raised with the human; the raw source was not edited.
- [[ADA-Ramp-Requirements]] now compares the handbook's "5 ADA guidelines" with the Access Board guide. The main difference is the handbook's minimum of one continuous handrail vs. ADA's both sides above 6 in of rise.
- EZ-ACCESS / `MANUALS/Ramps/` is now fully ingested apart from the deliberately skipped pay scales.
## [2026-09-24] update | Confirmed: round the ramp run up (28.5 in rise → 29 ft)
The human confirmed that the [[Ramps Handbook]] example should round up to 29 ft, not down to 28 ft. Updated its source page, [[Ramp-Slope-and-Length]] and index.md. The raw docx still says 28 ft.
## [2026-09-24] update | PATHWAY = PATHWAY 3G (same product); capacity settled at 850 lb
The human confirmed that "3G" is synonymous with PATHWAY. The 2015 "Pathway" Assembly Manual is therefore the PATHWAY 3G install manual. The generation caveat was removed from [[PATHWAY-3G]], its manual's source page, [[EZ-ACCESS]] and index.md. Capacity is settled at **850 lb** (manual + 2018 parts sheet). The 2021 blog's "1,000 lb" is marked overridden on [[Different Types of Threshold Ramps]] and [[Ramp-Site-Planning]]. The human also asked to leave the Ramps Handbook docx unedited.
## [2026-09-24] update | GATEWAY 3G classification re-confirmed: not temporary, so 1:12 applies
Checked because an earlier "the 3G is long-term / modular" answer may have referred to PATHWAY 3G. The human confirmed that GATEWAY 3G is not temporary like the SUITCASE ramps. There is no change in substance; [[GATEWAY-3G]] now cites the confirmation.
## [2026-09-24] lint | 245 pages; 0 broken links, 0 orphans, 0 duplicate names; fixed 2 line-split wikilinks and 2 stale notes; flagged Bruno raw-path drift
- **Fixed**:
  - 2 wikilinks split across a line break ([[J6]], [[J6 Specifications]]); the same defect class as the 2026-09-17 lint.
  - A stale "Ramps un-ingested" note in [[AutoSlide]].
  - index.md's "all manuals ingested" sentence, which now mentions the skipped EZ-ACCESS pay scales.
- **Flagged, not changed: Bruno raw-path drift.** All 20 Bruno source pages (and the Harmar CSL photo-measuring page) cite `MANUALS/Bruno/<Product Line>/<file>.pdf`. On this device, `MANUALS/Bruno/` is **flat**: the same 21 files, with no subfolders. The out-of-repo drop at `/home/lu/Work/MANUALS/Bruno/` is flat too. Queries on this device will therefore report these PDFs as "not cached". MANUALS/ is local per device, so the subfolder paths may still be right elsewhere. Asked the human which layout is canonical.
- **Flagged**: the Harmar exclusion total is stated as 17 image/CSV files, but only 10 unreferenced image/CSV files are on disk here (13 non-PDF files total). This may be a device difference or an overcount; not resolved.
- Every other raw file in MANUALS/ is referenced by a source page, apart from the known GP162 PTC duplicate, the Harmar `_dupe1` duplicate and the skipped pay scales. Frontmatter is otherwise well-formed. The 4 consolidated Harmar reference pages intentionally have no single `source:`.
- Ramp-area consistency is clean: 1:12 / 4.8°-or-less, the SUITCASE exemption, GATEWAY 3G permanent, PATHWAY = 3G at 850 lb, and origin-unknown sheets are consistent across all pages.
## [2026-09-24] lint | Bruno raw-path drift resolved on this device (local only, no wiki changes)
Per the human: recreated the `MANUALS/Bruno/<Product Line>/` subfolders (Bruno Straight SL, VPL, Bruno Curved SL, Vehicle Lifts) on this machine by **copying** the 20 flat PDFs to the paths their source pages cite. The originals were left in place and the copies were byte-verified with cmp. Every `source:` path in the wiki now resolves on this device. MANUALS/ is gitignored, so nothing changed in git except this log entry.
## [2026-09-24] lint | Resolved: the Harmar exclusion count is 10, not 17 (double count)
Investigated the discrepancy flagged earlier today. All 10 Harmar image/CSV assets (5 AL425HD photos, 3 AL425 photos, 2 DAM metadata CSVs) have been in the out-of-repo drop `/home/lu/Work/MANUALS/Harmar/` since 2026-09-11, before both the second pass (2026-09-12) and the third pass (2026-09-17).
- The second pass excluded them but logged the count as "7" without naming the files. It also didn't copy them into the repo.
- The third pass found the same files again, copied them in (hence the repo mtimes of 2026-09-17), excluded them, and added 10 to the earlier 7 to get "17".
- Only 6 drop files are dated 2026-09-17 (4 Hybrid manuals + 2 duplicate Helix files), which matches what the third pass reported as new.
- No files are missing, and the human made no changes to the folder. index.md is corrected to 10. The 2026-09-12 log entry's "7" is left as written (the log is append-only) and is superseded by this entry.
## [2026-09-25] field-note | Pride Q6 Edge 3 (standard) + iLevel — completely dark, no power (open)
Started the first field note and the new `field-notes/` section. Linked it from [[Q6-Edge-3-Stretto]] (the closest model page, since there's no standard Edge 3 page), from [[Q6 Edge Basic Troubleshooting]] and from index.md. The root cause and fix are still TBD.
## [2026-09-25] field-note | Pride Q6 Edge 3 (standard) + iLevel — completely dark, no power (resolved)
Return visit: the function test passed and all functions work. Marked the note resolved in the note, index.md and [[Q6-Edge-3-Stretto]]. Why the old batteries ran down is still unknown, and the list of things to rule out stays in the note.
## [2026-09-25] field-note | Pride Q6 Edge 3 (standard) + iLevel — frayed joystick cable, joystick replaced (open)
The charger completed a full cycle on the new batteries. The joystick cable was frayed, so the joystick is being replaced with the same part (CTL143976), with the old joystick's SD card moved to the new one to keep the customer's config. Reopened the note until the post-swap check. Updated index.md and [[Q6-Edge-3-Stretto]].
## [2026-09-25] field-note | Pride Q6 Edge 3 (standard) + iLevel — joystick forced an update after swap (open)
The new joystick forced an update on first power-up with the old SD card. Added to Fix and Takeaways; details and the post-swap check are still pending.
## [2026-09-25] field-note | Pride Q6 Edge 3 (standard) + iLevel — completely dark, no power; joystick replaced (resolved)
The joystick update finished, the customer's settings carried over via the reused SD card, and all functions work. Closed the note and marked it resolved in index.md and [[Q6-Edge-3-Stretto]]. Why the original batteries ran down is still unknown.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation (open)
Started from the ramp evaluation template (`field-notes/Templates/`). Product defaults to PATHWAY 3G per the house rule. Linked from [[PATHWAY-3G]] and index.md. Site details to come.
## [2026-09-25] ingest | EZ-ACCESS (PMS) — PMS Ramp Site Evaluation Form (Part A)
Copied `PMS_RampEval.pdf` from the out-of-repo drop into `MANUALS/Ramps/`. One page, scanned upside down, undated. New source page under `sources/EZ-ACCESS/General/`. Added the total-rise formula (exterior threshold + steps or porch, whichever is higher, ± grade by line level), the "enter 0" rule and the photo list to [[Ramp-Site-Planning]] and [[Ramp-Slope-and-Length]]; listed under [[PATHWAY-3G]] documents; linked from [[Ramps Handbook]]. Open item: the form refers to a Fig. 4 and a map sheet that aren't in the PDF (probably a Part B).
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation (open, restarted)
Rebuilt the ramp evaluation template around the PMS form's fields and rise formula, and restarted today's note from it. No site data had been entered yet, so nothing was lost.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation, refocused on measurement methods (open)
Per the human, this note records how each measurement is taken (tool, reference points, method, snags) rather than the values. The template is unchanged.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: threshold measurement method (open)
Threshold heights (outside and inside) are measured with a tape; a pen balanced on the threshold makes the reading and the photo easier to read. Added to Checked, Photos and Takeaways.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: threshold reference points (open)
Outside threshold measured from the closest solid surface (porch, top step or ground); inside from the bare interior floor, moving rugs or mats first.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: porch height method (open)
Porch height measured with a tape from the ground to the top of the porch.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: porch height location (open)
Porch height is taken on the edge where the first platform connects, at the lowest point along it; it sets leg height and feeds total rise.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: no-porch height and site snags (open)
No porch: measure ground to threshold. Common snags: bushes to remove, porch handrails to modify. Never build over a septic tank access, main water shut-off valve or plumbing clean-out.
## [2026-09-25] house-standard | Ramps — never build over service access points; steps don't count toward rise
Per the human: (1) House standard: never build a ramp over a septic tank access, main water shut-off valve or plumbing clean-out. Added to [[Ramp-Site-Planning]] and the ramp template. (2) Steps up to a porch don't count toward total rise for PATHWAY; only a SUITCASE ramp over the steps uses them, per the manufacturer's guidelines. Updated the rise formula on [[Ramp-Site-Planning]], [[Ramp-Slope-and-Length]], the template, [[PMS Ramp Site Evaluation Form]] (noted as a PMS clarification of the form) and [[SUITCASE-Ramps]]. Field note updated to match.
## [2026-09-25] clarification | Ramps — "steps or porch, whichever is higher"
Per the human: a home has steps up to a porch, steps straight up to the outer threshold, or no steps. Initial rise is porch height, step rise, or 0 respectively (porch steps still only matter for SUITCASE). Replaced the earlier blanket "steps don't count" wording on [[Ramp-Site-Planning]], [[Ramp-Slope-and-Length]], [[PMS Ramp Site Evaluation Form]], the template and the field note.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: porch depth and width method (open)
Tape; depth from the front door to the porch edge, width edge to edge, both to the inside edges of any handrails or posts.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: porch depth start point, door location (open)
Depth is measured from the threshold; door location is sketched on the map sheet.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: door width and swing method (open)
Tape, door fully open, inside jamb to inside jamb. Record swing for both the main and storm door (often one in, one out).
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: door swing and storm door (open)
An out-swinging door is why the porch or first platform must be 60 x 60 in. Storm doors are removed mainly when they hang lower than the outer threshold.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: handrail width method (open)
Tape, inside edge to inside edge, recording the narrowest point; applies to step handrails or rails beside the porch entry.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: handrail narrowest point (open)
One measurement at the narrowest point, usually the top or bottom of the porch stairs (fanned or decorative stairs).
## [2026-09-25] clarification | Ramps — grade is measured with a laser level
The form's "line level" is a laser level in PMS practice. Updated [[Ramp-Site-Planning]] (also fixed a run-on list item), [[Ramp-Slope-and-Length]], [[PMS Ramp Site Evaluation Form]], the template and the field note.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: grade method (open)
Laser level on the porch corner, aimed at the landing area (usually near parking); tape down from the laser line to the ground.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: grade math (open)
Laser must be level. Grade = tape reading - porch height; more than porch height means the ground drops (add), less means it rises (subtract). Laser height ignored.
## [2026-09-25] template | Ramp evaluation template — laser-level grade and total rise method
Added the laser-level steps and grade math to the template. Per the human, the laser reading (laser line down to the ground at the landing) is the ramp's total rise and must be recorded; added to the template worksheet and the field note.
## [2026-09-25] clarification | Ramps — ramp total rise excludes the threshold
Per the human: ramp total rise = porch height +/- grade (the laser reading). The threshold is handled at the door (e.g. threshold ramp), except when the first platform is built on the porch flush with the threshold, then H is added. Also moved the full laser-level method into [[Ramp-Site-Planning]]. Updated [[Ramp-Slope-and-Length]], [[PMS Ramp Site Evaluation Form]], the template and the field note.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: locate first platform before run (open)
The first platform location is decided before measuring the ramp run. Most jobs: platform off the porch, first run off the platform. Some: porch big enough to run the ramp directly off it.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: choosing the first platform location (open)
Porch at least 60 x 60 in can take the ramp directly. First platform placed for the shortest, most direct ramp to where the customer parks or wants to land.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: marking the first platform (open)
First platform marked with 4 cones in a 60 x 60 in square once its location is set.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: laying out the run (open)
Tape from the first platform cone edge toward the landing, cone the end; add platforms where the run exceeds 30 ft or the ramp turns.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: side clearance (open)
Common width interference: trees, gazebo, fencing. Move if movable, otherwise build around. Handrail width is measured for the same reason.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: landing surface (open)
Concrete good; grass acceptable with a landing pad; rooty ground bad.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: rooty ground and landing pad (open)
Rooty ground avoided; dig out roots if unavoidable. Grass gets an EZ-ACCESS MLP landing pad. Pad size unconfirmed: the human thinks 4 x 4 ft; the layout/install-time sheet says 5 ft ALP.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation: cone photos, landing pad size (open)
Photos must show the cones laid out. Landing pad (MLP) most likely 5 x 5 ft per the human, matching the layout sheet; added to [[PATHWAY-3G]].
## [2026-09-25] house-standard | Ramps — PMS measurement methods adopted
Per the human, the measurement methods from [[2026-09-25 PATHWAY-3G ramp evaluation]] are now house practice. Added a "PMS measurement methods" section to [[Ramp-Site-Planning]] (door and porch, laser-level total rise, tape-and-cone layout, landing surfaces) and rebuilt the template's Checked section around them (method column in the form table, ordered layout checklist, extra photo items). Updated index.md.
## [2026-09-25] field-note | EZ-ACCESS PATHWAY 3G — ramp evaluation measurement methods (resolved)
Closed the note. It is a method write-up, not a specific site record; empty site/value/design placeholders removed. All methods are now in [[Ramp-Site-Planning]] and the template. Open item carried forward: MLP landing pad size (most likely 5 x 5 ft) unconfirmed. Updated index.md and [[PATHWAY-3G]].
## [2026-09-29] clarification | EZ-ACCESS PATHWAY 3G — landing pad (MLP) is 4.5 x 4.5 ft
Per the human. Replaces the unconfirmed "most likely 5 x 5 ft"; the layout sheet's "5' ALP" is a rounded name. Updated [[PATHWAY-3G]], [[Ramp-Site-Planning]], [[Ramp-Install-Time-Estimates]], the template and [[2026-09-25 PATHWAY-3G ramp evaluation]]. Closes the open item.
## [2026-09-29] ingest | EZ-ACCESS TRANSITIONS — Angled Entry Mat Instructions (doc 20516, 2025-07-23)
Copied `TRANSITIONS-AngledEntryMat.pdf` from the out-of-repo drop into `MANUALS/Ramps/`. New source page under `sources/EZ-ACCESS/TRANSITIONS/`. It overrides the 2021 article on the mat: 9 heights (1/2 to 2-1/2 in, 1/4 in steps), 850 lb capacity (not 700), top edge within 1/4 in of the landing and flush, trim height only (never width), notch for the jamb, 2 anchors (screws into wood, drive pins into concrete). Updated [[TRANSITIONS-Threshold-Ramps]], [[Ramp-Site-Planning]] (capacity) and index.md.
## [2026-09-29] clarification | EZ-ACCESS PATHWAY 3G — landing pad size follows the layout sheet (5 ft)
Per the human: keep the landing pad at 5 ft as the EZ Access layout sheet says ("5' ALP"). Reverted the 4.5 x 4.5 ft entry on [[PATHWAY-3G]], [[Ramp-Site-Planning]], [[Ramp-Install-Time-Estimates]], the template and the field note. Also noted on [[TRANSITIONS-Threshold-Ramps]] that PMS has no house rule for mat vs. Angled Entry Ramp.
## [2026-09-29] house-standard | Ramps — ramp completion pictures
Per the human: 10-item PMS photo list for finished installs (door thresholds panoramic, beginning/middle up/middle down/end of ramp, angle meter reading on each run, tie-downs, angle braces, whole-ramp panoramic, signed delivery ticket). Added to [[Ramp-Site-Planning]] section 4 and the template's install verification. Updated index.md.
## [2026-09-29] ingest | Harmar AL-Series Outside Vehicle Lifts — Bulletin 630-00072 AL1235U Universal Drop Hitch Adapter
Copied `[Untitled]_2026092514532919.pdf` (name kept as-is) from the out-of-repo drop into `MANUALS/Harmar/`. 2-page bulletin scanned sideways on one sheet; chart read from a 300 dpi render. New source page under `sources/Harmar/Vehicle Lifts/`. Parts list, 75 ft-lb torque, no-drop/2/3/5 in settings, hitch-to-ground measurement and rounding, and the setting chart for the standard AL107 post vs. AL105/AL105L swing-away. Updated [[AL-Series-Outside-Vehicle-Lifts]] and index.md (Harmar 75 files / 37 source pages, 10 bulletins). Caveat: part numbers and chart row edges read from a small, offset scan.
## [2026-09-29] note | Harmar AL-Series — AL1236 6 in drop adapter and Extra Long adapters for rear spare tires
Per the human. Confirmed against the Hitch Adapter Size Chart in the 2025 Rev D install manual (pp. 10-11): AL1236 6 in drop (20-24 in std, 18-22 in swing-away; HD and V versions), Extra Long series with D1 7.5-13.5 in. Noted the manual's ban on aftermarket expanders/extenders. Added to [[AL-Series-Outside-Vehicle-Lifts]] and [[Bulletin - AL1235U Universal Drop Hitch Adapter]].
## [2026-09-29] ingest | Harmar (PMS) — Vehicle Lift Workflow
`Vehivle_Lift_Workflow.pdf`, 2 scanned pages, undated, PMS-authored. Page 1 is the same phone interview sheet as [[Vehicle Lift Phone Interview Form]]; page 2 is the PMS estimate workflow (AL100 for scooters, AL301XL for power wheelchairs, HD for larger devices; swing-away for rear-access vehicles; hitch adapter on every estimate; hitches from etrailer/etowing). New source page [[Vehicle Lift Workflow]]; added a PMS estimate workflow section to [[AL-Series-Outside-Vehicle-Lifts]]; updated index.md (Harmar 76 files / 38 source pages). Per the human, the Harmar contact phone number and the Etowing.com login are omitted; also removed the phone number from [[Vehicle Lift Phone Interview Form]].
## [2026-09-29] ingest | VA — RFQ: Supply & Installation of ADA-Compliant Bathroom Grab Bars (2026)
Copied `BATHROOM_GRAB-BAR.pdf` into `MANUALS/Misc./`. One page, upside down, issued 2026-05-26, v2.0, deadline 2026-06-09. Not a manual: a VA request for quote. Filed under a new `sources/VA/Grab Bars/` folder (issuing body, no manufacturer page, following the Standards precedent). Requester name, email and phone omitted. No grab bar install source exists in the wiki yet. Updated index.md.
## [2026-09-29] ingest | Batteries — MK Battery and Interstate price sheets
`mk_prices.pdf` (3 pages) copied into `MANUALS/Misc./`. MK MSRP (2024-12-15), MK National Distributor Program (2025-03-01), Interstate Mobility Price Sheet CSCT100 (2024-06). New source page under `sources/Batteries/Price Sheets/` (multi-vendor, so no manufacturer folder) and new concept [[Mobility-Batteries]] cross-referencing MK and Interstate by size group. Interstate dealer column printed without decimals (likely cents). Phone/fax omitted. Linked from [[2026-09-25 Q6-Edge-3 iLevel no power]].
## [2026-09-29] ingest | Scootaround — VA repair workflow (PMS)
`scootaround_workflow.pdf` (4 pages) copied into `MANUALS/Misc./`. Scootaround 8-step VA repair process with PMS handwritten notes, sample quote rules, parts pricing notes (MSRP x 0.75; Golden parts 2x cost; a "70% of MSRP" note that conflicts, flagged), and a sample PMS invoice ($80/hr; travel in 30-min increments). New source page under `sources/Scootaround/VA Repair Program/`. Phone numbers and the sample veteran name/address omitted. Updated index.md.
## [2026-09-29] clarification | Scootaround and Interstate — confirmations
Per the human: PMS makes 75% of MSRP on Scootaround parts (the handwritten "70%" is a slip); travel is billed in 30-min increments. The Interstate sheet's "Dealer" numbers are dealer reference numbers, not prices, and not used by PMS; removed from [[Battery Price Sheets (MK, Interstate)]]. Updated [[Scootaround VA Repair Workflow]].
## [2026-09-29] ingest | PMS — Harmar orders/installs workflow, vehicle lift reference order, ordering and returning parts
Copied `harmar_orders_workflow.pdf`, `vl_workflow.pdf` and `order_return_parts.pdf` into `MANUALS/Misc./`. New source pages: [[Harmar Orders and Installs Workflow]] (under `sources/Harmar/Vehicle Lifts/`; combines the handwritten order/install steps with the 2021 reference order email and VA invoice) and [[Ordering and Returning Parts]] (new `sources/PMS/Parts and Repairs/` folder; parts ordering, Repair Eval Information form, returns). New hub concept [[PMS-Office-Procedures]]. Added ordering/invoicing to [[AL-Series-Outside-Vehicle-Lifts]]; linked from [[Vehicle Lift Workflow]] and [[Scootaround VA Repair Workflow]]. Omitted: customer and staff names, addresses, phone numbers, personal emails and the VA PO number (the reference scans are only partly redacted). Updated index.md.
## [2026-09-29] clarification | Harmar — "Class 3 hitch" invoice line is the vehicle receiver hitch
Per the human: the HITCH CLASS III line is the vehicle's receiver hitch; the separate universal drop line is the Harmar adapter. Zone chart to come from the human. Updated [[Harmar Orders and Installs Workflow]] and [[AL-Series-Outside-Vehicle-Lifts]].
## [2026-09-29] clarification | PMS — zone charge is VA-specific
Per the human: the travel zone charge on invoices applies only to VA jobs. Updated [[Harmar Orders and Installs Workflow]] and [[AL-Series-Outside-Vehicle-Lifts]].
## [2026-09-29] ingest | PMS — Grab bar quote response (VA, 2026) and Ambulatory Aids Training
Copied `grabbarsinstall.pdf` and `ambulatory_aids_training.pdf` into `MANUALS/Misc./`. New source pages under `sources/PMS/Grab Bars/` ([[PMS Grab Bar Quote Response (2026)]]: PMS reply to the VA RFQ; tile and drywall yes, fiberglass no; methods, 12/18/24 in pricing, trip charges; 32 in not priced) and `sources/PMS/Training/` ([[Ambulatory Aids Training]]: 5 parts scanned out of order, fitting points, video links). New concepts [[Grab-Bar-Installation]] and [[Ambulatory-Aids-Fitting]]. Linked from [[RFQ - Bathroom Grab Bars (VA, 2026)]] and [[PMS-Office-Procedures]]. Omitted PMS phone/fax and the staff name and email. Updated index.md.
## [2026-09-29] clarification | PMS grab bars — 32 in price left blank
Per the human: the 32 in grab bar price stays blank. Added a blank row to [[PMS Grab Bar Quote Response (2026)]].
## [2026-09-29] ingest | PMS, VA, Bruno — 8 new files in Misc., sorted by job type
Copied 8 files into `MANUALS/Misc./` (raw copies kept flat; the wiki sorts them). Stairlift evaluations: [[Stairlift Evaluation Measurements and Photos]] (from `Important Stairlift Eval Items.pdf` + `Evaluation Do's & Don'ts.pdf`). Invoicing and delivery: [[Delivery Ticket and Invoice Examples]] (from `delivery_ticket_ex.pdf` + `invoice_ex.pdf`; VA vs. private pay/DSN tickets; private pay parts = cost / 0.65, $85 assessment; VA invoice rules). VA paperwork: [[VA Form 10-0103 HISA Application]] (new `sources/VA/HISA/`); [[Bruno Lead Sign Off Form]] (property owner consent). Pricing: [[Bruno Lifts Price List (PMS SC-0307)]] (dealer = 40% of MSRP, cameras 50%; printout truncated). New `sources/Bruno/General/` folder. The P440 owners manual is a duplicate of the 2021 Handicare revision; noted on [[P440 Owner's Manual (2021, Rev 19-Oct)]], no new page. Reorganized [[PMS-Office-Procedures]] by job type and paperwork. Omitted customer names/addresses, veteran IDs, PA names, PO/invoice numbers, equipment serials, staff names and all phone numbers. Updated index.md.
## [2026-09-29] clarification | PMS invoicing, Bruno lead form — confirmations
Per the human: Harmar serials carry no letter prefix on invoices; the illegible bill-to note stays omitted; the property owner sign-off form is used on Bruno lead jobs. Updated [[Delivery Ticket and Invoice Examples]] and [[Bruno Lead Sign Off Form]].
## [2026-09-29] reorg | MANUALS/Misc. sorted into job-type subfolders (one-time exception)
Per the human, a one-time exception to the "raw sources are never moved" rule: moved the 16 files in the repo copy of `MANUALS/Misc./` into subfolders Stairlift Evaluations, Vehicle Lifts, Grab Bars, Repairs, Invoicing and Delivery, VA Paperwork, Training and Ceiling Lifts. Updated `source:` and raw-path lines on 13 source pages; older log entries keep the old flat paths. The out-of-repo drop (`/home/lu/Work/MANUALS/Misc./`) is untouched. The standing rule is unchanged: no further moves without asking.
## [2026-09-30] ingest | PMS — evaluation forms (Admin/Paperwork/Evals, 7 files)
Copied 7 blank PMS eval forms into `MANUALS/Admin/Paperwork/Evals/` (folder structure kept). New source pages: [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]] and [[PMS Porch Lift (VPL) Evaluation Packet]] (new `sources/PMS/Evaluation Forms/`); [[PMS Ramp Assessment and Approval Forms (Part B)]] (under EZ-ACCESS/General with Part A; from `ramp_eval_B.pdf` + `ramp_appr.pdf`). Part B is the "sheet provided" Part A refers to; Fig. 4 is still missing. Duplicates/newer versions noted on existing pages: `ramp_eval_A.pdf` (clean Part A), `tech_eval.pdf` (repair eval form, adds "repair completed @ eval"), `cl_eval.pdf` (2-page ceiling lift form). New concepts [[Stairlift-Evaluation]] and [[Porch-Lift-Evaluation]], linked from stairlift and VPL model pages and [[PMS-Office-Procedures]]. Ramp Part B and approval added to [[Ramp-Site-Planning]] and the ramp template. PMS phone/fax omitted. Updated index.md.
## [2026-09-30] clarification | PMS ramp Part A — no Fig. 4
Per the human: the form's "See Fig. 4" refers to nothing; there is no Fig. 4 in PMS forms. Closed the open item on [[PMS Ramp Site Evaluation Form]], [[PATHWAY-3G]] and index.md.
## [2026-09-30] ingest | PMS — install forms (Admin/Paperwork/Installs, 3 files)
Copied 3 blank PMS install forms into `MANUALS/Admin/Paperwork/Installs/` (folder structure kept). New source pages: [[PMS Ramp Installation Sign-Off]] (EZ-ACCESS/General; site and install check-offs: platforms level within 1:50, braces over 36 in, corner kits, closure kits on openings 10 in+, loops, photos, mobility test, owner approval; notes the form's "1:12 unless specified on layout" vs. the 1:12 house standard); [[PMS Porch Lift Install Instructions and HISA Final Payment]] (new `sources/PMS/Install Forms/`; Bruno/Harmar porch lift handover incl. 600 lb passenger+chair figure vs. 750 lb model ratings, GFI monthly, PM program; HISA statement of satisfaction and final payment with UFAS/Southern Building Code compliance); [[PMS Grab Bar Waiver of Liability]] (tile/fiberglass damage; notes fiberglass vs. the no-fiberglass rule). Updated [[Ramp-Site-Planning]], the ramp template, [[Porch-Lift-Evaluation]], [[Grab-Bar-Installation]], [[VA Form 10-0103 HISA Application]], [[PMS-Office-Procedures]] and index.md. PMS phone/fax omitted.
## [2026-09-30] clarification | PMS install forms — wording confirmed
Per the human, the wiki's handling of all three flagged points stands: the ramp sign-off's "unless specified on layout" doesn't override the 1:12 house standard; the porch lift form's 600 lb figure is recorded alongside the 750 lb model ratings; the grab bar waiver's fiberglass wording is noted against the no-fiberglass rule.
## [2026-09-30] ingest | PMS — blank delivery paperwork (Admin/Paperwork/Misc. Tickets, 4 files)
Copied `va_ticket.pdf`, `other_ticket.pdf`, `comm_form.pdf` and `rights_resp.pdf` into `MANUALS/Admin/Paperwork/Misc. Tickets/` (folder structure kept). One new source page, [[PMS Delivery Paperwork (Blank Forms)]], under `sources/PMS/Invoicing and Delivery/`: blank VA and private pay/DSN tickets (filled-in guidance stays on [[Delivery Ticket and Invoice Examples]]), the unlabeled communication log, and the client Rights & Responsibilities notice. Phone numbers omitted, including the 24/7 line and the Joint Commission number. Linked from [[PMS-Office-Procedures]]; updated index.md.
## [2026-09-30] ingest | EZ-ACCESS (PMS) — VA ramp return email (2025)
Copied `ramp_returns_va.pdf` into `MANUALS/Ramps/`. Page 3 of 4 of a real 2025-07-02 email thread; job-specific. New source page [[VA Ramp Return Email (2025)]] under EZ-ACCESS/General: install delayed by months of unannounced yard work; PMS offered the VA a full PO charge with the ramp held or reused, or a return with 10% restocking fee plus manufacturer shipping (custom configuration may be non-returnable under the FSS return goods policy). Added "ask about planned yard work" to [[Ramp-Site-Planning]] intake and the VA return options to [[PMS-Office-Procedures]]. Omitted names, emails, the PO number and phone. Updated index.md.
## [2026-09-30] reorg | EZ-ACCESS (PMS) — VA ramp email refocused on the restocking policy
Per the human, the restocking policy is the main takeaway. Renamed the page to [[VA Ramp Returns and Restocking Fee (2025)]] (was "VA Ramp Return Email (2025)") and led it with the policy: custom-configured orders may be non-returnable; 10% restocking fee plus manufacturer shipping; or charge the PO in full and hold/reuse the parts; VA chooses. Added the policy to [[Ramp-Site-Planning]] (new VA returns section), [[PMS-Office-Procedures]] (common rules and Parts) and [[Ordering and Returning Parts]]; updated links and index.md.
## [2026-09-30] note | PMS — "VA Stock"
Per the human: the VA often tells PMS to keep undelivered ramp parts as "VA Stock", which PMS pulls from to build ramps for other veterans. Added to [[VA Ramp Returns and Restocking Fee (2025)]], [[Ramp-Site-Planning]], [[PMS-Office-Procedures]] and [[Ordering and Returning Parts]].
## [2026-09-30] note | PMS — VA Stock log
Per the human: VA Stock is tracked in an Excel log kept locally on a co-worker's PC, with columns Vet's Name, Item Number/Description and Used For. Added to [[VA Ramp Returns and Restocking Fee (2025)]] and [[PMS-Office-Procedures]]. The log itself is not in the wiki.
## [2026-09-30] note | PMS — PMS Stock
Per the human: PMS keeps its own "PMS Stock" of small consumable ramp parts (legs, feet, transitions, hardware) left over from builds or salvaged from repairs. Unlike VA Stock, it has no tracker log. Added to [[VA Ramp Returns and Restocking Fee (2025)]], [[PMS-Office-Procedures]] and [[Ramp-Site-Planning]].
## [2026-09-30] ingest | PMS — Admin/Invoicing and Delivery (2 new files, 3 duplicates)
Copied `ramp_bid_ex.pdf` and `vpl_invoice_ex.pdf` into `MANUALS/Admin/Invoicing and Delivery/`. `delivery_ticket_ex.pdf`, `invoice_ex.pdf` and `order_return_parts.pdf` in that folder are identical (md5) to files already ingested from `Misc./`; not copied again. New source pages: [[VA Ramp Bid Package Example (2026)]] (real VA bid: filled Part B, EZ-ACCESS layout, estimate to Dorn VA with GSA FSS line and FSS discount, $6,979.91) and [[EZ-ACCESS Program Invoice Examples]] (file is named vpl but all three are mod ramp invoices billed to EZ-ACCESS: $75 base eval, mileage, $115 service eval, project ID as PO, last name as Veteran ID). Added PATHWAY 3G "P" ordering codes with 2026 prices to [[PATHWAY-3G]]; bid package and EZ-ACCESS program sections to [[Ramp-Site-Planning]]; links in [[PMS-Office-Procedures]] and [[Delivery Ticket and Invoice Examples]]. Omitted customer/evaluator names, phones, estimate/invoice/project numbers. Updated index.md.
## [2026-09-30] clarification | PMS VA ramp bids — site pictures and labor
Per the human: a VA bid package also includes the site pictures taken during the eval. Labor is included in PMS's markup; a labor line is added only for extra work such as porch modification or debris clean-up. Updated [[VA Ramp Bid Package Example (2026)]], [[Ramp-Site-Planning]] and [[PMS-Office-Procedures]].
## [2026-09-30] correction | EZ-ACCESS — PMS does not take work from EZ-ACCESS
Per the human: EZ-ACCESS is only a manufacturer; PMS takes no work from it. Treat any pay scales or prices as manufacturer suggestions. Renamed the invoice page to [[EZ-ACCESS Invoice Examples (Historical)]] (was "EZ-ACCESS Program Invoice Examples") and reframed it as old invoice-layout examples; removed the "EZ-ACCESS program jobs" section from [[Ramp-Site-Planning]] and the EZ-ACCESS billing line from [[PMS-Office-Procedures]]; added a prices section to [[EZ-ACCESS]] and a note on [[Ramp-Install-Time-Estimates]]; added a standing rule to CLAUDE.md.
## [2026-09-30] ingest | Golden (PG Drives) — Mobility Diagnostic Guide, S-Drive brochure; GP303 raw file repaired
New in `MANUALS/Golden/`: `pgdt_mobility_diagnostics.pdf` (PGDT Mobility Diagnostic Guide, 32 pp, 2017: programmer trip codes for newVSI/VSI/VR2/Pilot+/S-Drive/EGIS/Solo, no-code faults, post-repair tests) and `S-Drive.pdf` (2-page PGDT brochure, 2020). New source pages under `sources/Golden/General/` and new concept [[PG-Drives-Trip-Codes]]; linked from [[TruCharge-Diagnostics]], [[GA541-Avenger]], [[GP162-LiteRider-Envy]], [[Golden]] and index.md (Golden 68 files). Also: the drop folder's `LIT-MB-0016, Rev. A (GP303 Hanress Replacement Instructions).pdf` differed from the repo copy by 19 bytes; the repo copy was damaged (page text did not render). Replaced it with the intact copy (damaged copy kept in the session scratchpad); noted on [[GP303 Ally Main Wiring Harness Replacement]]. Page content unchanged.
## [2026-09-30] field-note | Golden GA541 Avenger — loses power over bumps; S-Drive connectors work loose (resolved)
Per the human: a design flaw lets the S-Drive connectors work loose, so the Avenger cuts out over bumps. Techs should look for strained wires into the connectors, then unplug and reseat them. Known-issue note, not a single job. Linked from [[GA541-Avenger]] (new Field notes section), [[PG-Drives-Trip-Codes]], [[PG Drives S-Drive Brochure]] and the index Field notes table.
## [2026-09-30] clarification | Golden GA541 Avenger — S-Drive wire strain cannot be relieved
Per the human: the strain on the wires into the S-Drive connectors is the design flaw and cannot be relieved. Removed the "relieve the strain" step; the fix is to reseat, and the fault can recur. Updated [[2026-09-30 GA541-Avenger S-Drive loose connectors]].
## [2026-09-30] house-standard | Stairlifts — back-to-knee + hip-to-hip feasibility rule
Per the human: back to knee + hip to hip must total 29 in or more for a stair glide to be feasible; under 29 in is a no bid. The same total determines whether the handrail must be removed. Added to [[Stairlift-Evaluation]] and [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]].
## [2026-09-30] correction | Stairlifts — feasibility rule restated
Per the human: the seated user's back-to-knee + hip-to-hip total must fit within the stair width; the 29 in figure assumes a new-construction standard stairway 34 in wide. Replaces the earlier "29 in or more" wording, which had the direction wrong. Same check decides handrail removal. Updated [[Stairlift-Evaluation]] and [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]].
## [2026-09-30] house-standard | Stairlifts — feasibility limit is stair width minus 5 in; handrail check
Per the human: the user's back-to-knee + hip-to-hip limit is stair width minus 5 in (34 in stair = 29 in). Check with the handrail in place, then with it removed; fits only without it = remove the handrail; fits neither way = no bid. Updated [[Stairlift-Evaluation]] and [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]].
## [2026-09-30] correction | Stairlifts — feasibility rule is back to knee + hip to hip + 6 in (VA rule)
Per the human, correcting the earlier notes: back to knee + hip to hip + 6 in must be no more than the stair width (34 in stair = up to 28 in). It is a general VA approval rule that PMS also applies; the user could often still ride by turning, but the VA will not approve a lift that fails it. Handrail check (with, then without) and no-bid steps unchanged. Replaces the "29 in" / "stair width minus 5 in" wording. Updated [[Stairlift-Evaluation]] and [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]].
## [2026-09-30] clarification | Stairlifts — 34 in stair limit stays at 29 in
Per the human: keep 29 in as the back-to-knee + hip-to-hip limit for a standard 34 in stairway (not the 28 in from 34 - 6). Updated [[Stairlift-Evaluation]] and [[PMS Stair Lift Evaluation Form (Rev Mar 2024)]].
## [2026-09-30] ingest | PMS, MedMizer — 4 new Admin files
Copied `elecricians_preffered.pdf`, `Invoicing and Delivery/ashville_fss.pdf`, `Paperwork/electrical_work_orders.pdf` and `Training/medmizer_hospital_bed_training.pdf` into `MANUALS/Admin/` (structure kept). New pages: [[PMS Electrical Work Orders and Preferred Electricians]] (new `sources/PMS/Electrical/`; VPL 110 V GFI with $450 approval limit, stair glide 120 V outlet 3-5 ft from stairs with $350 limit, PMS pays; companies-only electrician list); [[Asheville FSS Sales Guidelines (2025)]] (Asheville office FSS flow; Supply vs Solutions; monthly x 0.96 reconciliation for Visa and IFF fees); [[MedMizer AC GOV Hospital Bed Training]] (new `sources/MedMizer/Hospital Beds/`), new model [[MedMizer-AC-GOV-Bed]] and manufacturer [[MedMizer]]. Linked from [[Stairlift-Evaluation]] (notes 3-5 ft vs the eval form's 4 ft), [[Porch-Lift-Evaluation]], [[PMS-Office-Procedures]] and index.md. Omitted customer details, staff/VA/electrician names, personal emails and all phone and fax numbers.
## [2026-09-30] clarification | PMS — electrician contacts, sister company, stair lift outlet distance
Per the human: include electrician names and phone numbers (added to [[PMS Electrical Work Orders and Preferred Electricians]]; handwritten entries flagged as read from the scan). Performance Medical Solutions is PMS's sister company (noted on [[Asheville FSS Sales Guidelines (2025)]]). Techs go by the eval form's 4 ft for stair lift outlet distance, not the work order's 3-5 ft (updated [[Stairlift-Evaluation]] and the electrical page).
## [2026-09-30] clarification | PMS electricians — Nancy is Mister Sparky of Augusta
Per the human: the pink "Nancy" note (843-897-2585) belongs to Mister Sparky of Augusta. Moved it into that row of [[PMS Electrical Work Orders and Preferred Electricians]].
## [2026-09-30] lint | 3 wrapped links, 4 missing source: fields, stale Bruno count; Bruno duplicates flagged
- Broken links outside the log: 3, all wikilinks split across a line break (index.md, [[PG-Drives-Trip-Codes]], [[TRANSITIONS Angled Entry Mat Instructions]]). Fixed. Broken links inside log.md are historical (renamed pages, examples) and left as written.
- Orphan pages: none. Field notes: all 3 in the index table.
- Frontmatter: the 4 consolidated Harmar General pages had no `source:`; added the file lists (all paths exist).
- Stale wording (5 ft pad, 4.5 ft, minus 5 in, Fig. 4, EZ-ACCESS program, 70%): none outside the log.
- Raw files not referenced: only the known exclusions (10 Harmar images/CSVs, 2 EZ pay scales) and the P440 duplicate (referenced by an abbreviated name).
- Duplicates: `MANUALS/Bruno/` holds 20 byte-identical top-level copies of its subfolder files (41 files, 21 unique); index count and note corrected. Known duplicates elsewhere unchanged (GP162 PTC, Harmar al-100 dupe1, AL100/300/301 Outside Lifts manuals). No raw files moved or deleted; asked the human about the Bruno copies.
- Counts: Golden 68 files / 67 pages (GP162 PTC duplicate shares a page); Harmar 75 in folder + 1 under Bruno = 76.
## [2026-09-30] reorg | MANUALS/Bruno — loose duplicates removed, ASL-250 moved
Per the human: deleted the 20 loose top-level files in `MANUALS/Bruno/` after confirming each was byte-identical (md5) to a copy in a product-line subfolder, and moved `ASL-250 INSTALLATION_03-12-2019.pdf` into `MANUALS/Bruno/Vehicle Lifts/`. Folder now holds 21 files, all in subfolders. Updated the `source:` on [[ASL-250 Install Manual]] and the Bruno row and note in index.md. All source paths re-checked and resolve. The out-of-repo drop (`/home/lu/Work/MANUALS/Bruno/`) was not touched.
## [2026-10-01] reorg | Out-of-repo MANUALS/Bruno sorted to match
Per the human: moved the 21 flat files in the out-of-repo drop `/home/lu/Work/MANUALS/Bruno/` into the same product-line subfolders as the repo copy (matched by md5). Both folders now have the same layout: Bruno Curved SL (8), Bruno Straight SL (6), Vehicle Lifts (3), VPL (4). No wiki paths affected.
## [2026-10-01] field-note | Bruno VPL — door stuck locked, interlock spring (open)
Per the human: the door interlock is spring-loaded and the spring can partially fail, leaving the door stuck locked. Test: raise the lift to the top, remove the friction-fit plastic post cap, push the lock rod down by hand; remove the four screws holding the call/send station to the post if the rod is hard to reach. Model not specified, so linked from both [[VPL-3100B]] and [[VPL-3200B]] and the index Field notes table. Fix not recorded yet.
## [2026-10-01] field-note | Bruno VPL — door stuck locked, interlock spring (resolved)
Per the human: applies to both VPL-3100B and VPL-3200B. A failed spring shows as the lock rod not springing back or springing back slowly; pushing the rod down unlocks the door. Fix: replace the whole interlock assembly, VPL-31452L (left hand); right-hand part number not recorded. Interlock description confirmed. Updated the note, both model pages and the index.
## [2026-10-01] clarification | PMS stair lift — outlet before install scheduling
Per the human: when an electrician is hired for a stair lift outlet, the outlet must be installed before the stair lift install is scheduled. Added to [[PMS Electrical Work Orders and Preferred Electricians]], [[Stairlift-Evaluation]] and [[PMS-Office-Procedures]].
## [2026-10-01] clarification | PMS stair lift — install completion pictures
Per the human: required pictures for stair lift installs are top, bottom, folding rail, serial number, outlet with the lift plugged in, and curves. Added as section 5 of [[Stairlift-Evaluation]] (folding rail and curves marked "if any"); index row updated.
## [2026-10-01] clarification | PMS stair lift eval — customer email required for DocuSign
Per the human: techs must get the customer's email at the stair lift eval; it's required for the customer's DocuSign e-signature approving the stair lift layout. Added to section 1 of [[Stairlift-Evaluation]]; index row updated.
## [2026-10-01] ingest | PMS Admin — cord policy, warranty sheet, VPL layout example
Three new scans in `MANUALS/Admin/` (copied from the out-of-repo drop, same paths):
- `sl_cord_organizatio.pdf` → [[PMS Stair Lift Charger Cord Policy (2019)]] (sources/PMS/Install Forms). Charger cords must be in a cord cover, Legrand CordMate C110 (Lowe's 65449), kept in stock. Added as section 6 of [[Stairlift-Evaluation]] and to [[PMS-Office-Procedures]].
- `bruno_warranty.pdf` → split in two: page 1 [[Bruno Warranty Summary]] (sources/Bruno/General; limited lifetime on SRE-3000/2010/2010C made after 2 Apr 2018, VPL 1 yr/2 yr major, Valet/Turny, demo, refurb, 90-day parts) and page 2 [[Harmar Warranty Policy (2018)]] (sources/Harmar/General; registration within 10 days, RMA process, labor only if pre-authorized). Updated [[Warranty]] (newer terms override the 2014 card for post-2018 straight rail), [[Harmar-Warranty]], [[Bruno]], [[VPL-3100B]], [[VPL-3200B]].
- `Training/morgan_vpl layout.pdf` → [[PMS Porch Lift Layout Example]] (sources/PMS/Training; titled without the customer's name). Linked from [[Porch-Lift-Evaluation]] and [[PMS-Office-Procedures]].
Index updated (Bruno count 23, PMS 16).
## [2026-10-01] reorg | Repo MANUALS/ now follows the human's MANUALS/ layout
Per the human: the repo's raw layout follows their out-of-repo `/home/lu/Work/MANUALS/`. Matched by md5 and moved 14 files out of `MANUALS/Misc./`: Training, VA Paperwork, Vehicle Lifts and Invoicing and Delivery files into the same subfolders under `MANUALS/Admin/`; `mk_prices.pdf` and `scootaround_workflow.pdf` to `MANUALS/Admin/`; `order_return_parts.pdf` to `MANUALS/Admin/Invoicing and Delivery/`; the two grab bar files to `MANUALS/Grab Bars/`. Updated `source:` paths on 12 source pages and the index (log entries left as written). Also added the human's byte-identical Helix copies under Harmar part-number names (`Harmar-610-00039-01-D-Helix-OM.pdf`, `Harmar-610-00016-01-C-Helix-Measure-Guide-V2.pdf`); Harmar folder now 78 files. Left in place: `MANUALS/Misc./Ceiling Lifts/` (P440 copy not in the human's folder). Not yet ingested: 17 Open Sesame files and `AutoSlide/AutoSwing-Installation-Manual-web.pdf` found only in the human's folder.
## [2026-10-01] ingest | Open Sesame (17 files) + AutoSlide AutoSwing — automatic door operators
Per the human: ingested the Open Sesame folder and the AutoSwing manual, copied from the out-of-repo drop into `MANUALS/Open Sesame/` and `MANUALS/AutoSlide/`.
- New manufacturer [[Open Sesame]]: models [[Open-Sesame-Model-133]] (residential, free swing by hand) and [[Open-Sesame-Model-233]] (public/storm door, slipping clutch acts as closer, M210 board).
- 10 source pages under `sources/Open Sesame/` (Swing Door Operators, Accessories, General); one-page sheets consolidated (2 spec sheets, 3 mount sheets, 4 strike drawings, 2 survey forms).
- New model [[AutoSwing]] + [[AutoSwing Installation Manual]] (`sources/AutoSlide/AutoSwing/`). Flagged: leftover draft text and a door-weight conflict (220.5 vs 198.4 lb; use 198).
- New concept [[Automatic-Door-Operators]]: product choice, comparison, swing-door site survey from the Open Sesame form, activation options.
- **Correction:** the AutoSlide RFID manual in `MANUALS/Open Sesame/` is not a misfile. Open Sesame's proximity tag system uses that reader ([[Open Sesame Proximity Tag Reader Wiring]]). Updated [[AutoSlide]], [[RFID Pet Sensor Operation Instructions]], [[AutoSlide-Drive-System]], index, and the CLAUDE.md example.
- Conflict noted: hold-open 5–50 s (2025 spec sheets) vs 5–35 s (install guide, owner's manual, M210 sheet).
- Battery cross-ref added to [[Mobility-Batteries]] (MK ES1.2-12).
## [2026-10-01] reorg | Old P440 copy deleted, MANUALS/Misc./ removed
Per the human: deleted `MANUALS/Misc./Ceiling Lifts/Owners-Manual_P-440-…_My-Mobility-Store.pdf`, an older revision (Rev 12 Mar 2021) of the manual on [[P440 Owner's Manual (2021, Rev 19-Oct)]]. `MANUALS/Misc./` was empty after that and was removed. Updated that source page and the index. The repo's `MANUALS/` now has the same folders as the human's.
## [2026-10-01] lint | Stale counts fixed; structure clean
- Broken links outside the log: none. Orphan pages: none. Duplicate page names: none. Pages missing frontmatter or `source:`: none. All `source:` paths resolve. Every model, concept, manufacturer and field-note page is linked from the index.
- Raw files not referenced: only the 10 known Harmar exclusions (8 AL425 photos, 2 metadata CSVs).
- Stale counts fixed in index.md: Golden 68 files / 67 pages (table said 68/68; note said 66/65); Harmar note rewritten (said 74 files / 36 pages / 17 excluded; now 78 / 40 / 10, with the two new Helix part-number duplicates listed); Harmar table 39 → 40 source pages; AutoSlide row now says where its 3 files are. [[Golden]] page said 66/65; fixed.
- Helix source pages now note their byte-identical part-number copies.
- "GP160 LiteRider PTC (not yet ingested)" on [[Golden]] and [[GL110-140-LiteRider]] reworded: there's no GP160 manual on disk to ingest.
- Open conflicts still flagged on their pages: Open Sesame hold-open 5–50 s vs 5–35 s; AutoSwing door weight 220.5 vs 198.4 lb.
- Possible gap: ceiling lifts (9 tagged pages) have no evaluation/concept page like [[Stairlift-Evaluation]] or [[Porch-Lift-Evaluation]]. Not created; asked the human.
## [2026-10-01] concept | Ceiling-Lift-Evaluation page
Per the human (from the lint's gap note): new [[Ceiling-Lift-Evaluation]] built from the PMS [[Ceiling Lift Evaluation Form]] (both copies re-read) and Vancare's [[Ceiling Lift Installation Guide]] (pp. 4–7 planning, 81 mounting, 170–173 testing, 203–204 span/cantilever and power). Covers which lift, patient and use, house structure and mounting method, sketching pick-up points, power (outlet within 2 ft of track end), span/cantilever limits for 450/600/625 lb, and final/annual testing (150% load, 100% function, L/200 deflection). Linked from [[C-450-C-625]] (its pre-install section now points here), [[P440]], [[Prism-Castor-2-Post-Lift-Stand]], [[Prism]], [[Vancare]], [[PMS-Office-Procedures]], both source pages and the index. Also removed a stale "AutoSlide/Open Sesame misfile" mention from [[Vancare]].
## [2026-10-01] field-note | Prism P440 — won't go up or down, red light on charge (resolved)
New [[2026-10-01 P440 batteries no lift]]. Lift light RED while plugged in, charger GREEN. Batteries read 12.9 V and 12.3 V; charger output 27.3 V unloaded (good). Root cause: bad batteries, replaced. Per the human: on these ceiling lifts, tape the batteries together so they keep a good connection. Linked from [[P440]] (new Field notes section), [[P440 Owner's Manual (2021, Rev 19-Oct)]] and the index.
## [2026-10-01] field-note | Prism P440 — both batteries replaced; new house standard
Per the human: both batteries were replaced on [[2026-10-01 P440 batteries no lift]]. New **house standard, every device: always replace both batteries.** Added to [[Mobility-Batteries]] (callout and an In the field entry), the field note and [[P440]]. The battery-taping tip also applies to [[C-450-C-625]]; added a Field notes section there.
## [2026-10-01] house-standard | Battery replacement rule widened to the whole set
Per the human: the rule is **always replace every battery in the device** (the whole set), not just both of a pair. Reworded in CLAUDE.md, [[Mobility-Batteries]], [[P440]], [[C-450-C-625]], [[2026-10-01 P440 batteries no lift]] and the index.
## [2026-10-01] field-note | Prism P440 — key takeaways moved to the top (resolved)
Per the human: the most important takeaways from [[2026-10-01 P440 batteries no lift]] are taping the batteries together and replacing both. Added a key-takeaways callout at the top of the note and led the index row with them.
## [2026-10-01] ingest | Scootaround — vendor guide, work order and invoice examples
Per the human: ingested the new `Admin/Scootaround/` folder. Moved the repo's `scootaround_workflow.pdf` into `MANUALS/Admin/Scootaround/` to match (md5 identical) and copied in the 3 new files. New source pages [[Scootaround VA Repair Vendor Guide and Contract Update (2025)]] (8 pp: Apr 2025 contract email, repair-process flyer, vendor FAQ, PO email and sample quote with handwritten notes) and [[Scootaround Work Order and Invoice Examples (2025)]] (work order email; invoice is the same sample as the workflow's p. 4). New concept [[Scootaround-VA-Repairs]]. Updated [[Scootaround VA Repair Workflow]] (path, links), [[PMS-Office-Procedures]], [[Mobility-Batteries]], index.
Flagged for the human: handwritten "Batteries – 30% off MSRP" vs. the 75%-of-MSRP rule; "S/H" note vs. shipping not billable. Source conflicts noted: assessment 3 vs 5–7 business days; tax form E-959E vs E595-E.
## [2026-10-01] clarification | Scootaround — battery rate and S/H note
Per the human: "Batteries – 30% off MSRP" is the Scootaround battery rate (MSRP × 0.70); it applies to Scootaround jobs only. Other parts stay at MSRP × 0.75. The "S/H" note on the sample quote is a reminder to find where shipping costs can be covered further along, e.g. in PMS's markup, since Scootaround won't pay shipping as a line. Updated [[Scootaround-VA-Repairs]] (open questions removed), both Scootaround source pages, [[PMS-Office-Procedures]] and the index.
## [2026-10-05] ingest | PMS FSS contracts binder — contract numbers, Bruno and Harmar VA FSS price lists, MedSurg
Copied `fss_contracts.pdf` (39 pp., scanned, no text layer) into `MANUALS/Admin/` and read every page as an image. Split by content into three source pages:
- [[PMS FSS Contracts Binder]] (sources/PMS/Invoicing and Delivery; pp. 1–9, 25–28, 36–39): PMS's contract map (Supply: 65 II A 36F79721D0084 and 65 II F 36F79721D0058, Harmar products; Solutions: 65 II F 36F79719D0128, Bruno vehicle lifts, **no 65 II A**), GSA SINs (A-76 lifts; F-7 transport lifts; F-8C modular ramps; F-9F grab bars), GSA contractor listings, MedSurg catalog search. Flagged: PMS's MedSurg listing "AL160 – Universal Scooter Lift" at $2,058.29 (AL-160 is Harmar's Profile lift; the price is above Harmar's 2022 FSS prices).
- [[Bruno VA FSS Price List (2021-2026)]] (sources/Bruno/General; pp. 10–24): contract 36F79721D0099, terms, full CRE/SRE/VPL price tables, CRE ordering rules ($350 / 50% cancellation), Bruno Gold Government Warranty, returns, damaged goods.
- [[Harmar VA FSS Price List (2018-2023)]] (sources/Harmar/General; pp. 29–35): contract 36F79718D0537 (mod 04/15/22), terms, FSS warranty (3 yr incl. batteries/paint/covers + 1 yr labor), returns (no fee on end-user death; 70/180-day PO rule), F-7 lift prices with installation, F-8A threshold ramps.
Per the human: manufacturer FSS prices are the **ceiling for what PMS charges the VA** and the reference for VA bids, needed only on request; the contracts have been renewed (5-year terms); Solutions handles nothing under 65 II A. Added the price-ceiling exception to CLAUDE.md (Manufacturer prices section).
New concept [[VA-FSS-Contracts]]. Updated [[Warranty]] (government version: lifetime only while the original owner has it; start no later than 14 months after shipping), [[Harmar-Warranty]] (FSS version), [[PMS-Office-Procedures]], [[Bruno]], [[Harmar]], [[SRE-2010]], [[SRE-3050]], [[CRE-2110]], [[VPL-3100B]], [[VPL-3200B]], [[AL-Series-Outside-Vehicle-Lifts]], [[Hoist-Series-Inside-Vehicle-Lifts]], [[Hybrid-Vehicle-Lifts]], index (Bruno 24, Harmar 41, PMS 17).
## [2026-10-05] clarification | FSS contracts — AL160 vs AL-100, price lists in QuickBooks
Per the human: **the AL160 is a different lift from the AL-100.** Its row showed up in the MedSurg "AL 100 Universal Scooter Lift" sample because the description matched. It isn't a mislabeled AL-100. Removed the "check this listing" callout on [[PMS FSS Contracts Binder]]; the note now just compares it with Harmar's own AL-160-13 line. Also per the human: **all of the FSS price lists are already loaded into PMS's QuickBooks**, so VA estimates use the QuickBooks items, and the wiki copies are for when someone asks for a list. Added to [[VA-FSS-Contracts]], [[PMS FSS Contracts Binder]], [[Bruno VA FSS Price List (2021-2026)]], [[Harmar VA FSS Price List (2018-2023)]], [[PMS-Office-Procedures]], the CLAUDE.md FSS exception and the index.
## [2026-10-05] query | GP162 — charging indication on joystick and charger
Answered what the joystick and charger should show while a GP162 charges. LiNX version: the gauge runs a left-to-right sequence and then shows the charge level, but only if the chair is powered on (OM p. 29). PG VR2 version: the gauge "steps up", and 6 bars means charger connected (SG PDF pp. 13, 16). Charger: green = full on both documented Golden chargers (HP8204B: red+yellow = charging; MRC24-4LX: red only = charging). Fixed [[Golden-Battery-Charging]]: it said the HP8204B shows "red only" while charging, but the HP8204B sheet says red+yellow, and the Charge LED off means the battery isn't connected.
## [2026-10-05] field-note | Golden GP162 — won't hold a charge, charger stays green (open)
New [[2026-10-05 GP162 bad charger stays green]]. New batteries wouldn't hold a charge. The original charger read 28 V / 3 A at the plug (normal), but its light stayed green the whole time. A known-good charger showed charging on the same chair, so the original charger is bad. The batteries were never being charged. Pending: replacement charger, 12-hour first charge, recheck. Key takeaways not given yet. Linked from [[GP162-LiteRider-Envy]] (new Field notes section), [[Golden-Battery-Charging]] (new In the field section), [[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]], [[LiteRider Envy LiNX Owners Manual (GP162)]] and the index. Added a caveat to the "charger with no load can show green" tip on [[2026-10-01 P440 batteries no lift]]: a good no-load voltage doesn't prove the charger charges.
## [2026-10-05] query | Can a 3 ft ramp section come straight off a client's front door (ADA)?
Answered no if the run starts at the door sill: ADA and the PMS [[Ramps Handbook]] both need a level landing at the door, and a 3 ft section covers 3 in of rise at 1:12. Per the human: added the landing size to [[ADA-Ramp-Requirements]]. The Access Board guide doesn't print it, so it comes from the 2010 Standards text (access-board.gov/ada, checked 2026-10-05): landings at least **60 in long** (§405.7.3) and as wide as the widest run (§405.7.2), plus the §405.7 advisory on a level landing at the door. Corrected the page's "length isn't given" note, the PMS-vs-ADA table (landings now match the handbook) and the residential defaults. Also updated the landings bullet on [[Ramp-Site-Planning]].
## [2026-10-05] field-note | Golden GP162 — won't hold a charge, charger stays green (resolved)
Per the human: [[2026-10-05 GP162 bad charger stays green]] is resolved (charger replaced). Key takeaway: **when the service call is "batteries not charging," check the charger.** Added the serial (PCT24J0289) and batteries (2 × MK ES17-12, 18 Ah per the price sheet, matching the PTC service guide's 18 Ah; the LiNX owner's manual lists 22 Ah). Added the takeaway callout, led the index row with it, and added it to [[GP162-LiteRider-Envy]], [[Golden-Battery-Charging]] and [[Mobility-Batteries]] (new In the field entry).
## [2026-10-05] query | Manual gaps vs. contracted equipment
Compared PMS's FSS contracts (and Scootaround's scope) with every file in `MANUALS/` (the repo copy and the human's folder match). Per the human, filed the result as a **Missing manuals** checklist at the top of the index's Ingestion backlog ([[index#Missing manuals]]): Harmar hoist lifts (AL-215 to AL-435T) and truck lifts (AL-815CC to AL-835) have only brochure, spec sheets and parts diagrams; no manual for AL-625HD, Outlander, Backpacker Plus or Commander 450; Bruno ASL-700 Chariot, VSL-4400 Joey and VSL-6000/6900 Curb-Sider have prices only; no manual wheelchair manuals. Can't check yet: Harmar 65 II A (list not on file) and the renewed contracts (a QuickBooks export of FSS items would allow an exact check). Pointers added to [[VA-FSS-Contracts]], [[Bruno]], [[Harmar]], [[Hoist-Series-Inside-Vehicle-Lifts]], [[Hybrid-Vehicle-Lifts]], [[Scootaround-VA-Repairs]]; Bruno and Harmar backlog lines updated. CLAUDE.md: ingest step 6 ticks items off; lint keeps the list current.
## [2026-10-06] ingest | Harmar — 11 Product Insights dealer sheets (2021–2023)
Per the human ("ingest the docs in Harmar dir"): copied the 11 new one-page files from the human's `MANUALS/Harmar/` into the repo and consolidated them on [[Harmar Product Insights (2021-2023)]] (sources/Harmar/General), like the spec-sheet page. Ranked below the manuals.
- Vehicle lifts: lift-type selection matrix, docking devices (DD list by type, checked against the page image), hitch adapter rules, AL015 Profile Micro specs (200 lb min tongue weight). Added to [[AL-Series-Outside-Vehicle-Lifts]], [[Hoist-Series-Inside-Vehicle-Lifts]], [[Hybrid-Vehicle-Lifts]].
- [[HighlanderII]]: Guardian System LED categories, 7,500-cycle service warning / 8,000-cycle shutdown, install prep (temporary cord, NEC permanent wiring within 60–90 days, static strap, safety nut), Q4 2022 changes (non-slip paint).
- [[Pinnacle-SL300]] / [[Pinnacle-SL600]]: nylon worm drive, no lube, 40–60 trips on battery, zero-overrun install (SL600TB1 tall bracket, cut track 6–9 in). New fifth mechanism on [[Overspeed-Safety-Brake]]: Pinnacle pawl brake, >70 ft/min, stops within ½ revolution (counts updated on [[Harmar]] and the index).
- [[Helix]]: Oct 2021 remote; board and remotes replaced together; not interchangeable with Pinnacle remotes.
- Threshold ramps: noted on [[TRANSITIONS-Threshold-Ramps]]; ADA 1:12 matches the house standard.
- Conflicts flagged: AL1235U drop settings (sheet 2/3/4/5 in vs bulletin 2/3/5 in; bulletin wins); Highlander II Service Mode (sheets 15 and 30 min; manuals 30 min up-only, no enclosure Rev G, and 10 min, with enclosure); "Pinnacles are commercially rated" vs SL300 residential-only (manual wins).
- Missing manuals checklist: hoist and threshold-ramp items note the new sheets; neither is closed. Index: Harmar 89 files / 42 source pages / 81 distinct by md5; fourth-pass entry added.
## [2026-10-06] ingest | Harmar — inside lift, truck lift and AL625 manuals; 2026 mobility chart
Per the human: 4 new files in the human's `MANUALS/Harmar/`, copied in. New source pages under sources/Harmar/Vehicle Lifts/:
- [[Inside Lifts Installation and Owner's Manual (2017, Rev F)]] (AL215/225/425/425HD/435/435T; 52 pp; truck-bed base page read from the image because its text layer overlaps).
- [[Truck Lifts Installation and Owner's Manual (AL800 Series, 2017)]] (AL815CC/825/825CC/835; 44 pp).
- [[AL625-AL625HD Installation and Owner's Manual (2012, Rev B)]] (legacy "Freedom Lift Tracker"; wiring page read from the image).
- [[Harmar Mobility Solutions Chart (2026, Rev F)]] (MK-000173 F, 11 May 2026; read from the page images; AL625 not on it, AL001/AL003/AL300RV new to the wiki).
Updated [[Hoist-Series-Inside-Vehicle-Lifts]] (model/capacity table, operation, install, troubleshooting, warranty), [[Hybrid-Vehicle-Lifts]] (AL600/AL690 headroom and depth; legacy AL625 section), [[AL-Series-Outside-Vehicle-Lifts]] (2026 lineup), [[Vehicle-Lift-Power-Wiring]] (new Harmar section: 23 ft SAE J1128 harness, 20 A self-resetting breaker, red last, never cut), [[Harmar-Warranty]] (hoist row: 180 days from manufacture, void without Compatibility Calculator approval), [[Harmar]], [[VA-FSS-Contracts]].
Missing manuals: ticked off hoist lifts, truck lifts and AL-625HD. Still open: Outlander, Backpacker Plus, Commander 450, rubber threshold ramps; Bruno Chariot, Joey, Curb-Sider; manual wheelchairs.
Flagged: AL815CC/AL825 capacity, 2022 FSS list 150/225 lb vs manual and 2026 chart 135/210 lb (manual wins). Index: Harmar 93 files / 46 source pages / 85 distinct by md5.
## [2026-10-08] ingest | EZ-ACCESS — lifetime warranty (2017) and SUITCASE brochure
Per the human: 2 new files in the human's `MANUALS/Ramps/`, copied in. Both scanned, read as images.
- [[EZ-ACCESS Lifetime Warranty (2017)]] (sources/EZ-ACCESS/General; form 0001 Rev 06-22-17): lifetime, parts and components only (not powder coat or applied non-skid tape), parts and labor free, original purchaser only, report defects within 30 days, contact EZ-ACCESS first for an RA or on-site exam; excludes installation, relocation, improper loads, soil movement or regrading, weather. Added to [[EZ-ACCESS]] (replaces "terms for other lines aren't on file") and [[PATHWAY-3G]].
- [[SUITCASE Portable Folding Ramps Brochure]] (sources/EZ-ACCESS/Portable Ramps; form 1027_E): all three styles 800 lb; Singlefold one-piece 2–8 ft, 30 in, extruded surface; **"AS" = splits into two sections with an applied surface** (closes the open question on [[SUITCASE-Ramps]]); full size, folded size, weight and application table. Per-section weights match the totals already on the page from [[EZ Access Parts and Pieces]]. No conflicts.
Index: EZ-ACCESS 12 files in MANUALS/Ramps/, 21 source pages.
## [2026-10-08] reorg | Admin/Memos folder; Bruno warranty sheet moved to MANUALS/Bruno/
Per the human: matched the human's new layout by md5. Moved `Admin/elecricians_preffered.pdf` and `Admin/mk_prices.pdf` to `Admin/Memos/`, and `Admin/bruno_warranty.pdf` to `Bruno/`. Updated `source:` paths on [[Bruno Warranty Summary]], [[Harmar Warranty Policy (2018)]], [[Battery Price Sheets (MK, Interstate)]], [[PMS Electrical Work Orders and Preferred Electricians]], and the index (Bruno 22 files +3 in Admin; Harmar note; PMS folder list). All `source:` paths verified to exist.
## [2026-10-08] ingest | PMS — Aluminum Platforms for VPLs memo (2026)
New file `Admin/Memos/AL_vpl_patform.pdf` (2 scanned pages, read as images) → [[Aluminum Platforms for VPLs (2026)]] (new sources/PMS/Memos/). PMS's 7 Oct 2026 email to the VA: aluminum platforms work as a VPL landing only sometimes; 60 × 60 can be too small (storm door, large chair, adjacent exit); at 30 in+ standard platform rails don't meet code, need 3.5 in vertical pickets (commercial railing); steps on a 5 × 5 platform can leave a roll-off gap. Names and emails omitted. Added to [[Porch-Lift-Evaluation]], [[PATHWAY-3G]], [[PMS-Office-Procedures]], index (PMS 18).
## [2026-10-08] clarification | Harmar Outlander = AL100-DE; Outlander discontinued
Per the human: the Outlander is the **AL100-DE** (DE = dual entry); the Outlander line is no longer on Harmar's site (discontinued); the AL300-FULL is the AL300 equivalent; the AL301XL is also dual entry. Closed the Outlander item on the Missing manuals checklist (current equivalents are covered by the Outside Lifts manuals). Updated [[AL-Series-Outside-Vehicle-Lifts]], [[Harmar VA FSS Price List (2018-2023)]], [[Harmar]], [[VA-FSS-Contracts]] and the index. Still open for Harmar: Backpacker Plus, Commander 450, rubber threshold ramps.
## [2026-10-08] clarification | Harmar Backpacker Plus = AL600
Per the human: the Backpacker (Plus, SSBPPLUS on the 2022 FSS list) is the **AL600**. Closed the Backpacker Plus item on the Missing manuals checklist (covered by the hybrid manuals). Noted on [[Hybrid-Vehicle-Lifts]], [[Harmar VA FSS Price List (2018-2023)]] (the list prices SSBPPLUS $2,515.32 and AL-600-12 $2,498.20 as separate lines), [[Harmar]], [[VA-FSS-Contracts]], index. Still open for Harmar: Commander 450, rubber threshold ramps.
## [2026-10-08] clarification | Harmar Commander 450 discontinued, replaced by AL425HD
Per the human: the Commander 450 (LS450B1002 2-axis, LS450B1003 3-axis on the 2022 FSS list) is discontinued and is now the **AL425HD**, covered by [[Inside Lifts Installation and Owner's Manual (2017, Rev F)]]. Closed the item on the Missing manuals checklist; no Harmar lift on the FSS list lacks a manual now (only the rubber threshold ramps remain). Updated [[Hoist-Series-Inside-Vehicle-Lifts]], [[Harmar VA FSS Price List (2018-2023)]], [[Harmar]], [[VA-FSS-Contracts]] (missing-manuals paragraph rewritten), index.
## [2026-10-08] ingest | Harmar threshold ramps — rubber ramp spec sheet, co-branded TRANSITIONS aluminum sheet
Per the human: 3 new files in the human's `MANUALS/Ramps/`, copied in. PMS mostly uses EZ-ACCESS TRANSITIONS (per the human).
- `Harmar-Choosing the Right Threshold Ramp.pdf` is byte-identical to the copy in `MANUALS/Harmar/` (already on [[Harmar Product Insights (2021-2023)]]); noted there, no new page.
- [[Harmar Rubber Threshold Ramps Spec Sheet (2020)]] (new sources/Harmar/Threshold Ramps/; MKT-000171 Rev A; read from images): modular recycled-rubber sections dovetailed front to back, ½ in steps 1–4 in, 850 lb, 36 in usable, max 4° (7%). Wiki arithmetic: a 4 in ramp ≈ 53 in deep, 130 lb.
- [[TRANSITIONS Aluminum Threshold Ramps Sell Sheet (Harmar, 2025)]] (sources/EZ-ACCESS/TRANSITIONS; MK-000206 A): co-branded Harmar/EZ-ACCESS, so Harmar sells the same TRANSITIONS aluminum line. All 700 lb (supersedes the 2022 Harmar guide's 600 lb). Angled Entry Ramp overall range 1⅜–5⅞ in supports the blog's range; per-size question still open.
- [[TRANSITIONS-Threshold-Ramps]]: new "Harmar's threshold ramps (compared)" section with a functional comparison table (one-piece trimmed mat vs wedge + risers vs dovetailed ½ in sections). Also updated [[Harmar]], [[Harmar Product Insights (2021-2023)]], index.
- Missing manuals: closed the Harmar rubber threshold ramp item. Every FSS-listed Harmar product is now covered. Still open: Bruno Chariot, Joey, Curb-Sider; manual wheelchairs.
## [2026-10-08] ingest | Bruno — Chariot (ASL-700), Joey (VSL-4400), Curb-Sider (VSL-6000/6900) manuals
Per the human: 6 new files loose in the human's `MANUALS/Bruno/`, copied in the same way. 6 source pages under sources/Bruno/Vehicle Lifts/ and 3 new model pages:
- [[ASL-700]] Chariot: wheeled hitch carrier (own tires/lights, VIN, title paperwork), class I/II 1.25 in only, 350 lb, ≥6.5 in bumper clearance, mileage-based maintenance (wheel nuts 75–88 ft-lb, 35 psi); missed maintenance voids the warranty.
- [[VSL-4400]] Joey: inside platform lift, 350 lb; mandatory door safety switch (else battery drain); board reset by passing the remote's magnet over the switch; FWD/RWD chairs need extra chocks.
- [[VSL-6000-6900]] Curb-Sider: boom lift for minivans/SUVs/pickups; 6000 250/400/450 lb, 6900 up to 400 lb with 8 in telescoping head; outer arm reach = half device width + 1 in; stop before the belt's white stitching; J11 jumper on the 6900.
All three carry the Bruno Gold 3-year vehicle-lift warranty. Updated [[Bruno]], [[Warranty]], [[Vehicle-Lift-Power-Wiring]] (new Bruno section), [[Bruno Lifts Price List (PMS SC-0307)]], [[Hoist-Series-Inside-Vehicle-Lifts]] and [[Hybrid-Vehicle-Lifts]] (Bruno equivalents), [[VA-FSS-Contracts]], index (Bruno 28 files / 30 source pages; 3 model rows).
Missing manuals: ticked off Chariot, Joey and Curb-Sider. **Every FSS-contracted lift now has a manual.** Only manual wheelchairs (Scootaround) remain open.
## [2026-10-08] clarification | Golden GC440 model change (2024)
Per the human: the GC440 changed in **2024**; the new model (2024–present) is **heavier and needs an appropriate Harmar lift**. No document on file gives the year or the scooter weights (checked all Companion PDFs; earlier query found only a 2012 "old style/new style" tiller bolt note). Added a callout to [[GC240-340-440-540-Companion]], a warning on the 2021 GC440 + AL100 reference order in [[Harmar Orders and Installs Workflow]], a "scooter year matters" note on [[AL-Series-Outside-Vehicle-Lifts]], and the index row.
## [2026-10-08] note | Golden's VA-marketed lineup
Per the human: Golden markets these to the VA — scooters GC240 Companion Mid-Size, GC340 Full-Size 3-Wheel, GC440 Full-Size 4-Wheel, GC540 HD 3-Wheel, GB147H Buzzaround 4-Wheel, GR595 Eagle, GA541 Avenger; power chairs GP162 LiteRider Envy, GP605 Compass Sport, GP302 Cricket, GP303 Ally. Added a "Golden's VA lineup (2026)" table to [[Golden]] with wiki coverage. Gaps added to the Missing manuals checklist: GR595 Eagle and GP302 Cricket (no documents), GB147H (only a GB147 alignment sheet; noted on [[GB1xx-Buzzaround-XL]]). Also noted in chat (not yet recorded, awaiting an official source): new GC440 = 222 lb with batteries.
## [2026-10-08] ingest | Golden — 14 sell sheets (specs and assembled weights)
Per the human: 14 new sell sheets in the human's `MANUALS/Golden/`, copied in. Consolidated on [[Golden Sell Sheets (2018-2026)]] (sources/Golden/General); spec pages for EX, Cricket, Compass Sport and the four Companions checked against page images.
- **Official GC440 (2024) weight: 222 lb assembled** (SHT-GC440-022624), 48 × 24.5 in, 35.5 in wheelbase; the human confirmed it includes batteries.
- New concept [[Mobility-Device-Weights]]: Golden scooter and chair weights, sizes, wheelbases, and the hitch rule (lift + swing-away + device ≤ hitch max tongue weight), with AL100 arithmetic per scooter.
- New model pages [[GR595-Eagle]] and [[GP302-Cricket]] (sell sheets only). Sell-sheet specs added to [[GC240-340-440-540-Companion]], [[GA541-Avenger]], [[GB118-148-Buzzaround-EX]], [[GB120-Buzzaround-CarryOn]], [[GB1xx-Buzzaround-XL]] (GB150 next-gen XL, GB107/108 Buzzaround LT), [[GP162-LiteRider-Envy]], [[GP6xx-Compass]], [[GP303-Ally]]; [[Golden]] VA table, [[AL-Series-Outside-Vehicle-Lifts]], index (Golden 82 files / 68 pages).
- Flagged: GC340/GC440 range 19 mi in the tables vs 12/14 mi in the text on standard U1s; 2024 GC340/GC440 ship with U1 (wiki's older spec said 50 Ah).
- Missing manuals: GR595 and GP302 now have sell sheets but still no manuals; GB147H unchanged.
## [2026-10-08] query | Minimum Harmar and Bruno lift + swing-away per Golden product, with tongue weight
Per the human: built a pairing table on [[Mobility-Device-Weights]] ("Minimum lift pairings (wiki estimate)"). Harmar: lightest lift by capacity/device type/wheelbase (AL015 65/70 lb, AL160 74, AL050 67, AL500 75, AL580-HDX 92) + AL105L 25 lb or AL105 40 lb. Bruno: ASL-275 installed with swing-away 110–125 lb (128 large platform), ASL-275L for 29–75 lb chairs; ASL-700 Chariot fit by wheelbase/width (tongue load not stated). Marked as an estimate to confirm with Harmar's Compatibility Calculator or Bruno; flagged Avenger/Eagle length, GP162 drive-wheel size, and that hitch-class tongue ratings quoted are typical, not from documents.
## [2026-10-08] clarification | GC440 batteries by generation
Per the human: PMS installs **MK M50-12 SLD M** (50 Ah AGM, 33.2 lb each) in the 2024+ GC440 and **MK MU-1 SLD** (U1, ~23 lb each) in the pre-2024 GC440. Golden's 2013 service guide confirms two 35 Ah U1s on the older Companion; Golden's 2024 sell sheet lists U1 standard, 50 Ah optional. Golden's 222 lb assembled weight is with U1s, so a 2024 GC440 with M50-12s is ~242 lb (wiki arithmetic). Updated [[GC240-340-440-540-Companion]] (battery table), [[Mobility-Batteries]], [[Mobility-Device-Weights]] (new row: AL160 ~316/341/356 lb, Bruno ~367 lb).
## [2026-10-08] clarification | Pre-2024 GC440 battery is MU-1 SLD M
Per the human: the pre-2024 GC440 battery is the MK **MU-1 SLD M** (AGM, 35 Ah, 23.1 lb). Updated [[GC240-340-440-540-Companion]], [[Mobility-Batteries]], [[Mobility-Device-Weights]]. Swap to M50-12 SLD M adds 20.2 lb per pair.
## [2026-10-08] clarification | Curb-Sider couldn't lift a 2024+ GC440 (PMS experience)
Per the human (from memory): a Bruno Curb-Sider couldn't lift a new-model GC440; it was too close to the lift's upper weight limit, and PMS and the VA both missed the upgraded model's weight change. Added warnings to [[VSL-6000-6900]], [[GC240-340-440-540-Companion]] and [[Mobility-Device-Weights]]. Field note not yet created: asked the human for the job date, Curb-Sider model/rating, outcome and key takeaways.
## [2026-07] field-note | Bruno VSL-6000 Curb-Sider — couldn't lift a 2024+ GC440 (resolved)
Logged 2026-10-08 from the human's memory: around July 2026, probably a 250 lb VSL-6000; the 2024+ GC440 was too close to the lift's weight limit; PMS covered replacing the actuator with a heavier-duty model. Key takeaway (per the human): be aware of the GC440 upgrade — PMS and the VA both missed the weight change. New [[2026-07 VSL-6000 GC440 too heavy]] (filename uses month only; day unknown). Linked from [[VSL-6000-6900]] and [[GC240-340-440-540-Companion]] (new Field notes sections) and the index Field notes table.
## [2026-10-08] lint | Counts and stale claims fixed; structure clean
- **Structure:** repo `MANUALS/` matches the human's folder exactly (no missing, extra or changed files). No broken links, bad heading anchors, duplicate page names, missing frontmatter or missing `source:` files. Every model, concept, manufacturer and field-note page is in the index.
- **Raw files without a source page:** 18, all accounted for (10 Harmar images/metadata excluded, 2 EZ pay scales skipped, 6 byte-identical duplicates each named on their page).
- **Orphan fixed:** [[Ramp Evaluation Template]] had no wikilink (only a path in CLAUDE.md); now linked from the index Field notes section.
- **Stale counts fixed in index.md:** Bruno row said 28 Bruno files (27 + the misfiled Harmar camera manual) and the Bruno note was garbled from an earlier edit, rewritten; EZ-ACCESS 22 → 23 source pages; Golden note 68 files / 67 pages → 82 / 81 distinct / 68 pages; Harmar note 46 → 47 pages and the Sources line 36 → 47.
- **Stale claims fixed:** [[Golden]] "Not yet ingested" (68 → 82 files) and model families (added Eagle, Cricket, GB150, GB107/108); [[Harmar]] intro ("three passes, nine model pages" → five passes, seven pages); [[2-Piece Brake Replacement (LiteRider, Buzzaround XL, Buzzaround Lite)]] no longer calls GL110/GL140 un-ingested.
- **Contradiction resolved:** [[Golden-Scooter-Warranty]] said lifetime frame except the Patriot; added the sell sheets' 5-year frame for GC540 and GR595 and the GB120's 2-year batteries.
- **Possible concept pages (not created; asked the human):** hitch adapters (16 pages), docking devices (13, Harmar and Bruno), gate/door interlocks (21: Bruno and Harmar VPLs, Open Sesame).
- Open items unchanged: Missing manuals checklist (Golden VA gaps GR595/GP302 manuals and GB147H; manual wheelchairs).
## [2026-10-12] ingest | Golden — 19 docs from the human's Downloads (service guides, OMs, IPBs)
Per the human ("check Downloads for any Golden docs not already in the wiki and ingest them"; batch pass). Compared `~/Downloads` (root, `Mobility/`, `Mobility (1)/`, both `Discontinued Models/` folders) against `MANUALS/Golden/` by md5 and against every `source:` field. 19 new documents were copied into `MANUALS/Golden/` (6 into `MANUALS/Golden/Discontinued Models/`, the folder name they came with). Skipped as duplicates: every file in `Downloads/Mobility/` (already on disk), the GL110/140 and GP162 service guides (same md5 as files already ingested), the `_REVA_` copies of GB106 and GP160 (same md5), and `GB116+GB146 Buzzaround XL_SG_REVA_100711.pdf` (different md5 but identical text to the copy that was filed).
- **19 source pages:** Buzzaround XL OM, SG and 2025 IPB (GB107/117/147); SGs for GB116/146, GB106, GB118/148, GB120; 2021 Companion IPB (pre-2024); GL109 LiteRider Mini SG; GP160 LiteRider PTC SG; Alante DX/LT SG (GP204/GP215); Alante Sport SG (GP205); Compass Sport SG (GP605, LiNX); Compass HD SG (GP620); Cricket OM and IPB; Eagle OM and IPB; Patriot SG. New source folders `Eagle/` and `Patriot/`.
- **New model pages:** [[GL109-LiteRider-Mini]], [[GP160-LiteRider-PTC]], [[GP205-Alante-Sport]], [[GR575-Patriot]]. GP215 Alante LT folded into [[GP204-Alante-DX]].
- **New concept pages:** [[S-Drive-Beep-Codes]] (GB106, GR575, GR595) and [[Shark-Diagnostics]] (11-code Dynamic Shark table, DX-HHP joystick calibration).
- **Open questions resolved:** **GB147H = GB147 HD** (325 lb, 2-22 Ah, 120 lb); the GB147 **does** separate into front and rear halves (drivetrain release lever); there's now a **Shark code table**; Golden VA lineup gaps closed on Missing manuals (Eagle and Cricket now have OM + IPB, still no service guide).
- **Corrections:** GP605 has had **two controllers** (SHARK in 2010–11 supplements, LiNX in the 2017 SG), so the wiki no longer treats GP605 as SHARK-only. GB106 uses a **PG S-Drive**, not the Dynamics R-Series. Shark and LiNX are both Dynamic Controls products.
- **Flagged:** Eagle weight disagrees between the 2022 OM (300 lb, 239 lb base) and the 2024 sell sheet (302.5 lb, 179 lb base). Buzzaround XL controller rating: 2019 OM says 50 A, 2025 IPB lists DR90-A01. Cricket GP302A (Micon) vs GP302B (LiNX) have different battery-pack part numbers.
- Updated: [[GB1xx-Buzzaround-XL]] (rewritten), [[GB118-148-Buzzaround-EX]], [[GB120-Buzzaround-CarryOn]], [[GC240-340-440-540-Companion]], [[GP6xx-Compass]], [[GR595-Eagle]], [[GP302-Cricket]], [[GL110-140-LiteRider]], [[GL111-141-LiteRider]], [[GP162-LiteRider-Envy]], [[Flash-Beep-Diagnostics]], [[TruCharge-Diagnostics]], [[LiNX-Diagnostics]], [[PG-Drives-Trip-Codes]], [[Golden-Scooter-Warranty]], [[Golden-Wheelchair-Warranty]], [[Golden-Seating-Systems]], [[Mobility-Device-Weights]] (GB117/147/147H rows), [[Golden]], index (Golden 101 files / 87 pages).
## [2026-10-12] note | Missing-manual reminder rule; Golden website fully ingested
Per the human: the 19 docs ingested today were all the manuals on Golden's website (Downloads copies deleted; `MANUALS/` now holds the only copies on this machine). New rule: when working on a device with a missing manual, remind the technician to get a copy. Added to CLAUDE.md (Query step 4) and the index's Missing manuals intro.
## [2026-10-12] ingest | Golden lift chairs — AutoDrive Hand Control Resets and Calibrations
Per the human: one new doc in Downloads, `Golden-Hand-Control-Resets-Calibrations-Revised-100621.pdf` (1 page, Oct 2021), copied to `MANUALS/Golden/`. It's the first lift chair procedure document in the wiki. New source folder `sources/Golden/Lift Chairs/` and source page [[AutoDrive Hand Control Resets and Calibrations]]; new model page [[Golden-Lift-Chairs]] (PR446/448/510/515/535/632/761/766, three hand controls: ZK3100-C5M, ZK3200-HC, ZKAD-5) with power-disruption calibration, position accuracy calibration and factory reset steps. ZKAD-5 can't be field-calibrated (call x502). Updated [[Golden-Dealer-Tips]], [[Golden Tips]], [[Golden]], index (Golden 102 files / 88 pages). **Missing manuals:** added Golden lift chair owner's manuals (none on file); reminded the human per the new rule.
## [2026-10-12] ingest | Joint Commission — DMEPOS accreditation standards (effective 2026-09-01)
Per the human: "PMS adheres to these JCAHO standards" (https://publicstandards.tools.jointcommission.org/6396.DOMESTIC). The site is a web tool, not a PDF. It shows standard titles only, 10 at a time, but the page embeds the full data. Extracted all **139 standards and 487 EPs** verbatim (with EP attributes) to `MANUALS/Standards/Joint Commission/Joint Commission DMEPOS Standards (eff 2026-09-01).md`, plus an HTML snapshot. New source page [[Joint Commission DMEPOS Standards (2026)]] (`sources/Standards/Joint Commission/`) and concept [[Joint-Commission-DMEPOS]], which summarizes the EQ, EC, PC, IC, NPSG, HR, RC and RI requirements that touch PMS's delivery, setup, repair, cleaning, storage, training and records. Added a **house standard** to CLAUDE.md and the index. Notable: EQ.01.03.01 EP 1 requires keeping manufacturer features, warranties and instructions for every item supplied, which backs the missing-manual reminder rule. Oxygen/respiratory EPs flagged as applying only if PMS supplies oxygen.
## [2026-10-12] clarification | PMS doesn't supply oxygen
Per the human. Marked the Joint Commission oxygen and respiratory EPs as not applicable on [[Joint-Commission-DMEPOS]] and in the CLAUDE.md house standard.
## [2026-10-12] lint | Stale controller claims fixed; JC house standard added to touched pages; Golden battery table
- **Structure clean:** no broken links, bad anchors, duplicate names, orphans, frontmatter problems or missing `source:` files; every model and concept page is in the index.
- **Raw files without a source page: 24, all accounted for.** 10 Harmar images/metadata (excluded), 2 EZ pay scales (skipped per the human), 8 byte-identical duplicates (each named on its page), 3 alternate eval-form versions in `Admin/Paperwork/Evals/` (named on the Ramp Part A, Ceiling Lift and Ordering/Returning Parts pages), 1 Joint Commission HTML snapshot (companion to the extracted text).
- **Stale claims fixed** (left over from before today's Golden ingest): GP605 described as SHARK-only on [[Golden-Joystick-Side-Conversion]], [[Brake-Replacement]], [[Compass Sport Brake Replacement (GP605)]], [[Right to Left Side Joystick Conversion]] and the [[GP6xx-Compass]] intro. Now: Shark is Dynamic Controls, and later GP605s use LiNX. Scheme counts ("third", "at least five") corrected to six on [[Flash-Beep-Diagnostics]], [[LiNX-Diagnostics]] and [[LiteRider Envy LiNX Owners Manual (GP162)]]. [[Golden]] no longer counts the A-Series as a fourth maker (its maker isn't stated). The GB147 "does it fold?" open question is marked resolved on [[Field Alignment Procedure (GB147)]]. GP208 seat-code note is now "no manual on file".
- **Corrections:** GB116/146 batteries are 12 Ah **or 18 Ah** (the source page said 12 Ah only). GB120 large pack: 15 Ah in the manuals vs 12.5 Ah on the sell sheet, now flagged on [[GB120-Buzzaround-CarryOn]].
- **House standard coverage:** CLAUDE.md requires house standards on every page they touch. Added a short Joint Commission section to [[PMS-Office-Procedures]], [[Scootaround-VA-Repairs]], [[Stairlift-Evaluation]], [[Porch-Lift-Evaluation]], [[Ramp-Site-Planning]], [[Ceiling-Lift-Evaluation]] and [[Mobility-Batteries]].
- **Synthesis added:** "Golden batteries by model" table on [[Mobility-Batteries]] (sizes were scattered across ~15 model pages); model-specific charging notes on [[Golden-Battery-Charging]].
- **Raw-folder drift:** the human's `/home/lu/Work/MANUALS` lacks the 22 files added today (20 Golden, 2 Joint Commission); the repo's `MANUALS/` holds the only copy on this machine. Noted on the index Missing manuals intro; offered to copy them over.
- **Still open:** Missing manuals (manual wheelchairs; Golden lift chair owner's manuals); possible concept pages for hitch adapters, docking devices and gate/door interlocks (raised 2026-10-08, no answer yet).
## [2026-10-12] note | Synced the human's MANUALS folder
Per the human: copied the 22 files added today (20 Golden in `Golden/` and `Golden/Discontinued Models/`, 2 Joint Commission in `Standards/Joint Commission/`) from the repo's `MANUALS/` to `/home/lu/Work/MANUALS`, with no overwrites, and verified each byte for byte. The two folders now match, except the 11 web clippings, whose originals live in the vault's `Clippings/` folder. Updated the index Missing manuals intro.
## [2026-10-12] concept | Docking-Devices and Gate-and-Door-Interlocks pages
Per the human (from the 2026-10-08 lint suggestion). Built from existing wiki pages plus the raw manuals: Bruno VSL-6000/6900 operator and install manuals (pickup devices, outer-arm clearance = half width + 1 in), PUL-1100 install manual (2 in clearances, yearly inspection), Bruno VPL-3100B/3200B install and operator manuals (interlock test at install; 2-month electronic vs GAL interlock checks), Harmar Highlander II and VPL400-X manuals ("approved interlocks (EMI) are Harmar and Honeywell", interlock beak, wiring layouts, gate status LEDs) and the Harmar interlock bulletin.
- [[Docking-Devices]]: which lifts need a DD (Harmar hoist and truck lifts, Curb-Sider, Out-Rider) and which use anchors or belts instead; Harmar DD types (DD19/DD21 most common); Bruno C-arm/claw; fitting; operation; "chair tips" troubleshooting; counting the DD in lift capacity; FSS prices; not-the-same-thing list (Bruno underseat hook plates, transit docking, ceiling-lift docking stations).
- [[Gate-and-Door-Interlocks]]: EMI, ESI, GAL and doors-by-others types; Bruno and Harmar install checks; Harmar vs Honeywell interlock (B-C vs B-D jumper, wire colors, not backward compatible, double jog); testing and maintenance; troubleshooting (Bruno door stuck locked, Highlander II red top cap and gate LEDs); other things called "interlocks".
- Linked from the Harmar and Bruno vehicle-lift and VPL model pages, [[Top-Landing-Gate-Installation]], [[Porch-Lift-Evaluation]], [[Mobility-Device-Weights]], both related field notes, the Harmar interlock bulletin and Product Insights source pages, [[Harmar]], [[Bruno]] and the index. A hitch-adapter page is still not created (not requested).
## [2026-10-12] concept | Hitch-Adapters page
Per the human. Built from the AL-Series and Bruno ASL model pages and sources, plus the raw manuals: Harmar Outside Vehicle Lifts Install Manual 2025 Rev D (HV/D1/D2 definitions, rounding, class by receiver size, which adapters can be inverted, class 3 anti-rattle pinch tube, expanders/extenders prohibited), Bruno ASL-275 install manual (6–24 in height table with adapter, position and mast hole; tongue-weight rating minus lift = max device; don't modify or add a receiver), ASL-700 install manual (4-bar settings 1–4 for 8–16 in, 6.5 in bumper clearance, hitch-pin check). Covers the two Harmar rules, measuring, choosing (AL1235U, AL1236/AL1238, Extra Long, short; ASL-275/250/700), installing, tongue weight, the AL1232 cold-weld bulletin, Harmar FSS and Bruno prices, and the estimate/order steps. [[Hitch-Adapters]] linked from the AL-Series and ASL model pages, the AL1235U and AL1232 bulletins, Vehicle Lift Workflow, Product Insights, [[Mobility-Device-Weights]], [[Docking-Devices]], [[Harmar]], [[Bruno]] and the index. Closes the 2026-10-08 lint's concept-page suggestions.
## [2026-10-13] ingest | Bruno SRE-3050/SRE-2010 — Power Folding Rail Logic Board Update (web clipping)
Per the human ("ingest the new Clipping"). New file in the vault's `Clippings/`: a Bruno email to authorized dealers (MailerLite webview, undated; clipped 2026-10-13). Copied to `MANUALS/Clippings/` (original left in place), and saved its two images next to it (notch/PCB photo and schematic), since the online copies may not last. New source page [[SRE-3050 and SRE-2010 Power Folding Rail Logic Board Update]] under `sources/Bruno/Bruno Straight SL/`, doc_type Web Article.
- Content: future SRE-3050 and SRE-2010 **power** folding rails get new board logic and a new down limit switch setup so an open circuit (broken wire, unplugged connector) can't cause accidental carriage movement at mid-park. **PCB-00193 replaces PCB-00157**; identified by a notch around the down limit switch and the PCB-00193 label. Manual folding rails unaffected. Updated schematics coming on Brunopartner.
- From the schematic image: the down limit switch symbol is redrawn (reads as normally open → normally closed; marked as the wiki's reading, not Bruno's wording) and the rail wiring colors are listed.
- None of the Bruno manuals on file mention either board number; the clipping is newer than all of them and doesn't conflict. Noted that it ranks below the manuals as a clipping.
- Updated [[Folding-Rail]] (new "Logic board update" section), [[SRE-3050]], [[SRE-2010]], [[Bruno]], and the index (Bruno row 31 pages; Straight SL sources line).
## [2026-10-14] field-note | Harmar AL-Series outside lifts — stuck lifting a load, J-cam flat spots (open)
Per the human: the J-cam on Harmar vehicle lifts can develop flat spots over time. Symptom: the lift gets stuck lifting a load, with no issue unloaded. Not to be confused with a bad actuator or a battery that can't power the load. A general note, not one job. New page [[2026-10-14 Harmar-AL-Outside-Lift J-cam flat spots]]. No wiki page mentioned the J-cam before. In the raw manuals it appears only in the outside-lift owner's manual (Figure 4-1, p. 13, next to the platform roller) and the AL100/AL301XL drawings (530-00716 cast J-cam, replacing H11010), so the note is filed under [[AL-Series-Outside-Vehicle-Lifts]]. Harmar's troubleshooting covers power only (test current as well as voltage, or use a known-good battery); added that as a manual tip, after the human's takeaways. Linked from the model page (new Field notes section), [[Outside Vehicle Lifts Owner's Manual]], [[Outside Vehicle Lifts Install Manual (2025, Rev D)]], [[Harmar Parts Diagrams]] and the index. Open: fix and part used, which models, and how to tell it from an actuator or battery problem.
## [2026-10-14] field-note | Harmar AL-Series outside lifts — J-cam flat spots, fix and diagnosis (resolved)
Per the human, follow-up to the entry above. **Fix: replace the J-cam.** Seen on **all the models**. Telling it apart: J-cam flat spots stick under load **at the same spot every time**, and the lift works fine until then. A **bad actuator or low power is slow the whole way up**. The flat spot can usually be **felt on the heel of the J-cam**. **Clean the J-cam, but never lube it.** The cleaner wasn't specified. Rewrote [[2026-10-14 Harmar-AL-Outside-Lift J-cam flat spots]] (status resolved, with a symptom comparison table). Corrected the J-cam's location: on the mast just above the platform, not beside the platform roller. Figure 4-1's oil can points at the platform roller, so "never lube it" doesn't conflict with the manual's "oil pivot points" instruction. Updated [[AL-Series-Outside-Vehicle-Lifts]], [[Outside Vehicle Lifts Owner's Manual]], [[Outside Vehicle Lifts Install Manual (2025, Rev D)]] and the index row. The part number used wasn't given; 530-00716 from the drawings stays reference only.
## [2026-10-14] field-note | Harmar AL-Series outside lifts — J-cam part number and cleaning (resolved)
Per the human: **replacement J-cam is 140-00075**. **Clean the J-cam with a dry 3M Scouring Pad (Synthetic Fiber)**, never lube it. 140-00075 isn't in any manual on file; the AL100/AL301XL assembly drawings list the J-cam as 530-00716 (cast). The note records 140-00075 as the part PMS orders and mentions the drawing number. Updated [[2026-10-14 Harmar-AL-Outside-Lift J-cam flat spots]], [[AL-Series-Outside-Vehicle-Lifts]], [[Outside Vehicle Lifts Owner's Manual]], [[Harmar Parts Diagrams]] and the index row. Nothing on the note is still open.
## [2026-10-14] field-note | VPL (make not recorded) — squealing and getting stuck, rotted plywood fascia (open)
Per the human: called out to a VPL "making a squealing noise". On test the noise could be recreated and the lift was getting stuck. The platform was jamming on the deck's fascia, a plywood sheet that was rotting and buckling. The lift was installed in 2020. New page [[2026-10-14 VPL squealing and jamming on rotted fascia]], started open. Not recorded yet: make, model and serial, the job date (assumed today), the fix and the key takeaways. Added the manuals' fascia requirements as manual tips: Bruno VPL-3100B/3200B (smooth, vertical, structurally sound; ASME A18.1 3/8–3/4 in running clearance; 125 lb side load over 4 in square) and Harmar Highlander II (smooth surface for the platform edge, Harmar fascia panels). Linked from [[Porch-Lift-Evaluation]] (new Field notes section, since the make is unknown), [[VPL-3100B Install Manual]], [[VPL-3200B Install Manual]], [[Highlander II Install Manual (no enclosure)]] and the index.
## [2026-10-14] field-note | Bruno VPL-3100B — squealing and getting stuck, delaminating plywood fascia (open, fix planned)
Per the human, follow-up to the entry above. The unit is a **VPL-3100B, sn 20060350524**. Renamed the note to [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]; the earlier log entry keeps the old link name. Key takeaways: the problem is **not make-specific**. The original installer used plywood, which met all the requirements in 2020 but is **delaminating 6 years later** and jamming the platform. **Fix (planned): remove the fascia and rebuild it with treated decking boards.** Status stays open until the rebuild is done. Added the manuals' fascia spec to the note as the rebuild's requirements (smooth, non-perforated, full length and width, 125 lb side load, 3/8–3/4 in running clearance verified by running the platform). Linked from [[VPL-3100B]], [[VPL-3200B]] and [[HighlanderII]] (new Field notes section), since it isn't make-specific. Added a **Fascia (deck installs)** row to the Site limits table on [[Porch-Lift-Evaluation]]. Updated the index row. Job date still assumed to be today.
## [2026-10-15] ingest | Bruno stairlifts — TechMate Stairlift Troubleshooter (dealer portal)
Per the human: bring Bruno's TechMate troubleshooting tool into the wiki, to make Bruno troubleshooting faster and to reuse its approach for other makes. TechMate is on the Bruno dealer portal (brunopartner.com → TECHMATE) and is built on Zingtree decision trees. Opened it in the human's logged-in Chrome (placeholder serial 11111111111, as the page itself suggests), then pulled every tree read-only from Zingtree's tree JSON. Nothing was submitted: the "Contact Bruno", "order a part", "problem resolved" and survey nodes send the session to Bruno and were never clicked. 62 trees in all: an entry tree, 26 stairlift, 35 VPL (one deleted). Raw JSON and readable outlines are in `MANUALS/Bruno/TechMate/`; `scripts/techmate_pull.py` refreshes them.
- New source page [[TechMate Stairlift Troubleshooter]] (`sources/Bruno/General/`, new doc_type Troubleshooting Tool): what's in each tree, how to use it, which buttons send to Bruno, and the conflicts with the manuals.
- New concept pages: [[Stairlift-Troubleshooting]] (symptom-first: triage, beep/code table, no power, single beep, seat safety, rocker, remotes and the CRE IR repeater, 3/4/5 short beeps, noises, seat, charging, slowdown/P0, shorts, power options; Harmar cross-references) and [[Troubleshooting]] (the cross-manufacturer method plus a symptom index for every equipment type; fills the "Troubleshooting" slot the index had flagged).
- Checked against the manuals: the Elan and Elite charger LED tables and the beep lists match. **Conflicts:** TechMate calls d6 over-current, but the SRE-2010 guide's table says **d4** (d6 = speed override on high temperature), so the manual wins. TechMate's CRE overspeed reset (crank until the hole centers) differs from the install manual's two-lever reset, and TechMate disagrees with itself on whether the Elite/CRE brake can be replaced alone. All three are flagged on the pages.
- [[Diagnostic-Codes]]: added the full d/F/C display table with beeps from the SRE-2010 guide. Model pages [[SRE-3050]], [[SRE-3000]], [[SRE-2010]] and [[CRE-2110]] got Troubleshooting sections with model-specific points (SRE-3050 factory key-switch jumper, dampener cap SRE-30477 / DPR-00101, SB81, paddle switch SRV-3050-025; CRE hand DIP switch 3 and IR repeater channels; Elan motor vs Elite brushes). Also updated [[Folding-Rail]], [[Harmar-Stairlift-Beep-Codes]], [[Bruno]] and the index.
- New: TechMate covers an **SRE-5000** (newer Bruno straight stairlift) that has no manual on file. Its beep codes and fold-rail notes are on [[Stairlift-Troubleshooting]]. PMS sells and services it (per the human), so it was added to the index's Missing manuals checklist and to [[Bruno]].
- Left out on purpose: Bruno staff names, customer-incident form fields, UK-only branches.
- Backlog: the 35 VPL trees.
## [2026-10-15] ingest | Bruno VPLs — TechMate VPL Troubleshooter (dealer portal)
Per the human ("now do the VPL trees"). Ingested the 35 VPL trees pulled earlier today (raw outlines in `MANUALS/Bruno/TechMate/VPL/`). TechMate sorts VPLs into five groups by model and serial: short residential DC (VPL-3153B/3175B = [[VPL-3100B]]), tall residential (VPL-3210B/3212B/3214B = [[VPL-3200B]]), short residential AC (VPL-3153/3175), short commercial (VPL-3353B/3375B) and tall commercial (VPL-3310B/3312B/3314B). Older boards in each group are sent straight to Bruno; the serial cutoffs are on the source page. The AC and commercial models have no manual or model page here and are covered only briefly.
- New source page [[TechMate VPL Troubleshooter]] (`sources/Bruno/VPL/`) and concept page [[VPL-Troubleshooting]]. The core is Bruno's series **safety-chain voltage walk** with board test points: VPL-3100B ground 20, 21 → 33 (top cover/E-stop/nut safety) → 29 (upper gate) → 25 (platform gate/lower door), then call, limit, safety pan, LED, JP1 output, relay. VPL-3200B ground 67, 50/52 (emergency lowering, pit at 51) → 58 → 59 → 61 (mid stop; 2-stop units need a yellow 59–61 jumper) → 63. Also: the AC board's E1–E18 light ladder, gate/door closed/locked/enable switch wire colors, calls (key switch, rocker colors, run bug to split platform control cable from travelling cable), click/hum/squeal (White Rodgers solenoid, relay ECR-24111, ½ in drive-nut gap → replace nuts and take out of service), noise (bearing block bolts, ½ in deflection test, pad adjustment, brass shavings = lift nuts), charging, runs on its own (JP harness isolation), blown fuse (order of re-plugging; never jump JP3 pin 4–6).
- Checked against the VPL install/operator manuals: no conflicts (their troubleshooting tables are short; both say dielectric grease on connectors). Noted two small inconsistencies inside TechMate itself (tall emergency-lowering test points; one call/send node's yes/no swapped).
- Updated [[VPL-3100B]] and [[VPL-3200B]] (new Troubleshooting sections), [[Troubleshooting]], [[Gate-and-Door-Interlocks]], [[Battery-Charger-LED-Diagnostics]], [[Bruno]], [[TechMate Stairlift Troubleshooter]] and the index (Bruno now 33 source pages, TechMate VPL backlog closed). Linked both VPL field notes from the new page.
## [2026-10-15] query | Pride and Prism troubleshooting → symptom-first pages
Per the human ("do the same for the Pride and Prism troubleshooting docs"). Re-read the raw PDFs (no new sources) and built two symptom-first pages in the same format as the Bruno ones:
- [[Power-Chair-Troubleshooting]]: from [[Q6 Edge Basic Troubleshooting]], the Q-Logic and Q-Logic 3 manuals and the Q6 Edge 3 Stretto and J6 operator manuals. Triage, dead system (Pride's charger won't start on batteries near zero, as in the Q6 field note), powers on but won't drive (freewheel levers, charger inhibit, joystick at power-up, the Q-Logic 3 drive-inhibit light and seat lockouts, controller lock, suspension lock), short range, slow and thermal rollback, pulling, clicking, breaker (Q6 Edge 3 Stretto's resets itself after about a minute; J6 has a button), charging. Golden is covered by a controller index pointing at the existing code pages, plus the GP162 and GA541 field notes.
- New data: the **Q-Logic 3 error code table** (pp. 24–25 of the BOI; the wiki only had legacy Q-Logic codes). Added to [[Joystick-Controllers]] too. Flagged that **#35 and #75 mean different things** on legacy Q-Logic and Q-Logic 3.
- [[Ceiling-Lift-Troubleshooting]]: from the [[C-450 C-625 Technical Manual]] "Symptoms and Problems" and LCD pages, and the P440 2021 owner's manual troubleshooting, indicator, emergency and charging sections. Before-you-open checklist, P440 light meanings, won't wake / E-stop must be ON to charge, airline reversed or self-triggering (grommet leaks; never pull the lift by the hand control), pneumatic puff and leak tests, slack- and thick-strap switches, overspeed governor = motor replacement, board plug map, motor jumper test, 25/30A fuses only, charging strips, track alignment, emergency lowering. Includes the human's P440 takeaways (tape the batteries, replace both).
- No conflicts between the documents. Updated [[Troubleshooting]], [[P440]], [[C-450-C-625]], [[Q6-Edge-3-Stretto]], [[J6]], the Pride/Prism source pages' feeds, and the index (two concept rows; the troubleshooting-candidates note now lists what's still uncovered: vehicle lifts, scooters as their own page, door operators).
## [2026-10-15] ingest | Pride — 46 Downloads files: Quantum/Jazzy spec sheets and charts, scooters, Q-Logic family and PG/Dynamic controller docs
Per the human ("ingest and sort the docs in /Downloads"), a batch pass. `~/Downloads` held 49 PDFs, all Pride/Quantum. Three were duplicates and were skipped (a second 4Front 2 sheet and a second Q6 Edge 4 sheet, byte-identical to their twins, and the Q6 Edge 3 Stretto spec sheet already in `MANUALS/Pride/`). The other 46 were **copied** (originals left in Downloads, verified byte for byte) into new product-line subfolders of `MANUALS/Pride/`, keeping their filenames: `Quantum Power Chairs/` (12), `Jazzy Power Chairs/` (2), `Scooters/` (8), `Controllers/Q-Logic/` (9), `Controllers/Q-Logic 3/` (9), `Controllers/Q-Logic NES/` (1), `Controllers/PG and Dynamic/` (4), `General/` (1). The original 10 loose files stay where they were. Not copied to the human's `/home/lu/Work/MANUALS` folder.
- **46 source pages** under `sources/Pride/`: new folders `Q6 Edge/`, `J4/`, `4Front/`, `R-Trak/`, `Jazzy 1450/`, `Scooters/`, `General/`, plus additions to `J6/` and `Controllers/`.
- **16 new model pages:** [[Q6-Edge-3]] (standard; the field-note chair), [[Q6-Edge-4]], [[Q6-Edge-2.0]], [[Q6-Edge-HD]], [[J4]] (J4/J4E/J4EHD), [[4Front-2]] (2 and 2 HD), [[R-Trak]], [[Jazzy-1450]] (Jazzy and Quantum 1450), and scooters [[Revo]], [[Go-Go-LX]], [[Elite-Traveller]], [[Go-Go-Sport]], [[Ultra-X]], [[ET-Series]], [[i-Go]], [[Super-Portable-SC15]]. Jazzy/retail chairs (EVO, Elite, Select, Carbon, etc.) are only on the charts, so they're covered on the lineup page instead.
- **6 new concept pages:** [[Pride-Power-Chair-Lineup]] (every model's batteries, charger and electronics → which code table; HCPCS; warranty), [[Q-Logic-Fault-Codes]] (full legacy 1–245, Q-Logic 3 1–221, QLNES digit blink), [[Pride-Controller-Flash-Codes]] (VR2/GC3/newVSI and Dynamic), [[Q-Logic-Firmware-Updates]], [[Q-Logic-Seat-Configuration]], [[Q-Logic-3-Bluetooth-and-Remote-Programming]] (Econ-W/I, Interactive Assist, mouse/Switch Control, GyroSet Vigo).
- **Updated:** [[Joystick-Controllers]] (now the Q-Logic family hub: which controller is on the chair, legacy system from the tech manual, QLNES, NE/NE+), [[Power-Chair-Troubleshooting]], [[Mobility-Batteries]] (Pride batteries by model, lithium minimum voltages), [[Mobility-Device-Weights]] (Pride section, ≈ totals are wiki arithmetic), [[Ramp-Slope-and-Length]], [[VA-FSS-Contracts]] (Quantum's FSS V797D-70001), [[Tru-Balance-3-Power-Positioning]], [[Troubleshooting]], [[J6]] and its 2015 spec page (newer Rev C 2020 sheet: 13.4 mi range, 250 lb with TRU-Balance 3, NE/NE+ electronics on the 2025 chart), [[Q6-Edge-3-Stretto]] (QLNES or Q-Logic 3; field note moved to [[Q6-Edge-3]]), [[Q-Logic 3 Programming Guide]], [[Pride]], the index (Pride 56/56, models, concepts, sources, backlog) and the field note [[2026-09-25 Q6-Edge-3 iLevel no power]] (Edge 3 spec sheet now on file; NF-22 confirms the DCM0055 size; its joystick's SD card points to Q-Logic 3).
- **Conflicts flagged:** Q-Logic 3 codes **32–36** are numbered differently in the 2025 fault list vs the Q-Logic 3 and QLNES BOIs; the 2025 Quantum chart says the Edge 3 needs Q-Logic 3 for 6.25/7 mph but lists only QLNES for it; chart vs sheet on the Edge 4 casters, 4Front 2 HD turning radius/base weight and Q1450 top speed; Pride's 50/60 A "Dynamic LiNX" uses the 11-code table that matches Golden's Shark, not Golden's 7-code LiNX table; the Dynamic BOI describes OONAPU with the thermal-rollback text; the SC15 sheet's reversing width looks misprinted; the new Q-Logic 3 Programming Guide download is the older **Rev A (2019)**, superseded by the Rev B already on file.
- **Missing manuals:** added a Pride item (owner's manuals for every model that has only a spec sheet, NE/NE+ manual, Q-Logic 3e BOI, TRU-Balance 4 technical troubleshooting guide).

## [2026-10-16] maintenance | Pride raw files moved from Downloads to the human's MANUALS
Per the human ("sort the docs in /Downloads to the appropriate /MANUALS dir"): **moved** the 46 Pride/Quantum PDFs ingested 2026-10-15 from `~/Downloads` into `/home/lu/Work/MANUALS/Pride/`, using the same subfolders as the repo (`Quantum Power Chairs/`, `Jazzy Power Chairs/`, `Scooters/`, `Controllers/{Q-Logic,Q-Logic 3,Q-Logic NES,PG and Dynamic}/`, `General/`). Each was checked byte for byte against the repo copy before and after the move, with no overwrites. The two `Pride/` folders now match exactly. The 3 duplicates skipped on 2026-10-15 are still in Downloads. Remaining drift between the folders: `Bruno/TechMate/` exists only in the repo (noted on the index Missing manuals intro). No wiki content changed.

## [2026-10-16] maintenance | Downloads duplicates deleted; TechMate copied to the human's MANUALS
Per the human: deleted the 3 duplicate PDFs left in `~/Downloads` (4Front 2 and Q6 Edge 4 spec sheet second copies, and the Q6 Edge 3 Stretto spec sheet), after confirming each was byte-identical to a filed copy. Copied `Bruno/TechMate/` (123 files) from the repo's `MANUALS/` to `/home/lu/Work/MANUALS/Bruno/`, no overwrites, verified identical. The two `MANUALS/` folders now match except the repo's `Clippings/`. Updated the index Missing manuals intro.

## [2026-10-16] workflow | VPL installation — PMS install workflow and per-job template
Per the human's walkthrough: new [[VPL-Installation]] (PMS workflow, then Bruno VPL-3100B manual requirements: pad, power, conduit, fascia, clearances, tools, install sequence, tests) and [[VPL Install Template]] in `field-notes/Templates/`. House practice: job approved only after the initial eval, nothing done at the eval visit; lift ordered on approval; all prep (pad, GFI, fascia, permits/inspections where the state requires them) finished before delivery, done by a PMS tech or a sub depending on capabilities; crew of 2; lift goes on a trailer; install order: stand tower, platform + walls (platform gate with the walls), upper gate, shift into place, level, check clearances, anchor, upper limit, wire call/send and upper gate, gate actuator, covers; then test all functions, photos (lift from the landing, wide angle, serial number), instruct the user and get the required signatures. Open item: GFI-before-lift follows from "all prep before delivery" but the 2024 electrician work order example had the lift in first; to confirm. Linked from [[Porch-Lift-Evaluation]], the three VPL model pages and index.md.

## [2026-10-16] clarification | VPL installation — GFI timing
Per the human: the porch lift GFI can be installed before or after the VPL install; before is preferred. It's the one prep item that doesn't have to be done before delivery. Closes the open item from the previous entry. Updated [[VPL-Installation]], [[VPL Install Template]], [[PMS Electrical Work Orders and Preferred Electricians]] and index.md.

## [2026-10-16] clarification | VPL installation — torque wrench and anchors on the truck list
Per the human: the load-out also needs a torque wrench and concrete anchors (not supplied with the lift). Added to [[VPL-Installation]] and [[VPL Install Template]].

## [2026-10-16] field-note | Pride Q6 Edge HD — cuts out, then powers down, on bumps (resolved)
New [[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]]. Q6 Edge HD, no iLevel. Over bumps the chair stopped for a moment, later powered down; display showed an X in a red dot, battery indicator blinking as if charging. Econ-M (Bluetooth) error log: repeated "joystick out of center". Firmware 1.5.35 → 2.0.16 didn't fix it; Pride tech support suggested the joystick-to-power-module connection; a bus cable coiled around the rear lower body panel was the cause, rerouted, fixed. Key takeaway per the human: not make-specific. Linked from [[Q6-Edge-HD]], [[Power-Chair-Troubleshooting]], [[Q-Logic-Fault-Codes]] and index.md. Serial number not recorded; controller (Q-Logic 3) inferred from the Econ app and firmware version.

## [2026-10-16] field-note | Pride Q6 Edge HD — takeaway: check cable connections first (resolved)
Per the human: the controller is Q-Logic 3 (confirmed). Key takeaway: with this symptom, check the cable connections first; the firmware update took over an hour, the cable reroute 10 minutes. Added to [[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]] (callout, Checked, Fix, Takeaways), its index row, [[Power-Chair-Troubleshooting]], [[Q-Logic-Fault-Codes]] and [[Q6-Edge-HD]].

## [2026-10-16] field-note | Pride Q6 Edge HD — serial number added (resolved)
Per the human: sn jc703824141020. Added to [[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]], its index row and [[Q6-Edge-HD]]. Removed the "serial not recorded" gap.

## [2026-10-16] clarification | Power chairs — cutting out over bumps is a wiring issue (Avenger and Q6 Edge HD)
Per the human: the Q6 Edge HD coiled bus cable is the same kind of issue as the Avenger's S-Drive flaw (wiring under strain at the connection; bumps break contact). Rewrote the "cuts out over bumps" item on [[Power-Chair-Troubleshooting]] as one pattern with both cases, check cable connections and routing first; cross-linked the two field notes, [[GA541-Avenger]] and the [[Troubleshooting]] hub.

## [2026-10-16] clarification | Pride Q6 Edge HD — coiled bus cable pulled on the connection
Per the human: the coiled bus cable was pulling on its connection, the same mechanism as the Avenger S-Drive. Stated in [[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]] and [[Power-Chair-Troubleshooting]].

## [2026-10-19] clarification | VPL installation — permits and licensing (SC, GA)
From a PMS email reply to a tech's questions, pasted by the human. A permit should be pulled for every VPL job, in all cases (replaces "permits not required in every state"). SC: no elevator license; a residential builder's license is required to subcontract electrical/HVAC/plumbing, so technically every SC VPL install needs one (PMS has one); with electrical already in place, a specialty license applies to jobs of $5,000 or under. GA: elevator license and elevator permit required. Open: what the permit covers and who pulls it. Updated [[VPL-Installation]], [[VPL Install Template]] and index.md. Staff names left out.

## [2026-10-19] ingest | Pride — 16 Downloads files: dealer troubleshooting guides, parts replacement guides, TRU-Balance 4, lift chairs, chargers, battery training
Per the human ("ingest and sort the docs in /Downloads"), a batch pass. `~/Downloads` held 18 PDFs, all Pride/Quantum. Two were byte-identical to files already on file and were skipped (Q6 Edge basic troubleshooting, lithium battery sheet); they're still in Downloads. The other 16 were copied into the repo's `MANUALS/Pride/` **and** the human's `/home/lu/Work/MANUALS/Pride/` (same subfolders, no overwrites, each checked byte for byte), then removed from Downloads: `Quantum Power Chairs/` (6), `Jazzy Power Chairs/` (3), `Scooters/` (2), new `Seating/` (1), new `Lift Chairs/` (1), `General/` (3).
- **16 source pages** under `sources/Pride/`: `Q6 Edge/` (TTG Rev A 2011 and Rev B 2012, 2017 parts guide, Edge 4 parts guide 2026), `Q6 Edge 3 Stretto/` (parts guide 2023), `J6/` (TTG 2011), new `Jazzy/` (Jazzy 614 TTG and basic sheet, Jazzy 600 ES parts guide), `Scooters/` (Elite Traveller sheet, GENERAL-010 S19 console bulletin), `Seating/` (TRU-Balance 4 parts guide), new `Lift Chairs/` (basic troubleshooting), `General/` (charger indicator codes, 2004 Battery Guide and Electronics Introduction chapters).
- **4 new model pages:** [[Q6-Edge]] (original Edge, NE/NE+/Q-Logic), [[Jazzy-614]], [[Jazzy-600-ES]], [[Pride-Lift-Chairs]] (PMS sells them).
- **2 new concept pages:** [[Pride-Parts-Replacement]] (torque values from four parts guides side by side, repair steps and warnings) and [[Tru-Balance-4-Power-Positioning]] (anterior tilt rules, legrest ≤ STF − 3.5 in, Q-Logic 3 calibration/teach procedures, torque, depth and STF tables).
- **Updated:** [[Power-Chair-Troubleshooting]] (TTG voltage walk, OCV table, charger inhibit jumper tests and programming, NE/NE+ lock and LCD message table, new §6a motor/brake/bus resistance by chair, Dynamic run-plug check, Elite Traveller beeps, low-battery walk, charger output test), [[Battery-Charger-LED-Diagnostics]] (now covers Pride's ten chargers by part number, not just the Bruno VPL charger), [[Mobility-Batteries]] (lead-acid testing section), [[Joystick-Controllers]] (NE/NE+ now covered from the TTGs), [[Pride-Controller-Flash-Codes]] (Dynamic dealer steps, inhibit), [[Tru-Balance-3-Power-Positioning]], [[Q-Logic-Fault-Codes]], [[Troubleshooting]] (new Lift chairs section), [[Pride-Power-Chair-Lineup]], model pages [[Q6-Edge-3-Stretto]], [[Q6-Edge-4]], [[Q6-Edge-3]], [[Q6-Edge-2.0]], [[4Front-2]], [[J6]], [[Elite-Traveller]], [[Golden-Lift-Chairs]], the [[Q6 Edge Basic Troubleshooting]] source page (NE/NE+ no longer uncovered), [[Pride]] and the index (Pride 72/72, models, concepts, sources, Missing manuals).
- **Conflicts and oddities flagged:** brake resistance differs by chair (Q6 Edge about 80 Ω, J6 about 60 Ω, Jazzy 614 about 35 Ω); the Q6 Edge 4 parts guide gives the **terminal fuse** two torques (10–15 N·m and 3.7–4.1 N·m), confirm with Quantum; the Jazzy 614 TTG prints the breaker test as both "under 1 Ω" and "about 1 Ω"; Dynamic code 10 is "unknown" in the TTG and "controller fault" on the basic sheet; the 2004 Battery Guide says replacing both batteries is only "recommended", the house standard (replace every battery) overrides it; the 2017 "Q6 Edge" parts guide is filed to the original Edge, not the 2.0 (title and parts point there, unconfirmed); the S19 scooter in GENERAL-010 isn't identified anywhere on file.
- **Missing manuals:** Pride item updated (Edge 4 now has a parts guide; NE/NE+ partly covered; IPBs added; TB4 TTG still missing). New item: Pride lift chair owner's manuals and technical troubleshooting guide.

## [2026-10-19] maintenance | Downloads duplicates deleted; S19 noted as legacy
Per the human: deleted the 2 duplicate PDFs left in `~/Downloads` (Q6 Edge basic troubleshooting, lithium battery sheet) after re-checking each was byte-identical to the copies in both `MANUALS/` folders. Downloads now holds no PDFs. The human doesn't recognize the S19 scooter from [[S19 Analog Console Part Runout (GENERAL-010)]] and thinks it's probably an outdated legacy model; noted on that page, [[Pride]] and the index, and closed as an open question.

## [2026-10-19] lint | 479 pages; structure clean, counts match, nothing to fix
- **Structure clean:** 0 broken wikilinks (outside log.md's own old example text), 0 line-split links, 0 bad anchors, 0 duplicate page names, 0 orphans, 0 frontmatter problems; every model, concept and manufacturer page has an index row; every `source:` path (each file in multi-file sources) exists on disk.
- **Raw files:** 521 in the repo's `MANUALS/`. Pride 72 raw = 72 source pages; Bruno, Golden, Harmar and Prism counts match the index notes. Files without their own source page are all accounted for: 10 Harmar images/CSV metadata (excluded), 2 clipping images and the Joint Commission HTML snapshot (companions), and 123 TechMate tree files (covered by the two TechMate source pages).
- **Folders in sync:** the repo's `MANUALS/` matches `/home/lu/Work/MANUALS` except `Clippings/` (expected; originals live in the vault's `Clippings/`, which matches `MANUALS/Clippings/`). `~/Downloads` holds no PDFs.
- **Field notes:** all 10 have a status, an index row and a model-page link. One is open: [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]] (fascia rebuild planned, not done; job date assumed).
- **No stale claims found** after the 2026-10-19 Pride ingest ("spec sheet only" remains true for R-Trak, Q6 Edge HD and Go Go LX).
- **Concept-page candidates (not created, for the human):** iLevel (13 pages mention it; the rules sit on the TRU-Balance 3/4 and Edge model pages) and freewheel/manual brake release (16 pages, Golden and Pride).

## [2026-10-19] concept | iLevel and Freewheel-Mode pages
Per the human (from today's lint suggestion). Built from existing wiki pages plus the raw manuals.
- [[iLevel]]: from the iLevel sections of the Q6 Edge 3 Stretto OM, TRU-Balance 3 BOI and Q-Logic 3 BOI, the QLNES BOI, the Q-Logic 3 fault list (#47), the spec sheets and 2025 Quantum chart, and the Stretto, Edge 4 and TRU-Balance 4 parts guides. Speeds by chair (Stretto, Edge 2.0 and Edge HD 3.5 mph; Edge 3 and Edge 4 4.5 mph; Edge HD 10 in HD iLevel, 400 lb), how it engages (boots lock the front caster arms, 1–1.5 in climbing, 20° tilt/recline), "not engaged" → 25% speed (0% during TB4 anterior tilt), Q-Logic 3 and QLNES indicators, use rules, base and seat parts with torque values. Noted that the chart's "elevate" speeds on the 4Front 2, R-Trak and J4E aren't called iLevel, and that the J6 elevating seat halves speed instead. No Quantum iLevel troubleshooting procedure is on file.
- [[Freewheel-Mode]]: from the Golden LiteRider, Eagle, Companion VA, Avenger, GP162 and Cricket owner's manuals, the Buzzaround XL service guide, the Pride J6 and Stretto OMs, and the Red Hawk Phoenix and Eagle HD manuals. Lever direction differs by model (table of 9), rules (level ground only, nobody on it, power off first, push slowly, don't force or stand on levers, not a tie-down point, never raise an elevating seat in freewheel), Golden's no-power slope procedure, service notes, and a table of what each controller shows when a lever is left in freewheel.
- Linked from the index (two concept rows), [[Power-Chair-Troubleshooting]], [[Troubleshooting]], [[Tru-Balance-3-Power-Positioning]], [[Tru-Balance-4-Power-Positioning]], [[Q-Logic-Seat-Configuration]], [[Q-Logic-Fault-Codes]], [[Joystick-Controllers]], [[Pride-Power-Chair-Lineup]], [[Pride-Controller-Flash-Codes]], the Golden code pages ([[Flash-Beep-Diagnostics]], [[S-Drive-Beep-Codes]], [[TruCharge-Diagnostics]], [[PG-Drives-Trip-Codes]], [[Shark-Diagnostics]], [[LiNX-Diagnostics]]), [[Brake-Replacement]], [[Pride]], [[Golden]], the Q6 Edge model pages and [[2026-09-25 Q6-Edge-3 iLevel no power]].

## [2026-10-19] ingest | Pride — PQ-365 dealer technical service library (96 files)
Per the human ("explore the library and pull any info not already in the wiki", logged in to pridemobility365.com). Explored the library in Claude in Chrome: 11 sections (Q-Logic Resource Center, Installation Instructions 316 links, Technical Troubleshooting Guides, Parts Replacement Guides, Basic Troubleshooting, Education, Basic Operating Instructions, TechnoBulletins 178, Product Recall, Warranty, FAQ) plus direct PDFs, about 590 document links. About 50 were already on file. Proposed 97 PDFs (about 165 MB) by relevance; the human approved downloading all 97. Two library links were dead (Elite Traveller Plus TTG, Jazzy 614 caster/spring retrofit). 97 downloaded via Chrome to `~/Downloads`; 96 unique (one alternate link was a byte-identical copy). Filed into the repo's and the human's `MANUALS/Pride/` (new `TechnoBulletins/` folder; others by product line), verified byte for byte, removed from Downloads along with 3 duplicate copies the download created. Two Q-Logic fault lists the human had downloaded themselves (already on file) were left in Downloads. Not pulled, deliberately: legacy 1990s–2000s Jazzy/Jet/Celebrity/Merits sheets, accessory holders, Synergy/TB2 seating, Kids Up, Litestream, TechnoBulletins 001–166, and 4 software installers (.exe/.zip). The FAQ and Recall pages were read as text (no download).
- **47 source pages** (96 files; small related sheets grouped, e.g. 12 lift chair frame sheets on one page, 12 TechnoBulletins on one page). New source folders `Outback/` and `Quantum Legacy/`.
- **7 new model pages:** [[Jazzy-Select-Elite]], [[Victory]], [[Quantum-Outback]], [[Quantum-600-Series]], [[Quantum-610]], [[Quantum-6000Z]], [[Quantum-614]]. **New concept page:** [[Pride-Warranty]] (the existing `Warranty` page is Bruno-only; now cross-linked).
- **Rewritten:** [[Pride-Lift-Chairs]] (from one 2008 sheet to 24 documents: hand control flash codes and lock, motors, frames, gap and timing, KD setup, measuring, battery backup, warranty).
- **Updated:** [[Power-Chair-Troubleshooting]] (brake values for more chairs and scooters, Jazzy 600 ES code swap, GC2/GC3, VSI eight-bar, DL50 numbering, legacy guides, UPG charger blink codes, 18 V under load), [[Pride-Controller-Flash-Codes]], [[Joystick-Controllers]] (NE+ lock differs on the Quantum 614; keypad/dial fixes), [[Q-Logic-Fault-Codes]], [[Freewheel-Mode]] (Pride's 2007 lever table for ~20 Jazzy/Quantum series, Victory, scooter brake), [[iLevel]] (retrofits, switch adjustment), [[Battery-Charger-LED-Diagnostics]] (13 chargers), [[Mobility-Batteries]], [[Pride-Parts-Replacement]] (other chairs and kits table), [[Tru-Balance-3-Power-Positioning]] (**TB3 recall**, kits), [[S-Drive-Beep-Codes]] (Pride scooters), [[TruCharge-Diagnostics]] (Pride voltmeters), [[Brake-Replacement]], [[Troubleshooting]], [[Pride-Power-Chair-Lineup]], [[Warranty]], model pages [[R-Trak]], [[Revo]], [[J4]], [[J6]], [[4Front-2]], [[Q6-Edge]], [[Q6-Edge-2.0]], [[Q6-Edge-3]], [[Q6-Edge-3-Stretto]], [[Q6-Edge-HD]], [[Jazzy-614]], [[Jazzy-600-ES]], [[Elite-Traveller]], [[Pride]] and the index (Pride 168, models, concepts, sources, Missing manuals, backlog). Fixed a slip from the earlier batch: the lift chair Missing-manuals item had absorbed the Pride item's "Source" line.
- **Conflicts and oddities flagged:** **Jazzy 600 ES bulletin numbers Dynamic codes 3/5 as right and 4/6 as left**, opposite to the Jazzy 614 sheets; the TB3 recall sheet gives 10 in lift / 95–175° / lockout at 25° vs the 2019 TB3 BOI's 12 in / 85–175° / 20° (BOI wins); NE+ lock is "both profile keys" on the Q6 Edge/J6 guides and the locking sheet but "Mode switch" on the Quantum 614 guide; brush wear limit ½ in (2004 guide) vs 0.25 in (model guides); Outback motor-nut torque printed 19–22 N·m beside 11.8–16.2 ft·lb; Quantum 600 guide prints "51 N·m (21.7 ft·lb)" once; Edge 2.0 8→6 in caster kit text says "attach the 8 in arms"; tech support hours 8–6 (FAQ) vs 8:30–7 (library page).
- **Missing manuals:** Pride owner's-manual item updated (Outback, Victory, Select Elite added; the PQ-365 library has no owner's manuals or IPBs); lift chair item updated (service docs on file, owner's manuals and bulletin LC-029 still missing).

## [2026-10-20] ingest | Pride — PQ-365 owner's manuals and basic operations documents (54 files)
Per the human ("here's the owner's manuals library. i'm logged in. go ahead and download the ones we need"). Listed the **Owner's Manuals** (67 links) and **Basic Operations Documents** (39 links) tabs at pridemobility365.com/resources in Claude in Chrome; the links serve PDFs from share.quantumrehab.com. Picked 67 that PMS needs and fetched them into a fresh folder. **13 were dropped:** 9 byte-identical to files already on file (battery charger manual, Dynamic/GC3/VR2/VSI BOIs, Jazzy fault codes = `appendix.pdf`, joystick lockout = the controller locking sheet), 2 internal repeats (Quantum 1450 = Jazzy 1450 OM; TB4 BOI listed twice) and 2 superseded revisions (Edge 4 OM Rev A, lithium insert Rev B). **54 new files** went into both `MANUALS/` folders (verified byte for byte, mirrors match; new `Pride/Controllers/NE/`).
- **48 source pages:** owner's manuals for the Edge 4, Edge 2.0/2.0X/3/2.0HD/Q4 2, Q6 series/Edge HD/Ultra, J4/J4 HD, J4E/J4E HD, 4Front series, R-Trak, Quantum/Jazzy 1450, Go Chair, Jazzy 600 ES, Air, Carbon (Innuovo), EVO 614, Elite ES, Elite HD/14, EVO 613, Ultra Light, mid-size scooters, Victory, both travel scooter editions, SC15, i-Go and lift chairs; BOIs for NE, NE+, Q-Logic 2, Q-Logic 3 (Rev G 2026), Q-Logic 3e, VR2 (Quantum copy), TRU-Balance 4, TRU-Balance 3 (Rev G 2025), TB-Flex, TB bariatric tilt and front riggings; the **TRU-Balance 4 technical troubleshooting guide**; consumer safety guides; lithium insert; SC15 voltmeter insert; Curtis, Jazzy Carbon, Dynamic LiNX, Go Go Carbon and SC15 code sheets; hand control reference Rev M; lift chair and VivaLift! inserts.
- **New concept page:** [[Pride-Power-Chair-Care]] (the shared owner's-manual content: charging rules, lithium plug order, routine check schedule, approved disinfectants, storage, battery and wheel change, freewheel direction by model).
- **New model pages:** [[Jazzy-Air]], [[Jazzy-Carbon]], [[Jazzy-EVO-613]], [[Jazzy-Elite]], [[Jazzy-Ultra-Light]], [[Go-Chair]].
- **Updated:** [[Joystick-Controllers]] (NE/NE+ from their own BOIs, Q-Logic 3e, Q-Logic 2), [[Q-Logic-Fault-Codes]], [[Tru-Balance-4-Power-Positioning]] (BOI speed matrix, full TTG troubleshooting table), [[Tru-Balance-3-Power-Positioning]], [[iLevel]], [[Pride-Controller-Flash-Codes]] (LiNX, Jazzy Carbon, Curtis, Jiuniu, Go Go Carbon), [[S-Drive-Beep-Codes]] (Pride scooter 1–9 list), [[Mobility-Batteries]], [[Pride-Warranty]] (VivaLift!, Carbon), [[Freewheel-Mode]], [[Pride-Power-Chair-Lineup]], [[Joint-Commission-DMEPOS]], [[Pride-Lift-Chairs]] (owner's manual: timing reset, 9 V / lithium backup, thermal shutoff, Rev M flash codes), model pages [[Q6-Edge-4]], [[Q6-Edge-3]], [[Q6-Edge-2.0]], [[Q6-Edge-HD]], [[J4]], [[4Front-2]], [[R-Trak]], [[Jazzy-1450]], [[Jazzy-600-ES]], [[Jazzy-614]], [[Quantum-614]], [[Victory]], [[i-Go]], [[Super-Portable-SC15]], [[Go-Go-LX]], [[Go-Go-Sport]], [[Elite-Traveller]], [[Revo]], [[Ultra-X]], and [[Pride]].
- **Resolved:** the NE+ lock disagreement (the NE+ BOI says both profile keys; the Quantum 614 guide's Mode switch is the odd one out). The "PQ-365 has no owner's manuals" note was wrong: they're under Resources, not the technical service section.
- **Flagged:** Dynamic LiNX sheet says "left" for the right-side codes 4 and 6; Jazzy Carbon 2+8 is "controller" on the sheet but "joystick" in the manual; the SC15 owner's manual (Jiuniu 2, 4–7, 9) and the SC15 insert (S-Drive-style 1–6, 8, 9) give different code lists; the 2026 Q-Logic 3 BOI drops #75 though the Edge 4 OM still uses it; the safety guides' "ADA requires 5°" (PMS builds 1:12, 4.8° or less); the Jazzy Carbon manual's inside page says Rev A July 2020 while the file name says Oct 2022.
- **Missing manuals:** Pride owner's-manual item mostly closed (still missing: original Q6 Edge, 2010 Jazzy 614, Select Elite, Outback, ET Series, Carbon 27/27X/HD, IPBs); NE/NE+, Q-Logic 3e and TB4 TTG gaps closed; lift chair item ticked (LC-029 still not on file).
- **Deliberately skipped:** Baja Bandit/Raptor 2/Wrangler 2, 2021 Maxima, Pursuit 2, CX/PX, Revo 2.0 (UK), AU mid-size and Canadian Go-Go duplicates, scooter intro insert, non-medical scooter safety guide, Synergy seat and Stealth cushion sheets.

## [2026-10-20] field-note | Bruno VPL-3100B — squealing and jamming on rotted fascia (resolved)
Per the human: closed [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]. Fix recorded as done (plywood fascia replaced with treated decking boards); the completion date and the running-clearance check weren't given. Index row set to resolved.

## [2026-10-20] maintenance | Downloads duplicates deleted
Per the human: deleted `fault_list-q-logic-3.pdf` and `qlogic_fault_codes.pdf` from `~/Downloads` after re-checking that each was byte-identical (md5) to the copies in both `MANUALS/` folders (`Pride/Controllers/Q-Logic 3/` and `Pride/Controllers/Q-Logic/`).

## [2026-10-20] ingest | Golden — 25 mobility owner's manuals and the Passport bed manual (Golden Dropbox library)
Per the human: they shared Golden's Dropbox owner's-manual library ("Owners Manuals", from Golden Marketing; folders Bed, Lift Recliners, Mobility) and asked to download anything missing. 81 files listed; 7 were already on file (byte-identical); **74 downloaded** into both `MANUALS/Golden/` folders in Golden's folder layout (`Bed/`, `Lift Recliners/`, `Mobility/Power Wheelchairs/`, `Mobility/Scooters/`). The human then asked to ingest "the 25 new mobility manuals and the 1 bed manual" (a batch pass). The other **48 (35 lift chair manuals, 13 Spanish-language mobility manuals) are on disk, not ingested.**
- **26 source pages:** power chairs GP130, GP161, GP164, GP205/206/207, GP208, GP301, GP303, GP304, GP305, GP309, GP605 (2022), GP620 (2017 Shark, 2019 LiNX); scooters GB107/108, GB118/148, GB119/149, GB120/220, GB121, GB121B/124A, Companion DME edition, GC540, GC340R, GL112, GR575, GR596; Passport bed (new `sources/Golden/Beds/`). Image-only spec pages (GB121B/124A, Companion DME, bed) were read as images.
- **New model pages:** [[GP130-CarryOn-Power-Chair]], [[GP161-LiteRider-Envy-Lite]], [[GP164-BuzzAbout]], [[GP208-Alante-Sport]], [[GP301-Stride]], [[GP304-Ally-Pro]], [[GP305-Ally-Sport]], [[GP309-Cricket-LT]], [[GB119-149-Buzzaround-LX]], [[GL112-LiteRider-HD]], [[GR596-Eagle-All-Terrain]], [[Golden-Passport-Bed]]. **New concept page:** [[Ally-Fault-Codes]] (display codes, voice prompts, app).
- **Updated:** [[GB1xx-Buzzaround-XL]] (LT, GB121 Lite, 2022 XL/XLS HD, fuses), [[GB118-148-Buzzaround-EX]], [[GB120-Buzzaround-CarryOn]] (GB220), [[GC240-340-440-540-Companion]] (DME edition, GC540 OM, GC340R, heaviest pieces), [[GR575-Patriot]], [[GR595-Eagle]], [[GL111-141-LiteRider]], [[GP162-LiteRider-Envy]], [[GP205-Alante-Sport]] (now covers GP206/207), [[GP204-Alante-DX]], [[GP6xx-Compass]] (three owner's manuals; GP620 Shark 2017 → LiNX 2019), [[GP303-Ally]], [[GP302-Cricket]], [[Golden-Lift-Chairs]] (manuals on disk), [[Flash-Beep-Diagnostics]], [[LiNX-Diagnostics]], [[TruCharge-Diagnostics]], [[Shark-Diagnostics]], [[S-Drive-Beep-Codes]], [[Freewheel-Mode]] (12 new lever rows, 4 new code rows), [[Golden-Wheelchair-Warranty]], [[Golden-Scooter-Warranty]], [[Mobility-Device-Weights]] (weights and lift pairings for every new device), [[Mobility-Batteries]], [[Power-Chair-Troubleshooting]], [[Golden-Seating-Systems]], [[Mobility Seats]], [[Golden]] and the index (counts, models, concepts, sources, Missing manuals, backlog).
- **Flagged:** GP301 Stride capacity 300 lb (spec) vs 265 lb (safety page and code table); GP304 code-90 text says 265 lb vs the 330 lb spec; GB107/108 OM weights 87/91.5 lb and 3.6/3.1 mph vs sell sheet 85.5/95 lb and 4 mph; GC540 OM says 120 A vs the IPB's Rhino 2 140 A, and its warranty says "GR540"; the 2017 GP620 OM numbers Shark codes 1–10 (3/5 right, 4/6 left, so M1 = right) vs the service guide's 11; every owner's manual calls R-Series code 3 "consult provider" (service guides: high voltage); GP309 remedies for 4/5 say "right"; Companion DME file name says 2025, PDF dated Nov 2023; the bed manual prints "2.4 MHz"; GR596 has 13-month drive train/electronics, the first Golden scooter on file without 2 years; the GP205 service guide sat in "Discontinued Models" but the 2021 OM still covers it.
- **Not done:** no IPB or service guide in this library; the GR596 (377–407 lb) exceeds every outside lift on file, so no lift pairing was suggested.

## [2026-10-20] ingest | Golden — 35 lift chair (lift recliner) manuals from Golden's Dropbox library
Per the human ("yes, ingest the lift chair manuals"), the `MANUALS/Golden/Lift Recliners/` files pulled earlier today. 35 files = **34 documents** (the PR126/PR631 Relax The Back manual is byte-identical under "RelaxBack" and "DreamMaker"). Filed as **23 source pages** in `sources/Golden/Lift Chairs/`, grouping editions and small sets: Universal (2024), MaxiComfort, two MaxiTwilight editions, DayDreamer, standard chairs, PR118/202 (2021 + 2023), PR404, PR445, PR446/448, PR502, PR117/119, value 115/165 + 116/166, Relax The Back (4 docs), Healthy Back PR127, AmeriGlide PR458, firstSTREET (2), PL340, Member's Mark PL830, massage/heat sheet, Nirvana flyer, international (2004 English/French, 2015 French), Spanish (5). The Universal manual's hand-control photos were read as images.
- **Rewritten:** [[Golden-Lift-Chairs]]: model lines (clearance, capacity, control), power and backups, installation, hand-control table, **M-button sequences** (factory reset, hand control disable, function lock, lights out), calibration (manuals + AutoDrive sheet, with the letter-to-button mapping), **symptom-first troubleshooting**, warranty (standard terms + 9 exceptions), capacities, private-label table, massage/heat/audio.
- **Updated:** [[Golden]], [[Golden-Dealer-Tips]], [[Golden Tips]], [[Pride-Lift-Chairs]] (link text), index (Golden counts 163 of 176 / 137 source pages, lift chair row, sources, Missing manuals item ticked, backlog).
- **Flagged:** PR118 2023 warranty says both "2 years" and "1 year" electrical; calibration hold time 3 s (owner's manuals) vs 5 s (AutoDrive sheet); the PL830 Member's Mark manual calls the chair **UltraComfort**, not Golden; 115/165, 116/166, PR117/119 and PL340 are written as "the manufacturer"; dual-motor wide chairs 450 lb (2004) vs 500 lb (2020); the 2015 French manual is for the French market (cm, French model names).
- **Still missing:** any Golden lift chair service guide or parts list. **Pending:** 13 Spanish-language mobility manuals.

## [2026-10-20] ingest | Golden — tech library: 18 IPBs, lift chair service guides and 32 instruction sheets (55 files)
Per the human: shared Golden's Dropbox **tech manuals** folder ("download the ones we need", then "ingest them"). 139 PDFs; 82 already on file byte for byte; skipped the GB116/146 service guide (text identical to the copy on file) and a one-page "Get Tech Certified" flyer. **55 downloaded** into both `MANUALS/Golden/` folders in Golden's layout (`Illustrated Parts Breakdown/Mobility/`, `Service Guides/Lift Recliners/`, `Instructions/Lift Recliners/`). Image-only IPB tables and the service guide's image pages (Smart Tek table, motor comparisons, grease points) were read visually.
- **26 source pages:** 17 IPB pages (GP605A's 2022 and 2023 editions share one), the 2021 [[Lift Chair Service Guide]], one page for the 115/165, PR116 and PR117/119 guides, the [[Adjustable Bed Service Manual (3101, 4101)]], and 6 grouped instruction-sheet pages (sync/calibration, control box and parts, back assembly, footrest and lift options, power/massage/lumbar, quick starts and set-up checklist).
- **New concept page:** [[Golden-Lift-Chair-Service]] (test values, Smart Tek table by chair type, sync after replacing parts, hand controls by model, motors, transformers, control boxes, frames and scissors, replacement tips, lubrication, heat/massage generations, lithium backup care, options, set-up checklist tied to [[Joint-Commission-DMEPOS]]).
- **Updated:** 15 model pages with their IPBs (controllers, batteries, chargers, shared parts), [[GP302-Cricket]], [[Golden-Lift-Chairs]], [[Golden-Passport-Bed]] (3100/4100 beds), [[TruCharge-Diagnostics]], [[LiNX-Diagnostics]], [[Shark-Diagnostics]], [[Power-Chair-Troubleshooting]], [[Golden]], index (231 files / 218 ingested / 163 source pages, concept row, sources, Missing manuals).
- **Findings:** the **GP130 is PG VR2**; the **GP301 Stride comes as GP301A (Micon) and GP301B (LiNX)**; the GP164 uses the GP605L's LiNX power module and the GP162B's joystick; the GB121 IPB confirms GB121 = 3-wheel, GB124 = 4-wheel.
- **Flagged:** GP620 2024 IPB lists only the Shark (2019 OM is LiNX); GP161 nVR2 40 A (OM 50 A); GB107 DR50-A01 (2024 IPB) vs DR90-A01 (2025 Lite/XL IPB); PR446 hand control ZK3100-C5M (service guide) vs ZK3200-HC (OM); calibration hold 3 s (manuals) vs 5 s (2021 sheet).
- **Still missing:** service guides for the Eagle, GR596, Cricket/Cricket LT, Ally family, Stride, GP130; IPBs for GR596, GP309, GL112. Pending: 13 Spanish mobility manuals.

## [2026-10-20] lint | 680 pages; structure clean; 4 stale claims fixed
- **Structure clean:** 0 broken wikilinks (outside log.md), 0 line-split links, 0 bad anchors, 0 duplicate page names, 0 orphans, 0 frontmatter problems; every model, concept and manufacturer page has an index row; every `source:` path exists on disk.
- **Raw files:** 800 in the repo's `MANUALS/`; mirrors match `/home/lu/Work/MANUALS` except `Clippings/` (expected). Files without their own source page are all accounted for: 123 TechMate tree files (two TechMate source pages), 10 Harmar images/CSV exports, 2 clipping images and the Joint Commission HTML snapshot (companions), the duplicate GP162 PTC guide, and other files cited in page bodies. **Backlog: 13 Spanish-language Golden mobility manuals** (not ingested, by choice so far).
- **Field notes:** all 10 resolved, with index rows and model-page links.
- **Stale claims fixed:** [[GP303-Ally]] said its folding frame was unlike any other Golden model (the Ally Pro/Sport, Cricket, Cricket LT and Stride all fold); [[Golden]] and the index still listed the GP130 as an unnamed controller (its IPB says PG VR2); the index's GP301 and GP130 rows now show Micon/LiNX and VR2; [[AutoDrive Hand Control Resets and Calibrations]] now points to its Nov 2021 revision.
- **Open conflicts carried forward** (all flagged on their pages): GP620 Shark vs LiNX; GP161 40 vs 50 A; GB107 DR50 vs DR90; PR446 hand control; GP301 300 vs 265 lb; PR118 warranty; calibration hold 3 vs 5 s.
- **Concept-page candidates (not created, for the human):** circuit breakers and fuses by model (27 pages mention them: locations, ratings, resets); transporting and tie-downs (9 pages).

## [2026-10-20] concept | Circuit-Breakers-and-Fuses page
Per the human (from today's lint suggestion). Built from the 27+ wiki pages and their source pages that mention breakers and fuses: [[Circuit-Breakers-and-Fuses]]. General rules (a trip is a symptom; cool-down waits; exact-rating replacements; **under 1 Ω good, over 3 Ω or open = replace**; repeat blows = short, unplug one at a time; voltage walk), then tables by unit: Golden scooters (Companion 50 A under the seat, GA541 50 A wait 5 min, Buzzaround XL/EX/LX/Lite fuse sets incl. the LX tiller panel, Carry On fuse ships loose), Golden chairs (GP605 50 A and routing upgrade, GP204 40 A, GP161/164 35 A, GP130 fuse ships loose), Pride/Quantum (J6 harness wiring trips the breaker, Stretto self-resets, Q6 Edge 4 yellow-button breaker and ceramic fuse torque conflict, Victory tiller fuse block, i-Go/SC15/Go Chair/Ultra Light, PTO pins 1–2, Q-Logic 69), Bruno stairlifts and VPLs (board fuse, B− in-line fuse, 3 A slo-blo, 60 A double breaker), vehicle lifts (Bruno 30 A ATO fuse vs Harmar 20 A self-resetting breaker), ceiling lifts, Highlander II, Open Sesame, lift chairs and chargers. Linked from the index and the see-also lists of [[Troubleshooting]], [[Power-Chair-Troubleshooting]], [[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]] and [[Vehicle-Lift-Power-Wiring]].

## [2026-10-20] concept | Transport-and-Tie-Downs page
Per the human (second lint suggestion). [[Transport-and-Tie-Downs]], built from the wiki pages and source pages on transport, tie-downs, docking and air travel: (1) occupied transit only on rated chairs with a WTORS (Pride rule; Stretto strap vs docking methods; J6 short towers only; 600 ES loops unoccupied; Golden manuals: never ride in it); (2) empty in a vehicle: tie-down points (GB118/148 kit angled inward; Pride loops; never freewheel levers), Golden handling rules (not by body or dash, not by the wheels, pad and stow), disassembly pieces by model; (3) vehicle lifts, unoccupied only: outside straps/hold-down arm and seat removal, hoist "on the floor, never hanging", truck ¾ on the bed, hybrids' cam straps, capacity and tongue-weight margins; (4) air travel: AGM/gel FAA, lithium not always, GB120 6.5 Ah pack and 160 Wh / 2-pack limit; (5) PMS deliveries: Joint Commission "secure during transport", MedMizer two-tech rule and splitting, VPL on a trailer, P440 hooks up; plus a note that PATHWAY storm tie-downs are a different thing. Linked from the index and the see-also lists of [[Docking-Devices]], [[Mobility-Device-Weights]], [[Pride-Power-Chair-Care]], [[Joint-Commission-DMEPOS]] and the three Harmar vehicle-lift pages.

## [2026-10-20] maintenance | README rewritten for non-technical setup
Per the human: the README now has three human steps (Claude Pro account, Claude app, paste one sentence) and a "Setup steps for Claude" section that Claude follows to install Git, clone, schedule the daily sync, optionally sign in to GitHub (only for devices that add manuals), copy MANUALS and install Obsidian. Obsidian is now optional; it notes the PDFs are not in git and that Claude must be started in the LLM-Wiki folder.

## [2026-10-21] ingest | Bruno — dealer-portal Tech Tips: stairlifts (46 files)
Per the human: searched Brunopartner → Service → **Tech Tips** (all 165 entries), downloaded the relevant ones, then "batch ingest starting with stairlifts". **107 files** pulled into `MANUALS/Bruno/Tech Tips/` (Stairlifts 46, VPL 49, Vehicle Lifts 9, General 3; `_manifest.md` maps portal ids to files). Skipped: Valet Signature Seating (about 50, incl. the TAS T5/T6 service manual), one entry marked "DELETE", and two mislinked entries. **Three VPL links are broken on Bruno's server** (Electric Strike Offerings, Von Duprin 6211, Fuse & Circuit Breaker Listing). Image-only sheets were read visually.
- **33 source pages** ("Tech Tip - …", `doc_type: Tech Tip`) for the 46 stairlift files: duplicate portal entries and identical copies share pages; the five SRE-3000 folding-rail tips and three legacy SRE-1540/1550/2000 tips are grouped. Filed in `Bruno Straight SL/`, `Bruno Curved SL/` and `General/`.
- **New pages:** [[Stairlift-Maintenance]] (yearly checklist from the manuals, grease by model, batteries, remotes, overspeed tests, Joint Commission records), [[Bruno-Serial-Numbers]] (YY MM PP M SSSS, checked against the 2020 VPL-3100B field-note serial), [[CRE-2100]] (Electra-Ride III, legacy).
- **Updated:** [[SRE-2010]], [[SRE-3000]], [[SRE-3050]], [[CRE-2110]], [[Bruno]] (Tech Tips and legacy models sections), [[Diagnostic-Codes]], [[Overspeed-Safety-Brake]] (on-rail reset, SRE-2010C drop test, legacy tests), [[Folding-Rail]], [[Stairlift-Troubleshooting]] (Elan run voltages, motor-lead voltages, IR interference, RF batteries, ride-out, drive adjustment, CRE final limit, old-rail bounce-back), [[Rail-Mounting-Guidance]] (clamps), [[Mobility-Batteries]], [[Brake-Replacement]] (Elan kit SRV-3000-016), [[Stairlift-Evaluation]] (garage = outdoor for an Elan), [[Joint-Commission-DMEPOS]], [[TechMate Stairlift Troubleshooter]], index. CLAUDE.md: new "Dealer-portal tech tips" convention.
- **Findings:** SRE-3000 battery BTR-12008 = MK ES3-12 (3 Ah); Elan needs 23 V up / 21 V down; gear rack SRE-30177 (new) and SRE-30066 (old) can't be mixed; ILS-01409 is the standalone copy of the tech support guide's opposite-hand conversion.
- **Flagged:** gear rack grease (PTFE in the SRE-3050 manual, white lithium in the SRE-3000/CRE-2110 manuals, Magnalube in TechMate, Lubriplate 130-AA in a tech tip; manual wins); charge-test rise 1 VDC (tech tips) vs 2 VDC (TechMate); tech-tip L7/L8 wording vs the manual's table; the footrest-link tip's "SRE-2100" (taken as SRE-2010); none of the tips name the SRE-3050.
- **Missing manuals:** added Bruno **ILS-01446** Maintenance Control Plan (ASME A18.1-2017 units). **Pending:** 61 tech tips (VPL 49, Vehicle Lifts 9, General 3).

## [2026-10-21] ingest | Bruno — dealer-portal Tech Tips: VPL (49 files)
Per the human ("do the VPL batch next"). All 49 files in `MANUALS/Bruno/Tech Tips/VPL/`; image-only sheets (LED table, schematics, certificates, cold-weather list, shims, panels, cart) read visually.
- **25 source pages** in `sources/Bruno/VPL/` ("Tech Tip - …"): grouped the four AC and two DC serial-range guides, the 8 jumper sheets, the three timer notes, three interlock-wiring tips, the two GAL post drawings, the five tall-VPL install notes, the 90 V board's LED sheet with its schematic, and the two certificates.
- **New pages:** [[VPL-Drive-Service]] (screw, nuts, bearings, belts, guide pads, shims, motor, brake, grease, cold weather) and [[VPL-3153-3175]] (AC low-rise VPL, from tips only).
- **Updated:** [[VPL-Troubleshooting]] (PCB-00143 E-lights and E18 flash codes, older units before TechMate's serials, July 2012 control change, jumper-left-in cases, Waupaca and timer checks, drive symptoms, charger reset), [[Gate-and-Door-Interlocks]] (timers, strikes and interlocks, Waupaca kit change, code excerpt, troubleshooting rows), [[VPL-Installation]] (shipping jumpers, cold weather, certificates, tall-VPL rigging), [[VPL-3100B]], [[VPL-3200B]], [[Battery-Charger-LED-Diagnostics]], [[Bruno-Serial-Numbers]] (VPL serial cutoffs), [[TechMate VPL Troubleshooter]], [[Bruno]], index.
- **Findings:** TechMate's supported-serial cutoffs (12070300108–112, 3214B 12110300156) are the same as the tips' July 2012 platform-control and Waupaca-kit change; the AC board is PCB-00143 with a ½ hp 90 VDC motor; tall VPL travel 3210B 123 in / 3212B 147 in / 3214B 171 in; a 2011 field notice covers VPL-3200B platform-gate units 11080300300–11100301707 (jumper plug bypassing the gate interlock).
- **Flagged:** tall VPL section weights (lower section about 550 lb in the training notes vs about 900 lb in the 2011 guide; manual gives only 1210 lb total); the wiki's AC E2/E3 labels refined from TSG-VPL-004; the code-requirements excerpt is cut off in Bruno's own PDF; the portal's titles for tech-tips 192/193 are swapped and 200 points to a Chariot sheet. No conflicts with the manuals or TechMate.
- **Missing manuals:** added the three VPL tips that are broken on Bruno's server. **Pending:** 12 tech tips (Vehicle Lifts 9, General 3).

## [2026-10-21] ingest | Bruno — dealer-portal Tech Tips: vehicle lifts and general (12 files)
Per the human ("do the vehicle lift and general batch"). The last 12 of the 107 downloaded tips; PUL-1100 drawings, the RC-300 manual and the Joey board page read visually.
- **9 source pages:** Vehicle Lifts: [[Tech Tip - ASL-700 Chariot Specification Sheet (2016)]], [[Tech Tip - ASL-700 Chariot Lights and Trailer Wiring]] (2 files), [[Tech Tip - ASL-700 Chariot Certificate Replacement]], [[Tech Tip - PUL-1100 Dimensions]] (3 files), [[Tech Tip - VSL-4000HW Joey Troubleshooting Guide (TSG-4000-001)]], [[Tech Tip - Trunk Lift Motor MDC-12009 Replacement]]. General: [[Tech Tip - Auto Meter RC-300 Battery Tester]], [[Tech Tip - Bruno Return Goods Policy]], [[Tech Tip - Bruno Serial Numbers (2017 Scheme)]].
- **Updated:** [[ASL-700]], [[PUL-1100]], [[VSL-4400]] (older VSL-4000HW section), [[Bruno-Serial-Numbers]] (3-digit product codes; group 01 = vehicle lifts, 03 = accessibility), [[Vehicle-Lift-Power-Wiring]], [[Hitch-Adapters]], [[Warranty]] (Bruno dealer returns and freight damage), [[Mobility-Batteries]] (RC-300), [[Bruno]] (legacy vehicle lifts), index. A staff name in the certificate tip was left out.
- **Flagged:** the 2016 Chariot sheet allows a 2 in receiver with adapter ASL-K-707; the 2025 install manual says 1¼ in only (manual wins).
- **Tech Tips backlog: none.** All 107 downloaded tips (46 stairlift, 49 VPL, 9 vehicle lift, 3 general) are ingested in 67 source pages.

## [2026-10-21] ingest | Bruno — Drawings library (ILS instruction sheets): stairlifts (161 files)
Per the human: searched Brunopartner → **Drawings** ("I found the ILS-01446 here, and I'm sure there's more"), then "batch ingest starting with stairlifts". The library has 4,601 entries; a search for "ILS" returned 1,368, and 1,345 files were downloaded and **classified from their own title pages** (the portal's category tags are unreliable: ILS-01409, an SRE-2010 doc, is tagged as a vehicle lift). **636 kept** in `MANUALS/Bruno/Drawings/` (Stairlifts 161, VPL 134, Vehicle Lifts 277, Docking Devices 60, General 3; `_manifest.md`). About 40 VPL drawings that first landed in the Stairlifts folder were moved to VPL (and one each to Docking Devices and Vehicle Lifts) before ingest. Skipped: 269 Valet sheets, 166 kits for discontinued vehicle lifts only, 188 image-only scans, paint specs, old scooter parts, part drawings, a duplicate of ILS-01409. Image-only sheets in the kept set were read visually where they mattered (ILS-01502); two charger LED sheets and an armrest sheet are noted as image-only.
- **31 source pages** ("ILS - …", `doc_type: Instruction Sheet`), plus single-sheet pages [[ILS-01446 Maintenance Control Plan for CRE-SRE Chair Lifts]], [[ILS-01512 SRE Rail Mounting Guidance (2026)]] and [[ILS-01620 CRE-3110 Technical Specifications]].
- **New model pages:** [[SRE-5000]] (specs, service, PCB kits by serial, continuous-mode folding rail) and [[CRE-3110]].
- **Updated:** [[Stairlift-Maintenance]] (ILS-01446 intervals and logs; grease settled), [[Overspeed-Safety-Brake]] (current trip-key, ruler and magnet tests; 5-year tag and 125% brake test; CRE overspeed certificate), [[Stairlift-Troubleshooting]] (brakes replaceable, Feb 2025 gear motor lead swap, RF order, folding rail comms, flood sensor stop), [[Folding-Rail]], [[Rail-Mounting-Guidance]], [[Staircase-Measuring-System]], [[Diagnostic-Codes]], [[Brake-Replacement]], [[Bruno-Serial-Numbers]], [[SRE-2010]], [[SRE-3000]], [[SRE-3050]], [[CRE-2110]], [[Bruno]] (new Drawings section), [[TechMate Stairlift Troubleshooter]], index. CLAUDE.md: new "Dealer-portal Drawings" convention (ILS sheets rank with the manuals; newer revision wins).
- **Resolved:** gear rack grease is **PTFE for every CRE/SRE** (ILS-01446 Rev 4, April 2026, newer than the white-lithium manuals); TechMate's "Elite/CRE brake can't be replaced alone" (Bruno sells SRV-2010-045 and SRV-2110-032 kits).
- **Findings:** Elite gear motor changed supplier Feb 2025 (blue/brown leads, swap if it runs backwards; CRE pinion heated to 450 °F); SRE-5000 product code 036 and PCB kit split at SN 26080361090; Elite seat belts changed Oct 2020 and Sept 27 2022; rail cross pin keeps the rack in if the bottom end plate comes off; ILS-01397 and ILS-01403 are newer Picture Perfect revisions.
- **Flagged:** ILS-01446 says the display shows "C4" with the seat swivelled (as written, odd); the SRE-5000G Australian addendum names the SRE-3050G by mistake.
- **Missing manuals:** ILS-01446 ticked off. SRE-5000 manuals still needed (the sheets cite an SRE-5000 Technical Support Guide). **Pending:** 474 Drawings sheets (VPL 134, Vehicle Lifts 277, Docking Devices 60, General 3).

## [2026-10-21] ingest | Bruno VPL — Drawings library ILS instruction sheets (134 sheets)
- **Scope:** all 134 VPL sheets in `MANUALS/Bruno/Drawings/VPL/` → 15 source pages in `sources/Bruno/VPL/`: [[ILS-01444 Maintenance Control Plan for VPLs]] plus "ILS - VPL …" pages (Technical Specifications, Application Drawings, Landing Gates/Platform Gates/Flush-Mount Doors, Platform Conversions and Canopies, ACME Screw/Nut/Bearing Service, Brake Retrofit Kits (AC), Electric Interlock Wiring Kits, Interlock Timers and Door Operators, 3-Stop and Redundant Limit Switch Kits, Cold Weather and Battery Kits, Electrical Retrofit Kits, Traveling Cable Kits, Flood Sensor Kits, Shipping/Handling/Brush Kits). Every sheet cited once.
- **New pages:** [[VPL-Maintenance]] (ILS-01444 plus the 2025 manuals' 12-month/2-month lists) and [[VPL-3300B]] (commercial line, no manuals).
- **Updated:** VPL-Drive-Service (grease, nut switch test tool, tall screw/nut and joint pins, brake, belts), VPL-3100B, VPL-3200B, VPL-3153-3175 (official 2026 specs), Gate-and-Door-Interlocks, Automatic-Door-Operators, Top-Landing-Gate-Installation, VPL-Installation, VPL-Troubleshooting (ILS symptom table), Joint-Commission-DMEPOS, Mobility-Batteries, Battery-Charger-LED-Diagnostics, Bruno, index, five older tech-tip pages (superseded/conflict notes).
- **Findings:** ACME screw grease is **Mobil Aviation Grease SHC 100 (LUB-00114)** (manuals, ILS-01444, ILS-01538 agree; the tips only said "Bruno grease"). Commercial and newer residential VPLs have no separate brake. Nut safety switch test tool VPL-32422 (won't fit = drive nut dropped, replace both). Interlocks: 24 VAC on AC VPL-3100, 24 VDC on 3100B. ILS-01129 Rev 3 (2023) supersedes the 2016 tech-tip copy.
- **Flagged:** belt deflection, ILS-01444 (2022) about ½ in vs the 2016 tip's ⅛ in at 2½–3½ lb: the newer ILS wins. VPL-3200B weight 1210 lb (manual) vs 1190 lb (2026 spec sheet). Tall tower bottom section: ILS-00992 says 570 lb (tech tips said 550 or 900).
- **Missing manuals:** added the Bruno commercial VPL (and AC VPL-3153/3175) manuals. **Pending:** Vehicle Lifts 277, Docking Devices 60, General 3.

## [2026-10-21] ingest | Bruno vehicle lifts — Drawings library ILS instruction sheets (277 sheets)
- **Scope:** all 277 sheets in `MANUALS/Bruno/Drawings/Vehicle Lifts/` → 8 source pages in `sources/Bruno/Vehicle Lifts/`. Fitment: [[ILS - Curb-Sider Sub-Base Fitment by Vehicle]] (144 base sheets, 1998–2026), [[ILS - Joey Mounting Kit Fitment by Vehicle]] (60), [[ILS - Pickup Truck Bases and Stow-Away Mounting Kits]] (8). Service: Curb-Sider, Joey, Out-Sider (ASL-250/275), Chariot (ASL-700), Out-Rider (PUL-1100) and Stow-Away. Every sheet cited once.
- **Method:** fitment tables built by script from each sheet's title block (part number, vehicle, date) and its "Before installation" notes (seat, jack/spare, drilling, exhaust items only); vehicle names hand-fixed where the title block was blank. Open the PDF for drill points.
- **Updated:** VSL-6000-6900, VSL-4400, ASL-275, ASL-250, ASL-700, PUL-1100, Hitch-Adapters, Vehicle-Lift-Power-Wiring, Docking-Devices, Bruno, index.
- **Findings:** VSL-36xxx = sub-base (VSL-26xxx weldment + VSL-K-550 kit). Base capacity decal must be re-punched when the lift is rated lower than the base (ILS-00891, 2025). Curb-Sider chain 1/8–1/4 in slack, bracket bolts 70 in-lb. Joey belt wraps counter-clockwise, catch edge out; current limits 25 A lift / 12 A in. Hitch-lift lighting: resistor kits for lights-stay-on (ASL-16727, ASL-70161) and hyper-flash/tow-recognition (ASL-K-284, AWL-K-1601). New products noted: PUL-1850 Stow-Away (no manual), ASL-275L lightweight and rigid-chair setups.
- **Flagged:** ASL-700 wheel nuts 75–88 ft-lb (manual) vs 62–65 ft-lb on the 2019 hub-spacer sheet; ASL-275 7-pin kit numbers INS-K-2002/2003 (manual) vs adapters ASL-16730/16716 (ILS-01450).
- **Pending:** Docking Devices 60, General 3.

## [2026-10-22] ingest | Bruno docking devices and general notices — Drawings library ILS sheets (63 sheets)
- **Scope:** 60 sheets in `MANUALS/Bruno/Drawings/Docking Devices/` → [[ILS - Docking Device Fitment by Mobility Device]] (scooters 20, power chairs 38, manual chairs 2; 1999–2023); 3 in `General/` → [[ILS - General Install Notices (Hybrid Vehicles, ESD, Dielectric Grease)]]. Every sheet cited once. Table built by script, device names hand-entered from each title block; two sheets are image-only.
- **Updated:** Docking-Devices (Bruno DD part numbers now on file), VSL-6000-6900 (hybrid HV caution, DD link), PUL-1100, Vehicle-Lift-Power-Wiring (hybrid/EV and ESD), Bruno, index.
- **Findings:** Bruno DD prefixes SLD (scooter) / WLD (wheelchair); balance point first, then shroud notching; universal options WLD-00978 belts, WLD-00801 clamps, Hook 'N Go WLD-01344/01355. Most listed devices are discontinued (newest sheet 2023, Pride Maxima). Hybrids: up to 650 V DC, never power mobility equipment from a hybrid's small 12 V battery.
- **Drawings library complete:** all 636 downloaded sheets ingested; no backlog.

## [2026-10-22] ingest | Bruno SRE-5000 — install, owner's, tech support guide, power options and folding rail manuals
- **Pull:** per the human ("download relevant docs from here"), Brunopartner **Service Docs** (Manual Search, all 1,708 entries) was indexed and the newest relevant edition of each manual downloaded: **54 PDFs** into `MANUALS/Bruno/{Bruno Straight SL, Bruno Curved SL, VPL, Vehicle Lifts}/` (manifest `MANUALS/Bruno/_service_docs_manifest.md`). Skipped Valet/TAS/VSS seats, Carony, scooters and chairs, discontinued vehicle lifts, CAN/G variants and the ELV-3600 elevator. Ingesting cluster by cluster, starting with the SRE-5000.
- **SRE-5000 (5 docs):** [[SRE-5000 Install Manual]] (08-10-2026), [[SRE-5000 Owner's Manual]] (08-06-2026), [[SRE-5000 Tech Support Guide]] (09-17-2026), [[SRE-5000 Power Options Install Guide]] (04-16-2026), [[SRE-5000 Folding Rail Install Guide]] (03-27-2026).
- **Updated:** [[SRE-5000]] (documents, install essentials, PCB matching, folding rail modes, troubleshooting), [[Stairlift-Troubleshooting]] (SRE-5000 continuous charge, code details, fold rail checks, IR/motor-lead routing), [[Diagnostic-Codes]], [[Folding-Rail]], [[Bruno-Serial-Numbers]], [[Bruno]], index.
- **Findings:** gearbox ratio changed 19 Aug 2026 (ECN8485). PCB-00180 rev 1 is for SN 26080361090 and later; P3 or PCB-00194 for older. A mismatch causes sudden stops going down, or slow down travel with relay clicking. Mid-park stop mode is the fold-board DIP switch, and the remote always stops at mid-park. DIP 1 = single-user, DIP 2 = right-hand. It charges anywhere on the rail.
- **Flagged:** "battery critical" is 2 short + 3 long in the install manual but B-B-L-L in the newer TSG table (TSG wins). The install checklist still says "move jumper" for RH (it's DIP 2). TechMate calls C-C a "safety relay" failure; the TSG says controller (drive circuit) failure.
- **Missing manuals:** SRE-5000 ticked off.

## [2026-10-22] ingest | Bruno SRE-2010 / SRE-2010E / SRE-3050 — install, owner's and power option manuals (Service Docs)
- **Docs (6):** [[SRE-2010 Install Manual]] (02-25-2026), [[SRE-2010 Owner's Manual]] (02-27-2026), [[SRE-2010E Install Manual]] (02-25-2026), [[SRE-2010E Operator Manual]] (03-05-2026), [[SRE-2010 Power Seat and Footrest Install (2022)]], [[SRE-3050 Power Options Install Guide]] (04-16-2024). These are the first Elite install and owner's manuals on file.
- **Updated:** [[SRE-2010]] (documents, install essentials, DIP table, outdoor differences, owner codes, power rail disable switch), [[SRE-3050]], [[Diagnostic-Codes]] (A2, A7, the full Elite DIP table), index.
- **Findings:**
  - Elite rail = stair length + 9 in, plus 4 in with an overspeed brake.
  - No mount on the top landing; no more than 3 steps without a mount.
  - Wall clearance is 4.25 in (5.25 with a canopy, 7.25 with the wide seat), measured from the back of the top of the rail.
  - RH needs the 12-pin jumper too.
  - Outdoor units charge only at the end contacts; dielectric grease on all rail connections; keyed 2.4 GHz RF remotes (9 V) at 35–48 in; 5-year major-component warranty.
  - Elite power swivel needs a second press at the top; the Elite power rail has a disable switch, and the emergency hand-fold must be slow.
- **Flagged:**
  - The ILS "single-user = DIP 1 and 2" wording vs the manual's table (single-user = #2 only, both ON = battery warnings only); the manual wins.
  - The 2010E owner's manual calls the seat "Elite Curve" and says it swivels 135° (copy error).
  - The SRE-3050 power-options footrest torque is given as both 40 and 50 ft-lb.

## [2026-10-22] ingest | Bruno CRE-2110 / CRE-2110E — 2026 install and owner's manuals, power options (Service Docs)
- **Docs (5):** [[CRE-2110 Install Manual (2026)]] (04-15-2026; supersedes the 2018 [[CRE-2110 Install Manual]], now marked superseded), [[CRE-2110 Owner's Manual]] (06-01-2026), [[CRE-2110 Power Options Install Guide]] (08-24-2022), [[CRE-2110E Install Manual]] (05-06-2026), [[CRE-2110E Owner's Manual]] (06-22-2026).
- **Updated:** [[CRE-2110]] (documents, new overspeed reset, 2026 install numbers, owner codes, outdoor notes), [[Overspeed-Safety-Brake]] (CRE, SRE-2010E and SRE-5000 resets), [[Diagnostic-Codes]] (A6/A7 split), [[Stairlift-Troubleshooting]], [[TechMate Stairlift Troubleshooter]], [[Bruno]], index.
- **Resolved:** the TechMate vs manual conflict on the CRE overspeed reset. The 2026 manual uses TechMate's method (8 mm CCW on the motor hex shaft, then the trip plate to neutral); the 2018 two-lever reset is superseded.
- **Findings:**
  - Rail joints M10 × 70 at 50 ft-lb with SRV-2110-012 clamps; slope ½° every 2 ft.
  - Flat-landing mounts at 3 in and 12 in from the end, then no more than 24 in; M12 at 67 ft-lb. Rail mount screws 225 in-lb.
  - RF XBee remotes (CRE-01065, 2 AA) now standard; keyed remotes at 15–48 in.
  - Power swivel stop adjustable 30–90° (small cam).
  - The curve beeps when stopped short of a charge position; a yellow LED on the bracket shows correct parking.
- **Flagged:** the remote height is printed as "15 in (220 mm)", a typo; the owner's manual's last pages still carry a 2023 footer.

## [2026-10-22] ingest | Bruno legacy stairlifts — SRE-3000 (2019), SRE-2000, SRE-2750, SRE-1550, CRE-2100 manuals (Service Docs)
- **Docs (10):**
  - [[SRE-3000 Installation Manual (2019)]] (trilingual; supersedes the 2015 manual, now marked superseded) and [[SRE-3000 Operator Manual (2019)]].
  - [[SRE-2000 Installation Manual (2007)]] and [[SRE-2000 Operator Manual (2007)]].
  - [[SRE-2750 Installation Manual (2011)]] and [[SRE-2750 Operator Manual (2009)]].
  - [[SRE-1550 Installation Manual (2009)]] and [[SRE-1550 Operator Manual (2009)]].
  - [[CRE-2100 Installation Manual (2009)]] and [[CRE-2100 Operator Manual (2009)]].
- **New model pages:** [[SRE-2000]] (Electra-Ride Elite, 400 lb), [[SRE-2750]] (Electra-Ride LT, 275 lb), [[SRE-1550]] (Electra-Ride II, 350 lb, belt drive).
- **Updated:** [[SRE-3000]], [[CRE-2100]] (first manuals on file), [[Overspeed-Safety-Brake]] (legacy resets), [[Diagnostic-Codes]] (new legacy beep code section), [[Bruno]] (legacy section rewritten), index.
- **Findings:**
  - Legacy units charge only at the ends.
  - DIP #4 is a coast delay (900 ms for remote dropouts).
  - SRE-2000 rail sits 1¼ in above the noses and 2⅝ in from the obstruction, and must never lean forward.
  - SRE-2750 clamp bolts are only 10 ft-lb (more deforms the rail); wedge locks are used when the rail is off the floor.
  - SRE-1550 is belt driven (belt tension per SRE-00648, rail groove check), and a real overspeed trip means returning the drive.
  - SRE-3000 2019: rail = stair length + 12 in; 3 in wall clearance; single-user is set by a jumper; adds a drive vibration adjustment and a folding joint reset.
- **Flagged:** the legacy manuals specify white lithium grease, but Bruno's current PTFE guidance (ILS-01446) applies.

## [2026-10-22] ingest | Bruno VPL — AC VPL-3100, VPL-3100B operator, VPL-3200B flood zone, commercial VPL-3300B/3310B/3353B and enclosure manuals (Service Docs)
- **Docs (15 → 11 source pages):**
  - [[VPL-3100 (AC) Installation Manual (2025)]] and [[VPL-3100 (AC) Operator Manual (2024)]] (first AC VPL manuals).
  - [[VPL-3100B Operator Manual (2024)]] (supersedes 2019).
  - [[VPL-3200B Flood Zone Tower Installation Manual (2025)]] and [[VPL-3200B Flood Zone Operator Manual (2024)]].
  - [[VPL-3300B Installation Manual (2022)]] and [[VPL-3300B Operator Manual (2023)]].
  - [[VPL-3310B Tall Commercial Installation Manual (2020)]] and [[VPL-3310B Tall Commercial Operator Manual (2019)]].
  - [[VPL-3353B 3-Gate Installation Manual (2019)]].
  - [[VPL Commercial Enclosure Installation Manuals (2019)]] (5 enclosure supplements on one page).
- **Updated:** [[VPL-3153-3175]], [[VPL-3100B]], [[VPL-3200B]], [[VPL-3300B]] (new "From the manuals" section), [[Battery-Charger-LED-Diagnostics]], [[Bruno]], index.
- **Findings:**
  - AC VPL: dedicated GFI 15 A circuit, no battery backup (hand wheel only); E-stop 5 s clears controller faults.
  - Commercial: AC hard-wired to a disconnect, junction boxes on both sides, PCB-00164 1–10 s strike/door timer, top and bottom final limits.
  - The tall commercial emergency lowering key switch is mounted outside the hoistway and bypasses the safeties; lock out three power sources.
  - A non-flush hoistway door needs a 60° deflector.
  - 3-gate "runs with gates open" = the yellow jumper is still in.
  - Enclosure door harness: pull the breaker first or the 24 V fuse blows.
  - Flood zone tower: NEMA 3R 60 A disconnect, FZ enclosure; won't run in more than 3 in of water.
- **Flagged:**
  - The 3310B and OFZ manuals print 1210 lb as "379 kg" (should be about 549 kg).
  - The AC VPL maintenance list includes "battery condition" (DC carry-over).
  - Several VPL manuals carry a stray "SRE-2010G INSTALLATION 06-07-2021" footer on the cover page.
- **Missing manuals:** commercial VPL and AC VPL-3153/3175 ticked off.

## [2026-10-22] ingest | Bruno vehicle lifts — operator manuals, VSL-4000HW Joey, PUL-1850 Stow-Away, AWL-150 Lifter, VSL-570 Big-Lifter, AWL-1600 Back-Saver (Service Docs)
- **Docs (13):**
  - Operator manuals: [[ASL-275 Operator Manual (2022)]], [[ASL-250 Operator Manual (2017)]], [[PUL-1100 Operator Manual (2022)]], [[VSL-4400 Operator Manual (2022)]].
  - Joey: [[VSL-4000HW Joey Installation Manual (2017)]] and [[VSL-4000HW Joey Operator Manual (2013)]].
  - Stow-Away: [[PUL-1850 Stow-Away Installation Manual (2018)]] and [[PUL-1850 Stow-Away Operator Manual (2013)]].
  - Lifter: [[AWL-150 Lifter Installation Manual (2023)]] and [[AWL-150 Lifter Operator Manual (2022)]].
  - Big-Lifter: [[VSL-570 Big-Lifter Installation Manual (2023)]] and [[VSL-570 Big-Lifter Operator Manual (2022)]].
  - Back-Saver: [[AWL-1600 Back-Saver Installation Manual (2020)]].
- **New model pages:** [[VSL-570]] (400 lb in-vehicle boom hoist), [[AWL-150]] (200 lb manual-chair hoist), [[AWL-1600]] (hitch lift for a folded manual chair), [[PUL-1850]] (under-vehicle transfer seat, 300 lb user).
- **Updated:** [[ASL-275]], [[ASL-250]], [[PUL-1100]], [[VSL-4400]] (VSL-4000HW manuals), [[Hitch-Adapters]] (AWL-1600 table), [[Docking-Devices]] (VSL-570 C-arms), [[Bruno]], index (model rows; Service Docs paragraph and Bruno status line).
- **Findings:**
  - PUL-1100 capacity depends on the drive (100 / 200 / 350 lb).
  - ASL-275/250 emergency crank: clockwise raises, a ⅜ in drill works; the ASL-250 needs the control arm held up.
  - AWL-150: never use a belt frayed more than ⅛ in; "switch reversed" = the belt wound backwards on the spool.
  - VSL-570: base bolts 12 ft-lb max criss-cross; a fender washer lowers the rating; chain tension by rotating the motor CCW, pivot nut first.
  - AWL-1600: receiver 7–25 in; Hold-Tite foam must deform around the armrests.
  - PUL-1850: runs only with the door open (no FMVSS impact); door switch gap ¼ in max.
  - VSL-4000HW: emergency board buttons bypass all limits; J8 XTRA jumper sets button C's direction.
- **Flagged:** several 2022 vehicle-lift operator manuals carry a stray "SRE-2010G OPERATOR" footer. **Service Docs pull complete: all 54 manuals ingested.**

## [2026-10-22] ingest | Bruno parts drawings — 252 assembly drawings from the Brunopartner parts lookup
- **Pull:** per the human ("here is the parts catalogue, download the relevant items"). The portal's Parts Lookup only accepts exact serials and returns a per-unit parts list linking to public assembly drawings. The catalogue was rebuilt by crawling from 45 top-level model/carriage drawings, three assembly levels deep: **252 drawings** into `MANUALS/Bruno/Parts/` (manifest `_manifest.md`). 540 referenced part numbers have no drawing (404-checked). Valet seat parts skipped; no prices recorded.
- **Pages (8):** [[Parts Drawings - SRE-5000 Elan]], [[Parts Drawings - SRE-3050 Elan]], [[Parts Drawings - SRE-2010 Elite]], [[Parts Drawings - CRE-2110 Elite Curve]], [[Parts Drawings - VPL Residential Short (3153-3175)]], [[Parts Drawings - VPL Residential Tall (3210B-3214B)]], [[Parts Drawings - VPL Commercial (3353B-3375B, 3310B-3314B)]], [[Parts Drawings - Vehicle Lifts]]. Each has a drawing table (level, parent, revision) and a key-service-parts table generated from 3,890 parsed BOM lines.
- **New concept:** [[Bruno-Parts-Lookup]] (serial lookup, the inquiry checkboxes email Bruno, current-revision caveat, common cross-model parts). Every Bruno model page now links its parts page. CLAUDE.md: new "Dealer-portal parts drawings" convention. Updated [[Bruno]], index.
- **Findings:**
  - All battery VPLs use charger BCR-24020; tall residential and commercial VPLs use BTR-12001 33 Ah U1 batteries.
  - Stairlift batteries: BTR-12002 (Elite and Curve), BTR-12008 (SRE-3050), BTR-12010 (SRE-5000).
  - SRE-5000 carriage PCB-00180, gear motor MDC-24035. Elite motors MDC-24031/24032 (pre-2025). CRE motor MDC-24033.
  - Joey controller PCB-00155 and up/down motor MDC-12025. Out-Rider heavy-duty motor MDC-12019 (shared with the VSL-570).
- **Flagged:** the AC VPL tower drawings list motor VPL-31953 "Elektrim 1 hp AC motor", while the 2025 AC manual and spec sheet say ½ hp 90 VDC. Check the motor tag before ordering.

## [2026-10-22] lint | links, orphans, citations, index coverage, stale notes
- **Clean:** no broken wikilinks, no orphan pages. Every model, concept, manufacturer and field-note page is in the index with the right `type:`. Every `source:` path resolves on disk.
- **Fixed:**
  - [[SRE-5000 Power Options Install Guide]] cited a filename that doesn't exist; now points to the real PDF.
  - [[SRE-3050]] still said ILS-01446 was "not on file"; now linked.
  - [[Stairlift-Troubleshooting]] still said the SRE-5000 had "no manual on file"; now links the TSG.
- **Uncited raw files (39), all known or intentional:**
  - 13 Golden Spanish-language scooter manuals (already listed as pending).
  - Harmar product photos and CSV metadata, plus 2 Clippings images (assets, not documents).
  - 8 files already summarized under another page's path (AL300/AL301 Harmar manuals, Helix guides, EZ-ACCESS pay scales, PMS eval forms, a GP162 service guide).
- **Gaps:**
  - [[CRE-3110]] still has no manuals; none are on the Brunopartner Service Docs index either.
  - The ELV-3600 home elevator manuals were skipped by choice.
  - 30 source pages have no `date:`; they are undated forms, sell sheets and brochures.
- **Suggestions:** a stairlift **power options** concept page (power swivel and power footrest across SRE-2010, 3050, 5000 and CRE-2110; mentioned on 7 model pages) and a vehicle-lift **emergency operation** page (cranks, hand wheels and board-button backups across ASL, PUL, VSL and AWL).

## [2026-10-22] concept | Stairlift-Power-Options and Vehicle-Lift-Emergency-Operation (from the lint suggestions)
- **New:** [[Stairlift-Power-Options]] compares the power swivel and power footrest across the Elite (SRE-2010), Elite Curve (CRE-2110), Elan (SRE-3050/3000) and SRE-5000: rider use (press again vs keep holding; CRE swivel stop 30–90° by cam), jam behavior and codes A6/A7, install kits, harness plugs, footrest torques (40 vs 50 ft-lb), seat-to-swivel torques, aux PCB and actuator part numbers.
- **New:** [[Vehicle-Lift-Emergency-Operation]] gives crank, drill and board-button backups for the Out-Sider, Chariot, Out-Rider, Joey (VSL-4400 and the older VSL-4000HW, whose board buttons differ), Curb-Sider and Stow-Away, with directions and the fuse/key-first rule.
- **Linked from:** 14 model pages, [[Stairlift-Troubleshooting]] §13, index.
- **Gap noted:** no documented emergency method for the VSL-570 Big-Lifter or the AWL-150 Lifter.

## [2026-10-22] field-note | Golden GC440 — 8 beeps, won't move, burnt motor connector (open)
- Started [[2026-10-22 GC440 8 beeps burnt motor connector]]: sn QCA15N0466, intermittent. Key on gives power, then 8 beeps (Dynamics code 8 = motor voltage fault, open circuit) and no drive. The first connector off the motor is burnt and melting. The serial label under the floor mat was rubbed off, so the tech read the serial from the bottom of the frame.
- Added Golden's code 8 test tree and harness part numbers (SE06E604 rear / SE06E606 front intermediate motor harness).
- Linked from [[GC240-340-440-540-Companion]], [[Flash-Beep-Diagnostics]], [[Companion Service Guide (GC240, GC340, GC440)]] (its step 14 is printed inverted) and the index. Takeaways pending.
- Takeaways added (per the human): read the serial off the frame on the bottom of the scooter when the label is gone; start with the easiest check (the motor connector) before the controller, which needs the tiller taken apart. Updated the note, index row, [[GC240-340-440-540-Companion]] and [[Flash-Beep-Diagnostics]].
