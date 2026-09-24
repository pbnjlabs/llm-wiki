---
type: concept
tags: [ramp, slope, planning, ez-access]
---

# Ramp Slope and Length

How to size a ramp from vertical rise, which ratios fit which uses, and
how those ratios compare with the incline ratings of the mobility
devices in this wiki. Built from EZ-ACCESS web articles (see
[[EZ-ACCESS]]), which serve as guidance, not code.

## The core math

1. **Measure the total rise.** Measure from the surface where the ramp
   starts to the top of the entry, porch or landing. Never estimate from
   step count, because step heights vary. If the ground slopes away from
   the house, the effective rise grows with distance.
2. **Length = rise × ratio.** At 1:12, a 24 in rise needs 288 in of
   ramp, which is 24 ft. The shortcut: **1 ft of ramp per inch of
   rise.**
3. **Check the footprint.** If the straight run won't fit, add turns
   and platforms (a modular L, U or switchback layout). **Never make the
   ramp shorter and steeper to fit.**

Step examples from the articles, at ~7 in per step and 1:12: 2 steps
need ~14 ft, 3 need ~21 ft, 4 need ~28 ft, and 5 need ~35 ft. At that
height, landings become mandatory under ADA and advisable at home (see
below).

## Ratio tiers

| Ratio | Grade | Angle | EZ-ACCESS guidance |
|---|---|---|---|
| 1:20 / 1:18 / 1:15 | 5.0 / 5.6 / 6.7 % | 2.9° / 3.2° / 3.8° | Easier for users with limited stamina ([[Configuration Factors for Residential Ramp Systems]]) |
| **1:12** | 8.3 % | 4.8° | ADA maximum. The default recommendation for wheelchair ramps. |
| 1:10 | 10 % | 5.7° | "Often acceptable" for some residential or light use ([[Understanding Ramp Incline]]) |
| 1:8 | 12.5 % | 7.1° | **Conflicting guidance**: see below |
| 1:6 | 16.7 % | 9.5° | Non-mobility loading only |
| 1:4 | 25 % | 14.0° | Pet or equipment ramps, short distances ([[How to Measure and Install a Ramp]]) |

**Contradiction on 1:8.** [[How to Measure and Install a Ramp]]
(2025-04) calls 1:8 "acceptable in some cases" for residential use.
[[Understanding Ramp Incline]] (2025-02) groups 1:8 with 1:6 as
**non-mobility** inclines. Both articles say to defer to the mobility
device's owner manual. That is the tiebreaker, and the table below
shows the answer is often no.

Every article repeats two further cautions: check the device owner's
guide for allowable slope **and chair direction**, and "at any
incline, use the ramp only with a qualified helper."

## Do the devices in this wiki handle the ramp?

These are the max-incline ratings already recorded on the model pages.
The steepest ratio each device can take is 1 ÷ tan(max angle).

| Device | Rated max incline | Steepest ratio | 1:12 | 1:10 | 1:8 |
|---|---|---|---|---|---|
| [[J6]] (Pride) | 6° | ~1:9.5 | ✅ | ✅ | ❌ |
| [[Air-Hawk-Eagle-HD]] (Red Hawk) | 6° | ~1:9.5 | ✅ | ✅ | ❌ |
| [[Q6-Edge-3-Stretto]] (Pride) | 7.5° | ~1:7.6 | ✅ | ✅ | ✅ (barely) |
| [[GA541-Avenger]] (Golden) | 8.0° recommended max ([[GA541 Avenger Operator Manual]]) | ~1:7.1 | ✅ | ✅ | ✅ (barely) |
| [[Pegasus Plus (DC02)]] (Red Hawk) | 8° | ~1:7.1 | ✅ | ✅ | ✅ (barely) |
| [[Phoenix]] (Red Hawk) | 8° | ~1:7.1 | ✅ | ✅ | ✅ (barely) |

**Takeaway:** 1:12 is safe for every rated device in the wiki. Don't
sell a 1:8 residential ramp to a J6 or Air Hawk/Eagle HD user. Even
where 1:8 falls inside the rating, it leaves almost no margin. A
device's max rated slope is a performance limit, not a comfortable
daily-use slope, and the ratings don't account for wet surfaces or
riding backward down the ramp. Other Golden scooters and chairs have no
incline figure in this wiki yet, so check their manuals before quoting.

## The rise-to-length tables disagree slightly

The EZ-ACCESS articles print "1:12" tables with odd rise values that
don't follow 1 in = 1 ft:

| Ramp length | [[How Long Should a Wheelchair Ramp Be]] | [[Wheelchair Ramp Slope Calculator Guide]] |
|---|---|---|
| 12 ft | 11-3/4 in | 12 in |
| 18 ft | 18 in | 17-1/4 in |
| 24 ft | 23-1/2 in | 24 in |
| 30 ft | 30 in | 29-1/2 in |
| 36 ft | 35-1/4 in | 36 in |

The fractional values are ¼–¾ in *below* the simple rule. They most
likely come from real PATHWAY section-length and transition-plate
geometry, which the articles don't explain. Neither table is
authoritative. For an actual PATHWAY layout, use the EZ-ACCESS layout key
or assembly manual (in the `MANUALS/Ramps/` backlog) or the online
Incline Calculator (ezaccess.com/pages/incline-calculator).

## Related

[[ADA-Ramp-Requirements]], [[Ramp-Site-Planning]], [[PATHWAY-3G]],
[[SUITCASE-Ramps]], [[GATEWAY-3G]], [[TRANSITIONS-Threshold-Ramps]]
