---
type: source
manufacturer: Bruno
model: VPL-3153-3175
doc_type: Install Manual
source: "MANUALS/Bruno/VPL/3100-I VPL-3100 Installation 05-19-2025.pdf"
date: 2025-05-19
tags: [vpl, bruno, vpl-3153, vpl-3175, ac, install]
---

# VPL-3100 (AC) Installation Manual (05-19-2025)

Install manual for Bruno's **AC-powered residential VPL**: the
**VPL-3153** and **VPL-3175**, with no batteries (58 pages). It is the
**first AC VPL manual on file**. The layout follows the battery
[[VPL-3100B Install Manual]].

**Specs:**
- 750 lb. Unit weight **656 lb (3153) / 713 lb (3175)**.
- **9 ft/min.**
- **120 VAC 8 A single-phase**, **½ hp 90 VDC motor**, 24 VDC controls.
- Platforms 36 × 48 standard, plus 36 × 60 and 42 × 60.
- Emergency: an **optional hand wheel only**. There is no battery
  backup.
- Options: call/send stations, platform alarm, handrail, platform gate,
  36 in or 42 in top landing gates (EMI or ESI), 90° platforms, GAL and
  electric-strike interlock kits.

**Site:**
- A **dedicated GFI 120 V 15 A circuit**. Long wire runs change
  performance.
- **4 in, 3500 psi reinforced slab.** Four ½ in (⅜ in bolt) × 2½ in
  anchors (red-head sleeve anchors).
- Outdoors: 15 in compacted rock, 1.5 in insulation where it freezes,
  then the slab.
- **80 in headroom.** **Sill gap ⅜–¾ in.** Fascia smooth and solid, takes
  **125 lb on 4 sq in**.
- The tower can be tied to a wall through the 5/16-18 holes; the housing
  must stay intact.
- Drawings ILS-01557 to 01562, ILS-00938 and ILS-00804.

**Install:**
- Bolt the platform to the tower (pull the control panel first).
- Fit the **top cover push-pull switch**: pull it up to run during
  service, and the cover pushes it down.
- Plug in the cord, check clearances and plumb (shims), then anchor.
- **Top landing and final limit:** measure the platform-to-landing
  offset from the factory mark on the channel, unplug, and slide the
  bracket.
- **The red-marked nuts are factory set. Don't touch them**: the platform
  could fall.
- **Gates:** 36 in EMI or ESI, or 42 in. Fix to the sill with ¼ in
  flat-heads or #14 wood screws. The sill must be flush with the fascia,
  and the gate level and plumb.
- **Cam and activator:**
  1. Start with the platform **1.5 in below the landing**.
  2. Set a **2 in gap** between the gate post and the activator's flat
     edge.
  3. Raise the activator until it just touches the cam.
  4. The gate must unlock at the landing.
- Call/send and gate harnesses go through the tower side punch-outs
  (sized for ½ in conduit).

**Tests:**
- **Safety pan** stops downward travel only.
- Top cover switch. **Top final limit** stops everything.
- Gate interlock (it opens only at the landing).
- Key switches and the E-stop.

**Reversing the ramp:** move the vertical bar (4 screws), the ramp
brackets (to the diagonal corners; mind the **nylon washers**), and the
activator wheel, with the cotter pin and steel washer outside.

**Emergency and cold:**
- Hand wheel: **power off**, top cover off, wheel in the brake shaft
  opening, **counter-clockwise to lower**.
- **Below 0 °F:** park mid-way, and warm it up with a down, up, then
  board cycle. A cold-weather package is available.

**Troubleshooting** (AC-specific rows):
- **Outlet not a dedicated 15 A circuit.**
- Loose belts.
- Gate and door switches, the safety pan, limits, the top cover switch.
- **Blown fuse (check for a 24 V short)**, the internal breaker, field
  wiring, the final limit.
- **Controller fault:** press the E-stop, wait 5 s, and pull it out. This
  also clears a button stuck at power-up or both buttons pressed.
- **Squeal:** **Mobil SHC 100 every 6 in along the ACME screw.**

**Maintenance** (per ILS-01444):
- **Every 12 months:**
  - Belts, pulleys and keys, motor, ACME screw and nuts, grease, pads and
    rollers, bearing.
  - Stops within **½ in** of the landing.
  - Controls, wiring (dielectric grease outdoors), cleanliness ("mouse
    nests"), the mechanical gate lock.
  - The checklist also lists "batteries", a carry-over from the DC
    manual.
- **Every 2 months:**
  - Electronic interlock: the platform must not move with a door open.
  - **GAL: no more than 2 in of movement.**
  - Safety pans.

**PCB-00143 board:**
- LEDs E1–E18 (power, top cover, E-stop/nut safety, gates, enables,
  limits, safety pan).
- **E18 red flashes the fault:**

| Flashes | Fault |
|---|---|
| 1 | Stall |
| 2 | Stall + over-temperature |
| 3 | Over-temperature |
| 4 | 24 V overload |
| 5 | Overvoltage |
| 6 | Over-current |
| 7 | Max current (motor failing) |
| 8 | Low AC |
| 9 | Low 24 VDC |

- Short flashes plus one long, added together.
- The E-stop clears most faults; otherwise unplug for 1 min.
- **Wait 3 min after unplugging** before touching the board (high
  voltage).

**Warranty:** residential VPL Gold, **2 years on major components** (motor,
ACME screw and nut, brake, pulleys, belt, bearings), **1 year on parts**,
30 days labor.

Feeds: [[VPL-3153-3175]], [[VPL-Maintenance]], [[VPL-Troubleshooting]], [[VPL-Installation]], [[Gate-and-Door-Interlocks]]
