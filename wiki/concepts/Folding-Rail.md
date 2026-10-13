---
type: concept
tags: [stairlift, bruno, folding-rail, option]
---

# Folding Rail (Manual and Power)

An option on Bruno straight-rail stairlifts where the bottom section of
rail folds up out of the walkway when not in use. Confirmed shared across
[[SRE-2010]] (Elite), [[SRE-3000]], and [[SRE-3050]] (Elan) — Bruno
publishes a single "SRE Folding Rail" install supplement
([[SRE-2010 Folding Rail Install Manual]]) covering both current model
lines, and near-identical procedures/figures also appear in the SRE-3000
and SRE-3050 install/tech-support guides.

## Mid-park position

Central safety concept: the carriage has a mid-park stop position on the
rail.
- **Manual folding rail**: carriage must be at or above mid-park before
  the rail can be folded up by hand (via a fold handle) — folding below
  that position damages the unit.
- **Power folding rail**: will *only* fold/unfold when the carriage is at
  mid-park; the carriage won't move past mid-park until the rail has
  fully folded/unfolded. A continuous beep and flashing yellow LED warn
  bystanders while the rail is in motion. An obstruction-detection system
  stops and reverses the rail briefly if it senses a jam.
- A **disable switch** on the power folding rail control box lets a
  technician keep the rail folded down for extended periods, or manually
  raise/lower it in an emergency (gently — fast manual lifting can damage
  the gearbox).

## Logic board update: PCB-00193 (power folding rails, 2026)

Bruno told dealers in a 2026 email that **future SRE-3050 and SRE-2010
power folding rails** get new circuit board logic and a new down limit
switch setup, so the carriage **can't move by accident at the mid-park
if a wire breaks or a connector comes unplugged**. **Manual folding rails
aren't affected.**

- **New board PCB-00193** replaces **PCB-00157**.
- **Spot it** by the **notch around the down limit switch** on the rail
  bracket and the PCB-00193 label on the rail's board.
- The email's schematic redraws the down limit switch, and gives the rail
  wiring colors (down limit blue/brown, up limit white/green, mid-park
  purple, disable switch orange). Updated schematics are going on
  Brunopartner.
- On an older rail (PCB-00157), a broken wire or loose connector at the
  rail is the failure this change guards against, so check those first
  if the carriage misbehaves at mid-park. That's the wiki's reading, not
  Bruno's wording.

Source: [[SRE-3050 and SRE-2010 Power Folding Rail Logic Board Update]]
(a clipped dealer email; ranks below the manuals but is newer than all
of them).

## Folding Rail Carriage Safety Bracket

A retrofit safety bracket, added because the carriage could rarely bypass
mid-park (if the charge/communication fingers lose contact with the charge
strip) and impact the folded short rail. With the bracket installed, any
such impact trips the carriage's safety-panel switch and stops it before
damaging the folding rail assembly.
- **Elite (SRE-2010)**: bracket mounts over the downside carriage cover.
- **Elan (SRE-3050)**: bracket mounts on the carriage's downward safety
  panel (part SRE-30609WG).
- Both use the same M5 screws (MBHCL-05007) and U-shaped nut bar
  (SRE-30610) — same fastener kit, different mounting geometry per model.

## Installation notes

- Never cut a folding-rail assembly shorter than 75" (1905mm).
- Minimum 2 rail mounts per mid-rail section (excluding the fixed bracket
  at the folding joint).
- Charger can be wired at the top of the rail or at the rail joint,
  depending on install configuration (illustrated for SRE-3050 in the
  folding rail supplement).
- Bottom-of-rail-to-floor clearance: 1/8" (3mm) or less; a landing pad
  (SRE-30492WG) is used when thick carpet would otherwise prevent this.

## Common field issues (from tech support guides)

- **Clicking/crunching noise from power folding rail drive**: caused by
  gear tightness/shifting during shipping. Fix: loosen motor mounting
  screws, shift motor "uphill" away from the gear train to relieve
  pressure, retighten.
- **Resistance closing the folding rail**: apply a small amount of grease
  between the latches and on the backside of the joint alignment block.
- **Mid-rail gear rack binding**: units made after 2020-01-22 use a
  redesigned mid-rail gear rack segment (SRE-30179 LH / SRE-30181 RH) with
  a wider chamfer specifically to prevent this.
- **Joint misalignment**: a documented clamp-and-adjust procedure
  (loosen primary bracket screws, reposition, re-tighten gear rack screw →
  jack bolt → latch screws → bracket screws in that order).

## See also

[[SRE-2010]], [[SRE-3000]], [[SRE-3050]], [[Bruno]]
