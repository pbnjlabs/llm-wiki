---
type: concept
tags: [stairlift, troubleshooting, diagnostics, bruno, harmar, techmate]
---

# Stairlift Troubleshooting

A symptom-first guide for stairlifts. Start with what the lift does,
not with which manual to open. The Bruno steps are condensed from Bruno's
dealer troubleshooter, [[TechMate Stairlift Troubleshooter]] (SRE-3050,
SRE-3000, SRE-2010, CRE-2110, SRE-5000), checked against the Bruno tech
support guides. Bruno's older dealer-portal **tech tips** (2013–2020) fill
in some steps; they're marked "tech tip" below and rank with TechMate,
below the manuals. Where Harmar's manuals cover the same symptom, it's noted.
For the general method behind this page, and for other equipment, see
[[Troubleshooting]].

**Names used below:** *Elan* = [[SRE-3050]] / [[SRE-3000]]. *Elite* =
[[SRE-2010]] family. *CRE* = [[CRE-2110]] family. *SRE-5000* = Bruno's
newest straight stairlift (no manual on file). Elite and CRE have a code
display under the seat; Elan and SRE-5000 talk in beeps only.

Bruno Technical Service: **1-800-656-0552**.

## 1. Triage: four questions, in order

TechMate starts every stairlift the same way. It's worth copying for any
make, because the answers sort the problem before anything is opened up.

1. **Where's the carriage?** Top, bottom, between landings, or mid-park.
   Many codes are normal at one end (see L2/L3 below).
2. **Is it beeping or showing a code with no one touching it?** Elite/CRE:
   read the display under the seat ([[Diagnostic-Codes]]). Elan: count the
   beeps (table in section 2). Harmar: [[Harmar-Stairlift-Beep-Codes]].
3. **Rocker switch, both directions.** Runs left only, right only, both,
   or neither?
4. **Each remote separately, up and down.** Same four answers, plus "no
   remote".

How to read the answers:

| Rocker | Remotes | Points to |
|---|---|---|
| Both ways | Both work both ways | Drive side is fine; go to "Runs, but…" (section 9) |
| Both ways | Neither works | Remote side (section 7) |
| Neither | Both work | Rocker circuit (section 6) |
| Both ways | One works, one doesn't | That one remote |
| One way only | Same direction only | Something stops one direction: section 4 |
| Neither | Neither, no response at all | Power (section 3) |

When it won't go in a direction, give it a command that way and note the
response: **click**, **one beep**, **3 / 4 / 5 short beeps**, or
**nothing**. Each one is its own branch below.

## 2. Bruno beep and code meanings

| Elan / Elite beeps | Elite/CRE display | Meaning | Go to |
|---|---|---|---|
| 1 chirp at power-up | | Normal power-up | — |
| Chirp on command | L2 / L3 | Safety or limit open in that direction | §4 |
| Chirp every 3 s | L1 | Seat not in riding position (seat safety switch) | §5 |
| 3 short | d5 | Over-temperature (board) | §8 |
| 4 short | d4 | Over-current, usually **brake not releasing** | §8 |
| 5 short | d7 | Low voltage stop (~16VDC, or drops under load) | §8 |
| 3 short + 2 long | C4 | Parked, charger not detected | §10 |
| 4 short + 1 long | C3 | Not parked and not charging (end-of-rail-charge units only) | §10 |
| 2 short, 3 long (5 beeps) | C5 | Battery voltage critical | §10 |
| 2 beeps, pause, 5 beeps | | Switch held at power-up (long beeps = which: 1–2 rocker, 3 learn/erase, 4–5 remote) | §3 |
| 2 beeps, pause, 3 beeps | | Multiple buttons pressed | §3 |
| | d8 | Remote not programmed | §7 |
| | P0 | Rail/fold board lost communication | §11 |
| | F code | Board failure (F2 = safety relay shorted) | replace board |

An **Elan never gives 4 short + 1 long**. It charges anywhere on the rail.
If you think you hear it, recount.

**TechMate vs the manual:** TechMate labels d6 as over-current. The
SRE-2010 manual's table says over-current is **d4** and d6 is "speed
override on high temperature". Use the manual. See [[Diagnostic-Codes]].

**SRE-5000 beep codes** (C = chirp, B = beep, L = long tone):

| Sequence | Meaning |
|---|---|
| C-L (1S1L) | All 3 terminal switches open: failure state. Check the switch wires under the battery cover |
| C-C-L (2S1L) | Upper **and** lower safety flaps/footrest pan both open: look for something pressing them, then call Bruno |
| C-C-C-L (3S1L) | Final limit: over-travelled at the top. Crank it downhill off the end plate, then call Bruno |
| B-B-L-L (2S2L) | Battery below 19.2V sitting |
| B-B-B-L-L (3S2L) | Charger not detected |
| C-C (2S) | Safety relay failed: call Bruno |
| C-C-C (3S) | CPU over-temperature |
| C-C-C-C (4S) | Over-current |
| C-C-C-C-C (5S) | Voltage dropped below 19.2V while running |

**Harmar** uses a different scheme (beeps counted after the power-up
beep: 1 runaway, 2 no power, 3–6 conflicting footrest/obstruction, 7–8
stop up/down, 9 final limit). See [[Harmar-Stairlift-Beep-Codes]].

## 3. No response at all / no startup beep

Power cycle at the circuit breaker first. It should **click and beep
once**.

- **Beeps twice** → seat safety (§5).
- **Odd sequence** (2 beeps, pause, 5) → a switch is held at power-up.
  Long beeps 1–2: unplug the rocker from the board and retest (still
  there → board). Beep 3: learn/erase button stuck; unstick it. Beeps
  4–5: check for a stuck remote button and unplug the IR harnesses.
- **No beep:**
  1. **Final limit** (roller switch, back of the carriage near the
     bottom). Depressed = no power at all. Find what's pressing it.
  2. **Overspeed** tripped? Reset it ([[Overspeed-Safety-Brake]]). CRE:
     TechMate says it's tripped when the hole isn't centered in the
     notch, and resets it by removing the black cap and cranking
     counter-clockwise (5/16" or 8 mm socket) until the hole centers.
     The CRE install manual uses a two-lever reset instead (see
     [[CRE-2110]]). Follow the manual if they disagree.
  3. **Fuse on the main board**: continuity across it. Blows again →
     §12.
  4. **In-line fuse** on the B− (black) battery wire. Before replacing a
     blown one, unplug B+/B− at the board and check red to black for a
     short (see §12).
  5. **Batteries**: each one 8VDC or less = replace (both).
     Across both (red on battery 1 to black on battery 2, never on the
     gray jumper terminals) should be 24VDC. Good singly but not
     together = gray jumper; re-crimp or replace.
  6. **Voltage walk**, using battery B− as ground: board B+/B− (breaker
     on) → both sides of the breaker → both sides of the final limit →
     both sides of the overspeed switch. "One side only" = that part is
     bad. "Neither side" = the wire feeding it. Overspeed switch bad with
     the switch not pressed → **carriage replacement** (not sold
     separately).
  7. Voltage at the board but still dead → unplug the IR sensors (one
     bad sensor can stop power-up), then all harnesses except B+/B−.
     Powers up bare → plug back one at a time. Still dead → board.

- **CRE dead at the top** (no lights, no B+/B−): the **final limit** is
  sitting on its ramp. Move the end bracket / charge contacts back so the
  end limit trips first (tech tip,
  [[Tech Tip - CRE-2110 Final Limit and End Limit Adjustment]]).
- The board needs **18 VDC or more** at B+/B− to run (Elite and Elan tech
  tips). Elan: at least **23 V to go up and 21 V to go down**; it cuts
  out under load at about 16 V.

Harmar equivalent: 2 beeps = no 12V power on board, 9 = final limit
([[Harmar-Stairlift-Beep-Codes]]).

## 4. Won't go one way: single beep (or L2/L3)

One beep on command means a **safety or limit circuit is open** in that
direction. The command itself is getting through.

- **At the end of the rail, commanding further that way** → one beep is
  normal.
- **Elite/CRE display:** L2 = upper limit circuit open, L3 = lower.
  At the top, L2 is normal and L3 is what stops it going down (and the
  reverse at the bottom). **L2 at the bottom or L3 at the top = the hand
  is set wrong** (CRE: DIP switch 3 on the diagnostic board, ON = right
  hand).
- **Key switch** (SRE-3000, Elite, CRE): turn it 90°. Off makes the unit
  beep on command in both directions. Still no: jump the key switch
  2-pin (double black) at the board. Runs → key switch or its harness.
  **SRE-3050** has the 2-pin too but it should have a **factory jumper**
  in it. Check the jumper is there.
- **Limit circuit test** (Elan videos and Elite videos in TechMate):
  - Wires: a 3-pin **red / green / black** limit harness (green in the
    middle). Red = one direction, green = the other; which is "up"
    depends on the hand.
  - Check continuity on the open color. Open → plug in the **footrest
    installation jumper**. Runs → the footrest circuit (switches,
    harness, or a switch held in by the safety pan; bend the pan tabs).
  - Still beeps → pull the **safety flap / cover** on that side. Runs →
    covers on too tight; refit loose. Elite/CRE: also bend the two
    **shroud limit tabs** under the carriage out.
  - Still beeps → unplug the 3-pin at the board and **jump all three
    pins**. Runs → board is fine; harness or limits. Still beeps →
    unplug the communication 3-pin (§11). Still beeps → jump the seat
    safety (brown/white) at the board. Still beeps → board.
- **SRE-5000** uses **three terminal switches** on the back of the
  carriage (4-pin harness: green, white, red, black). Normally 2 of the 3
  are open when parked at an end or mid-park. Green–black and red–black
  are the two ends, white–black the mid-park. Wiring under the battery
  cover, left to right from the back: green/black, white/black,
  red/black. All three open anywhere = wiring fault, call Bruno.

Harmar: beeps 3–8 are conflicting footrest/obstruction/stop switches
([[Harmar-Stairlift-Beep-Codes]]).

## 5. Seat safety: chirp every 3 s, L1, or two beeps at power-up

The unit thinks the seat is swivelled. In multi-user mode it
chirps every 3 seconds when the seat isn't locked in the riding
position. That's normal until it's swivelled back.

1. Swivel to the riding position and lock it. Still beeping → the
   switch, or the cam it rides on, needs adjusting.
2. Brown and white wires on the switch terminals? Reconnect if not.
3. Jump brown to white **at the board**. Elan: the 5-pin (red, black,
   green, brown, white). Elite: the 2-pin (brown, white). Still beeping
   → board.
4. Plug back in and fit the **installation jumper** (Elan 8-pin, Elite
   6-pin). Stops → the fault is past the jumper; jump brown/white at the
   switch itself. Stops → switch. Doesn't → harness from the jumper plug
   to the switch. Still beeping with the jumper → harness from the board
   to that plug.

## 6. Rocker doesn't work, remotes do

Jump black to red and black to green at each point, working out from the
board:

1. **Board header** (harness unplugged). No response → unplug the key
   switch and limit harnesses and retry (a short there can block it).
   Still nothing → board.
2. **Back of the board connector** (harness plugged in). No response →
   short in the rocker harness (§12).
3. **3-pin under the seat**. No response → harness from board to seat.
4. **At the rocker switch**. Runs → **rocker switch**. Doesn't → the
   harness through the armrest.

A rocker that sticks (keeps running, or has to be re-centered to stop) →
replace the rocker switch assembly. On the SRE-3050 that's
**SRV-3050-025**; return the old one.

## 7. Remotes

1. **Does the remote light up green** when a button is pressed? No →
   new batteries (TechMate's RF remote notes say a good battery reads
   about 9VDC).
2. **Is it sending?** Point an IR remote at a **phone camera** (selfie
   camera works). A purplish light at the tip = transmitting. Green light
   but no IR → remote.
3. **d8 on the display** = remote not programmed. Erase: hold
   LEARN/ERASE until the board LED goes out (about 9–12 s). Program: hold
   LEARN/ERASE and press up or down on the remote; the LED goes out in a
   second or two. Repeat for the second remote. DIP switches on both
   remotes must match and sit fully up or down.
4. **IR sensors:** one bad sensor or harness can block both. Unplug one
   at the board and test, then swap. The sensor plug should read **5VDC**
   red to black. None at the plug or at the header pins → board.
5. **RF (2.4 GHz) units**, both remotes dead with fresh batteries: unplug
   the **antenna coax** from the board (carefully). Remotes work without
   it (short range) → shorted antenna wire. Internal Bruno notes for
   CRE/SRE-2010E double failures: power-cycle and wait 60 s; repeat
   failures → newer remote CRE-01065 (replaces SRE-00947); outdoor units
   have no new remote, so board SRV-2010-007. Antenna parts SRE-20778 +
   ANT-00109.
6. **One IR call station flaky** (SRE-3000 tech tip): **unplug the IR
   sensor at the opposite end** of the carriage. Now works → a reflected
   signal was interfering, not a bad part
   ([[Tech Tip - SRE-3000 IR Call-Send Interference]]).
7. **RF remotes eating batteries** (tech tip): high-power X-Bee Pro
   remotes make it worse, not better. The 9 V works down to 4 V; use good
   alkalines; replace yearly. Good battery but only a re-seat brings it
   back → the battery contacts. Remotes time out after **3 minutes** of a
   held button ([[Tech Tip - Stairlift RF Remote Battery Issues]]).
8. **Stops intermittently on the remote with no beep** = interference.
   Does the remote's green light go out when it stops? Yes → remote.
   Otherwise look for sources: IR (IR smoke or motion detectors, alarm
   sensors, robot vacuums, CFL bulbs, sunlight, TV boxes, garage door
   sensors) or RF 2.4 GHz (routers, wireless devices, smart TVs; metal,
   stone and concrete between remote and lift). Does the failure follow
   the remote, the remote's location, or the carriage position? That
   tells you remote vs interference vs range.

**CRE IR repeater ("puck") system:** receivers plug into a wall outlet
(non-switched 120VAC) and relay to an **emitter** on the upper battery in
the carriage. Each blinks blue once on power-up and stays lit while a
remote button is held.
- Remote works pointed straight at the carriage sensor but not through a
  receiver → receiver (power, or channel).
- **Channels:** the dial on every receiver and the emitter must show the
  same number (white plastic screw).
- Emitter dark → check 5VDC on its plug (red/black on a 3-pin with 2
  wires). Lights on wall power but not on the carriage → emitter power
  harness.
- Check nothing blocks the eye of the emitter extension harness.
- Bruno's install training: Brainshark, "Installation of IR Receivers
  for CRE".

## 8. Click only, or stops with 3, 4 or 5 short beeps

**Click, no run, no beep.** Hold the command: any beeps after the click?
Follow those. None → press a limit or footrest safety by hand and command
that way. No beep even then → call Bruno. Beeps → the relays are working;
unplug the motor leads at the board and read them on a command (about
24VDC, or 17VDC). Nothing → board. Voltage → motor: **Elan, replace the
motor**; **Elite/CRE, replace the brushes**.

The tech tips give the motor-lead numbers by direction, with the
batteries resting at 25 V or more: **Elan (blue/brown) 23–24 V up,
12–13 V down**; **Elite (blue/orange) about 21 V up, 12 V or more down**.
Lower than that → board. Direct power to an Elan motor only very briefly
(the brake overheats). TechMate's "about 24 or 17 VDC" is the same idea
in round numbers.

**3 short (d5), over-temperature.** If it has ever given 4 short too,
treat it as over-current (below). Only ever 3 short → board.

**4 short (d4), over-current.** The motor is trying but can't move. The
usual cause is a **brake that isn't releasing**.
1. Take the brake off the motor and run it.
   - **Runs:** with a command, read the brake terminals at the board (about
     24VDC; the SRE-3050 guide says at least 22VDC). No voltage → board.
     Voltage present: Elan/SRE-5000, feel for the brake **click** on
     command. No click → follow the brake wires. On some units one runs
     through the **circuit breaker's aux contacts**, which should be on
     **NO and COMM** and close when the unit is on. Wire the brake
     straight to the board to test. Runs → breaker aux switch or that
     wiring. Clicks but drags → brake.
   - **Still won't run:** unplug the motor leads and command it. Still 4
     beeps → board. Only clicks → try **cranking it manually**. Won't
     crank → gearbox (carriage). Cranks, and runs after → the overspeed
     may have been set mechanically without tripping the switch. Trips
     again → overspeed (carriage).
2. **Elite/CRE brake:** TechMate disagrees with itself on whether the
   brake can be replaced alone. Confirm with Bruno before ordering.
   (The **SRE-3000 Elan** brake has its own kit, **SRV-3000-016**:
   [[Tech Tip - SRE-3000 Elan Brake Replacement (ILS-01324)]].)

See also the SRE-3050/SRE-3000 brake procedure on [[SRE-3050]].

**5 short (d7), low voltage stop.** Batteries near 16VDC (SRE-5000:
19.2V), or dropping under load.
1. Unplug the charger. Read the charge strips (or the batteries):
   - **Faults with no command** and reads 16V or less → is the charger
     showing yellow/green (charging)? Yes → batteries. No → §10.
   - **Faults only with a command** → watch the voltage while running.
     **Drops more than 4VDC** → batteries (always replace both, see
     [[Mobility-Batteries]]). Doesn't drop → board, confirm with Bruno.
2. Still 5 short with new batteries (TechMate's "deep dive"): read under
   load at each point. Across both batteries drops but each alone doesn't
   → **gray jumper** between them. Steady at the batteries but drops at
   board B+/B− → test B− (board B− to battery 1 +): drops → B− harness.
   Then walk the + side under load: breaker → final limit → overspeed →
   board. The part where it drops is the bad one.

## 9. Runs both ways, but…

**Runs slow:** Elan/Elite/CRE → the slowdown/communication circuit (§11).
SRE-5000 → a **terminal switch held open** (any one open = slow), or a
voltage drop over 4V under load (batteries), or a dragging brake.

**Noises:**

| Noise | Likely cause / fix |
|---|---|
| Clicking | Drive adjustment (pinion to rack). Elan: a guide block in the carriage can be in backwards; flip it so the arrow points up |
| Grinding | Gearbox (call Bruno). CRE: first check the carriage isn't rubbing the rail, i.e. gear on the rack flange (ride-out adjustment) or guides/rollers out of place |
| Screeching | Charge fingers pressing too hard (pull the charge block; quiet → round off or replace fingers/block), or a dragging brake (§8) |
| Whining | Bad motor or low power to it: call Bruno |
| Rattling / popping | Loose gear rack (tension bolts, or add rack) or drive adjustment |
| Rhythmic thump, about every 6 in | Flat spot on a roller: replace rollers |
| Clunk only at a joint | Adjust the rail joint |
| Clunk all the way | Drive adjustment |
| Vibration, loose carriage (SRE-3000) | Tech tip: loosen the three motor bolts, set screw ¼ turn left, run 6 in each way, torque **20 ft-lb (27 Nm)** ([[Tech Tip - SRE-3000 Drive Adjustment]]) |
| CRE kicks out / climbs the rack on inside turns (**ride-out**) | Press on the footrest while it runs: goes away → fine. Check paint in the rack, the downside nylon guide, the business-card gap. Fix: gear-motor tension screw out ½ turn, then ¼ ([[Tech Tip - CRE Ride-Out]]) |
| Elan binds at the fold only with a heavy rider | Lower end cap not on the floor, so the rail twists ([[Tech Tip - SRE-3000 Folding Rail Fixes]]) |
| Rumble / just noisy | Needs grease. Clean old grease and dust off the rack, then Magnalube. New installs: grease before running |

**Seat:**
- **Won't stay folded up:** SRE-3000, loose fold hardware (thread
  locker). **SRE-3050**: the **dampener cap** (SRE-30477) is off or
  missing, or the dampener (DPR-00101) is gone too. Fit the dampener
  dimple up with the seat folded at least 45°. The cap must click in on
  **both** sides; it usually pops off because one side didn't. Elite: gas
  spring.
- **Elan swivel won't lock:** missing spring or broken plastic.
- **SRE-3050 seat loose, cracked or broken:** check **Service Bulletin
  81** (SRE-3050 seats from a certain date range): either a seat
  reinforcement (metal plate) or a seat bottom replacement, both on
  Brunopartner. Bruno wants a report on any broken seat: injury,
  seatbelt worn, user weight, seat height, install date, cleaners used,
  photos of the top and bottom landings and a transfer video.
  (Customer details go to Bruno, never into the wiki.)
- **Broken wheel:** a broken wheel is replaced. A wheel **broken off the
  carriage casting** = carriage replacement, logged with Bruno as a
  safety issue (severity 3, with photos).

## 10. Not charging

First, which charger:
- **Elan / SRE-5000** (single LED): red = AC on (normal when it's not
  charging); **yellow** = charging; **green** = full/float; **flashing
  red** = batteries dead (under about 4V total) or defective; **flashing
  green** = reverse polarity; **flashing yellow and green** = bad
  connection (clean the strips, bend the block fingers down).
- **Elite / CRE** (separate red, yellow, green and blue LEDs): red on =
  AC on; red + yellow = charging; red + green = float/full; **yellow and
  green blinking alternately** = low voltage (batteries); **red and
  yellow blinking alternately** = bad batteries/sulfation; **green fast
  blink** = bad contact or partial sulfation; **blue** = battery
  connector reversed.

Then:
1. **Where can it charge?** Elan and indoor SRE-2010 are continuous
   charge (anywhere on the rail). CRE, outdoor SRE-2010 and older units
   charge only **at the ends or mid-park** (C3 / 4 short + 1 long when
   stopped elsewhere). TechMate doesn't say which the SRE-5000 is.
2. **No lights** → plugged into the wall and the rail? Outlet 120VAC?
   Charger on/off switch on? Charger input/output fuses? Then the charger.
3. **Is it actually charging?** Unplug the charger, read the charge strips
   (about 24V), plug it back in. With yellow/green showing the strips
   should rise **at least 2VDC**. (Bruno's older Elite and Elan tech tips
   say **at least 1 VDC**, and that the carriage must sit on the contacts,
   or be switched on, **3 s** before the board starts charging. Neither
   number is from a manual; under 1 V is a fail by both.)
4. **Lit but not charging:** walk the voltage from the batteries out:
   strips → charge **block** (end of rail) → carriage **fingers**. No
   voltage at the block → pull it and bend its fingers down. Still none
   → block.
5. **Reverse polarity:** test red to + and black to − at the block, then
   the strips (top strip +, bottom −). Strips right but block wrong → the
   block is on the wrong end or backwards. Strips wrong → the **carriage
   finger wires: red in the middle, black on the bottom**. Fingers right
   → board harness (3-pin) or board.

Harmar: an intermittent beep every 5 minutes means it's parked off a
charge strip ([[Harmar-Stairlift-Beep-Codes]]). VPL chargers:
[[Battery-Charger-LED-Diagnostics]].

## 11. Slowdown, mid-park and communication (P0)

The **purple / red / black 3-pin** (orange connector) on the main board
is the charging and communication circuit. It tells the carriage to
slow at the ends and stop at a folding rail's mid-park.

- **Quick test:** unplug it and power-cycle. The P0 clears, and the unit
  runs, but now **won't leave slow speed, won't charge, and won't stop at
  slowdowns or the mid-park**. If unplugging it fixes the symptom, the
  problem is in this circuit.
- **Clean the charge strips** (Bruno says Lemon Pledge on a rag).
- Fails at the **bottom only / top only / both** → the charge **block**
  at that end: remove it, bend the fingers down, refit (clamp the rack
  if the block stays on). **Mid-park failures** → usually the **top**
  block.
- **Carriage fingers** riding off-center onto the plastic: all off →
  call Bruno. One off → bent finger; replace the fingers.
- Only happens **with someone in the seat** → too much front-to-back
  play: rollers. No play → carriage fingers.

## 12. Fuse keeps blowing / short

Unplug things at the board one at a time and see which makes the short
go away: limit harness (jump its three pins: runs → harness short; no
response → board), key switch harness, rocker harness, charging harness
(5A fuse still blows with it off → unplug the power-option aux harnesses).
For the in-line battery fuse, check red to black on the B+/B− wires at
the board. Shorted only with the breaker on → wiring after the breaker.
Shorted with it off too → battery harness. Shorted on the board terminals
with every harness off → board.

## 13. Power options

**Power swivel** (at the top of the rail):
- Beeps once and never swivels → is the slowdown working at the top?
  No → communication (§11). Yes → board or actuator (Bruno).
- Stops and **reverses slightly** = pinch protection → pivot bolt nut
  too tight; loosen.
- Swivels back but won't run down → seat safety switch pressed or not
  in its notch (§5).
- Stops partway and continues when pressed again → actuator or aux
  board (Bruno).

**Power footrest:**
- No response → unplug the **double orange trigger wire** from the aux
  board and use it to trigger. Works → trigger wiring or switch. No
  response → about 24VDC into the aux board? Yes → aux board. No →
  harness from the main board.
- Clicks/ratchets, or folds then goes back → disconnect the actuator
  from the footrest plate. Actuator runs fine alone → adjust its timing
  in the slotted bracket. Still clicks alone → actuator.

**Power folding rail** (SRE-3050/SRE-2010; see [[Folding-Rail]]):
- The carriage must **always stop at the mid-park**, rail up or down,
  enabled or disabled.
- Slows but doesn't stop at the mid-park → unplug the purple/red/black
  3-pin **on the folding rail board**. Now stops → fold board. Still just
  slows → rail harness grounded.
- No response at the mid-park → about 6VDC purple to black on the
  carriage board 3-pin? Yes → fold board. No → rail harness.
- Beeps continuously (rail light flashing) but doesn't fold → the logic
  is folding but the motor isn't getting power. The motor is wired
  through the **disable switch**, so check its wiring, then 24VDC on the
  fold motor leads (yes → motor, no → board). Folds slowly at 12V → check
  the board's input under load (drops → harness; doesn't → board).
- Rail slams or bounces at the top → bend the upper limit flag out.
- **Old-style SRE-2010 rail bounces back off the floor** (tech tip):
  bumper, short end hitting the U-channel, contacts, bent pivot bar or
  rack, then the **lower actuator mounting plate** (two M6 bolts; lower
  it with gentle hand pressure, it's seated when the carriage will jog).
  Don't adjust the linkage bar
  ([[Tech Tip - SRE-2010 Power Folding Rail Bounce-Back (Old Style)]]).
  Binds at the bottom → adjust the down limit; still binds → remove the
  lower latch; then joint alignment.
- Runs up with the rail down → disable switch on (normal), or wired
  backwards.
- Rough or stuck at the joint → joint alignment or gear rack timing at
  the joint (install manuals for SRE-3050 / SRE-2010).
- Not charging below the fold → voltage on the strips below with the
  carriage above? Check the upper joint block (+ right, − left), wiring
  and fingers.
- Newer power folding rails have board **PCB-00193** and a notched down
  limit bracket ([[SRE-3050 and SRE-2010 Power Folding Rail Logic Board Update]]).

**SRE-5000 folding rail** (its own design):
- **Both fold switches pressed at once** → nothing moves. Look for
  debris.
- **Folds only at the mid-park** → the switch on the fold board is set
  to ON. Set it to "1" to fold while running with the arm switch. With a
  **remote it always folds only at the mid-park**.
- Rail up and carriage runs down without folding, or the reverse → the
  **hand** is wrong: fold board switch 2, ON = right hand.
- Won't fold, flashing red light on the main board → no power to the
  actuator; check the motor leads on the fold board.

## Field notes

None yet for stairlifts. Add them here as they come in.

## See also

[[Stairlift-Maintenance]] (yearly checklist, grease, batteries, overspeed tests),
[[Tech Tip - SRE-3000 Elan Troubleshooting Guide]],
[[Tech Tip - SRE-2010 Troubleshooting Guide (No Power Options)]],
[[Circuit-Breakers-and-Fuses]] (breaker and fuse locations, ratings and resets by unit),
[[Troubleshooting]], [[TechMate Stairlift Troubleshooter]],
[[Diagnostic-Codes]], [[Harmar-Stairlift-Beep-Codes]],
[[Overspeed-Safety-Brake]], [[Folding-Rail]], [[Mobility-Batteries]],
[[SRE-3050]], [[SRE-3000]], [[SRE-2010]], [[CRE-2110]], [[Helix]],
[[Pinnacle-SL300]], [[Pinnacle-SL600]]
