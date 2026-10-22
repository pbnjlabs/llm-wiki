---
type: source
manufacturer: Bruno
model: VPL-3300B
doc_type: Install Manual
source: "MANUALS/Bruno/VPL/3300B-I VPL-3300B Installation 03-29-2022.pdf"
date: 2022-03-29
tags: [vpl, bruno, vpl-3300b, vpl-3353b, vpl-3375b, commercial, install]
---

# VPL-3300B Installation Manual (unenclosed commercial, 3300B-I, 03-29-2022)

Install manual for Bruno's **unenclosed commercial battery VPL**:
VPL-3353B, and VPL-3375B, which sometimes ships with the platform off
(57 pages). Listings: **ASME A18.1 Section 2**, CSA B355, B44.1/A17.5,
NEC, CEC. **Unenclosed travel is limited to 60 in** under A18.1 Section 2.

**Specs:**
- 750 lb. **793 / 835 lb (3353B, 17 / 34 Ah).**
- 10 ft/min. ½ hp 24 VDC (2 hp peak). Charger 120 VAC 3 A.
- **53 in travel.** Platforms up to 42 × 60.
- **Top and bottom final limit switches as standard.**
- Options: canopy, **telephone kit**, cold-weather package, **pit
  switch**, door/gate operator.

**Electrical (differs from residential):**
- **Hard-wired AC to a dealer-supplied disconnect.** GFI 15 A where code
  requires; the charger draws 3 A.
- **Junction boxes on both sides of the tower** (5 × ½ in NPT each):
  - The **upper box takes the AC input** (factory default is the
    lower-landing side).
  - The lower boxes take the **landing controls**: the 6-wire gate
    harness (with call/send) and the 3-wire call/send harness.
  - Swap sides by re-routing through the cable bushing.
- **Call/send box:** mount it **at least 3 ft from the platform**. Wires
  **white = up, black = down, red = keyswitch**.
- **PCB-00164 timer** for the electric strike or door operator:
  - Adjustable **1–10 s** output: S2/VR2 and JP8 for the top landing,
    S1/VR3 and JP9 for the bottom.
  - A landing button press re-unlocks the strike or restarts the door
    operator.
- **PCB-00164 LEDs:**
  - None lit = the E-stop, top cover or nut safety circuit is open.
  - Bottom 4 lit = safeties OK (the safety switch, pit switch, top or
    bottom final limit are closed).
  - Others show up or down, and the timer running at each landing.

**Install:**
- Breaker in, **white Molex battery connectors** joined.
- **Top cover push-pull service switch** as on the residential lifts.
- Running clearance ⅜–¾ in for the full travel. Anchors are ½ in
  red-heads.
- Limit bracket from the factory mark. **Never touch the red drive-nut
  retention nuts.**
- **Gates (standard or wide):** the smooth face goes toward the platform.
  Drill a ½ in hole in the landing for wiring if needed. Level and plumb.
- **Cam and actuator:** 1.5 in below the landing, **2 in gap**.
- **Platform gate extension foot:** measure latch-rod tip to ground, add
  **1.25 in**, cut, seal the cut end, and threadlock it on.

**Tests:**
- **With the gate wheel held unlocked, the platform must stop within
  2 in going down.**
- Underpan, top cover, **top and bottom final limits**, interlock, keys,
  E-stop.

**Batteries:**
1. AC off, top cover off, breaker out, service switch up.
2. Remove the hold bar. **Don't bump the platform**: the batteries can
   slide out.
3. Anderson and Molex connectors.
4. **BTR-12003 (17 Ah) or BTR-12001 (34 Ah).**

**Charger:** 4-LED chart. Fault or over-temperature reset: unplug AC and
the battery for 1–2 min, then reconnect; if it still won't charge,
replace the charger.

**Troubleshooting:**
- AC voltage and voltage drop.
- Batteries.
- Belts.
- **Motor if the relays click.**
- Gate switches, underpan, limits, PC board fuse (24 V short), breaker,
  top cover switch, final limits.
- Squeal: SHC 100 every 6 in.

**Maintenance and warranty:** the same 12-month and 2-month lists as the
residential lifts (ILS-01444; the weekly checklist applies to commercial
units). Warranty is 2 years on major components and 1 year on parts.

Feeds: [[VPL-3300B]], [[VPL-Maintenance]], [[VPL-Troubleshooting]], [[Gate-and-Door-Interlocks]], [[Automatic-Door-Operators]], [[VPL-Installation]]
