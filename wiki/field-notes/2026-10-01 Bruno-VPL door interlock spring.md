---
type: field-note
manufacturer: Bruno
model: VPL-3100B / VPL-3200B
date: 2026-10-01
status: resolved
tags: [bruno, vpl, porch-lift, door-interlock, lock-rod, spring, field-note]
---

# 2026-10-01 — Bruno VPL: door stuck locked (interlock spring)

**Status: resolved (known issue and fix).** PMS field experience with
the **door interlock** on Bruno vertical platform lifts. The manuals
don't cover it. Not tied to one job. **Applies to both the
[[VPL-3100B]] and the [[VPL-3200B]]** (confirmed by the human).

## Unit

- Bruno porch lift (VPL) with a **door interlock**: the spring-loaded
  lock that keeps the landing door locked unless the platform is there.
  (The install manuals cover wiring the door/gate interlock; see
  [[VPL-3100B Install Manual]] and [[VPL-3200B Install Manual]].)

## Symptom

**The door is stuck in the locked position.**

## Checked

How to test the interlock:

1. **Raise the lift to the top.**
2. **Remove the plastic post cap.** It's a friction fit; pull it off.
3. **Manually push down the lock rod** and see whether the lock
   releases.
4. **Can't reach the lock rod?** Remove the **four screws** holding the
   **call/send station** to the post and move it aside for easier access.

**Reading the test:**

- **Bad spring:** the rod moves but **doesn't spring back**, or is
  **slow to spring back**.
- When the lock rod is pushed down, **the door unlocks**.

## Root cause

**The interlock is spring-loaded, and the spring can partially fail.** A
weakened spring can leave the door **stuck in the lock position**.

## Fix

**Replace the whole interlock assembly.** The spring isn't replaced on
its own.

## Parts used

- **VPL-31452L**: interlock assembly, **left hand** (per the human; the
  part number isn't in the Bruno manuals on file). **Right-hand part
  number unknown**; confirm it with Bruno when ordering for a right-hand
  door.

## Takeaways

- **Door stuck locked on a Bruno VPL: suspect the interlock spring.**
  Test the lock rod by hand from the top of the post. If it doesn't
  spring back, or springs back slowly, **replace the interlock assembly**
  (VPL-31452L, left hand).
- The post cap is **friction fit**; it pulls straight off.
- If the lock rod is hard to reach, the **call/send station comes off
  the post with four screws**.

## See also

- [[VPL-3100B]], [[VPL-3200B]]
- [[Porch-Lift-Evaluation]]
