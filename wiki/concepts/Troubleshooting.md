---
type: concept
tags: [troubleshooting, diagnostics, method, index]
---

# Troubleshooting

The starting point for any "it doesn't work" call, whatever the make. It
has two parts:

1. **The method**: a way of working that applies to every manufacturer.
   It's modeled on Bruno's dealer troubleshooter
   ([[TechMate Stairlift Troubleshooter]]), whose structure works
   well beyond Bruno.
2. **A symptom index**: where the wiki has the answer for each kind of
   equipment.

Manuals still set the specs and procedures. This page helps you find the
right one faster.

## The method

TechMate asks one small question at a time, each with only a few
answers, and every answer cuts the possibilities down. The same habits
work on a Harmar lift, a Golden scooter or a Pride chair.

**1. Record the state before touching anything.** Where is the unit
(carriage at top/bottom/mid, platform up/down, chair on or off charge)?
Is it already beeping, flashing or showing a code? Many "faults" are
normal for that position. A Bruno L2 at the top of the rail is normal,
for example, and a Harmar stairlift beeps every 5 minutes when parked
off a charge strip.

**2. Try every input separately.** Rocker, then each remote, then the
call stations. Write down **which direction** works for each. When one
input works and another doesn't, the fault is in the input that failed,
not the drive. If nothing works from any input, it's power.

**3. Classify the response.** When it won't go, what does it do on
command: **click, beep (how many), run then stop, or nothing**? Each
response is a different branch. Counted beeps and flash codes go straight
to the manufacturer's table (index below).

**4. Prove power before anything else.** Does it power up (startup
beep or light)? Batteries **one at a time, then together**: each 12V
battery should read close to 12V and the pair about 24V (Bruno: 8V or
less on one battery = replace). Good one at a time but not together = the
jumper between them. Low at rest → is the
charger actually charging? Fine at rest but **drops under load** (Bruno
uses more than 4V) → batteries. **Always replace every battery in the
device** (house standard, [[Mobility-Batteries]]).

**5. Walk the voltage down the circuit.** With battery negative as
ground, read **both sides** of each part in series: breaker, fuse, final
limit, safety switch, connector, board. "Voltage on one side only" = that
part. "Neither side" = the wire feeding it.

**6. Isolate by jumping and unplugging, working outward from the board.**
Jump the input at the board header first. If it responds, the board is
good and the fault is upstream. Then jump at each connector further out
until it stops responding: the fault is between the last good point and
that one. For shorts it's the reverse: unplug harnesses one at a time
until the short (or blown fuse) goes away.

**7. Swap and compare before condemning.** Swap the two remotes, the two
receivers or the two batteries. Does the fault follow the part, its
location, or the position of the unit? That separates a bad part from
interference, wiring or a mechanical spot.

**8. "Same spot every time" vs "the whole way".** A fault at one
position is mechanical or positional: a flat spot, a joint, a dirty or
loose strip, a fascia rubbing. A fault that's slow or weak the whole way
is power or the motor/actuator. (From the Harmar J-cam field note and
TechMate's slowdown trees.)

**9. Clean, adjust and reseat before ordering parts.** TechMate fixes a
lot with "clean the strips, bend the fingers down, loosen the cover,
adjust the switch" before it ever says "replace". The same goes for
loose connectors (the GA541 S-Drive field note).

**10. Know when to stop.** If the steps lead somewhere that doesn't make
sense, or past what's safe in the field, call the manufacturer's tech
support with what you've already measured.

**When "it won't charge", check the charger** as well as the batteries
(GP162 field note): a charger can show green and never charge.

## Symptom index

### Stairlifts
- **Everything (Bruno + Harmar), symptom-first:** [[Stairlift-Troubleshooting]]
- Codes: Bruno [[Diagnostic-Codes]] (Elite/CRE display, Elan beeps),
  Harmar [[Harmar-Stairlift-Beep-Codes]]
- Overspeed reset: [[Overspeed-Safety-Brake]]
- Folding rail: [[Folding-Rail]]

### Vertical platform lifts (VPLs)
- **Everything (Bruno VPL-3100B/3200B + Harmar), symptom-first:** [[VPL-Troubleshooting]]
  (safety-chain voltage walk, gates and doors, calls, click/hum/squeal,
  runs on its own, blown fuse, noise)
- Bruno charger LEDs: [[Battery-Charger-LED-Diagnostics]]
- Door stuck locked / interlocks: [[Gate-and-Door-Interlocks]],
  [[2026-10-01 Bruno-VPL door interlock spring]]
- Squealing, jamming on the fascia: [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]
- Model pages: [[VPL-3100B]], [[VPL-3200B]], [[HighlanderII]]

### Vehicle lifts
- Stuck lifting a load at the same spot (Harmar): [[2026-10-14 Harmar-AL-Outside-Lift J-cam flat spots]]
- Can't lift the device: [[Mobility-Device-Weights]],
  [[2026-07 VSL-6000 GC440 too heavy]]
- Power/wiring: [[Vehicle-Lift-Power-Wiring]]
- Chair tips or won't dock: [[Docking-Devices]]
- Model pages: [[ASL-275]], [[ASL-700]], [[PUL-1100]], [[VSL-4400]],
  [[VSL-6000-6900]], [[AL-Series-Outside-Vehicle-Lifts]],
  [[Hybrid-Vehicle-Lifts]]

### Scooters and power chairs
- **Symptom-first (Pride detail, Golden controller index):** [[Power-Chair-Troubleshooting]]

Identify the **controller** first. It decides which code table applies,
not the brand or model name.
- Golden Dynamics R-Series (flash/beep, 9 codes): [[Flash-Beep-Diagnostics]]
- Golden PG S-Drive scooters (beeps): [[S-Drive-Beep-Codes]]
- Golden PG S-Drive/VR2 chairs (TruCharge 10-bar): [[TruCharge-Diagnostics]]
- PG Drives programmer trip codes: [[PG-Drives-Trip-Codes]]
- Dynamic Shark: [[Shark-Diagnostics]]
- Dynamic LiNX: [[LiNX-Diagnostics]]
- Pride Q-Logic / Q-Logic 3 / QLNES: [[Joystick-Controllers]],
  full code lists [[Q-Logic-Fault-Codes]],
  [[Q6 Edge Basic Troubleshooting]]
- Pride Jazzy PG VR2 / GC3 / newVSI and Dynamic (flash codes):
  [[Pride-Controller-Flash-Codes]]; which Pride chair has which
  controller: [[Pride-Power-Chair-Lineup]]
- Pride tilted chair won't drive (tilt thresholds): [[Q-Logic-Seat-Configuration]]
- Pride lithium batteries (don't load-test; sleep mode):
  [[Lithium Battery Field Inspection Instructions]]
- Charging: [[Golden-Battery-Charging]], [[Mobility-Batteries]],
  [[2026-10-05 GP162 bad charger stays green]]
- No power at all: [[2026-09-25 Q6-Edge-3 iLevel no power]]
- Loses power over bumps: [[2026-09-30 GA541-Avenger S-Drive loose connectors]]
- Brakes: [[Brake-Replacement]]

### Ceiling and patient lifts
- **Symptom-first (Prism/Handicare P440 and C-450/C-625):** [[Ceiling-Lift-Troubleshooting]]
- Won't lift: [[2026-10-01 P440 batteries no lift]] (tape the batteries
  together, replace both)
- Prism technical manual: [[C-450 C-625 Technical Manual]]

### Door operators
- [[Automatic-Door-Operators]]

## Adding to this

When a field note solves something, link it from the matching line
above as well as from its model page. When another manufacturer's manual
has a troubleshooting chart, add it here under the symptom, not just on
the model page.

## See also

[[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]], [[Power-Chair-Troubleshooting]],
[[Ceiling-Lift-Troubleshooting]], [[TechMate Stairlift Troubleshooter]],
[[TechMate VPL Troubleshooter]], [[Mobility-Batteries]], [[Joint-Commission-DMEPOS]] (maintenance and
repairs follow the manufacturer's instructions; keep repair records)
