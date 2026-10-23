---
type: concept
tags: [circuit-breaker, fuse, electrical, troubleshooting, power-chair, scooter, stairlift, vpl, vehicle-lift, ceiling-lift, golden, pride, bruno, harmar]
---

# Circuit Breakers and Fuses

Where the breaker and fuses are on each unit, what they're rated, how to
reset or test them, and what a repeat trip means. Pulled together from
the model, source and troubleshooting pages linked below (each cites
its manual). A tripped breaker or blown fuse is one of the most common
"dead unit" calls: **check it before the board or controller.**

## Rules that apply everywhere

- **A breaker trip is a symptom.** Something drew too much current:
  overload or overweight, long climbs, curbs, low tire pressure,
  run-down batteries (Golden Companion, Pride chairs); a foreign object
  jamming the rail or exceeding the rated load (Bruno stairlifts). Reset
  once; **if it trips again, find out why** before resetting again
  (Pride, Bruno).
- **Let it cool before resetting:** Pride chairs about a minute; Golden
  GA541 **5 minutes**; GP161/GP162 about a minute.
- **Replace fuses only with the exact type and rating** (Golden
  Buzzaround EX dock, LiteRider battery pack, Pride Victory tiller,
  Prism/Vancare ceiling lift boards). A bigger fuse hides a short and
  can burn a harness.
- **Meter it; looks can lie** (Pride 2004 guide). **Breaker: under 1 Ω
  is good; open or over 3 Ω = replace** (Pride 2004 guide; the Q6 Edge,
  J6 and Jazzy 614 guides say under 1 Ω or about 1 Ω).
- **A fuse that blows again = a short.** Unplug harnesses one at a time
  until it stops blowing; the last one plugged back in holds the short
  (Bruno stairlifts §12 and VPLs §11). A short only with the breaker on
  means wiring after the breaker.
- **Voltage walk:** read both sides of the breaker, then each switch and
  fuse in series. Power on one side only = that part is bad
  ([[Troubleshooting]]).
- **Warranty:** fuses and bulbs are wear items on Golden and Pride
  warranties ([[Golden-Scooter-Warranty]], [[Golden-Wheelchair-Warranty]],
  [[Pride-Warranty]]).

## Golden scooters

| Model | Breaker | Fuses | Notes |
|---|---|---|---|
| Companion GC240/340/440 ([[GC240-340-440-540-Companion]]) | **50 A**, resettable, **under the seat on the rear shroud panel** (SE06E602) | **3 A** blade (2021 IPB); the service guide also lists a control panel fuse and a charger harness fuse | Trips: low tire pressure, long climbs, curbs, low batteries, overload |
| GA541 Avenger ([[GA541-Avenger]]) | **50 A** manual reset, **under the battery cover next to the freewheel release** | — | Wait **5 min** before resetting |
| GR575 Patriot ([[GR575-Patriot]]) | Main breaker (rear harness) | **125 A** battery fuse, **15 A**, **3 A** | |
| GR595 Eagle ([[GR595-Eagle]]) | Breaker with harness (MBE-595-BREAKER) | — | |
| Buzzaround XL GB117/147 ([[GB1xx-Buzzaround-XL]]) | **30 A on the battery pack** | **40 A** battery and **5 A** charger fuses inline on the battery harness; **1 A** on the throttle pot | |
| Buzzaround Lite GB121, XL GB121B/124A | — | **3 A under the battery pack** (dead dash, no drive); **5 A under the charger port cover** (won't charge) | |
| Buzzaround EX GB118/148 ([[GB118-148-Buzzaround-EX]]) | **40 A** (exact rating) | **100 A** in the left battery pack; **10 A** charger; **1 A** throttle; fuse box assembly | Charging dock: **10 A blade** (9 bottom screws) |
| Buzzaround LX GB119/149 ([[GB119-149-Buzzaround-LX]]) | — | **Tiller fuse panel**: **1 A** top = dash, lights, power; **2 A** middle = USB; **10 A** bottom = XLR charge port | |
| Carry On GB120/GB220 ([[GB120-Buzzaround-CarryOn]]) | — | **35 A** battery (blade) and **3 A** | **The fuse ships loose**: fit it under the controller cover beneath the seat pedestal at setup |
| LiteRider GL110/140 ([[GL110-140-LiteRider]]) | On the battery pack, under a button cover | Inline battery fuse | Battery pack procedure: [[Battery Replacement (GL110, GL140, GP160)]] |
| Older guides (GB106, GB116/146, GL109) | Listed | Battery-harness fuse | |

## Golden power chairs

| Model | Breaker | Fuses / notes |
|---|---|---|
| Compass Sport GP605 ([[GP6xx-Compass]]) | **50 A** in the main harness (GP605A IPB) | 2011 **routing upgrade**: turn the front breaker so its wires route inside (17 mm socket on the cap; don't over-tighten): [[Compass Sport Circuit Breaker Wire Routing Upgrade (GP605)]] |
| Compass HD GP620 | Main breaker in the power harness (MBE-COCBH, also GP600M and Alante GP201) | |
| Alante DX GP204 / LT GP215 ([[GP204-Alante-DX]]) | **40 A** (P3026-0033-01, "for Compass Jr") | |
| Alante GP205/206/207 | Breaker in the main harness (WE04E601) | |
| LiteRider Envy GP162 ([[GP162-LiteRider-Envy]]) | Main breaker with reset button | Wait about 1 min |
| Envy Lite GP161 ([[GP161-LiteRider-Envy-Lite]]) | **35 A**, reset **under the battery box handle** | Wait about 1 min |
| BuzzAbout GP164 ([[GP164-BuzzAbout]]) | **35 A** (the Buzzaround GB106 breaker), reset button on the base | Light bypass switch also on the base |
| Carry On power chair GP130 ([[GP130-CarryOn-Power-Chair]]) | — | **35 A blade fuse, ships loose**: fit it under the controller cover beneath the basket |

## Pride and Quantum

| Unit | Breaker / fuse | Notes |
|---|---|---|
| Q6 Edge, J6 | Push-in reset button | **J6:** the battery/breaker harness must run **+ of one battery to − of the other**; wired wrong, it won't power up and the breaker trips ([[J6]]) |
| Q6 Edge 3 Stretto | Left side of the frame; **resets itself** after about a minute | [[Q6-Edge-3-Stretto]] |
| Q6 Edge 4 ([[Q6-Edge-4]]) | Breaker **on the rear battery** (Group 24 tray build), opened with the **yellow button**, closed with the yellow lever to the left; at the breaker the short wire goes left at about 120° | **Ceramic terminal fuse** on the rear negative harness: check the decal for the stack-up. Torque printed **3.7–4.1 N·m** and **10–15 N·m** in the same guide: confirm with Quantum |
| R-Trak ([[R-Trak]]) | Breaker lead nuts **11.3 N·m**; bracket screws 10–14, breaker to bracket 4–6 N·m | |
| Quantum Outback | Battery fuse screw **3.7–4.1 N·m** | [[Quantum-Outback]] |
| Jazzy Ultra Light | **The power switch on the back of the battery box is the breaker** | [[Jazzy-Ultra-Light]] |
| Go Chair | **Front of the battery box** | [[Go-Chair]] |
| i-Go scooter | Pops out when tripped; rest a minute, push it in **toward the rear**; frequent trips = charge more | [[i-Go]] |
| Go Go Super Portable SC15 | Breaker (push toward the rear), **fuse under a rubber cover**, battery **disconnect switch** | [[Super-Portable-SC15]] |
| Elite Traveller | Push the breaker reset; dealer test: **fuse 5c**; charger fuse if the meter doesn't rise while charging | [[Elite-Traveller]] |
| Victory scooters | **Tiller fuse block (back of the tiller)**, ATO: **10 A red = charger, 5 A tan = key, 1 A black × 4 = lights**. **No power → key fuse first** (about 1 Ω) | [[Victory]] |
| Lithium packs (Pride) | Battery fuse | Won't charge: plug order, **battery fuse**, disconnect switch ([[Mobility-Batteries]]) |
| Run-plug / PTO harness | Harness fuse | **Never jumper pins 1–2** on the round 4-pin PTO barrel: it sparks and blows the harness fuse ([[Power-Chair-Troubleshooting]]) |
| Q-Logic | Code **69** = bus overload (**B+ fuse tripped**) | Unplug modules one at a time ([[Q-Logic-Fault-Codes]]) |
| Legacy Jazzy/Jet (2000–2002) | Fuse under or beside the utility tray, on the battery box, etc. | [[Jazzy Fuse Locations]] |

## Stairlifts

- **Bruno** ([[Stairlift-Troubleshooting]]): power cycle **at the
  circuit breaker** first; it should click and beep once. No beep: final
  limit, overspeed, **board fuse** (continuity), **in-line fuse on the
  B− (black) battery wire** (check red to black for a short before
  replacing), batteries, then a voltage walk through the breaker. On some
  units the brake runs through the **breaker's aux contacts (NO and
  COMM)**. **5 A charging-harness fuse** keeps blowing → unplug the
  power-option aux harnesses. Breaker trips on the CRE: a foreign object
  jamming the rail or gear rack, or over the rated load ([[CRE-2110]]).
  SRE-3050 grinding: test the **on/off breaker switch** by bypassing it
  with the grey brake lead ([[SRE-3050]]).
- **Harmar Pinnacle SL300** power options ([[Pinnacle-SL300]]): power
  swivel has a **resettable fuse** that trips after 5 s of holding at a
  stop (1–2 min reset); power footrest has a **self-resetting fuse** on
  obstruction (30 s).

## Porch lifts (Bruno VPL)

([[VPL-Troubleshooting]])
- Battery power runs **through the breaker and upper final limit** to the
  board. **VBATT LED on** = batteries, breaker, final limit and the
  **3 A slo-blo board fuse** are all good.
- **VPL-3200B:** **60 A double breaker**, plus an **aux contact
  disconnect** if fitted, before the White Rodgers solenoid
  ([[VPL-3200B]]).
- Tripped more than once → find the cause. Board fuse blowing → §11's
  unplug-in-order hunt. **Never jump JP3 pin 4 to pin 6** on the
  VPL-3100B: that blows the fuse by itself.
- Install: breaker pushed in before connecting the battery Molex
  connectors ([[VPL-Installation]]).

## Vehicle lifts

([[Vehicle-Lift-Power-Wiring]])

| Maker | Protection | Where |
|---|---|---|
| **Bruno** ASL-250/275, PUL-1100 | **30 A ATO inline fuse** | At the battery, on the red (+) lead; you cut the cable to length |
| Bruno VSL-4400 / VSL-6000 / 6900 | In-line fuse at the battery; VSL-6000 also a **breaker at the control box** (ON before setup) | [[VSL-4400]], [[VSL-6000-6900]] |
| **Harmar** inside, outside, truck, hybrid lifts | **20 A self-resetting breaker**, about **6 in from the battery** on the pre-made harness (never cut it) | Black to negative first, red last |

Harmar's #1 cause of "won't run, slow or intermittent" is a bad
connection or the breaker: clean connections, inspect the harness for
chafe, verify or swap the breaker ([[Hoist-Series-Inside-Vehicle-Lifts]],
[[AL-Series-Outside-Vehicle-Lifts]], [[Hybrid-Vehicle-Lifts]]). The
AL625's **RF remote has its own fuse**.

## Ceiling lifts, platform lifts, door operators

- **Prism C-450/C-625** ([[C-450-C-625]], [[Ceiling-Lift-Troubleshooting]]):
  external **thermal breaker** (C-450); two **board fuses, 25 A or
  30 A**: replace only with the specified one, still dead → board.
- **Prism P440** ([[P440]]): internal **15 A fuse**.
- **Harmar Highlander II** platform lift ([[HighlanderII]]): **60 A fuse**
  on the 24 V battery bank.
- **Harmar RPL** (older residential platform lift, no manual on file):
  **15 A resettable breaker** on the motor side and **3 A resettable**
  on the 24 V control side, next to the controller
  ([[Video - Electronic Components of the Residential VPL (RPL)]]).
- **Open Sesame** door operators (pre-2021): tube fuse holder on the
  **orange battery wire**; no red light → check it
  ([[Open-Sesame-Model-133]], [[Open-Sesame-Model-233]]).

## Lift chairs and chargers

- **Golden lift chairs** have no breaker on the chair: check the **house
  breaker** and the transformer LED ([[Golden-Lift-Chair-Service]]). The
  heat/massage system has its own power supply.
- **Golden HP8204B charger:** **10 A 125/250 V** fuse; replace with the
  charger off and unplugged ([[Golden-Battery-Charging]]). Pride
  off-board chargers: a red LED can mean a blown fuse
  ([[Battery-Charger-LED-Diagnostics]]).

## See also

[[Troubleshooting]], [[Power-Chair-Troubleshooting]],
[[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]],
[[Vehicle-Lift-Power-Wiring]], [[Ceiling-Lift-Troubleshooting]],
[[Mobility-Batteries]], [[Golden]], [[Pride]], [[Bruno]], [[Harmar]]
