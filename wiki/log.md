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
