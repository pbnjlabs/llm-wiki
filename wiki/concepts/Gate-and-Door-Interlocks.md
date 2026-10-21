---
type: concept
tags: [vpl, platform-lift, interlock, gate, door, bruno, harmar, safety]
---

# Gate and Door Interlocks (platform lifts)

On a vertical platform lift (VPL), each landing gate or door has an
**interlock**: a lock plus electrical contacts. It does two jobs:

1. The gate or door **can only be opened when the platform is at that
   landing**.
2. The lift **won't run while any gate or door is open**.

Harmar's interlock is built to **ASME A18.1**, the platform lift
standard. Covers the Bruno [[VPL-3100B]] and [[VPL-3200B]] and the Harmar
[[HighlanderII]] (and VPL400-X).

## When one is needed

PMS evaluations record a **door interlock only when the VPL is installed
directly at the door**. Also record door direction (in/out, left/right,
including screen or glass doors) and the gate hinge side, standing in
the lift ([[Porch-Lift-Evaluation]]). Bruno's optional top landing
gates come with a Bruno interlock.

## Types

| Type | What it is | Where |
|---|---|---|
| **EMI** (electro-mechanical interlock) | A mechanical lock **released by the motion of the platform** (Bruno: an activator bracket on the platform and a gate wheel on the interlock), backed by electrical contacts that stop the lift while it's engaged | Bruno EMI top landing gates; Harmar's "approved interlocks (EMI) are Harmar and Honeywell" |
| **ESI** (electric strike interlock) | An electric strike on the gate, plus a separate gate actuator | Bruno ESI top landing gates |
| **"GAL" interlock** | Electro-mechanical interlock kit for a **gate or door not made by Bruno** | Bruno option (L or R; also a top-landing version) |
| **Interlocks and strikes for doors by others** | Ship with the lift in the maker's packaging; install per their instructions | Harmar Highlander II |

Bruno recommends a **landing timer** with its flush-mount doors and
electric strike interlocks; it isn't needed with electro-mechanical
interlocks. Bruno's tech tips spell it out
([[Tech Tip - VPL Delay Timers and ESI Shut-off Timers]]):
- **Residential VPLs need a delay timer** (one per landing) for any
  platform gate operator, landing gate operator or door operator, and
  should have one for electric strikes. **Commercial VPLs** have a relay
  for operators; a timer is only recommended for strikes.
- Factory settings **3 s** (door operators) and **6 s** (interlocks),
  adjustable to about 30 s. Power left on an interlock shortens its life.
- Not for **Waupaca EMI III, Honeywell RDI2, Porta** or **GAL**
  interlocks.
- Tall VPL **ESI shut-off timer kits**: VPL-K-3222 (single), VPL-K-3223
  (dual), VPL-K-3225 (add-on); each landing also needs an extra limit
  switch from its interlock wiring kit.

Strikes and interlocks on Bruno's wiring sheets: **HES 5200** and **Von
Duprin 6211** electric strikes (the Von Duprin is on the flush-mount
doors), **Waupaca** EMI and **Euchner** interlocks
([[Tech Tip - VPL 90V Board PCB-00143 (TSG-VPL-004, SCH-00229)]],
[[Tech Tip - VPL Door Interlock Wiring (Waupaca, HES 5200, Upper Gate Switches)]]).
Waupaca wiring kits changed in **July 2012**: VPL-K-3138 (upper door) and
VPL-K-3139 (lower door) replace VPL-K-3121 / VPL-K-3131. A **GAL**
interlock on a wood gate post needs the post machined to Bruno's drawing
([[Tech Tip - GAL Interlock Wood Posts (Left and Right)]]).

**Code** (ASME A18.1 excerpt, [[Tech Tip - Code Requirements for Door Interlocks]]):
every door needs a combination **mechanical lock and electric contact**;
it may unlock only with the platform **within 2 in** of that landing, and
the platform must stop if it gets more than 2 in away before the door
locks. Residential (Section 5) follows the commercial door rules
(Section 2). Offset doors need a **toe guard** round the interlock; Bruno
recommends **flush doors** ([[Tech Tip - Tall VPL Flush Mount Doors]]). VA FSS prices (Bruno): EMI top landing gate $695.75 (36 in)
or $833.09 (42 in); ESI $1,196.25 / $1,344.75; interlock kit for a
gate or door not by Bruno **$462.00**; landing timer $187.01
([[Bruno VA FSS Price List (2021-2026)]]). These are the ceiling for
VA work ([[VA-FSS-Contracts]]).

## Installing

**Bruno** (full steps on [[Top-Landing-Gate-Installation]]):
- Route the gate wiring from the interlock (latch) post to the VPL; it
  can exit the side or the bottom.
- Choose the gate wheel (offset or straight) by platform and hand.
- **Cam and activator adjustment is the interlock's core safety
  check.** The gate must **unlock at landing level**. With the gate
  wheel held unlocked, the platform must **stop within 2 in** of the
  unlock point when run down.

**Harmar Highlander II / VPL400-X**
([[Highlander II Install Manual (no enclosure)]], [[VPL400-X Install Manual]]):
- Route the interlock and call/send wires through the trailing cable.
  The manual has three layouts: call/send and interlock in a gate post,
  both in the same location, or in different locations.
- **Install the interlock beak last**, on the gate's keeper panel, so it
  slots into the interlock when the gate closes. Gates are field
  reversible (call Harmar Technical Service for how).
- The PC board is static-sensitive: **wear a static strap and watch wire
  colors and positions at the interlocks.** Don't add jumpers; use
  Service Mode instead.

## Harmar vs Honeywell interlocks (Highlander II)

From 7/18/2022, Harmar fits **its own interlock** in place of the
Honeywell ([[Bulletin - New Harmar Interlock Introduction]]):

| | Honeywell (before 7/18/22) | Harmar (from 7/18/22) |
|---|---|---|
| Internal jumper | B to D | **B to C** |
| Wires | White, orange, green | White, red, green (yellow stripe on the cable) |
| Landing gates | Plus a black wire | Plus a black wire |

- **The Harmar interlock doesn't fit pre-7/18/22 gates.** Newer gates
  accept either brand. Tell LiftSquad support which brand is on the unit
  for any warranty claim.
- IP65, field hand-switchable, commercial-rated, round barrel key.
- **On a platform gate the lift jogs up twice before running normally.**
  That's intentional (a solenoid-enable feature). Two spacer washers
  between the keeper and keeper plate make it work.

## Testing and maintenance

- **At install (Bruno):** with the door open, the VPL must not run in
  any direction, and the door must only open with the platform at that
  landing. Test the panel sensors, top cover sensor, final limit, key
  switches and E-stop at the same time ([[VPL-3100B Install Manual]]).
- **Every 2 months (Bruno operator manuals):** with an **electronic
  door interlock**, the platform must not move when any door isn't
  closed and locked. With a **GAL interlock**, it must not move more than
  **2 in** from the landing.
- **Harmar owner maintenance:** check all interlocks, strikes and
  obstruction sensors.
- **Train the user** on gate and door use and the status lights at
  handover. Joint Commission requires written and verbal instructions
  ([[Joint-Commission-DMEPOS]]).

## Troubleshooting

| Symptom | Check |
|---|---|
| **Bruno VPL: door stuck locked** | The spring-loaded interlock spring can partially fail. With the lift at the top, pull the friction-fit post cap and push the lock rod down by hand. If it doesn't spring back, or springs back slowly, **replace the interlock assembly** (VPL-31452L, left hand; right-hand number not on file). The call/send station comes off the post with four screws for access. See [[2026-10-01 Bruno-VPL door interlock spring]]. |
| Bruno VPL: lift runs with the platform gate open | Jumper left in. VPL-3200B with platform gate, serials 11080300300–11100301707: remove the 6-pin blue-wire jumper plug in the lower interlock harness ([[Tech Tip - VPL-3200B Lower Interlock Jumper Issue (2011)]]). |
| Bruno VPL: Waupaca interlock dead | 24 V at pins 3–4 needs the bottom tower limit made; jump 1–2 to bypass; terminal block must be at the **top** ([[VPL-Troubleshooting]]). |
| Bruno VPL: door locked at its own landing | Timer timed out: press the landing button at least 1 s. |
| Highlander II: no function, **top cap solid red** | Check the E-stop and the **interlocks** ([[HighlanderII]]). |
| Highlander II: which gate is open? | On the control board, the **Bottom/Mid/Top Gate** green LEDs mean that gate's interlock is closed; **Bottom/Mid Lock** green means the lock is active ([[Highlander II with Enclosure Installation and Service Manual]]). |
| Highlander II platform gate jogs up twice | Normal with the Harmar interlock (see above). |

## Other things called "interlocks"

These aren't gate or door interlocks:
- **Bruno VPL top cover service switch**: the lift won't run with the
  top cover off ([[VPL-3100B]]).
- **Golden power seat**: speed is limited by seat height
  ([[Golden-Power-Seat-Operation]]).
- **LiNX OONAPU**: the chair won't drive if the joystick is off center at
  power-up ([[LiNX-Diagnostics]]).
- **Harmar Pinnacle stairlift seat swivel**: the seat reports an
  "interlock" when it isn't locked in the travel position
  ([[Bulletin - Pinnacle Seat Swivel Modifications]]).
- **Harmar AL625 van lift**: ships with an "interlock install kit". The
  manual doesn't say what it interlocks
  ([[AL625-AL625HD Installation and Owner's Manual (2012, Rev B)]]).

## See also

[[VPL-3100B]], [[VPL-3200B]], [[HighlanderII]], [[Top-Landing-Gate-Installation]],
[[Porch-Lift-Evaluation]], [[Bruno]], [[Harmar]], [[VPL-Troubleshooting]] (Bruno closed/locked/enable switch wire colors and board test points, from TechMate)
