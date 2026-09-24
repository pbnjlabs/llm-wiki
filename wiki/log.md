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
