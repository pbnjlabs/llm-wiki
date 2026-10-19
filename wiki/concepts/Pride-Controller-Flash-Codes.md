---
type: concept
tags: [pride, jazzy, controller, flash-codes, diagnostics, pg-drives, vr2, gc3, newvsi, dynamic-controls]
---

# Pride Controller Flash Codes (VR2, GC3, newVSI, Dynamic)

Pride's **Jazzy** and retail chairs mostly don't use Q-Logic. They use
**PG Drives** (VR2, GC3, newVSI) or **Dynamic Controls** electronics,
which report faults by **flashing LEDs**. This page puts Pride's four
basic-operation manuals side by side:
[[VR2 Controller Basic Operation Instructions (INFMANU3354)]],
[[GC3 Controller Basic Operation Instructions (INFMANU3937)]],
[[newVSI Controller Basic Operation Instructions (INFMANU4935)]] and
[[Dynamic Controller Basic Operation Instructions (INFMANU3676)]],
plus the Jazzy 614 Dynamic dealer guides
([[Jazzy 614 Technical Troubleshooting Guide (INFMANU3834)]],
[[Jazzy 614 Basic Troubleshooting (INFINFB2468)]]).
Which chair has which controller: [[Pride-Power-Chair-Lineup]].
Quantum Q-Logic chairs: [[Q-Logic-Fault-Codes]].

**Identify the controller first:** a speed dial = GC3; speed/profile
buttons with a 10-LED arc = VR2; a 5-segment meter with speed/profile
keys and the controller built into the joystick box = newVSI; a
16-light speed ring around the horn key and a separate **service
indicator** = Dynamic.

## PG Drives: VR2, GC3, newVSI (same 1–10 scheme)

All the battery-meter LEDs flash the count quickly, pause, and repeat
until the fault is fixed.

| Flashes | VR2 / GC3 / newVSI meaning | Do |
|---|---|---|
| 1 | Batteries need charging, or bad battery connection | Check battery connections; charge |
| 2 | Left motor bad connection | Left motor connections and harness |
| 3 | Left motor short to a battery connection | Provider |
| 4 | Right motor bad connection | Right motor connections and harness |
| 5 | Right motor short to a battery connection | Provider |
| 6 | **Charge inhibit** (charger connected to the base). GC3 shows it as a left-to-right scroll; on the newVSI a side-to-side ripple of the speed lights means **locked** instead | Unplug the charger / unlock |
| 7 | Joystick fault | Center the joystick, power off and on |
| 8 | Control system fault | Power module and joystick module connections and wiring (newVSI: all connections, batteries charged) |
| 9 | Park brake bad connection | **Both freewheel levers in drive** (GC3), then left and right motor/brake connections |
| 10 | Excessive voltage | Battery connections (usually a poor connection) |

This is the same table Golden prints for its VR2 chairs
([[TruCharge-Diagnostics]]). For the 4-digit codes a PG programmer
reads, see [[PG-Drives-Trip-Codes]].

## Dynamic (50 A / 60 A): 1–11 on the service indicator

The **service indicator** flashes the code (the battery meter flashes
an inhibit at the same time).

| Code | Fault | Do |
|---|---|---|
| 1 | Possible stall timeout or user error | Release the joystick |
| 2 | Battery fault | Check batteries and cables, charge; may need replacing |
| 3 / 4 | Left / right motor fault | That motor, connections, cables |
| 5 / 6 | Left / right park brake fault | That brake, connections, cables |
| 7 | Controller module fault | Communication connections and wiring |
| 8 | Power module fault | Communication connections and wiring |
| 9 | Communications fault | Communication connections and wiring |
| 10 | Unknown fault ("controller fault" on the Jazzy 614 sheet) | Provider |
| 11 | Incompatible controller | Provider |

**Dealer steps per code** (Jazzy 614 TTG, the only Dynamic dealer
guide on file; [[Jazzy-614]]): 1 = motors stalled for too long (check
for an obstruction, else power module); 2 = about **20 V** at the power
module (low-battery walk); 3/4 = motor **0.5–1.5 Ω** at the plug, else
motor, if good power module; 5/6 = freewheel levers in drive, then
brake **about 35 Ω** (Jazzy 614), else brake; 7–11 = bus cable and
extension continuity (under 1 Ω each pin), corrosion, then power
module, then joystick.

**Same numbering as Golden's Dynamic Shark** table
([[Shark-Diagnostics]]), which gives resistance checks (cold motor
0.3–50 Ω, brake 40–80 Ω) and DX-HHP joystick calibration. Pride's
charts call these 50/60 A controllers "Dynamic **LiNX**", but Golden's
LiNX manuals give a **different 7-code table** ([[LiNX-Diagnostics]]).
Use the table for the indicator you're looking at: a numbered service
indicator with 11 codes → this table.

## GC2 / GC3 dealer tests (Jazzy Select Elite TTG)

Same 1–10 numbering as above, with the GC chairs' values: **1 = under
22 V at the power module**; 2/4 = left/right motor open (0.5–1.5 Ω
good); **3/5 = left/right motor-to-brake wiring fault** (the BOI table
says "short to battery"); 6 = inhibit (charger in, or charger socket
pins 2–3 shorted); 9 = brake (**about 60 Ω** each); **10 = over 32 V**
(charger output over 30 V → charger). [[Jazzy-Select-Elite]].

## Jazzy 600 ES: left and right swapped

TechnoBulletin JAZZY-176 (2013) gives the 600 ES Dynamic table as **3 =
right motor, 4 = left motor, 5 = right brake, 6 = left brake**, the
reverse of the Jazzy 614 sheets and the table above. M1 = left motor,
M2 = right. [[Jazzy-600-ES]].

## Older PG and Dynamic controllers

- **VSI 8 flashes** is usually the controller, but a **conductive path
  between the motors** can cause it: any resistance between the two
  motors' leads (or motor lead to frame) = motors
  ([[Eight Bar Flash Code for VSI Controllers]]).
- **DL50** numbers differently: 1 low battery, 2 high voltage, 3/4
  motors, 5 brake, 6 controller, 7 joystick. **Dynamic DX** status LED:
  1 module, 2 accessory, 3/4 motors, 5/6 brakes. Pilot, Remote Plus and
  VSI use the 1–10 set. Full legacy tables:
  [[Technical Troubleshooting Guide - Glossary and Appendix (2004)]].
- **Remote Plus lock** uses a 3-pin key (KEYJAZ1001): insert and remove
  to unlock. **Flight** controller: lock by holding on/off 2 s, unlock
  with the horn twice. All locks in one table:
  [[Controller Locking Instructions (INFINFB2311)]].
- VR2 cable replacement: [[VR2 Controller Cable Replacement (INFINFB2005)]].

## Battery meter and other patterns

| | VR2 | GC3 | newVSI | Dynamic |
|---|---|---|---|---|
| Meter | 10 LEDs | 5 LEDs | 5 segments | 8 LEDs |
| Low battery | Left red flashing or steady (≤10%) | Left red flashing; red + yellow flashing = charge overnight | Red only or slow flash | Left red flashing (≤10%) |
| Charging / inhibit / programming | LEDs step up | LEDs scroll left to right | Step up left to right = charger plugged in | Left-to-right ripple alternating with steady |
| Joystick off center at power-up | Ripple side to side | Ripple twice, then all flash | Ripple twice, then 7 flashes | All speed lights flash fast (**OONAPU**) until centered |
| Sleep | All blink every 2.5 s | — | All blink every 2.5 s | — |
| Locked | Speed/profile indicator ripples | LEDs step up for two cycles | Speed/profile lights ripple | Right-to-left ripple |

## Lock, sleep, thermal rollback, charging

- **Lock (VR2, GC3, newVSI):** power on, hold on/off about 1 s until it
  beeps, release; joystick full forward until beep, full back until
  beep, release (long beep). **Unlock:** power on, full forward until
  beep, full back until beep, release.
- **Lock (Dynamic):** hold on/off **4 s** (display goes off, LEDs flash,
  short beep). **Unlock:** power on and press the **horn twice before the
  right-to-left ripple ends** (about 10 s), or it switches itself off.
- **Dynamic inhibit with no charger plugged in** (left-to-right ripple
  alternating with steady; speed light flashes when the joystick
  moves): the charger socket's pins 2–3 read as shorted. Check the
  **run plug** (pin 1–4 and 3–4 under 1 Ω) or that the 4-pin plug is in
  the power module.
- **Sleep:** powers off after a programmed idle time. VR2: switch off
  and on. GC3: press on/off. newVSI: **press on/off twice**. Dynamic: any
  key.
- **Thermal rollback:** VR2 and GC3 drop to **50%** output until cool.
  newVSI cuts current progressively and **stops the chair** at its limit.
  (Q-Logic and QLNES drop to 20%.)
- **Off-board charger** through the 3-pin socket, **Neutrik NC3MX plugs
  only**, max **8 A** (VR2, Dynamic) or **12 A** (newVSI). Use the
  charger supplied with the chair.
- **GC3 charge reminder** (GC2 too): after **8 h or more of driving**
  without a charge, the left red LED flashes 4 times at every
  power-down. Bulletin JAZZY-170's reset order: controller on → charger
  to the controller → charger to the wall → full charge → unplug the
  wall, then the controller → power-cycle. Batteries already full: drive
  a while first so the charger actually charges. Charge
  8–14 h **with the controller switched on before the charger is
  plugged in**, and leave it on for the whole charge, or the reminder
  won't reset.
- **Emergency stop:** release the joystick, then press on/off (abrupt).
- **Temperature:** keep VR2 chairs between 18 °F and 122 °F.
- **Harness routing:** under or inside the armrest, on the tie-down
  points, never outside the armrest pad where wheels, seat frame or
  doorways can damage it.

## See also

[[Power-Chair-Troubleshooting]], [[Pride-Power-Chair-Lineup]],
[[Jazzy-614]], [[Jazzy-600-ES]],
[[Joystick-Controllers]], [[PG-Drives-Trip-Codes]],
[[TruCharge-Diagnostics]], [[Shark-Diagnostics]], [[LiNX-Diagnostics]],
[[Freewheel-Mode]]
