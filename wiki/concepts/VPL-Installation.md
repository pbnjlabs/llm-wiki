---
type: concept
tags: [vpl, porch-lift, installation, pms, bruno, harmar, workflow]
---

# VPL Installation

How PMS installs a porch lift (vertical platform lift), from approval to
handover. The **PMS workflow** comes from the human (house practice). The
**manual requirements** come from the install manuals, which set the
spec. Models: [[VPL-3100B]], [[VPL-3200B]] (Bruno), [[HighlanderII]]
including VPL400-X (Harmar).

Comes after [[Porch-Lift-Evaluation]]. Per-job checklist:
[[VPL Install Template]].

## PMS workflow

### 1. Approval → order the lift
- The job is **approved only after the initial evaluation**
  ([[Porch-Lift-Evaluation]]). **Nothing is done at the evaluation
  visit.**
- **On approval, order the lift.**
- **All prep and site modifications are scheduled and finished between
  ordering and delivery.** The lift should never arrive at a site that
  isn't ready.

### 2. Prep and site modifications
Everything the evaluation flagged counts as prep, and all of it is
finished **before the lift is delivered**:

- **Concrete pad**: see the pad spec under Manual requirements.
- **GFI outlet**: within 10 ft of the VPL, reset button reachable, not
  under a deck or crawl space. When an electrician does it:
  [[PMS Electrical Work Orders and Preferred Electricians]] ($450
  approval limit). Because the GFI is prep, it goes in **before** the
  lift. (The 2024 example work order had the lift in first.)
- **Fascia**: smooth, vertical, sound, 3/8–3/4 in running clearance.
  Use treated decking boards, not plywood
  ([[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]).
- **Permits and inspections**: **not required in every state**. Check
  local requirements for each job.

**Who does it depends on the technicians' capabilities.** A PMS tech
does the work they're able to do; the rest is subbed out (e.g. an
electrician for the GFI).

### 3. Crew, tools and transport
- **Crew of 2.** (Bruno also says never work alone, and the lift weighs
  700–800 lb.)
- **Tools:** the install manual lists what's needed (Bruno's list is
  under Manual requirements), but in practice it comes down to:
  - socket set
  - Allen wrenches
  - wrenches
  - level
  - tape measure
  - hammer drill with bits (for the pad anchors)
- **Transport:** the lift travels **easiest on a trailer** to the job
  site.

### 4. On site: install
PMS order, per the human. Manual specs for each step are under
**Manual requirements** below.

1. **Stand the tower** on the pad.
2. **Assemble the platform and platform walls.** The **platform gate**
   (if the job has one) goes on at the same time as the walls.
3. **Install the upper gate** (top landing gate;
   [[Top-Landing-Gate-Installation]]).
4. **Shift the lift into place**, aligned to the top landing opening.
5. **Level the lift** (plumb both ways; shim at the mounting holes).
6. **Check clearances**: running clearance to the fascia and upper sill
   clearance, both **3/8–3/4 in**.
7. **Anchor the lift** to the pad.
8. **Set the upper limit** (top landing / final limit switch). Never
   touch the drive nut retention hardware.
9. **Wire in the call/send and upper gate** (in conduit).
10. **Install the gate actuator** (the activator/cam that works the gate
    interlock; [[Top-Landing-Gate-Installation]]).
11. **Install the covers.** The top cover pushes the service switch back
    down to normal operation.

Steps 6 and 8 need the lift running: on a Bruno, that means power
plugged in, top cover switch pulled up (service), breaker in and
batteries connected (VPL-3100B pp.10–11). On a Harmar, use Service /
Bypass Mode.

### 5. Test, photos and handover
1. **Test all functions.** Minimum: the manual's test list under
   Manual requirements (underside panel, top cover, final limit,
   door/gate interlock, key switches, call/send, E-stop).
2. **Photos:**
   - **Multiple pictures of the lift from the landing**
   - **Wide-angle picture of the completed job**
   - **Pictures of the serial number**
3. **Instruct the user on the unit**, going down the customer handover
   form ([[PMS Porch Lift Install Instructions and HISA Final Payment]]):
   safety platform, 600 lb limit, key switch, emergency down crank, GFI
   check, charging (DC) or power-only (AC), owner's manual, annual PM
   offer. Have the user run the lift while you watch (Bruno, and Joint
   Commission: written and verbal instructions).
4. **Get the required signatures**: the customer initials and signs the
   handover form. **VA/HISA jobs** also need the statement of
   satisfaction (veteran), the installer's UFAS / Southern Building Code
   statement, the final invoice and the color photos (the photos above
   cover these).

## Manual requirements

From the [[VPL-3100B Install Manual]] (pp.5–11, 29–31) unless noted.
The [[VPL-3200B Install Manual]] and the Harmar manuals
([[Highlander II Install Manual (no enclosure)]],
[[Highlander II with Enclosure Installation and Service Manual]],
[[VPL400-X Install Manual]]) have their own versions; go by the unit's
manual.

### Site must be ready before install
| Item | Requirement |
|---|---|
| Concrete pad | **4 in thick, 3500 psi minimum, reinforced**, level and flat, in place before install (not supplied by Bruno). **Never** on asphalt, patio stones, concrete blocks or other unstable surfaces. Freezing climates: about **15 in compacted rock + 1.5 in insulation** under the slab. PMS eval minimum: **5 × 5 ft** ([[Porch-Lift-Evaluation]]) |
| Power | **15 A grounded outlet** installed by a qualified electrician to local code. Outdoors: **GFI, 120 V, 15 A** (NEC). The charger draws 3 A max |
| Control wiring | Kit cabling **isn't outdoor-rated**: run it in **conduit or raceway** (tower knockouts take 1/2 in conduit) |
| Fascia | Smooth, non-perforated, vertical, structurally sound, fastened from the upper to the lower landing sill, takes a **125 lb side load over any 4 in square**. Running clearance **3/8–3/4 in** (ASME A18.1). See [[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]] |
| Upper sill clearance | Platform floor to upper landing sill **3/8–3/4 in** |
| Headroom | **80 in minimum** through the whole travel (Bruno). PMS eval wants **100 in, 120 in for a 72 in VPL** |
| Pathway | No conduit, wireways, or liquid/steam/gas discharge in the platform's path; area well lit |
| Path in | A clear path to move the unit into place (VPL-3153B weighs **705–745 lb**, VPL-3175B **758–798 lb**) |
| Parts | Check the order form against what arrived; **ramp and ramp activator on the correct side** (moving them is an involved procedure, pp.32–34) |

Harmar ships with a **temporary power cord**; the **NEC requires
permanent wiring within 60–90 days**, and there's no disconnect supplied
([[HighlanderII]], from [[Harmar Product Insights (2021-2023)]]).

### Tools (Bruno list)
Hammer drill with 1/2 in masonry bit, **four 1/2 in × 2-1/2 in (min.)
masonry anchors** (e.g. red head sleeve anchors, not supplied), torque
wrench (20–133 ft-lb), 4 ft level and plumb bob, volt-ohm meter, SAE
wrenches/sockets/Allens, wire stripper and crimper, pry bar, Sawzall,
circular saw, **appliance dolly**, 50 ft extension cord.

### Install sequence (VPL-3100B)
1. Pick the side for the call/send and gate harnesses **before** placing
   the unit.
2. Attach the support legs, stand the tower on the pad (it can be moved
   on its back or side), remove the front access panel.
3. Attach the platform deck, walls, ramp and any platform gate; connect
   the platform harnesses to the travel cable.
4. Place, align the platform to the top landing opening, **plumb both
   ways, shim** at the mounting holes (kit VPL-K-3103CP).
5. Plug in, install the top cover switch, pull it **up** (service
   position), push in the breaker, connect the battery Molex connectors.
6. Run up and down to check the **3/8–3/4 in** running clearance.
7. **Anchor** to the pad.
8. Set the **top landing / final limit switch**. **Never adjust the
   drive nut retention hardware** (factory set).
9. Top landing gate: [[Top-Landing-Gate-Installation]]; interlocks:
   [[Gate-and-Door-Interlocks]].
10. Wire the call/send (3-wire) and gate (6-wire) harnesses; mount the
    call/send box **at least 3 ft from the platform** (PMS eval: within
    10 ft) — white = up, black = down, red = key switch.

VPL-3200B differs: two half-towers joined with a hoist and coiled spring
pins, plus an emergency lowering kit at the lower landing
([[VPL-3200B Install Manual]]). Harmar: use **Service Mode / Bypass
Mode** instead of jumpers, and **check the safety nut and retaining bolts
for shipping looseness** before the first run ([[HighlanderII]]).

### Tests before handing over (VPL-3100B p.31)
- **Underside panel:** push up on several spots; downward travel stops
  from every station.
- **Top housing cover** removed: all controls dead.
- **Final limit** pressed: no movement in any direction.
- **Door/gate interlock:** door open → no movement; door opens only with
  the platform at the top.
- **Platform key switch** off: platform controls dead.
- **Call/send** key off: station controls dead.
- **E-stop** stops the unit.

Then remount covers and panels, clean up, and have the user run the lift
while you watch.

## Joint Commission (house standard)

Delivery, setup, patient training (written and verbal) and the record of
the home's suitability fall under [[Joint-Commission-DMEPOS]]; see the
same section on [[Porch-Lift-Evaluation]].

## See also

[[Porch-Lift-Evaluation]], [[VPL-Troubleshooting]],
[[Top-Landing-Gate-Installation]], [[Gate-and-Door-Interlocks]],
[[Battery-Charger-LED-Diagnostics]], [[PMS-Office-Procedures]]
