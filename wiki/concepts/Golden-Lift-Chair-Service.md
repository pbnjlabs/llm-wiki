---
type: concept
tags: [golden, lift-chair, service, troubleshooting, parts, calibration, smart-tek, wiring]
---

# Golden Lift Chair Service (tech reference)

How to diagnose and repair Golden power lift recliners, from the
[[Lift Chair Service Guide]] (2021), the
[[Discontinued Lift Chair Service Guides (115, 165, PR116, PR117, PR119)]]
and Golden's instruction sheets. Owner-level operation, hand-control
features, warranty and models are on [[Golden-Lift-Chairs]]. Parts:
Golden tech support 800-624-6374, **lift chair/bed tech x502**,
parts@goldentech.com; have the **model and serial number** (hand control
cord, rear of the lift frame).

## Before you start

- Plugged into a working outlet? Outlet on a wall switch? Breaker?
  Corroded terminals, bare insulation, unseated connector pins?
- Are the **Smart Tek LEDs** on (transformer, power cord, hand control)?
- **Unplug the transformer** before any repair. Most jobs start by
  tipping the chair onto its footrest, upside down, or onto the side
  **opposite the hand control**.
- **Never put the transformer under the chair.**
- Tools: #8–10 flat and P2/P3 Phillips screwdrivers, **T30 Torx**,
  drill; for MaxiComfort also 7/16, 3/8 and 1/2 wrenches, 5/32 Allen,
  needle-nose pliers, spare hair pins, zip ties, a chair stand, a
  voltmeter, white lithium grease or Zep 2000.

## Components and test values

Everything electrical is **replace-only**; nothing is field-repairable.

| Component | Where | Test | Expected |
|---|---|---|---|
| Transformer | Behind the chair | DC volts at the chair connection | **About 27 V DC** (24 V class; current transformers are rated 29 V) |
| Control box (500 and 700 lb chairs; multi-motor chairs) | On the lift frame | DC volts | **27–32 V DC**. Failure: no lift/recline, **clicking, motors out of sync** |
| Motor (lift, recline, cradle, head, lumbar) | Between frame and seat | Smart Tek table | Noisy just before it fails |
| Hand control extension | Pocket to motor/box | Continuity | Replace if open |
| Heat pad | Lumbar | Resistance across the pins | **About 40 Ω** |
| Massage vibrator | Back or seat | DC volts / resistance | **About 13.8 V DC; about 25 Ω** |

## Is the motor running?

Press down if it's stuck lifted, up if it's stuck reclined, and listen.

- **Motor silent:** plug, wall switch, another outlet (worn sockets
  can't carry the current), frayed power or switch cords; try a
  known-good hand control; then the Smart Tek table below.
- **Motor runs, chair doesn't move or only partly moves:** broken lift
  frame; broken push tube or gear case; **stripped gears**; stripped push
  tube or **broken fork head**.

## Smart Tek troubleshooting (by chair type)

| Symptom | Single-motor chairs (most 2-button, 2-position, MaxiComfort, PR404) | Dual-motor wide (501M26D, 501L26, 501T28) | PR502 (700 lb) |
|---|---|---|---|
| Dead, **both LEDs off** | Right-angle plug into the transformer; transformer into the outlet; breaker/fuse; then **replace the transformer** | Same | Same; **replace both transformers** |
| Dead, **both LEDs on** | **Motor** | Motors plugged into the control box? Then the **control box** (two motors rarely fail together) | Same |
| Motor runs one way only, LEDs on | **Hand control** | Hand control | Hand control |
| Dead, **hand control LED off** | Quick-release connector in the pocket locked? Extension to the motor? Then hand control (the extension rarely fails) | Same, to the control box; replace the **hand control first**, then the box | Same |
| PR502 works **slowly**, hand control lit, **one Y-connector light off** | — | — | That transformer: plug, outlet, then replace it |

## Sync and calibration after replacing parts

**After replacing any motor, control box, hand control or cable, run
the sync/calibration or the chair won't position correctly.**

| Chair | Procedure |
|---|---|
| **3-way (2-motor) chairs** | Hold **S2** until the motor stops; hold **S3** until it stops; hold **S2 + S3** until the backlight goes out; release (lights back on = reset). Both motors must be fully retracted |
| **MaxiComfort AutoDrive** | Hold **S4**, then **S2**, each until the motor stops |
| **AutoDrive with cradle** | **S4**, **S2**, then **S5** |
| **4-zone (ZK3200-HC)** | Hold **A + C** (backrest down + footrest up) until it stops, then 3–5 s more |
| **5-zone (ZK3100-C5M)** | Hold **A + C + D** (+ twilight), then 3–5 s more. PR130: the chair ends reclined with the footrest out |
| **ZKAD-5** | Can't be field-calibrated; lights flashing in sets of 2–4 → x502 |

The 2021 4/5-zone sheet adds: **no buttons work** → hold M 4 s, press
**RISE** (hand control disable off); **only RISE and RECLINE work** →
M 4 s, then A, E, C, ZG (function lock off). On the **old-style
ZKAD-4 / ZKAD-HR** the disable is SP then S7 without the 4-second hold.

## Hand controls by model

| Hand control | Models (per the service guide) |
|---|---|
| **ZK1200-HC-1** (2-button, LED, USB) | PR118, PR202, PR200, PR355, PR359, PR401, PR410, PR451, PR501 (all sizes incl. 26/28 D), PR643, PR747, PR751, PR752, PR906, PR931 |
| ZK404-HC (2-button + head + lumbar) | PR404 |
| **ZK756HCL** (MaxiComfort LED, 3 motors) | **PR502**, PR505-M26, PR535-M26, PR531-M26; PR119 |
| **ZKAD-5** (AutoDrive, current) / ZKAD-4 / ZKAD-1 | PR505, PR506, PR508, PR510, PR535 (PSA, M, L, T), PR712, PR713, PR735, PR756, PR766 |
| ZKAD-HR-1 (AutoDrive + headrest) | PR512, PR630, PR632 |
| ZKAD-C3M (cradle, 3 motor) | PR514 |
| ZK3000-C2P (2-button cradle) | PR405 |
| **ZK3100-C5M** (5 motor) | PR515, PR761, PR130; the service guide also lists PR446 |
| ZK3200-HC (4 motor) | PR446/448 per their owner's manual; PR632 per the AutoDrive sheet |
| ZK1710-HC | 115, 165 |
| ZK805-2 (optional) | PR805 (plugs into the control box phone jack) |

> [!note] PR446 hand control
> The service guide lists the **ZK3100-C5M** for the PR446; its 2021
> owner's manual describes the **ZK3200-HC**. Check the part label.

## Motors, transformers and control boxes

- **Okin lift motors:** old style (model 1.31.000.034.30) has **three
  wires** out of the case (transformer, hand control extension, recline
  motor plug). New style (**72276**) has **one wire** to the transformer;
  the hand control plugs into the **top** of the case and a 2-motor
  chair's recline motor into the **side**.
- **Richmat:** **GM1400-LM for 2- and 3-position chairs**, **GM1450-LM
  for MaxiComfort** (with a recline motor plug and AutoDrive extension).
  Don't swap them.
- **Wide 26–28 in chairs:** two GMOKI-28W motors on a GMOKI-CB control
  box (PR502 adds GMOKI1502OM and a GM502YL Y-connector with LED; two
  transformers).
- **5-motor chairs** (PR515, PR761, PR130): GM3100 lift, back and cradle
  motors **with Hall sensors**, headrest and lumbar motors, control box
  **GM3100-CB** (GM3200-CB = 4-motor, cradle port sealed). Motor plugs
  are **color coded: grey lift, green back, yellow cradle**.
- **Transformers:** current **GM2102-TR-PK** (2 A); older GM2000-TR,
  GM1400-TR, GM1410-TR, GM1450-TR; **GM2100-TR** 3 A for cradle chairs;
  lithium-backup combo YH-D290020-A (29 V 2 A). Plug lead GM1501-APUS-36.
  9 V backup wire **GM1502L-B** (with LED) on wide and wall-hugger chairs.
- Control boxes go in their metal protection plate with hook-and-loop,
  and **cables and ty-wraps must be routed exactly as Golden shows**;
  wrong routing affects operation and damages parts. Check for pulled
  cables through the full range afterward.

## Lift frames and scissor mechanisms

| Frame | Used on |
|---|---|
| **LM5100** | Small and medium 2/3-position and MaxiComfort (PR118, PR202, PR401-SME, PR404, PR501 JP/S/M, PR505, PR510-SME, PR535-PSA/M and others) |
| **LM5120** | Large and tall (PR401MLA, PR446, PR501L/T/S23, PR510-MLA, PR512, PR630–632, PR713, PR735, PR756, PR535-L/T) |
| LM6111 / LM6112 | Dual-motor wide (PR501/505/531/535 M26–T28) |
| LM5124 | **Cradle / Twilight** (PR405, PR514, PR515, PR761, PR130) |
| LM5000C | PR200 (Capri) |
| LM502 | PR502 |
| LM992S / N | PR931 wall hugger (motor GM1900) |

Scissor (recline) mechanisms: **RM621** 3-way, **RM622** HD Maxi,
**RM620** MaxiComfort, **RM8300** 2-way, **RM631** (PR118/202), RM502.
**Replace both sides.** Left and right are as you sit in the chair.

## Replacement tips that save a callback

- **Lift frame to arm assembly:** 4 T30 lag screws (**8 on the wide
  dual-motor chairs**). **The footboard must be fully closed** when you
  bolt the frame back in, or it won't close afterward.
- **Arm assembly:** pull it off **without twisting**: the board holding
  the arms together snaps.
- **Fork head** (GMOKI-13, the plastic tip on the motor push tube):
  **left-hand thread**, and so is the push tube in the motor. Turn
  **clockwise to loosen**. Grip the tube with vise-grips over a cloth. If
  the push tube comes out, screw it fully in, back off **2 full turns**,
  then just enough to pin it to the motor straps.
- **MaxiComfort back bolts** (BB5671) must be **Grade 8**, with an MS25W
  split washer and BB5603 lock nut, three a side.
- **LM5124 cradle frame** can spring open when removed: pinch hazard.
- Hand control and extension: unlock the latch in the pocket and pull
  the two plug bases apart; the extension is stapled through the pocket
  fabric and zip-tied to the frame (note the tie points).
- **Right-to-left conversion:** reroute the extension along the left
  side of the frame at the same tie points (mark them with tape), move
  the wire clamp and the black hand-control hook.

## Lubrication (only for noise)

Not a routine maintenance item. **White lithium grease** on the lift
frame pivots, **Zep 2000** on the scissor mechanisms, sparingly (excess
drips on the chair and floor). A squeaking **recline bar** (the wide U
under the seat): unpin it from the motor straps and rock it to confirm,
then grease the bushings where the bolts pass through the square tube
(Golden recommends **Super Lube** grease; CRC 3-36 for hard-to-reach
spots, but it doesn't last).

## Heat and massage systems

| System | Parts | Used on | Cut-in |
|---|---|---|---|
| HV3000 | HV3001 hand control, HV3002-2 transformer, 18 in pad, vibrators | All except PR200, PR724, PR630, PR712 | Sep 2014–Jul 2015 |
| HV3100 (DHV, 2 zones) | HV3100-HC, junction box HV3100-JBOX, 4 vibrators | All except PR200, PR724 | Jul 2015 |
| HV3200 | HV3200-HC, -JBOX, -TR, 12 or 18 in pad, 4 vibrators | All except PR200, PR724 | Oct 2019 |
| HV4000 / HV4100 / HV4200 | Combined lift + heat + massage controls (HV4101-HC lock key; HV4200 PWR button, 20-min timers) | PL340, PR480, PR522, PR524 | 2012–2016 |

The heat/vibrate system has **its own power supply**: the wire is behind
the back rail on the **right** side. Dead heat or massage: that supply
and wall outlet, the junction box wiring, then the remote; heat pad
about 40 Ω, vibrators about 25 Ω. **AutoFlex** lumbar (PR510-MLA,
PR120) and **Shiatsu** (PR724; 29 V 2 A supply; if it stops or runs out
of order, unplug for 20 min) have their own control boxes.

## Battery backup

- 9 V backups: **brand-name batteries**, one use from recline to seated,
  then replace; replace yearly anyway.
- **Lithium backup (YH-B1600B):** slides onto the transformer; LED red
  charging, green full; sealed. **Recharge every 3 months and cycle
  every 6 months**; store charged and separated from the transformer.
- The **PR511** (air massage chair) needs **two outlets**: one
  transformer with the lithium backup for the chair, one for the
  "Accessory" cord.

## Options

- **Straight lift** (from serial GT2001RAP01783; not Twilight or PR502):
  move the detent pin on each side of the frame to the upper hole.
- **5 lb footplate** (BB5632): helps the footrest close for very light
  users.
- **Footrest extension** kit: sits slightly lower than the footboard when
  open; that's correct.

## Delivery and setup (house standard)

Golden's **Set Up Checklist** matches the Joint Commission delivery and
training requirements ([[Joint-Commission-DMEPOS]]): inspect with the
customer and note damage; confirm model, size and color; wall distance,
power, levelers, full recline; run every function and option; explain
SmartTek and the battery backup; teach the hand control, getting in and
out, seated when idle and the weight limit; show the manual and
warranty; have the customer sign.

## See also

[[Golden-Lift-Chairs]], [[Pride-Lift-Chairs]], [[Golden]], [[Troubleshooting]]
