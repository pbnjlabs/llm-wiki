---
type: concept
tags: [power-chair, scooter, troubleshooting, diagnostics, pride, quantum, golden, q-logic, qlnes, vr2, gc3, dynamic]
---

# Power Chair Troubleshooting

A symptom-first guide for power chairs, built the same way as
[[Stairlift-Troubleshooting]] and [[VPL-Troubleshooting]]. The detail is
from **Pride/Quantum**: [[Q6 Edge Basic Troubleshooting]], the Q-Logic,
Q-Logic 3 and QLNES manuals ([[Joystick-Controllers]],
[[Q-Logic-Fault-Codes]]), Pride's VR2/GC3/newVSI/Dynamic manuals
([[Pride-Controller-Flash-Codes]]), the [[J6]] /
[[Q6-Edge-3-Stretto]] operator manuals, and Pride's dealer **technical
troubleshooting guides** (meter values, §2, §3 and §6a):
[[Q6 Edge Technical Troubleshooting Guide (INFMANU4109 Rev B, 2012)|Q6 Edge]]
and [[J6 Technical Troubleshooting Guide (INFMANU4132)|J6]] (NE, NE+,
Q-Logic), [[Jazzy 614 Technical Troubleshooting Guide (INFMANU3834)|Jazzy 614]]
(Dynamic), plus the [[Elite Traveller Basic Troubleshooting (INFINFB2039)|Elite Traveller]]
scooter sheet. Which Pride model has which
controller: [[Pride-Power-Chair-Lineup]]. **Golden** chairs and scooters
follow the same steps but report faults through their own controllers
(index at the bottom). For the general method, see [[Troubleshooting]].

Pride's own sheet makes the main point: most problems are **batteries that
aren't fully charged or are worn out**. Start there.

## 1. Triage

1. **Does it power on?** Joystick light or display when the on/off is
   pressed? No → §2.
2. **Is it showing an error code, flashing, or beeping?** Write down the
   number or count and **which controller** it is (§7). Read the code
   before anything else.
3. **Does it drive?** Forward/back/left/right. Powers on but won't drive →
   §3.
4. **Drives, but…** short range, slow, pulls, clicks, cuts out → §4–§6.

Before every test drive: **freewheel levers in drive mode**, tires
inflated, connections tight, battery charged (the operator manuals'
pre-ride check).

## 2. Dead: no light, no display

Pride's checklist, in order:
1. Batteries **installed and wired correctly**.
2. **Battery terminals tight**.
3. **Battery quick-disconnect harness** fully joined.
4. **Main circuit breaker:** Q6 Edge/J6 have a reset button (push it in).
   The Q6 Edge 3 Stretto's breaker (left side of the frame) **resets
   itself after about a minute's rest**. Trips repeatedly → Pride/Quantum
   provider.
5. **Joystick** fully connected to the power module (and the cable not
   frayed or pinched).
6. **Measure the batteries** at their terminals: about 12V each, 24V for
   the pair.
   - **Near zero** (a PMS job read 4V each): the Pride charger **won't
     start on batteries discharged to nearly zero volts**, so plugging in
     won't fix it, and deep discharge can damage them permanently.
     Replace them (**always both**, [[Mobility-Batteries]]), then find out
     why they ran down: charging habits, storage, a wall-switched outlet,
     the charger. See [[2026-09-25 Q6-Edge-3 iLevel no power]].
   - **Lithium near 0 V** (Go-Go Endurance, Jazzy EVO 613 Li, Pursuit 2,
     Bandit) may be **sleep mode**, not dead: wake it per the device's
     instructions, charge, then check against Pride's minimum voltage.
     **Never load-test lithium**
     ([[Lithium Battery Field Inspection Instructions]]).
7. **Lead-acid state of charge** (Pride's 2004 Battery Guide, at rest
   3 h): 12.8 V = full, 12.5 = 75%, 12.2 = 50%, 12.0 = 25%, 11.8 =
   empty, per battery. Then **load-test**: 50 A or more for 10 s on a
   charged battery ([[Mobility-Batteries]]).

**Voltage walk (Pride TTGs).** Batteries good but still dead: meter
from the joystick outward, all with the chair switched on.
1. **Charger socket on the joystick**, pins 1 (B+) and 2 (B−): about
   **25 V** → replace the joystick; **under 18 V** (not 0) → charge the
   batteries; **0 V** → keep going.
2. **Battery harnesses** (front and rear, at the battery cable): 0 V at
   both ends → batteries; voltage at the battery but not the plug →
   that harness.
3. **Circuit breaker**: under 1 Ω good, open → breaker. **J6:** the
   battery/breaker harness must run from **+ of one battery to − of the
   other**; wired wrong, the chair won't power up and the breaker trips.
4. **Power module bus port**, then the **bus cable extension** and
   **bus cable** (pins 1 and 4 on the Q-Logic/NE bus connectors; on the
   Jazzy 614, pins 1–4 at the power module and 2–3 along the Dynamic
   bus cable): voltage in but not out → that cable; voltage
   at the joystick end → joystick.

## 3. Powers on, won't drive

- **Freewheel levers:** both must be in **drive** (pulled up on the Q6
  Edge 3 Stretto). On PG chairs a released brake shows as **9 flashes**
  (GC3: "ensure both freewheel levers are in drive mode"); Dynamic 5/6. In freewheel the brakes are released. Q-Logic 3's
  brake errors (#3/#4, #25/#26) say to disengage and re-engage the lever,
  so a half-set lever is worth checking first.
- **Charger plugged in:** charging inhibits driving (legacy Q-Logic code
  107; VR2 6 flashes; GC3 left-to-right scroll; Dynamic left-to-right
  ripple). On Q-Logic 3, a charger still connected to the controller but not
  the wall gives **"Chair is not charging"** (#75): unplug the charger
  from the controller and power-cycle.
- **Joystick held at power-up:** release it to center, power off and on
  (legacy 36/110; Q-Logic 3 #34/#35).
- **Seat tilted, reclined or elevated:** power seating limits or blocks
  driving. On Q-Logic 3 the **Drive/Function Inhibit light** shows it:
  green = OK, **red = full drive lockout**. Bring the seat back toward
  neutral. iLevel chairs also lock driving when elevated past their
  thresholds ([[Tru-Balance-3-Power-Positioning]]). The inhibits are
  factory set; don't bypass them.
- **Charger inhibit with no charger plugged in** (legacy Q-Logic
  **#107**, NE/NE+ "Battery Charging or Drive Inhibit"; Dynamic:
  left-to-right ripple alternating with steady): an **open in the
  inhibit circuit**. Pride's jumper tests (Q6 Edge and J6 TTGs), chair
  off between tests:
  1. Seat module or run plug on a **PTO harness with a round 4-pin
     barrel**: unplug it and jumper **pin 3 to pin 4**. Drives → replace
     the run plug (or see that seating system's guide). **Never jumper
     pins 1–2**: it sparks and blows the harness fuse.
  2. Unplug the PTO harness or **14-pin run plug** at the power module
     and jumper the module socket: **NE pin 4–6; NE+ or Q-Logic pin
     1–9.** Wrong pins can damage the electronics. Drives → replace the
     PTO harness or run plug.
  3. Still no drive: check the programming (NE `chrgInb` **ON**; NE+ /
     Q-Logic Inhibit **High**), else replace the power module.
  - **Jazzy 614 (Dynamic):** with nothing in the charger socket, check
    the **run plug**: pin 1–4 and pin 3–4 under 1 Ω, else replace it;
    both good → joystick.
  - **Q6 Edge 4:** an accent-light or backup-camera module connector
    not fully latched gives a drive inhibit
    ([[Pride-Parts-Replacement]]).
- **Controller locked:** "Lock" on the display. Unlock: power on, push the
  joystick full forward, then full reverse (legacy Q-Logic; Q-Logic 3 has
  the same option if it's been programmed). **NE** shows a key icon on
  the LCD, **NE+** a key icon right of the battery gauge, **Q-Logic**
  "System Lock": same unlock (full forward to a beep, full back to a
  beep). Dynamic (Jazzy): right-to-left ripple, **horn twice** within
  about 10 s.
- **Suspension lock** (Q-Logic 3 #47): get to level ground.
- Still nothing → read the error code (§7).

## 4. Short range (doesn't go as far on a charge)

From Pride's checklist:
- **Battery age:** over a year old may be worn out.
- **Charging habits:** daily users charge **overnight, 8–14 hours**.
  Unused chairs still need a charge **at least weekly for 12–14 hours**.
  Constant undercharging, or running the meter all the way down,
  shortens battery life. **Never fully deplete them.**
- **Wall-switched outlet:** the switch may be off overnight.
- **Extension cord:** Pride prohibits them for charging; plug straight
  into a proper outlet.
- **Dirty or wet batteries**, terminals or harnesses.
- **Loose battery terminals or breaker connections** (voltage loss).
- **Worn or missing motor brushes** (draw more current).

## 5. Slow, or slows to a stop

- **Speed/profile setting:** check which drive profile and speed it's in.
- **Low battery:** less voltage, slower motors.
- **Overheating (thermal rollback):** the controller cuts output when
  the motors or controller get hot: to **20%** on Q-Logic, Q-Logic 3 and
  QLNES, to **50%** on VR2 and GC3; the newVSI cuts it progressively and
  **stops the chair** at its limit. Let it cool and it recovers. Hot days, long climbs,
  stop-and-go driving and heavy bags cause it. Q-Logic 3 shows it as #32
  "Speed reduction (overtemperature)", which is normal behavior.

## 6. Pulls to one side, clicks, cuts out

- **Pulls:** joystick not pushed straight (a little sideways deflection
  adds up), **uneven tire pressure** (it pulls toward the low tire; use the
  pressure on the tire. bar = psi × 0.06895, kPa = psi × 6.89476), or a
  caster that isn't pivoting freely.
- **Single click** when the joystick first moves = the brakes releasing.
  Normal. Other clicking → check the **drive wheel lug nuts**.
- **Cuts out or powers down over bumps: a wiring problem until proven
  otherwise. Check the cable connections and routing first**, on any
  make or model, before firmware or part swaps. PMS has seen the same
  kind of issue twice (per the human): wiring routed so the connection
  is under strain, and the jolt of a bump breaks contact.
  - **Golden GA541 Avenger, PG S-Drive:** the wires pull on the S-Drive
    connectors (design flaw) and work them loose; unplug and reseat
    ([[2026-09-30 GA541-Avenger S-Drive loose connectors]]).
  - **Pride Q6 Edge HD, Q-Logic 3:** a bus cable coiled around the rear
    lower body panel pulled on its connection; the controller logged "joystick out of center"
    and stopped the chair. Rerouting took 10 minutes; the firmware
    update tried first took over an hour and didn't help
    ([[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]]).
  - Also check the battery terminals and the joystick cable.
- **Breaker keeps tripping:** heavy strain (overload, climbing). Rest a
  minute and reset. Repeated trips → provider.

## 6a. Motor, brake and cable checks (meter)

From Pride's technical troubleshooting guides. Power off and unplug the
motor harness at the power module (and at the motor, to split motor
from harness).

| Check | Q6 Edge (NE/NE+/Q-Logic) | J6 (NE/NE+/Q-Logic) | Jazzy 614 (Dynamic) |
|---|---|---|---|
| Motor (armature through brushes) | 0.5–1.5 Ω | 0.5–1.5 Ω (red–black pins) | 0.5–1.5 Ω (pins 1–2) |
| Park brake | **about 80 Ω** | **about 60 Ω** (two white pins) | **about 35 Ω** (pins 3–4) |
| Motor brushes | replace if under **0.25 in** or damaged | same | — |
| Bus cable, extension, multiplier | under 1 Ω each pin | same | same |
| Circuit breaker | under 1 Ω | under 1 Ω | about 1 Ω or less |

Motor reads wrong → pull the brushes; brushes fine → motor. Motor and
brake read right at the plug → power module. Brake values differ by
chair, so use the column for the chair (Golden's Shark guide gives
40–80 Ω, [[Shark-Diagnostics]]). Freewheel levers in drive before any
brake test.

## 7. Error codes: identify the controller first

The **controller**, not the brand or model name, decides which table
applies. Codes from one family mean something else on another.

**Pride/Quantum Q-Logic 3 / 3e** (display hand control; an option on
the Q6 Edge 3 Stretto, Edge 4, Edge 2.0, Edge HD, J4E, 4Front 2, R-Trak
and Q1450). Messages are Information, Warning or Error, shown by
number:

| # | Meaning | Fix |
|---|---|---|
| 1 / 2 | Motor 1 / 2 not connected | Power off, inspect motor connections, power on |
| 3 / 4 | Brake 1 / 2 not connected | Power off, **disengage and re-engage the brake (freewheel) lever**, inspect motor connections |
| 20 | Undervoltage | Charge |
| 21 | Overvoltage | Check battery voltage (overcharged?). Avoid fast downhill driving on full batteries |
| 23 / 24 | Motor 1 / 2 output defect | Power off, inspect motor connections |
| 25 / 26 | Brake 1 / 2 error | As 3 / 4 |
| 32 | Speed reduction (overtemperature) | Let it cool. Normal |
| 34 / 35 | Joystick not centered / out of center at power-up | Power off, release joystick, power on |
| 46 | Bluetooth not working | Power off, wait 5 s, power on |
| 47 | Suspension lock not engaged | Seek level ground; check the suspension lock |
| 75 | Chair is not charging (charger plugged into controller, not the wall) | Unplug charger from controller, power-cycle |
| 174 | Invalid memory (seat) position | Bring the seat out of anterior tilt and retry; reset the memory position |

Q-Logic 3 battery meter: green about 100–50%, yellow 49–25%, red 24–0%,
with optional pop-ups at 50/30/15%. Providers can read the **error
history** with Econ-W or the hand-held programmer
([[Q-Logic 3 Programming Guide]]).

**Codes 32–36 are numbered differently** in Pride's 2025 Q-Logic 3
fault list (32 overtemperature stop, 33 speed reduction, 34 bus voltage,
35/36 joystick). Go by the text on the display.
**Full Q-Logic 3 list (about 1–221, incl. TRU-Balance 4 seat codes):**
[[Q-Logic-Fault-Codes]].

**Pride/Quantum QLNES** (2024+, LED-only joystick; most new Q6 Edge,
J4, 4Front 2, R-Trak): Q-Logic 3 numbers, blinked as three digits
(red = hundreds, yellow = tens, green = ones; #208 = red 2, green 8).
Power-cycle to see the next fault. [[Q-Logic-Fault-Codes]].

**Pride PG Drives VR2 / GC3 / newVSI** (Jazzy Air, Go Chair, EVO 613,
Elite ES, Select, Jazzy 1450, Q1450 VR2 option): battery-meter flashes
1–10 (1 battery, 2–5 motors, 6 charger inhibit, 7 joystick, 8 control
system, 9 park brake, 10 overvoltage). **Pride Dynamic** (Jazzy 614 /
614 HD, EVO 614/614HD, Elite 14, 600 ES, Elite HD): service indicator
1–11. [[Pride-Controller-Flash-Codes]]; dealer steps per code on
[[Jazzy-614]].

**Pride/Quantum Q-Logic (legacy):** full table on
[[Joystick-Controllers]]; full 1–245 list on [[Q-Logic-Fault-Codes]]. Note the overlap: **legacy #75 = motor
disconnected, Q-Logic 3 #75 = not charging; legacy #35 = joystick
connection fault, Q-Logic 3 #35 = joystick out of center.** Check which
controller it is before acting on a number.

**Pride NE / NE+ electronics** (original [[Q6-Edge]]; the 2025 chart
still lists them on the J6 and Edge HD): the LCD shows an icon and a
text message; read details with a **Curtis handheld programmer**
(Diagnostics → Actual Faults, or Fault History for past faults). From
the Q6 Edge and J6 TTGs:

| LCD message | Do |
|---|---|
| Power Section Error | Power-cycle; check power module and joystick connections and wiring |
| Joystick Not Centered / Out of Center | Release to center, power off and on, check connections |
| Communication(s) Error | Joystick cable and bus connections |
| Motor/Brake Error | Freewheel levers in drive; brake resistance (§6a) |
| Open Motor (Error/Warning) | Motor connections and resistance (§6a) |
| Low Battery / Low Battery Voltage | Charge; low-battery walk (§2, §8) |
| High Battery Voltage | Disconnect the charger; call Quantum |
| Drive Thermal Warning | Let the motors cool |
| Battery Charging or Drive Inhibit (joystick on or off) | Unplug the charger; else the inhibit tests (§3) |
| Drive Inhibit | Power module connections (§3) |
| Speed Limit Warning (NE+) | Seat back to upright/normal |
| Idle Mode (NE+) | Power-cycle |
| Attendant Control Error (NE+) | Attendant control connections |
| System Lock Mode (NE+) / key icon | Unlock (§3) |
| Missing or defective module | Check connections; if removed on purpose, **Save System Configuration** on the programmer |

The same guides' **legacy Q-Logic** table: #1–6 software, #19 / #23
communication (check bus cables; unplug devices one at a time), #36
not centered, #37 joystick connection, #38 out of range (calibrate),
#105 low battery, #192 / #193 motor disconnected, #203 / #204 brake
disconnected, #229 module missing ([[Q-Logic-Fault-Codes]]).

**Pride scooters, beep codes** (Elite Traveller / Plus / Plus HD,
2008 sheet; check the scooter's own manual for newer models):
2 battery low (charge), 3 battery high, 5 brake trip (freewheel lever
to drive, restart), 6 throttle pressed at key-on (release, reinsert key),
7 throttle or speed pot fault, 8 motor disconnected, 9 controller trip
(battery pack installed with the key in, or hot; wait, reinsert the
key). Won't move after a long idle = **power-down timer** (remove and
reinsert the key). [[Elite-Traveller]].

**Remote look first (Q-Logic 3, QLNES):** with **Interactive Assist**
the provider can read the error list, battery statistics and live values
over the user's phone before a visit
([[Q-Logic-3-Bluetooth-and-Remote-Programming]]).

Any code not listed, or one that comes back after the fix → Pride/Quantum
provider support.

**Golden** (and other brands):

| Controller | Seen on | Page |
|---|---|---|
| Dynamics R-Series (flash/beep, 9 codes) | Companion, LiteRider, Buzzaround XL/EX/Carry On, LiteRider Mini | [[Flash-Beep-Diagnostics]] |
| PG S-Drive (beeps) | GB106, Patriot, Eagle | [[S-Drive-Beep-Codes]] |
| PG S-Drive / VR2 (TruCharge 10-bar) | GA541 Avenger, GP160, GP162 PTC, GP204/215, GP205 | [[TruCharge-Diagnostics]] |
| PG programmer trip codes | PG S-Drive, VR2, VSI, Pilot+ | [[PG-Drives-Trip-Codes]] |
| Dynamic Shark (11 codes) | GP620, older GP605 | [[Shark-Diagnostics]] |
| Dynamic LiNX (7 codes) | GP162 LiNX, 2017 GP605, GP302B | [[LiNX-Diagnostics]] |
| Micon (beeps) | GP302 Cricket | [[GP302-Cricket]] |

## 8. Charging

- Use the **supplied off-board charger**, never an automotive charger.
  Plug straight into the wall.
- **Pride** charging time: 8–14 hours from depleted.
- **Charger limits** through the 3-pin socket: 8 A (VR2, Dynamic,
  Q-Logic, QLNES), 12 A (newVSI), **Neutrik NC3MX plugs only**. QLNES has
  an XLR and a magnetic port: **never two chargers at once**.
- **GC3 charge reminder:** left red LED flashes 4 times at power-down
  after 8+ hours of driving without a charge. Clear it by switching the
  controller **on before** plugging in and leaving it on for a full
  charge ([[Pride-Controller-Flash-Codes]]).
- **Lithium:** charge fully, then compare with Pride's minimum (19.6–30
  V by model). Don't load-test ([[Mobility-Batteries]]).
- **When the call is "batteries won't charge", check the charger too.** A
  Golden charger stayed green and never charged
  ([[2026-10-05 GP162 bad charger stays green]]). Pride charger LEDs by
  part number: [[Battery-Charger-LED-Diagnostics]]. Pride's output
  test: charger in the wall, unplug its 3-pin DC harness, **25–30 VDC**
  across the two outside pins.
- **Low-battery walk (Pride TTGs):** joystick charger socket over 16–18 V
  → plug the charger in and read its lights (charging → charge 8–14 h;
  powered but not charging → charger); no lights → **about 120 VAC** at
  the outlet and at the charger cord. Battery voltage the same at the
  batteries as at the joystick → **too low for the off-board charger**:
  take the batteries to the shop to charge and load-test.
- Batteries near zero won't wake a Pride charger (§2).
- Always replace **both** batteries, matched type, chemistry and Ah (Pride
  requires it too). Battery cross-reference: [[Mobility-Batteries]].
  Golden chargers: [[Golden-Battery-Charging]].

## Field notes

- [[2026-09-25 Q6-Edge-3 iLevel no power]]: completely dark; 4V per
  battery; replaced both; frayed joystick cable and joystick replaced.
- [[2026-10-05 GP162 bad charger stays green]]: won't hold a charge with
  new batteries; the charger was bad.
- [[2026-09-30 GA541-Avenger S-Drive loose connectors]]: loses power over
  bumps; S-Drive connectors work loose.
- [[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]]: Q6 Edge HD stops, then powers down, over bumps; "joystick out of
  center" in the log; a bus cable coiled around the rear lower body
  panel; rerouted. Not make-specific.

## See also

[[Troubleshooting]], [[Joystick-Controllers]], [[Q-Logic-Fault-Codes]],
[[Pride-Controller-Flash-Codes]], [[Pride-Power-Chair-Lineup]],
[[Q6 Edge Basic Troubleshooting]],
[[Q6-Edge]], [[Q6-Edge-3-Stretto]], [[J6]], [[Jazzy-614]],
[[Elite-Traveller]], [[Tru-Balance-3-Power-Positioning]],
[[Tru-Balance-4-Power-Positioning]], [[Pride-Parts-Replacement]],
[[Battery-Charger-LED-Diagnostics]], [[Mobility-Batteries]],
[[Brake-Replacement]], [[Scootaround-VA-Repairs]]
