---
type: concept
tags: [vpl, bruno, drive, acme-screw, drive-nut, belts, bearings, guide-pads, maintenance]
---

# VPL Drive Service (Bruno)

The mechanical side of a Bruno VPL: ACME screw, drive nuts, bearings,
belts, brake, guide pads and motor. Built from Bruno's dealer-portal tech
tips (2010–2021), checked against the [[VPL-3100B]] and [[VPL-3200B]]
manuals. **The manuals win.** For symptoms (hum, squeal, shudder, won't
lift), start at [[VPL-Troubleshooting]] §7–8.

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
  gap** at the bottom of the journal).

## Procedures

| Job | Key points | Source |
|---|---|---|
| **Short VPL screw and/or nuts** (kits SRV-3153-006 / SRV-3175-006) | Top cap switch up; carriage on a 12–16 in wood block; note belt tension first; measure the upper bearing position before pulling the screw; short bolt goes left rear; ½ in nut gap; kit grease on the screw; tighten the bottom bearing last, within 1 ft of it | [[Tech Tip - Short VPL ACME Screw and Nut Replacement (ILS-01129)]] |
| **Tall VPL nuts** | All AC and battery power off, platform blocked, lower bearing out, nuts off the bottom; clean and re-grease the screw; ½ in gap; bearing bolts loose, run fully down, then tighten | [[Tech Tip - Tall VPL Drive Nut Replacement]] |
| **Lower bearing** | Check the top pulleys line up (if not, the screw dropped); heat the splined brake hub to free its Loctite and re-Loctite on assembly; ¼ in gap; brake plate bearing flush with the plate | [[Tech Tip - VPL Lower Bearing Replacement]] |
| **Belts** (serial 12020300831 on) | Pry the ground strap toward the back; motor studs **150 in-lb**; **⅛ in deflection mid-span at 2½–3½ lb**; never loose enough to slip under load | [[Tech Tip - VPL Field Tensioning of Belts]] |
| **Guide pads shudder or grab** (TSG-VPL-007, 2021) | Round off the pad edges; outside pads: corner bolts ¼ turn at a time; re-seat the screw by running with the lower bearing bolts loose; **0.5–0.75 in deflection is normal**; ball plungers bottomed then **back ¼ turn** at the least-deflection point | [[Tech Tip - VPL Guide Pad Adjustment (TSG-VPL-007)]] |
| **Squealing** | Ball plungers first; then square the screw: under 90° shim the back, over 90° the front | [[Tech Tip - VPL Squealing and Not Lifting Rated Load]] |
| **Won't lift rated load** | Carriage not square → nut binds. Feeler-gauge the carriage-to-nut gap and shim to the next .005 in; jack the carriage ¼ in to fit it | same |
| **Old motor VPL-31496** (5-wire) → VPL-31953 (4-wire) | 14 AWG jumper **orange to brown** | [[Tech Tip - VPL-31496 Motor Replacement]] |

TechMate's noise steps (loosen the bearing block bolts and run it;
deflection ½ in or more → adjust the pads, back off ¼ turn) match the
2021 guide-pad tip. The tip's "0.5–0.75 in deflection is normal" is the
more precise number.

## Brake

The brake sits on top of the screw (three Allen screws). Bruno's old
troubleshooting guides: lift the **silver release handle** or remove the
brake, and see if it runs. AC relay-logic units feed the brake **105+
VDC** from a bridge rectifier; no voltage there with 115 VAC on the
rectifier input → rectifier. See
[[Tech Tip - Low-Rise AC VPL Troubleshooting Guides (2009-2010)]].

## Grease

Use **Bruno's grease** on the screw (supplied in the screw/nut kits and
the cold-weather kits). The tips don't name it. Clean the old grease off
before re-greasing. Guide-pad columns get a **dry lubricant**.

## Cold weather

Outdoor VPLs in cold climates: travelling cable carrier kits, battery
heater pads (17 Ah or 34 Ah sets) and full cold-weather packages per
model ([[Tech Tip - VPL Cold Weather Solutions]]).

## Joint Commission

Drive and nut checks are the safety-critical part of a VPL's
manufacturer maintenance; record them ([[Joint-Commission-DMEPOS]]).

## See also

[[VPL-Troubleshooting]], [[VPL-3100B]], [[VPL-3200B]], [[VPL-3153-3175]],
[[VPL-Installation]], [[Bruno]]
