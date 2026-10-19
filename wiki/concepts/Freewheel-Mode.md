---
type: concept
tags: [freewheel, brake, park-brake, safety, power-chair, scooter, golden, pride, quantum, red-hawk, troubleshooting]
---

# Freewheel Mode (manual brake release)

Every power chair and scooter on file has a **freewheel lever** (Red
Hawk: "brake release lever") that disengages the drive and **releases
the electromagnetic park brake** so the unit can be pushed by hand.
Chairs have **one lever per motor**; most scooters have one on the
transaxle. **In freewheel there is no brake.**

Sources: the freewheel sections of Golden's owner's manuals
([[LiteRider Owners Manual (GL111, GL141)]], [[GR595 Eagle Owners Manual]],
[[Companion Owners Manual (VA Contract Variant)]],
[[GA541 Avenger Operator Manual]],
[[LiteRider Envy LiNX Owners Manual (GP162)]], [[Cricket Owners Manual (GP302)]]),
Golden's [[Buzzaround XL Service Guide (GB117, GB147)]], Pride's
[[J6 Operator Manual]] and [[Q6 Edge 3 Stretto Operator Manual]], the
Red Hawk [[Phoenix Owner's Manual]] and [[Eagle HD Owner's Manual]], and
the controller code pages linked below.

## The lever goes a different way on each model

Check the label on the unit. Don't go by feel.

| Model | Freewheel (brake off) | Drive (brake on) |
|---|---|---|
| Golden LiteRider GL111/141 | Push lever **forward** | Push lever **back** |
| Golden Eagle GR595 | Pull **up** toward **N** | Push **down** toward **D** |
| Golden Companion | Brake handle toward "**disengage**" on the label | Toward "**engage**" |
| Golden LiteRider Envy GP162 | Pull lever **up** | Push lever **down** |
| Golden Cricket GP302 (2 levers) | The other position (the manual only names drive) | **Forward** |
| Pride J6 (2 levers) | Pull **outward** | Push **inward** |
| Pride Q6 Edge 3 Stretto (2 levers) | Push **down** | Pull **up** |
| Red Hawk Phoenix (2 red levers) | Push in the arrow direction | Reverse |
| Red Hawk Eagle HD | Flip brake release lever **forward** (manual) | Flip **back** (electric) |

Golden LiteRider / Buzzaround brakes come with two lever styles
(rear-facing and the newer upward-facing); see [[Brake-Replacement]].

## Rules from the manuals

- **Level ground only.** Never put a chair or scooter in freewheel on a
  slope or incline: it can roll away on its own (Pride, Golden).
- **Nobody sits on it in freewheel**, and never switch to freewheel
  while driving. Before anyone gets on or off: **lever in drive**.
- **Power off first.** On the Stretto, switching with the power on can
  leave an error on the controller: power off, set drive mode, power
  on. Red Hawk: never open or close the brake with the power on.
  Golden scooters: key off before freewheeling, and the brake engaged
  before the key goes back on.
- **Push slowly.** Pushed fast, the motor acts as a generator and the
  unit gets hard to push (Golden). Golden scooters also have **motor
  braking** that limits pushing speed with the key off. On the Eagle,
  dead batteries mean no motor braking.
- **Don't force the levers**, kick them or stand on them: it damages the
  levers, motors and brakes. If a lever is stiff, **rock the chair back
  and forth** slightly (Pride J6).
- **Never use the lever handles as tie-down points** (Pride).
- **Never raise a power elevating seat in freewheel** (Pride J6).
- **Charging:** controller off and levers engaged (Pride J6).
- **Pushing is much easier with the power off** (Pride).

### Emergency: no power on a slope (Golden scooters)

1. Key off, get off the scooter.
2. Lever to freewheel.
3. Standing alongside, walk the scooter slowly down the slope. If you
   can't control it, get help or don't try.
4. At the bottom, on level ground, lever back to engaged, then key on.

## Service

- **Before any repair:** lever in **drive / engaged** so the unit can't
  roll (Golden's Buzzaround XL service guide starts every procedure
  this way; Pride's parts guides: "place the unit in drive mode").
- **Wheel change or disassembly:** power off and **not** in freewheel
  (Pride J6 and Stretto, Golden GP162).
- **Pride motor replacement (2017 Q6 Edge, Jazzy 600 ES):** loosen the 2
  setscrews on the **freewheel release linkage** and slide it off the
  release shaft; refit it after ([[Pride-Parts-Replacement]]).
- **Golden brake replacement:** the new brake goes on in the freewheel
  position (12 o'clock) ([[Brake-Replacement]]).

## Left in freewheel? What the controller shows

A half-set lever looks like a brake fault. **Check the lever first**,
then the brake and wiring.

| Controller / unit | Code | Page |
|---|---|---|
| Golden Dynamics R-Series scooters (Companion, LiteRider, Buzzaround) | **5** flashes/beeps, brake fault | [[Flash-Beep-Diagnostics]] |
| Golden PG S-Drive scooters (Eagle, Patriot, GB106) | **5** solenoid brake trip; **8** motor disconnected says check the freewheel lever | [[S-Drive-Beep-Codes]] |
| Golden PG S-Drive / VR2 (TruCharge 10-bar) | **4** bars, parking brake off | [[TruCharge-Diagnostics]] |
| PG programmer trip codes | **7000 / 7001** freewheel mode engaged | [[PG-Drives-Trip-Codes]] |
| Golden Dynamic Shark | **5 / 6** park brake | [[Shark-Diagnostics]] |
| Golden Dynamic LiNX | **5 / 6** park brake | [[LiNX-Diagnostics]] |
| Pride PG VR2 / GC3 / newVSI | **9** flashes, park brake | [[Pride-Controller-Flash-Codes]] |
| Pride Dynamic (Jazzy) | **5 / 6** left / right park brake | [[Pride-Controller-Flash-Codes]] |
| Pride Q-Logic 3 | **#3 / #4, #25 / #26** brake; fix: **disengage and re-engage the lever** | [[Q-Logic-Fault-Codes]] |
| Pride NE / NE+ | "Motor/Brake Error" | [[Power-Chair-Troubleshooting]] |
| Pride Elite Traveller scooter | **5** beeps, solenoid brake trip | [[Elite-Traveller]] |

Brake resistance checks by chair, with the lever in drive:
[[Power-Chair-Troubleshooting]] §6a.

## Joint Commission (house standard)

Show the user and caregiver the lever and the level-ground rule at
delivery (patient training), and follow the manufacturer's steps for
repairs ([[Joint-Commission-DMEPOS]]).

## See also

[[Power-Chair-Troubleshooting]], [[Troubleshooting]],
[[Brake-Replacement]], [[iLevel]], [[Pride]], [[Golden]]
