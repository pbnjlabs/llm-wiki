---
type: concept
tags: [electrical, vehicle-lift, bruno, harmar, wiring]
---

# Vehicle Lift Power Wiring

All three Bruno vehicle lifts ([[PUL-1100]], [[ASL-275]], [[ASL-250]])
share the same battery wiring pattern, described near-identically across
their install manuals. Harmar's inside, truck and hybrid lifts use a
different pre-made harness; see the Harmar section below.

## Standard routing

1. Route a twin-lead power cable from the **vehicle battery** to the lift
   (through the firewall/interior for PUL-1100; along the frame to a
   hitch-mounted control box for ASL-275).
2. Cut the cable to length, split back ~10", strip conductors.
3. Red (+) conductor: gets an inline **fuse holder** (PUL-1100: ATO-style;
   ASL-275/ASL-250: 30A — [[ASL-250]]'s manual confirms this is
   specifically an **ATO 30A fuse**, the same style as PUL-1100's, just a
   higher amperage) before terminating in a ring terminal on the
   battery's POSITIVE post.
4. Black (−) conductor: ring terminal directly to the battery's NEGATIVE
   post (or a separate chassis ground wire, on PUL-1100).
5. Secure the harness along the route with P-clips/wire ties/tape; avoid
   road debris, hot exhaust, moving driveline parts, and sharp edges.
6. Seal any drilled firewall/floor penetrations with silicone sealant or
   underbody coating.

## Hybrid/EV note

Both manuals flag: for hybrid or all-electric vehicles, connect to the
vehicle's **low-voltage 12V accessory battery**, not the high-voltage
traction battery. Check the vehicle owner's manual for its location.

## Safety warnings (both manuals, near-verbatim)

- Disconnect the vehicle's ground (−) battery cable before working, to
  avoid electrocution/short-circuit risk.
- Remove metal jewelry (rings, bracelets, necklaces) before working near
  electrical components.
- Read the vehicle OEM's electrical/battery-disconnect instructions first —
  incorrect disconnection can cause data loss, wiring damage, or accidental
  airbag deployment.

## Harmar vehicle lifts

Harmar's inside, truck and hybrid lift manuals ([[Inside Lifts Installation and Owner's Manual (2017, Rev F)]], [[Truck Lifts Installation and Owner's Manual (AL800 Series, 2017)]], [[AL625-AL625HD Installation and Owner's Manual (2012, Rev B)]]) use a
different, **pre-made harness** instead of a cut-to-length cable:

- **~23 ft harness to SAE J1128** with a **20 A self-resetting circuit
  breaker** about 6 in from the battery end. The end connector ships
  loose so the wire fits through small openings.
- **Black to battery negative first; red to positive at the very end.**
- **Never connect to a secondary power source**: both leads straight to
  the battery.
- **Don't cut or shorten the harness**: coil the excess and tie it to
  the frame. Grommet any floor hole.
- Check the pins' retaining flanges after pulling them through, seat
  them (A = red, B = black), keep the rubber seals in.
- "Improper wiring is the #1 cause of problems." The motor can draw
  **up to 30 A**, so a single intact strand reads 12 V on a meter but
  won't run the motor. **Troubleshoot with a known-good battery**, not
  just a test light.

Bruno vs Harmar: Bruno uses an inline **30 A ATO fuse**; Harmar uses a
**20 A self-resetting breaker**. Bruno has you cut the cable to length;
Harmar says never cut the harness.

## See also

[[PUL-1100]], [[ASL-275]], [[ASL-250]], [[Bruno]], [[Hoist-Series-Inside-Vehicle-Lifts]], [[Hybrid-Vehicle-Lifts]], [[Harmar]]
