---
type: concept
tags: [vpl, bruno, drive, acme-screw, drive-nut, belts, bearings, guide-pads, maintenance]
---

# VPL Drive Service (Bruno)

The mechanical side of a Bruno VPL: ACME screw, drive nuts, bearings,
belts, brake, guide pads and motor. Built from Bruno's dealer-portal tech
tips (2010–2021) and **ILS instruction sheets** (2007–2023), checked
against the [[VPL-3100B]] and [[VPL-3200B]] manuals. The ILS sheets rank
with the manuals (newer revision wins); the tech tips rank below them.
For symptoms (hum, squeal, shudder, won't lift), start at
[[VPL-Troubleshooting]] §7–8. Schedules and inspection checks:
[[VPL-Maintenance]].

## How the drive works

The motor turns the ACME screw through **two belts and pulleys** at the
top of the tower. The screw **hangs from a thrust bearing** in the brake
mounting plate at the top; the lower bearing only keeps it straight.
Two **ACME drive nuts** on the carriage ride the screw, with a **nut
safety switch** behind them that stops the lift if the load nut fails.
Guide pads and ball plungers keep the carriage square in the tower.

## Rules that matter for safety

- **Drive nut retention hardware is factory-set: don't adjust it**
  ([[VPL-3100B]] manual). Bruno's replacement tips agree: when nuts are
  replaced, the bolts end with **4–6 threads past the nut** and are
  **free to move up and down by design**.
- **Gap between the two drive nuts: ½ in (12.7 mm).** Never let the bolts
  draw the nuts together: Bruno warns of **serious injury or death**.
  Less than ½ in in service, or the **nut safety switch pressed** →
  replace the nuts and keep the lift **out of service** until done.
- **Brass shavings** at the bottom of the tower = the nuts are wearing.
- The screw must **never rest on the lower bearing** (about a **¼ in
  gap** at the bottom of the journal; the 2022 tall-VPL sheet gives
  about **3/16 in** from the bearing top to the threads).
- **Nut safety switch:** never bypass it. Test it with tool
  **VPL-32422** (ILS-01544, all VPLs): with the carriage blocked, the
  tool goes between the activation plate and the switch, and the lift
  must not run either way. **If the tool won't fit, the drive nut has
  dropped onto the safety nut: replace both nuts**
  ([[ILS - VPL ACME Screw, Nut and Bearing Service]]).
- ILS-01444 adds: the four drive-nut bolts need **at least ¼ in of
  play**. The 2022 tall-VPL sheet says they should lift about ½ in
  ([[ILS-01444 Maintenance Control Plan for VPLs]]).
- **Tall VPL screw joint (about 8 ft up):** the coiled spring pins must
  sit **below the thread root**. **Brass filings = lock the unit out**
  and order nut kit SRV-3200-002 (ILS-01185, Service Bulletin 60).

## Procedures

| Job | Key points | Source |
|---|---|---|
| **Short VPL screw and/or nuts** (kits SRV-3153-006 / SRV-3175-006) | Top cap switch up; carriage on a 12–16 in wood block; note belt tension first; measure the upper bearing position before pulling the screw; short bolt goes left rear; ½ in nut gap; kit grease on the screw; tighten the bottom bearing last, within 1 ft of it. **Rev 3 (2023) adds torques: motor nuts 150 in-lb, pulley locking hub bolts 95 in-lb**, then the ILS-01444 checks | [[Tech Tip - Short VPL ACME Screw and Nut Replacement (ILS-01129)]] (Rev 2, 2016); Rev 3 on [[ILS - VPL ACME Screw, Nut and Bearing Service]] |
| **Short VPL top bearing support** (ILS-01029, 2011) | Shim VPL-32194 at the bottom; drop the top bearing; support plate hole **7/8 in = OK**, **about 1 7/16 in = fit VPL-31933** (plate + 3 spacers per bolt); cross-corner torque; check pulley alignment | [[ILS - VPL ACME Screw, Nut and Bearing Service]] |
| **Tall VPL screw and/or nuts** (ILS-01538, 2022) | Platform off on a dolly; carriage on a block, not the stabilizer base; the joint pins hold the lower screw, so clamp it; **½ in nut gap (tool VPL-32422 fits)**; bearing plate **35 ft-lb**, lower bearing **18 ft-lb**; Nyloc nuts loose, 4–6 threads; switch bracket **10 ft-lb**; Mobil SHC 100; test on setup harness VPL-32249 | [[ILS - VPL ACME Screw, Nut and Bearing Service]] |
| **Tall VPL joint pins** (ILS-01185 / ILS-00975, 2018) | One pin at a time; clean the grease, then torch (fire extinguisher at hand); new coiled pins with retaining compound, **isopropyl alcohol only** to clean; press to depth with the tool; gauge must turn smoothly over the joint | same |
| **Tall VPL nuts** | All AC and battery power off, platform blocked, lower bearing out, nuts off the bottom; clean and re-grease the screw; ½ in gap; bearing bolts loose, run fully down, then tighten | [[Tech Tip - Tall VPL Drive Nut Replacement]] |
| **Lower bearing** | Check the top pulleys line up (if not, the screw dropped); heat the splined brake hub to free its Loctite and re-Loctite on assembly; ¼ in gap; brake plate bearing flush with the plate | [[Tech Tip - VPL Lower Bearing Replacement]] |
| **Belts** (serial 12020300831 on) | Pry the ground strap toward the back; motor studs **150 in-lb**; **⅛ in deflection mid-span at 2½–3½ lb**; never loose enough to slip under load | [[Tech Tip - VPL Field Tensioning of Belts]] |
| **Belts (ILS-01444, 2022)** | **About ½ in deflection**, one belt at a time, halfway between the pulleys; short VPL: pry the motor; **tall VPL: idler at 60 in-lb** with a torque wrench in its 3/8 in hole; belt dressing if dry | [[ILS-01444 Maintenance Control Plan for VPLs]] |
| **Guide pads shudder or grab** (TSG-VPL-007, 2021) | Round off the pad edges; outside pads: corner bolts ¼ turn at a time; re-seat the screw by running with the lower bearing bolts loose; **0.5–0.75 in deflection is normal**; ball plungers bottomed then **back ¼ turn** at the least-deflection point | [[Tech Tip - VPL Guide Pad Adjustment (TSG-VPL-007)]] |
| **Squealing** | Ball plungers first; then square the screw: under 90° shim the back, over 90° the front | [[Tech Tip - VPL Squealing and Not Lifting Rated Load]] |
| **Won't lift rated load** | Carriage not square → nut binds. Feeler-gauge the carriage-to-nut gap and shim to the next .005 in; jack the carriage ¼ in to fit it | same |
| **Old motor VPL-31496** (5-wire) → VPL-31953 (4-wire) | 14 AWG jumper **orange to brown** | [[Tech Tip - VPL-31496 Motor Replacement]] |

⚠️ **Belt tension conflict:** the 2016 tip says **⅛ in at 2½–3½ lb**;
Bruno's 2022 maintenance control plan says **about ½ in** (no force
given). They may describe similar tension measured differently, but
they read differently. **ILS-01444 is newer and ranks with the manuals:
use ½ in.** The tip's force figure is only useful with a tension gauge.

TechMate's noise steps (loosen the bearing block bolts and run it;
deflection ½ in or more → adjust the pads, back off ¼ turn) match the
2021 guide-pad tip. The tip's "0.5–0.75 in deflection is normal" is the
more precise number.

## Brake

**Commercial and newer residential VPLs have no separate brake**
(ILS-01444): the screw holds the load, and the spec sheets list
"precision landing control" for the DC units. On older residential units
the brake sits on top of the screw (three Allen screws). AC
VPL-3153/3175 units with **excess drift or coasting** can take Bruno's
2013 brake retrofit: **SRV-3100-032** (S/N 12070300108 on, with diode
module VPL-31989) or **SRV-3100-039** (PCB-00137 board: BRK+/BRK-,
**remove fuse F2**). Brake bolts **67 in-lb**, green Loctite 609 in the
keyway, blue 242 on the hub set screws
([[ILS - VPL Brake Retrofit Kits (AC VPL-3153-3175)]]). Bruno's old
troubleshooting guides: lift the **silver release handle** or remove the
brake, and see if it runs. AC relay-logic units feed the brake **105+
VDC** from a bridge rectifier; no voltage there with 115 VAC on the
rectifier input → rectifier. See
[[Tech Tip - Low-Rise AC VPL Troubleshooting Guides (2009-2010)]].

## Grease

**ACME screw: Mobil Aviation Grease SHC 100 (Bruno LUB-00114)**. The
2025 [[VPL-3100B Install Manual]] and [[VPL-3200B Install Manual]]
(preventive maintenance page), ILS-01444 and the 2022 tall screw/nut
sheet all name it; it's the "Bruno grease" in the kits. Degrease first
(Super Clean or similar). **Bearings:** Mobil Epic EP 102 through the
zerk, 1–2 squirts (ILS-01444). Guide-pad columns get a **dry
lubricant**; ILS-01444 says the **guide rails are not lubricated**.

## Cold weather

Outdoor VPLs in cold climates: travelling cable carrier kits, battery
heater pads (17 Ah or 34 Ah sets) and full cold-weather packages per
model ([[Tech Tip - VPL Cold Weather Solutions]]). Install steps and
thermostat points (DC nut heater on below 15 °F; battery pads on below
20 °F, off at 32 °F; tall-VPL blanket outlet 40–60 °F):
[[ILS - VPL Cold Weather and Battery Kits]].

## Joint Commission

Drive and nut checks are the safety-critical part of a VPL's
manufacturer maintenance; record them ([[Joint-Commission-DMEPOS]]).

## See also

[[VPL-Maintenance]], [[VPL-Troubleshooting]], [[VPL-3100B]],
[[VPL-3200B]], [[VPL-3300B]], [[VPL-3153-3175]], [[VPL-Installation]],
[[Bruno]]
