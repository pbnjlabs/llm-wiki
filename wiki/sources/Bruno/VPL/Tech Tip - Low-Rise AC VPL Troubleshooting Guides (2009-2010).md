---
type: source
manufacturer: Bruno
model: VPL-3153-3175
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/VPL/VPL Trblshtng Guide - 1st to 09070300179 (revised 08-06-09).pdf; MANUALS/Bruno/Tech Tips/VPL/VPL Trblshting Guide - 09070300179 to 09090300040 (revised 8-14-09).pdf; MANUALS/Bruno/Tech Tips/VPL/VPL Trblshting Guide - 09090300041 to 10020300227 (revised 9-30-09).pdf; MANUALS/Bruno/Tech Tips/VPL/AC VPL Trblshtng Guide - #10020300227 to current (rev 4-19-10).pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2010-04-19
tags: [bruno, vpl, tech-tip, troubleshooting, ac, legacy, vpl-3153, vpl-3175]
---

# Tech Tip - Low-Rise AC VPL Troubleshooting Guides (2009-2010)

Four Bruno Technical Service step guides (10–12 pages each, 2009–2010; portal tech-tips 197–200 and 191) for **AC low-rise VPLs** (VPL-3153/3175), each for a serial range. The portal title of tech-tip 200 points to a Chariot measurement sheet instead; tech-tip 199's file is the 08-06-09 guide.

| Guide | Serials | Control box |
|---|---|---|
| Rev 08-06-09 | 1st to 09070300179 | **Relay logic**: transformer, 24 VAC control, terminal strips TB1/TB2/TB3, E pause relay, up relays U1/UA/UB, down relays D1/DA/DB, bridge rectifier for the brake |
| Rev 8-14-09 | 09070300179 to 09090300040 | Same, adds an **E1 brake relay** |
| Rev 9-30-09 | 09090300041 to 10020300227 | Same steps, redrawn common/up/down circuit diagrams |
| Rev 4-19-10 (dated 2/25/10 inside) | 10020300227 to "current" | **Control board** with test points below each terminal block (TB1–TB5), plug-in relays |

**Relay-box units, TB2 jumper map** (jump to bypass and test): top cap 1–2, nut safety 2–3, upper gate closed 3–4, upper gate locked 4–5, platform E-stop 1–6, up switch 7–8, down switch 7–10, upper limit 8–9, under-panel (safety pan) 10–11, lower limit 11–12. **7–9 runs up and 7–12 runs down with every safety bypassed** (it starts at once).

Steps (all versions): 115 VAC minimum in (TB1-2 to TB1-4; on the 2010 board, LINE to NEU, then NEU to UFL for the upper final limit) → 24 VAC after the fuse → transformer → E-stop → top cap (pull it up into service) → nut safety → upper gate closed (**12+ VAC**) → upper gate locked → jump the platform controls → **E relay** (out of circuit: no continuity 8–6 [and 4–2]; jumped coil: clicks and closes) → motor test → brake → limits and directional relays.
- **Motor test** (relay box): power cord out, crank 6 in off the landing, release or remove the brake, move the black and red motor leads across TB3 per the sheet, jump TB1-1 to TB3-1, plug in: it runs **up at once**, so be ready to unplug. (2010 board: tie black+yellow and orange+red, jump LINE to the black/yellow pair.)
- **Brake:** lift the brake's silver release handle, or remove its three Allen screws. Runs → brake circuit. Brake leads at the rectifier should read **105+ VDC** on a command; none → rectifier input should read 115+ VAC (yes → rectifier; no → E/E1 relay). On the 2010 board, no 105 VDC at the white/black brake terminals → board.
- **Relays click but nothing moves** → brake, motor, E and E1 relays.

Interlock and gate tips are the same in every guide (see [[Gate-and-Door-Interlocks]]): 24 VAC at interlock pins 3–4 needs the **bottom of the three tower limits** made; jump 1–2 to bypass the interlock; the interlock's **terminal block must be at the top**. "Runs down 2 in and stops" (with gate) → the gate's lock switch must release before the tower's gate enable switch.

TechMate starts the AC group at serial 17090350001 and sends older units to Bruno, so these guides are the only Bruno steps on file for pre-2017 AC units. They're old; confirm with Bruno Technical Service before trusting a terminal number.

Feeds: [[VPL-3153-3175]], [[VPL-Troubleshooting]]
