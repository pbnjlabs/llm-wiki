---
type: concept
tags: [seating, tilt, recline, elevate, anterior-tilt, power-positioning, pride, quantum, tru-balance-4, ilevel, q-logic-3]
---

# TRU-Balance 4 Power Positioning System (Quantum)

Source: [[TRU-Balance 4 Parts Replacement Guide (INFMANU5359)]] (Rev B,
2022). Quantum's newer power seat: tilt (incl. **anterior tilt** to 20°
or 30°), recline, lift (elevate), an **articulating foot platform
(AFP)**, an **AAM** actuator module on the seat back, and iLevel. Run
from a **Q-Logic 3** controller. The guide illustrates it on the
[[Q6-Edge-3]], [[Q6-Edge-3-Stretto]] and [[4Front-2]]; the
[[Q6 Edge 4 Parts Replacement Guide (INFMANU5618)|Edge 4 guide]] also
mounts TB4 tilt and TB4 lift & tilt seats. The older system is on
[[Tru-Balance-3-Power-Positioning]].

No TB4 owner's manual or **technical troubleshooting guide** is on file
(Missing manuals). Q-Logic 3 seat/actuator fault codes **150–177** are
on [[Q-Logic-Fault-Codes]].

## Rules from the guide

- **20° and 30° anterior tilt need the chest support (chest bar or an
  aftermarket one) and the knee block.**
- **Legrest length ≤ seat-to-floor height − 3.5 in** (19 in STF → 15.5
  in max).
- **AFP near the floor locks out driving** so the footplates aren't
  driven into the ground; that point is taught (below).
- Don't retract the recline actuator past its min-stroke position. With
  the top recline bolt out, the back falls backward: push it forward past
  90° first.
- Chair unoccupied for calibration; two people to remove the seat.

## Q-Logic 3 programmer procedures (Seat → Memory Seating Setup)

| Procedure | When | Path |
|---|---|---|
| **Actuator Calibration** | After replacing the AAM, recline or elevate actuator, AFP upper, or the seat base | Actuator Calibration (Start) → Start Actuator Feedback Calibration (Yes); confirm by pushing the joystick forward |
| **Teach Anterior Tilt and Transfer Position** | Seat base replaced; tilt limit switch replaced **with a different angle** (reset, then teach); at delivery to set the user's anterior tilt | Teach Anterior Tilt and Transfer Position (Start), follow the prompts |
| **Teach Elevate vs AFP Articulation** | Lower leg length or STF height changed (delivery or repair) | Seat home → start → AFP down until the footplates are just above the floor → elevate up to fully articulate the AFP, then elevate down until just above the floor → save |

## Torque values

| Fastener | Torque |
|---|---|
| Side rails to width brackets | 15.5 N·m (11.4 ft·lb) ±10% |
| Depth bracket to seat frame | 24–28 N·m (17.7–20.6 ft·lb) |
| Seat back to seat (interface plate, 4 screws) | 22–26 N·m (16.2–19.1 ft·lb) |
| Recline actuator, top and bottom | 10–15 N·m (7.4–11 ft·lb) |
| AFP lower to upper | 15 N·m (11 ft·lb) ±10% |
| Calf pad mounting bracket | 4.5–9 N·m (3.3–6.6 ft·lb) |
| AFP upper to depth bracket | 20.5–23.5 N·m (15.1–17.3 ft·lb) |
| AFP elevate actuator acorn nut | Loctite 243/242, snug to the bushings, then **+¼ turn** |
| iLevel roller switch | Loctite 262, 0.5–1.0 N·m (0.4–0.7 ft·lb) |
| iLevel seat assembly, side screws | 18–22 N·m (13.2–16.2 ft·lb) |
| Seat base to interface rails (8 screws) | 18–22 N·m (13.2–16.2 ft·lb) |
| Interface rails to seat frame | 35 N·m (26 ft·lb) ±10% |
| Armrest width screws; support-joint pivot; front angle | 25–35 N·m (18.5–25.8 ft·lb) |
| Armrest support joint to back rail | 18–22 N·m (13.3–16.2 ft·lb) |

Seat-to-base values for each chair are on [[Pride-Parts-Replacement]].

## Adjustments

- **Width:** loosen 4 front and 4 rear screws, set to the mark on the
  seat pan; back width to the mark on the back pan.
- **Depth:** depth bracket, seat interface position and back position,
  from the tables in Appendix B. Seat interface position:

| Seat depth | Q6 Edge 3 / Stretto | 4Front 2 |
|---|---|---|
| 14 in | 2 in forward | — |
| 15 in | 1 in forward | 2 in forward |
| 16 in | middle | 1 in forward |
| 17–20 in | middle | middle |
| 21 in | 1 in rearward | 1 in rearward |
| 22 in | 2 in rearward | 2 in rearward |

- **Seat-to-floor height** is set by the interface rail holes (p. 32):
  Q6 Edge 3 about 17.5 / 18.25 / 18.75 / 19.25 in, 4Front 2 17.75 /
  18.25 / 18.75 in, Stretto 18 / 18.5 / 19 in; one hole on each is
  marked "do not set". Check the drawing.
- **Armrests:** height first (markers 8–10, 11–13, 14–16 in), then
  angle. Keep the turnbuckle pivot link within **25°** of the back mount
  or it interferes.
- **Anterior tilt switch:** button faces **up**; plugs into the
  switching motor on the front of the tilt frame.

## Layout notes

- **AAM** ports: articulate, elevate, recline, lift, tilt, two bus, AFP.
  Photograph before unplugging. AFP harness: **articulate on the left,
  elevate on the right**; color-coded plugs under the seat.
- Bus: one seat-to-base bus cable always, plus two bus cables, a bus
  cable and a multiplier, or two multipliers. Elevate the seat fully to
  reach the woven-wrap cable run.
- **Stretto iLevel seat assembly uses a spacer** between seat frame and
  interface rail.
- iLevel base parts (caster-arm stop, suspension limiter) are in the
  base guides: [[Q6 Edge 3 Stretto Parts Replacement Guide (INFMANU5103)]],
  [[Q6 Edge 4 Parts Replacement Guide (INFMANU5618)]].

## See also

[[Tru-Balance-3-Power-Positioning]], [[Q-Logic-Seat-Configuration]],
[[iLevel]], [[Joystick-Controllers]], [[Pride-Parts-Replacement]],
[[Power-Chair-Troubleshooting]], [[Pride]]
