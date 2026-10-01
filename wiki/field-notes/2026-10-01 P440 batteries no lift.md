---
type: field-note
manufacturer: Prism
model: P440
date: 2026-10-01
status: resolved
tags: [prism, handicare, p440, ceiling-lift, portable-lift, batteries, charging, field-note]
---

# 2026-10-01 — P440: won't go up or down, red light on charge (batteries)

**Status: resolved. The batteries were bad.** PMS field experience on a
[[P440]] portable ceiling lift.

> **Key takeaways (per the human):**
> 1. **Tape the batteries together** so they keep a good connection.
>    This applies to ceiling lifts ([[P440]] and [[C-450-C-625]]).
> 2. **Replace both batteries**, never just the bad one. House standard
>    for every device: replace every battery in the device
>    ([[Mobility-Batteries]]).

## Unit

- Prism/Handicare [[P440]] portable ceiling lift. Serial number not
  recorded.
- Batteries per the manual: 2 × 12 VDC 2.3 Ah in series (24 V), with an
  internal 15 A fuse.

## Symptom

- **Won't go up or down.**
- **Lift indicator light RED while plugged into the charger.** The
  manual says the lift's light should be **solid ORANGE** while it
  charges. RED (with fast beeps) means the batteries are fully
  discharged.
- **Charger light GREEN**, meaning the charger reported a full charge.

Note: up and down are **always disabled while the charger is
connected** (per the manual). Only emergency down works. Unplug the
charger before you test the lift.

## Checked

1. **Battery voltages** after charging: **12.9 V and 12.3 V** (about
   25.2 V total). A 0.6 V gap between two batteries in series, after
   the charger reports full, means one battery isn't holding a charge.
2. **Charger output, unplugged from the lift: 27.3 V.** That's normal
   for a 24 V lead-acid charger, so the charger was good.

## Root cause

**Bad batteries.** The weak battery couldn't hold a charge, so the lift
saw low voltage and showed RED, even though the charger had finished
and showed green.

## Fix

**Both batteries replaced.**

## Parts used

- **2 ×** batteries, 12 V 2.3 Ah sealed lead-acid (spec per the
  manual). Part number not recorded.

## Takeaways

- **Most important (see the callout at the top): tape the batteries
  together, and replace both.** Tape them whenever the batteries are
  replaced or the case is opened.
- **Red lift light + green charger light = suspect the batteries.** The
  charger has finished but the lift still reads flat. Measure each
  battery. A big gap between the two points to a failing battery.
- **A charger with no load can show green.** Check its output voltage
  with a meter (about 27–29 V) to rule it out quickly.
- With a red light while plugged in, also check that the **Emergency
  Stop is ON**. The lift won't charge with it OFF.

## See also

- [[P440]], [[C-450-C-625]]
- [[Mobility-Batteries]]
- [[P440 Owner's Manual (2021, Rev 19-Oct)]]: charging and indicators on
  pp. 7 and 14–15, troubleshooting on p. 19
  (`MANUALS/Prism/753001-19-Oct-2021-P-440-Owners-Manual-English.pdf`)
