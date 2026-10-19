---
type: concept
tags: [pride, quantum, ilevel, seat-elevation, power-positioning, q-logic-3, qlnes, drive-inhibit, safety]
---

# iLevel (Quantum elevate-and-drive)

**iLevel** is Quantum's option that lets a power chair user **drive with
the seat raised** (up to 12 in) at a reduced speed. The power base locks
its front suspension while the seat is up so the chair stays stable. It
works with TRU-Balance 3 or 4 seating
([[Tru-Balance-3-Power-Positioning]], [[Tru-Balance-4-Power-Positioning]]).

Sources: the iLevel sections of the
[[Q6 Edge 3 Stretto Operator Manual]], [[Tru-Balance 3 Power Positioning Systems BOI]]
and [[Q-Logic 3 Basic Operation Instructions]]; the
[[QLNES Basic Operation Instructions (INFMANU5366)]]; the spec sheets
and the [[Quantum End-to-End Chart (INFINFB4546, 2025)]]; and the parts
guides for the [[Q6 Edge 3 Stretto Parts Replacement Guide (INFMANU5103)|Stretto]],
[[Q6 Edge 4 Parts Replacement Guide (INFMANU5618)|Edge 4]] and
[[TRU-Balance 4 Parts Replacement Guide (INFMANU5359)|TRU-Balance 4]].

## Which chairs, and how fast elevated

| Chair | Top speed | With iLevel | Notes |
|---|---|---|---|
| [[Q6-Edge-3-Stretto]] | 6.25 mph | **3.5 mph** | 12 in iLevel |
| [[Q6-Edge-3]] | 6.25 mph | **4.5 mph** (UK 3.2) | spec sheet |
| [[Q6-Edge-4]] | 7 mph | **4.5 mph** | spec sheet and chart |
| [[Q6-Edge-2.0]] | 6.25 mph | **3.5 mph** (UK 3) | |
| [[Q6-Edge-HD]] | 4.7 mph | **3.5 mph** | **10 in HD iLevel**; capacity drops **450 → 400 lb**; seat 20 × 20 to 24 × 24 in |

The 2025 chart lists "elevate" or "elevation" speeds for other Quantum
chairs (4Front 2 and R-Trak 3.5 mph, 4Front 2 HD 2.7, J4E 1.25), but it
doesn't call those iLevel. Don't assume they have the iLevel suspension
lock. The **J6**'s power elevating seat is different again: it halves
the chair's speed once the seat is up more than 1–2 in
([[J6 Operator Manual]]).

## How it works

- iLevel **engages automatically** when the power elevating seat is
  raised and the iLevel indicator shows on the controller. Raise it
  from the seat screen (elevate actuator) or a single switch (press and
  hold to raise, press and hold again to lower).
- Once the seat actuator starts, the **iLevel boots lock the front
  caster arms**. Climbing ability drops to **1–1.5 in**.
- Tilt or recline up to **20°** while iLevel is active.
- The chair drives at a **preset reduced speed** while elevated. If the
  controller shows **"iLevel not engaged"**, speed drops to **25%** when
  elevated. On a TRU-Balance 4 chair in **power anterior tilt**, it drops
  to **0% (full drive lockout)** instead.
- **"Not engaged" on level ground = a fault.** Stop using iLevel and get
  it to the provider.

### Controller indicators

| Controller | What you see |
|---|---|
| **Q-Logic 3** | Indicators: 1a no restrictions, 1b **safe elevation**, 1c power anterior tilt, 1d reduced speed, 1e full drive lockout. Drive/Function Inhibit light (top left): **green** OK, **yellow** speed reduced as the seat rises, **red** full drive lockout. Error **#47 "Suspension lock not engaged"**: seek level ground, check the suspension lock mechanism |
| **QLNES** (LED joystick) | **Green blinking** = iLevel active; **orange blinking** = suspension lock not engaged while elevated |
| **NE+** (older) | TRU-Balance 3 BOI figure shows "iLevel engaged" on an NE+ display |

The TRU-Balance 3 inhibit matrix ties iLevel to the **elevated** state:
elevated = 1/4 speed and iLevel active; tilt or recline past 20°, or
combined past 125°, locks out driving
([[Tru-Balance-3-Power-Positioning]]).

## Use rules (from the manuals)

Teach these at delivery (patient training, [[Joint-Commission-DMEPOS]]):

- Raise the seat only on a **flat, level surface**; iLevel is for
  **indoor** use (malls, offices, medical facilities) and **limited,
  flat, level, hardscape** outdoor surfaces.
- **Never** raise the seat on an incline, on bumpy or uneven ground, or
  while going up or down a **curb** of any height.
- **Never** use iLevel on gravel, hills or other loose, uneven ground, or
  in fields.
- **Never** raise or change the seat height under a table, desk or other
  fixed object. Keep the area clear.
- Fasten the positioning belt. Some users need to practice with a
  trained attendant first (Q-Logic 3 BOI).
- **Check that the speed limiting works** before using the chair.

## Parts and service

The iLevel hardware is split between the base and the seat:

- **Base:** caster-arm **stop** with a backing plate (**sloped edges
  face up**), the **suspension limiter** with its switch plate and
  switch, the **iLevel cable** and spring assembly from the seat, and a
  **suspension lock harness** to the controller. On the Edge 4, QLNES
  power modules have an **iLevel inhibit** port.
- **Seat (TRU-Balance 4):** iLevel **roller switch** and **iLevel seat
  assembly**. The Stretto needs a **spacer** between seat frame and
  interface rail.

| Fastener | Torque |
|---|---|
| Caster-arm stop to caster arm | 15–20 N·m (11.1–14.7 ft·lb) |
| Suspension limiter to frame, bottom 3 screws | 15–20 N·m |
| Switch plate screws and the middle limiter screw | **1.5–2.0 N·m** (1.1–1.5 ft·lb) |
| TB4 iLevel roller switch | 0.5–1.0 N·m, Loctite 262 |
| TB4 iLevel seat assembly, side screws | 18–22 N·m (13.2–16.2 ft·lb) |

- **Disconnect the iLevel cable from the suspension limiter before
  lifting the seat off** (Edge 4 guide). Unscrew the nut; don't kink or
  deform the cable.
- Replacing an Edge 4 front caster arm: move the **stop block** to the
  new arm.
- Re-route the iLevel / suspension lock harness exactly as found; on the
  Edge 4 it's bundled with the motor and light harnesses.
- More torque values: [[Pride-Parts-Replacement]].

No Quantum troubleshooting procedure for iLevel faults is on file. The
"not engaged" warning and #47 point at the **suspension lock** side:
the cable, the limiter switch and its harness are the parts involved.

## Field notes

- [[2026-09-25 Q6-Edge-3 iLevel no power]]: an Edge 3 with iLevel that
  was completely dead. The cause was flat batteries and a frayed joystick
  cable, nothing iLevel-specific; iLevel up/down passed the function test
  afterward.

## See also

[[Tru-Balance-3-Power-Positioning]], [[Tru-Balance-4-Power-Positioning]],
[[Q-Logic-Seat-Configuration]], [[Joystick-Controllers]],
[[Q-Logic-Fault-Codes]], [[Power-Chair-Troubleshooting]],
[[Pride-Power-Chair-Lineup]], [[Pride]]
