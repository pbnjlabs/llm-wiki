---
type: source
manufacturer: Harmar
doc_type: Engineering Drawing
source: "MANUALS/Harmar/310-00005.msd2.webp; MANUALS/Harmar/310-00005.msd.webp"
date: 2019-10-02
tags: [harmar, outside-lift, hitch-lift, actuator, specs, al100, al301xl]
---

# Actuator Drawing 310-00005 (Rev C)

Harmar's engineering drawing for actuator **310-00005, "Actuator, Outside
Lifts"**: two sheets, size B, given to the human as two screenshots
(`310-00005.msd2.webp` = sheet 1, `310-00005.msd.webp` = sheet 2). Drawn
12-23-13. Rev C, "promote to production", is dated **02OCT19**. It's a
drawing, not a procedure: specs, dimensions and an exploded view, with
**no torque values and no removal or install steps**. Feeds
[[AL-Series-Outside-Vehicle-Lifts]].

## Where it came from: the ALA10010

The revision block answers part of the open
[[Ingestion-Backlog]] question:

| Rev | Change | Date |
|---|---|---|
| A | **"Formerly PN ALA10010 actuator"**; removed the shaft pin hole and replaced it with a recess, key way and **shaft collar** type assembly (ECO-003300) | 16JUL18 |
| B | Heat treat the collar relief area; actuator part number changed from -NB450 to **NX450** | 30OCT18 |
| C | Promote to production (**ECO-004479**) | 02OCT19 |

So the 310-00005 is the **ALA10010, renumbered and revised**, not a
different actuator. ECO-004479 is the same change order that swapped
ALA10010 for 310-00005 on the AL100 assembly drawing (rev H, 13AUG19,
[[Harmar Parts Diagrams]]). The design changes are **inside the
actuator** (drive shaft and collar). The parts that the removal touches
look the same: the **ball nut** threads into the lift's nut plate, there's
a **manual override hex**, and the motor and tube layout match. So
[[Actuator Removal Instructions (ALA10010-INS rev 2)]] and
[[Video - How to Replace the Actuator (AL-100)]] most likely apply to
the 310-00005 too. That's inferred from the drawing, not stated by
Harmar.

## Specs (sheet 1)

| Item | Value |
|---|---|
| Maker | **Moteck Electric Corp.**, mfr no. `JDHM-12-20-B-635.2-NX450` (first letter hard to read) |
| Voltage | 12 V DC |
| Drive | Ball screw, 20:1 gear ratio |
| Load | **4,500 N dynamic** (about 1,010 lbf), **13,600 N static** (about 3,060 lbf) |
| Back drive | Motor must not back drive at the maximum static load |
| Duty cycle | **25 %** at rated load and 70 °F (21 °C); "on time" is one full cycle |
| Motor | 2.5 kg·cm full-load torque, 3,600 RPM, **10 A** at full load |
| Clutch slip torque | 150–175 kg·cm (**130–152 in-lb**) |
| End of stroke | Mechanical limit with **clutch protection** |
| Operating temp | −15 °F to 150 °F (−26 °C to 66 °C) |
| Sealing | IP54 or better |
| Noise (max) | 72 dB no load, 80 dB with load, at 1 m |
| Connector | Packard 56 series female housing #2984883, 2 male blade terminals #2962987; **red +, black −** |
| Payload thread | Male **15/16-16-UN-2A** |
| Size | About 25.05 in (636.1 mm) overall, 19.84 in (503.9 mm) screw, motor housing 6.63 × 5.97 in; lead 9.29 ± 0.25 in |

The brake detail reads "30 mm +0.7/−1.0 mm, 19.5 turns ±0.25 turn,
restraining torque of brake system". It's a factory setting, not a field
adjustment. The chart ("nominal performance at 12 VDC and 70 °F, as reported by
Moteck") plots speed and current against load. The lines aren't
labelled, but read as speed falling from about **23 mm/s with no load to
about 14 mm/s at 4,500 N**, while current rises from about **2 A to
about 11.5 A**. The values are read off the curve, so they're
approximate. Read that way, a lift that draws much more current, or
moves much slower, than this with a light load points to the actuator
or wiring. That's an inference, not a Harmar test procedure.

The end-of-stroke clutch is the ratchet a tech hears at full travel. See
the operation notes on [[AL-Series-Outside-Vehicle-Lifts]] (normal only
going **up**).

## Ball nut (sheet 2)

- Thread **15/16-16UN-2A** (external), 1.00 in square body, 1.8 in long,
  Ø0.87 in neck.
- Material SCM415HL2, hardness **58–62 HRC**, tensile strength at least
  **5 tons force (4,536 kgf)** in Harmar's compression test.
- The test setup threads the ball nut into a nut plate until its sides
  are **parallel with the plate's sides, about ¼–½ turn short of fully
  seated**. That matches the video's install step: back the nut off
  until its flats are parallel to the tube walls, then fit the locking
  tab.

## Still open

No torque values for the actuator-to-tube screws or the locking-tab bolt
are on this drawing or anywhere else on file. Ask Harmar
(800-833-0478).

## Feeds into

[[AL-Series-Outside-Vehicle-Lifts]], [[Harmar Parts Diagrams]],
[[Actuator Removal Instructions (ALA10010-INS rev 2)]],
[[Video - How to Replace the Actuator (AL-100)]], [[Ingestion-Backlog]]
