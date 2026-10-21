---
type: concept
tags: [vpl, platform-lift, troubleshooting, diagnostics, bruno, harmar, techmate]
---

# VPL Troubleshooting

A symptom-first guide for vertical platform lifts. The Bruno steps are
condensed from Bruno's dealer troubleshooter,
[[TechMate VPL Troubleshooter]], for the [[VPL-3100B]] (VPL-3153B/3175B,
"short residential DC") and the [[VPL-3200B]] (VPL-3210B/3212B/3214B,
"tall residential"). Bruno's older dealer-portal **tech tips** add the
pre-2012 units TechMate doesn't cover, the AC board's fault codes and
the drive work ([[VPL-Drive-Service]]); they rank with TechMate, below
the manuals. Harmar notes are added where the wiki has them. For
the general method and other equipment, see [[Troubleshooting]].

Bruno Technical Service: **1-800-656-0552**. Older Bruno boards (see the
serial cutoffs on [[TechMate VPL Troubleshooter]]) go straight to Bruno.

**How a Bruno VPL decides to run:** everything is one **series safety
chain**. Battery power goes through the breaker and final limit to the
board, then through the top cover switch, E-stop and nut safety switch,
the upper gate/door, any mid-stop door, and the platform gate/lower door.
That's the **direction-independent** part: all of it must be closed
before anything moves. A call (platform control or call/send) then
connects it to the **up** side (up limit) or the **down** side (down
limit, then safety pan). The board lights its up or down LED and fires
the relay/solenoid, which runs the motor. Troubleshooting is finding the
first point in that chain where the 24VDC stops.

## 1. Triage

1. **Charger lights first** (DC units). Through the access panel: solid
   red plus yellow and/or green (steady or flashing) is normal charging.
   Red only, flashing red, or nothing → §9.
2. **Where's the platform?** Top, bottom, between landings, or about
   **2 in from a landing** (that position has its own fault, §2).
3. **Platform control, up and down.** Up only, down only, both, neither?
4. **Call/send, up and down.** Same answers.

| Platform control | Call/send | Points to |
|---|---|---|
| Both ways | Both ways | Drive side is fine: noise or stopping, §8 |
| Both ways | Neither | That call/send, §6 |
| Neither | Both ways | Platform control, §6 |
| Up only (either input) | Up only | The **down** side: down limit or safety pan, §4 |
| Down only | Down only | The **up** side: the up limit, §4 |
| Neither | Neither | Check for a click or hum (§7). Silent → quick checks (§2), then the chain (§3) |

**No call/send to compare?** Jump the rocker circuit with the
installation rocker jumper (the "run bug") on the travelling cable. Runs →
the platform control.

**Moving with nobody pressing anything** → §10, now.

## 2. Quick checks before opening the control box

- **E-stop** on the platform control pulled out.
- **Key switch** on the call/send or platform control **horizontal** (on).
- **Top cover switch:** the cover pushes it down to run. With the cover
  off it must be **pulled up until it clicks** (maintenance position).
  Won't stay up → replace the switch.
- **Upper gate wheel** (EMI gate): is the activator holding it up? A
  wheel stuck up leaves the gate unlocked and the lift stopped. Push it
  down (a broom handle works); it may just need lubricating.
- **Hold the door shut** and try down. Runs → bend the **door closed
  switch** flag out so it's pressed sooner.
- **Stuck about 2 in below the top:** the gate is unlocked but the
  **upper gate enable switch** isn't pressed. Adjust the upper gate ramp
  activator until the door locks and the lift runs off the landing,
  standing in different spots on the platform.
- **Safety pan** under the platform pressed in or skewed (stops down
  only): free it; check for corrosion or a bent pan.
- **AC models:** 120VAC at the outlet (check GFI and breaker panel).

## 3. The voltage walk (control box)

Ground the black probe on the board's ground terminal: **20** on the
VPL-3100B, **67** on the VPL-3200B. Read each point in order. The first
point without about 24VDC tells you which circuit is open. Fix it,
**re-read that point**, then carry on down the list. TechMate won't go
further until it reads good.

### VPL-3100B (short residential DC), ground = terminal 20

| Read | Good means | No voltage → |
|---|---|---|
| **VBATT LED** (red, on the board) | Batteries, breaker, upper final limit and the **3A slo-blo board fuse** are good | JP1.1 (red) to JP1.6 (brown) has 24V → replace the fuse (blows again → §11). No 24V → power walk below |
| 21 | Supply into the chain | — |
| **33** | Top cover, E-stop and nut safety switch closed | JP6.1 (red) → JP6.2 (black) = top cover (§4). Then JP3.4 (orange) → JP3.5 (brown) = E-stop/nut safety (§4). No voltage even at JP6.1 → board |
| **29** | Upper gate/door closed and locked | Upper gate (§5) |
| **25** | Platform gate/lower door closed and locked: the direction-independent chain is complete | Platform gate/lower door (§5) |
| Up: **JP3.2** (white) on command | Up call made | Up call (§6) |
| Up: **JP6.6 → JP6.5** on command | Up limit closed | Up limit (§4) |
| Down: **JP3.3** (black) on command | Down call made | Down call (§6) |
| Down: **JP5.2 → JP5.1** on command | Down limit closed | Down limit (§4) |
| Down: **JP3.7** (yellow) on command | Safety pan closed | Safety pan (§4) |
| Yellow **up/down LED** on the board on command | Board has the call | No LED → board |
| **JP1.3** (green, up) / **JP1.5** (blue, down) | Board output to the relay | None → board |
| Relay post: green (left relay, up) / blue (right relay, down) | Harness to relay good | None → harness relay–JP1 |
| Across relay green→white (up) / blue→brown (down) | Command and ground both at the relay | None → harness relay–JP1 |
| All good but **relay doesn't click** | — | Replace the relay, **ECR-24111** |

**Power walk (VBATT off and JP1 dead),** using battery 2's black terminal
as ground: each battery about 12V and both together 24V (good singly,
bad together → battery jumper wiring; match Bruno's picture) → both sides
of the **circuit breaker** (one side → breaker; tripped more than once →
find out why) → both sides of the **upper final limit** (clear body) →
the big red wire on the **White Rodgers solenoid** → red on battery 1 to
the solenoid's black (missing → the black battery wire). Solenoid has
power and ground → harness from solenoid to JP1.

### VPL-3200B (tall residential), ground = terminal 67

| Read | Good means | No voltage → |
|---|---|---|
| **VBATT LED** | Batteries, **60A double breaker**, any **aux contact disconnect**, 3A slo-blo fuse | JP1 red→brown 24V → fuse. Else power walk (batteries, breaker, aux disconnect, solenoid) |
| 50 → **52** (residential; commercial is 52 → 50) | **Emergency lowering** circuit closed (and pit switch, read at 51) | Emergency lowering (§4) |
| **58** | Top cover, E-stop, nut safety | JP7.1 (red) → JP7.2 (black) = top cover; JP3.4 → JP3.5 = E-stop/nut safety |
| **59** | Upper gate/door | §5 |
| **61** | Mid-stop door (3-stop lifts). **2-stop lifts need a yellow jumper 59–61** | Mid stop (§5) |
| **63** | Platform gate/lower door | §5 |
| Up: JP3.2 (call), **JP7.6 → JP7.5** (up limit), up LED, JP1.3, relay | as above | as above |
| Down: JP3.3 (call), **JP6.3 → JP6.2** (down limit), **JP3.7** (safety pan), down LED, JP1.5, relay | as above | as above |

The VPL-3200B also has the **PCB-00164 indicator board** (see
[[VPL-3200B]]): no lights there = E-stop, top cover, nut safety, pit or
final limit open.

### AC models (VPL-3153/3175, no "B")

The AC board has **18 status lights, E1–E18**. Work down them: E1 AC
into the board (none → 120VAC at the bottom, then the top, of the line
filter) · E2 safety circuit power supply · E3 board fuse · E4 top cover
(jump JP6.1–JP6.2) · E5 E-stop/nut safety (jump J3.4–J3.5) · E7 upper
gate locked (JP4.6–JP4.4) · E9 platform gate (J3.11–J3.9) · E14 up limit
(JP6.4–JP6.5) · E16 down limit (JP5.1–JP5.2) · E17 safety pan
(J3.7–J3.8) · E13/E15 up/down call received · E10 + E11/E12 board firing
the up/down relays. Jumping a circuit should light its E-light; if it
doesn't, the board is suspect. All lit and no click → power down until
every light (E1 too) goes out, then retry. PMS has no AC VPL on file; see
the raw outline before working on one.

Bruno's **TSG-VPL-004** sheet for this board (**PCB-00143**, 90 V motor)
adds detail: **E1** HV bus (no light → AC in, **F1 20 A**, or the upper
final limit), **E2** 3.3 V logic (off → 24 V regulator bad, replace the
board), **E3** 24 VDC through **F2 2.5 A**, **E6/E8** upper/platform gate
**closed** (E7/E9 are **locked**). **E18 (red) is the fault light: off
is normal.** It flashes a code as short flashes plus one long, counted
together:

| Code | Fault | Likely cause |
|---|---|---|
| 1 / 2 | Stall / stall + over-temperature | Overloaded platform |
| 3 | Over-temperature | |
| 4 | 24 V overload | Accessory short |
| 5 | Over-voltage | High AC line |
| 6 | Over-current | Overloaded platform |
| 7 | Max current | Motor failing |
| 8 / 9 | Low voltage / low 24 VDC | AC line too low |

Most codes clear by pressing the **E-stop**; otherwise remove AC power
and wait 1 minute. High voltage: wait 3 minutes after unplugging before
touching the board. See [[VPL-3153-3175]] and
[[Tech Tip - VPL 90V Board PCB-00143 (TSG-VPL-004, SCH-00229)]].

### Older units (before TechMate's serials)

TechMate sends pre-2012 low-rise and tall units (and AC units before
2017) to Bruno. Bruno's 2009–2011 step guides cover them; they use
terminal-strip test points instead of JP connectors:
- **AC relay-logic** (to serial 10020300227) and the first AC control
  board: 115 VAC minimum in, 24 VAC control; a TB2 jumper map; E (pause)
  and E1 (brake) relays; brake 105+ VDC from a bridge rectifier
  ([[Tech Tip - Low-Rise AC VPL Troubleshooting Guides (2009-2010)]]).
- **DC low-rise** (2010–2011): 24 VDC at J1, 3 A fuse, TB1/TB3/TB5 test
  points; jump **TB2-1 to TB1-7 = up, TB2-1 to TB5-6 = down**; motor test
  12–24 VDC on orange/blue
  ([[Tech Tip - Low-Rise DC VPL Troubleshooting Guides (2010-2011)]]).
- **Tall** (2011): same method, tall terminals, emergency lowering and
  phone options ([[Tech Tip - Tall VPL-3200 Troubleshooting Guide (2011)]]).
- Wiring schematics with the circuit under test circled:
  [[Tech Tip - VPL Troubleshooting Diagrams (AC and DC)]].

**July 2012 (serials 12 07 …)** is when Bruno changed the residential
controls, Waupaca wiring kits and the boards TechMate supports
([[Tech Tip - VPL Platform Control Change (2011-2012 Serials)]]). Jumper
bypasses start the lift **immediately** and skip safeties: keep clear and
never leave one in.

## 4. One circuit at a time

- **Top cover switch:** pulled up into maintenance (or pressed down by
  the cover) it should have continuity. None → switch. Continuity but no
  voltage through → wiring to the board.
- **E-stop / nut safety switch:** first the **8-pin connector** where
  the travelling cable meets the platform control cable. Corroded →
  replace the corroded cable(s). On outdoor units it should have
  **dielectric grease** (the manuals say so too). Then check the E-stop's
  two wires are on the back of the switch. **Nut safety switch pressed =
  the drive nuts are failing: replace them immediately.** Not pressed →
  wiring in the travelling cable or platform control.
- **Up / down limit:** pressed while the platform isn't at that end →
  free it. Should read **continuity red–black when not pressed**, open
  when pressed; try other terminal pairs in case the wires are on the
  wrong ones. Switch reads right → its wiring.
- **Safety pan:** pressed or skewed → free it and test down. Not pressed
  → continuity on the **2-pin (red/black)** that plugs into the
  travelling cable's purple/yellow 2-pin. None → pan switches or wiring
  (check for corrosion). Continuity → travelling cable.
- **Pit switch** (if fitted): pulled out it should read continuity
  (VPL-3200B: green to brown, outer pins of its 3-pin). **No pit switch →
  the 3-pin must have its jumper** (green–brown).
- **Emergency lowering (VPL-3200B):** the keyed switch must be on
  **AUTO** for normal running. On AUTO, the 4-pin to the switch reads
  continuity **green to white**. No → check its wiring matches Bruno's
  picture (switch not backwards). Yes but still dead → jump green–white
  on the 4-pin to the tower: runs → the lowering box/switch; doesn't →
  tower harness. Also check the **bottom final limit** (crank the
  platform up off it) and **top final limit** (crank down).

## 5. Gates and doors

Each gate or door has a **closed** switch and a **locked** switch in
series. At a landing, an **enable switch** lets the lift run with that
door unlocked. See [[Gate-and-Door-Interlocks]] for interlock types.

**Can you open it without unlocking it by hand?**
- **Yes, and the platform isn't there** → the interlock is stuck
  unlocked. EMI gate: the **wheel** (upper) or **rod** (platform gate) is
  stuck up. Push it down, lubricate with a **dry lubricant**, and replace
  the interlock if it keeps sticking (PMS field note: Bruno door
  interlock VPL-31452L LH, [[2026-10-01 Bruno-VPL door interlock spring]]).
  **ESI** (electric strike) → call Bruno.
- **Yes, and the platform is at that landing** → normal; the fault is
  the **enable switch** (below).
- **No (locked)** → read the closed and locked circuits at the board.

| Circuit | Wires | VPL-3100B test (ground 20) | VPL-3200B |
|---|---|---|---|
| Upper door **closed** | blue/brown | JP4.6 (blue) → JP4.5 (brown) | JP5.6 → JP5.5 (ground 67) |
| Upper door **locked** | green/brown | → JP4.4 (green) | → JP5.4 |
| Upper **enable** switch | green/white, **lowest switch on the upper limit bracket** | continuity | continuity |
| Platform gate **closed** | red/black | JP3.11 (tan) → JP3.10 (pink) | same pins, ground 67 |
| Platform gate **locked** | black/white | → JP3.9 (gray) | same |
| Lower door closed / locked | blue/brown, green/brown | terminals 27 → 26 → 25 | 61 → 62 → 63 |
| Lower **enable** switch | green/white, **highest switch on the lower limit bracket** | continuity | continuity |
| Mid-stop door (3-stop) | closed blue/brown via the 6-pin at the tower bottom | — | 60 (closed), 61 (locked) |

- Switch reads good but no voltage at the board → wiring between the
  gate and the tower. Prove it with the **upper gate jumper** or
  **platform gate jumper**: jumper doesn't close the circuit → tower
  wiring (upper) or **travelling cable** (platform gate).
- **ESI switches aren't sold separately**: replace the interlock.
- **Mid-stop door unlocked away from the mid landing:** unplug the
  door solenoid 2-pin. Locks now → something is powering the solenoid
  all the time: check for a constant mid call (voltage at terminal 64
  with no call). Remove the call-station red wire from 63: voltage
  gone → mid call station switch or harness; still there → platform
  control mid-call switch, its harness, or the travelling cable.
  Doesn't lock → interlock (check it isn't unlocked with an emergency
  key).
- A lift that **runs with a gate or door open** is miswired or has a
  jumper left in. Call Bruno, and don't leave it in service. Known case:
  **VPL-3210B/3212B/3214B with a platform gate, serials 11080300300 to
  11100301707 (Aug–Oct 2011)**, shipped with a jumper plug (6-pin, one
  blue wire) in the lower interlock harness; remove it
  ([[Tech Tip - VPL-3200B Lower Interlock Jumper Issue (2011)]]). Older
  tall units: an uncut **J1 jumper** with a lower gate lets the door open
  anywhere ([[Tech Tip - Tall VPL Installation Notes]]).
- **Waupaca interlock not working:** 24 V at its pins 3–4 needs the
  **bottom of the three tower limits** made; jump 1–2 to bypass it. Its
  **terminal block must be at the top** of the interlock or it won't
  work.
- **Electric strike / door won't unlock at the landing:** it's on a
  timer. Press the landing button for at least 1 s. On an ESI timer the
  LED blinking with only the tower switch made just means it has power;
  it also needs a call button ([[Tech Tip - VPL Delay Timers and ESI Shut-off Timers]]).
- Upper gate switch wiring after a repair (PBS-00118 closed, PBS-00116
  lock with its roller on the beveled edge):
  [[Tech Tip - VPL Door Interlock Wiring (Waupaca, HES 5200, Upper Gate Switches)]].

## 6. Calls: platform control and call/send

1. Platform control: the **8-pin** first (corrosion; replace both sides
   if both are corroded).
2. **Key switch:** two red wires; continuity across it. None → turn it
   90° and recheck. Still none → key switch.
3. **Rocker:** red in the middle (from the key switch), **white on top
   (up)**, **black on the bottom (down)**. Continuity red–white on up and
   red–black on down. Missing → rocker switch.
4. Switches good → wiring. With the **run bug** (installation rocker
   jumper) on the travelling cable: runs → **platform control cable**;
   doesn't → **travelling cable**. For a call/send, it's usually the
   wiring from the tower to the call/send.

## 7. It clicks, hums or squeals but doesn't move

- **Single click and hold (DC):** read the **White Rodgers solenoid**,
  green→black (up) or blue→black (down), on command. No 24V → board.
  24V → read the big **orange and blue** wires on command. No voltage →
  solenoid/relay. Voltage → **motor**.
- **Hum:** the motor is trying. Can you turn the **screw by hand** from
  the top? Yes → motor (call Bruno). No → check the **drive nuts**: there
  should be a **½ in gap between the two nuts**. Less → **replace the
  drive nuts and take the lift out of service until they're replaced**.
  (Never adjust the drive nut retention hardware; see [[VPL-3100B]].)
- **Repeated clicking:** a power problem or the relay. Read 24V at the
  relays (red/black) while it clicks. Drops → read each battery under the
  same load: drops → batteries (replace both, [[Mobility-Batteries]]);
  doesn't → wiring between batteries and relays. No drop → relay.
- **Squeal with no movement:** belts turning? No → tighten or replace the
  belts. Yes → turn the screw by hand; seized → drive nuts.

## 8. Runs, but…

**Noise:**
- **Scraping / rumbling:** usually the **guide pads**. First loosen the
  **4 bearing block bolts** at the bottom of the screw and run it. Quiet
  → screw alignment; retighten and recheck. Still noisy → measure
  **deflection**: weight on one side, mark the plate's top on both tube
  weldments, walk to the other side, mark again. **½ in or more** → at the
  position with the least deflection, adjust the pads: check the 4 bolts
  (flat-head set screws in welded nuts), add thread locker, tighten fully
  then **back off ¼ turn**, same top and bottom. **Under ½ in** → the pads
  may be too tight; loosen ¼ turn each side.
- **Squeal / squeak:** clean and re-grease the screw. Still squealing →
  **brass shavings in the bottom of the tower** = lift nuts; otherwise a
  bearing.
- **Squealing and jamming** on a deck: check the platform isn't rubbing
  the fascia ([[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]).

**Shudders or grabs** → guide pads (round the pad edges, then the ball
plungers: bottom out, back ¼ turn; 0.5–0.75 in deflection is normal).
**Won't lift its rated load** → carriage not square to the nut; shim it.
**Squealing** with ball plungers fitted → square the screw. Belts:
⅛ in deflection at 2½–3½ lb. All on [[VPL-Drive-Service]].

**Stops partway:** give another command the same way. Runs on → does it
stop at the same spot every time? Note where (2 in from top, 2 in from
bottom, mid, top, bottom) and call Bruno. Doesn't always restart → treat
the failed state with §7 (noise) or §3 (silent).

## 9. Not charging (DC models)

Charger LED meanings: [[Battery-Charger-LED-Diagnostics]].
- **Solid red, no yellow/green:** AC is reaching the charger but it
  doesn't see the batteries. Check the batteries (§3 power walk).
- **Flashing red:** batteries have charge but **no AC**. Plugged in? Is
  the outlet 120VAC?
- **No lights:** plugged in? Outlet 120VAC (check GFI and breaker)?
  Outlet good (dedicated standard or GFI) and still no lights →
  **charger**.
- Batteries read 24V together but won't charge → wiring between batteries
  and charger, or the charger; call Bruno.
- **All four charger lights flashing** (older guides): unplug the charger
  from the wall **and** the batteries for about a minute and reconnect.
  Still flashing → replace the charger.

## 10. Runs on its own

Take it out of service until found. TechMate: either a **short in the
call circuit** or a **relay stuck closed**.

- **Runs past the final limit** (jams into the landing, often trips the
  breaker): safeties are bypassed. **Call Bruno immediately.**
- **VPL-3100B runs past the upper limit but stops at the upper final** →
  board relay shorted: replace the board.
- **Stops at the normal limit** → short in the call circuit. With
  power off, continuity **JP3.1 (red) to JP3.2 (white)** = an up call
  stuck on; **JP3.1 to JP3.3 (black)** = down. Then unplug harnesses one
  at a time until it clears:
  - VPL-3100B: **JP4** (upper gate circuit and the surface-mount call
    sends; jump **33–29** to keep running), then **JP2** (jump
    JP2.2–JP2.5; a JP2 short on a residential low-rise means call
    Bruno), then **JP3** (jump JP3.4–JP3.5).
  - VPL-3200B: **JP5** (upper gate; jump **58–59**), **JP2** (lower door
    and screw terminals; jump JP2.2–JP2.5), **JP4** (the call/sends),
    then **JP3** (jump JP3.4–JP3.5). If it's JP2, unplug the lower door
    harness at the tower bottom and jump 61–63 to split tower side from
    door side. If it's JP4, unplug the two 4-pin (3-wire) call/send
    harnesses.
  - Clears at a JP → unplug that circuit's harness at the bottom of the
    tower: still shorted → tower-side harness; clears → gate/door-side
    harness (or the call/send harness). JP3 → unplug the platform
    control harness from the travelling cable: clears → platform control
    harness; doesn't → travelling cable.
  - Still shorted with everything unplugged → board.

## 11. Board fuse keeps blowing (short to ground)

**When does it blow?**
- **As soon as it's powered:** unplug everything the tower connects to:
  upper gate 6-pin, lower gate 6-pin, call/send 4-pins, platform gate
  3-pin, travelling cable 8-pin. Still blows → unplug JP2–JP6 at the
  board (leave JP1). Still blows → **board**. Then plug back **one at a
  time, in order**, until it blows: (peripherals) platform control 8-pin
  → upper gate 6-pin → platform gate 3-pin → call sends; (board) JP6 →
  JP3 → JP4 → JP2 → JP5. The last one plugged in holds the short.
- **Only on an up or down command:** unplug JP2–JP6, leave JP1, and jump
  to run it. VPL-3100B: **up = JP6 pin 2 to pin 5**; **down = JP3 pin 4 to
  pin 7. Never jump JP3 pin 4 to pin 6: that blows the fuse by itself.**
  Fuse still blows → board. Runs → add the JPs back in the order above,
  repeating the jump each time. For JP3, also unplug the platform
  control cable from the travelling cable to split those two. For JP4,
  unplug the upper gate 6-pin and call/send 4-pins to split them.
- A **JP2** short can be any screw-terminal circuit: platform gate,
  door solenoids, lower door switches, a gate operator or an external
  timer. Look for corrosion and damage, then call Bruno.
- The VPL-3200B tree uses the same method with its own connector numbers;
  follow the raw outline (`MANUALS/Bruno/TechMate/VPL/VPL Short (short comm-tall comm-res DC).md`).

## Harmar

The Harmar [[HighlanderII]] reports faults itself: the **Guardian**
top-cap LEDs (green OK, amber service or minor fault, red solid = check
E-stop and interlocks, **red flashing = do not use**) plus a 32-LED
diagnostic array on the board. The safety-chain method above still
applies; the Highlander has its own interlock wiring
([[Gate-and-Door-Interlocks]]).

## Field notes

- [[2026-10-01 Bruno-VPL door interlock spring]]: door stuck locked;
  interlock lock rod slow to spring back; VPL-31452L.
- [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]:
  squealing and jamming on delaminating plywood fascia.

## See also

[[VPL-Drive-Service]], [[VPL-3153-3175]], [[Tech Tip - VPL Traveling Cable Assignments]],
[[Circuit-Breakers-and-Fuses]] (breaker and fuse locations, ratings and resets by unit),
[[Troubleshooting]], [[TechMate VPL Troubleshooter]], [[VPL-3100B]],
[[VPL-3200B]], [[HighlanderII]], [[Gate-and-Door-Interlocks]],
[[Battery-Charger-LED-Diagnostics]], [[Top-Landing-Gate-Installation]],
[[Porch-Lift-Evaluation]], [[Stairlift-Troubleshooting]]
