---
type: concept
tags: [ceiling-lift, patient-lift, troubleshooting, prism, handicare, p440, c-450, c-625]
---

# Ceiling Lift Troubleshooting

A symptom-first guide for ceiling (patient) lifts, built the same way as
[[Stairlift-Troubleshooting]] and [[VPL-Troubleshooting]]. It covers
Prism/Handicare's **[[P440]]** portable lift (from its owner's manual) and
the **[[C-450-C-625]]** fixed lift (from the [[C-450 C-625 Technical Manual]],
a full service manual). For the general method, see [[Troubleshooting]].

Prism customer service (C-450/C-625 manual): **1-800-265-0677**.

**How they work:** both use a **pneumatic hand control**. Buttons push
air down the airline to air switches on the circuit board, so the hand
control has no wires. The C-450 manual splits the lift
into three systems and checks them in this order: **pneumatic** (hand
control, airline, grommets, air tubes, air switches), **electrical**
(charger, board, harnesses, limit switches, display, on/off and emergency
controls) and **mechanical** (strap, tape switch, motors and gears,
trolley). Most faults turn out to be **outside the cover**.

## 1. Triage and "before you open it"

Check these first (the C-450 manual's list; it applies to the P440 too):
- **Charger and charging connections.**
- **Hand control and airline:** plugged in, the right way round.
- **Twisted strap or slack tape.**
- **External thermal breaker** (C-450).
- **Emergency stop / shut-off** in the run position.
- The owner's manual troubleshooting chart.

**What the lift is telling you:**

| P440 indicator light (front left) | Meaning |
|---|---|
| Off | Asleep: it turns itself off after about 2 minutes idle. Press a button to wake it |
| Green | On |
| Orange + slow beeping | Batteries low: finish the transfer, then charge |
| Red + fast beeping | Batteries fully discharged: **UP is disabled**, DOWN and emergency down still work |
| Solid orange on the charger | Charging (charger's own light goes orange → green when full) |

C-450/C-625 **LCD**: battery % (or lift count). Under 25% it flashes "Low
Battery" and beeps every 10 seconds. "Charging" shows whenever it's
docked. "Maintenance" plus beeping = the **preventive maintenance alarm**
(about 1,000 lifts or 5 operating hours); do the semi-annual PM and reset
the counter in programming mode (hold Up + Down 3 seconds). See
[[C-450-C-625]].

## 2. Won't do anything

- **P440:** press a hand control or lift button to wake it (light goes
  green). **Red emergency stop switch** (front left) must be **ON**. Not
  charging? The lift won't charge with the E-stop off either.
- **C-450/C-625:** the **emergency shut-off pull cord**. Pulled by
  accident → push the button toward the lift until it clicks. Pulled in
  a real emergency → have it inspected before use (P440 E-stop too). Still
  dead → check the shut-off isn't obstructed; replace the switch if it
  doesn't switch.
- **Batteries** (§6). **Up and down are disabled while a P440 is on the
  charger**, so unplug it to test. Only emergency down works on charge.
- **Both the hand control and the lift's own buttons dead** (C-450): with
  pneumatic and electrical both failing at once, it's almost always the
  **circuit board**. Prove it with a known-good board.

## 3. Buttons do the wrong thing, or it moves by itself

- **Up button goes down (functions swapped):** the airline is attached
  wrong. Reattach: the plug's cap has a raised ridge that lines up with
  and slides over the ridge on the grommet, so you can check it by touch
  and by eye.
- **Moves by itself now and then** (on/off, up, down, emergency lowering
  or traverse): a **slow air leak**. Check the grommets first (one on the
  hand control, one on the lift); they wear from frequent unplugging and
  from **pulling the lift along the track by the hand control. Never do
  that.**
- **Pneumatic test (C-450):** unplug the airline and press each button:
  you should feel a puff of air at the brass pins on the end of the curly
  cord. Reconnect, then check the air tubes inside run free (not trapped
  by wires or the cover) and go to the right switches (color-coded
  stickers on the main board; on traverse boards, nearest tube to nearest
  switch). Leak test each tube: take it off its switch, press that
  function, pinch the open end, release the button. **The button dome
  should stay slightly pressed in.** Tubes are fragile: don't use
  fingernails, and don't pierce them on the pins.
- **No leak → electrical** (§5).

## 4. Strap and lifting faults

- **Won't go down, light green (P440):** the slack tape detector is
  sensitive. Take hold of the strap about 10 cm above the lift, pull it up
  to tighten it, then press down. Keeps happening → dealer.
- **Goes down to the end of the strap, then goes back up with up/down
  reversed** (C-450): the **slack-strap** safety isn't working. The
  roller in the tape switch assembly is stuck, or the micro switch is too
  far from (or too close to) the roller. Clean out the assembly, make sure
  the parts move freely, listen for the switch click at the end of the
  slot, and move the switch with its 2 screws. Then check its wiring to
  the board, then replace the switch.
- **Strap winds all the way into the gearbox** (C-450): the
  **thick-strap** safety isn't working. Put a slight bend in the metal
  strip that trips the switch, so a doubled strap trips it. Then wiring,
  then the switch.
- **Motor runs but it won't go up or down** (C-450): the motor's output
  shaft or worm wheel has worn and the **overspeed governor** has
  stopped it. That's a deliberate lock-out: **replace the motor**. There's
  no field reset ([[Overspeed-Safety-Brake]]).
- **Strap fraying on one side:** the lift isn't directly above the person
  when lifting. Fix the positioning; if it keeps fraying → dealer.

## 5. Electrical (C-450/C-625, cover off)

In this order:
1. **Batteries charged?** Check the LCD. No reading → test the batteries
   off the lift with a load tester, or fit a known-good set. Look for
   **acid leaks at the vents** (shows as corrosion on the battery leads).
2. **Burn marks or a burnt smell** on the board → replace the board (or
   the adaptor board). The board isn't repairable at component level.
3. **Every harness plugged in**, fully (a missed pin is easy), with no
   cuts or bare wire. Plug positions on the combined board #613880-XUS:
   battery (white, 2nd from left), lift motor (rightmost), traverse motor
   or adaptor board (top, 1st from right), charger (large 2-pin, top
   middle), LED (3-pin, 1st left), LCD (16-pin), tape switch limits
   (4-pin, 2nd from right).
4. **Motors:** unplug the motor and battery leads and jumper the motor
   straight to the battery. Runs → motor is fine (reversed polarity just
   runs it backwards).
5. **Board fuses:** both good? Replace a blown one **only with the
   specified 25A or 30A fuse**. Still dead → replace the board.
6. **Hidden board failure:** connect a known-good board (it can sit
   outside the lift for the test).
7. Emergency lowering still dead after a board swap → the slack-tape
   lower limit switch (§4).

The number of air switches on the board identifies the model: 2 = Manual,
4 = Power or Manual Power Turntable, 6 = Power X-Y or Power Turntable.

## 6. Charging and batteries

- **P440:** charge 5 hours before first use. On the charger the lift's
  light is solid orange, and the charger goes orange → green when full.
  Usable after an hour, but charge overnight. E-stop must be ON to charge.
- **C-450/C-625:** five parts: charger, charger end stop, charger
  plates, harness, board.
  - The charger light should be **green when the lift isn't docked**
    (power is reaching it).
  - The **charging strips** (bent in a wave, middle section tensioned)
    must touch the stainless contacts on the trolley block. Older lifts
    have **copper strips that corrode** in humid or pool rooms.
  - Harness: the charger's black wire meets the harness black (red =
    positive throughout).
  - Board: plug the charger's white plug into a replacement board.
  - Battery voltage: over 27.5V charged, 27–30V while charging
    ([[C-450-C-625]]).
- **Lift light red on the charger while the charger shows green** = the
  batteries aren't taking a charge. Replace them
  ([[2026-10-01 P440 batteries no lift]]).
- **Per the human: tape the batteries together** so they keep a good
  connection (P440 and C-450/C-625), and **always replace both**
  ([[Mobility-Batteries]]).

## 7. Track and traversing

- **Sticks at certain spots:** at a **track seam** → fix the vertical or
  horizontal alignment. In a **curve** → curve walls can collapse when
  bent; replace the curve or reshape it with a track bending tool. At a
  **turntable** → align it with the track and use brackets to hold it.
  Clean inside the track with alcohol.
- **Power traverses badly everywhere** (C-450 power models): open it up
  and check the traverse motor is tight and the gears are aligned and
  secure. Laboured noise and a swaying motor bracket are the signs.
- **P440 won't pass a turntable or gate:** see that component's manual.
- Track install and mounting: [[Ceiling Lift Installation Guide]]
  (Vancare) and [[Ceiling-Lift-Evaluation]].

## Emergency lowering

- **P440:** the lift's blue DOWN button (front right) if the hand control
  fails, then the **red emergency lowering button** (front middle): about a
  2-second delay, with an alarm. It only lowers. Report any lowering
  failure to the dealer at once.
- **C-450/C-625:** the emergency shut-off pull cord, held at full
  extension, lowers the lift ([[C-450-C-625]]). Pulled once it only stops the
  lift (push the white tab back to reset). With no power, turn a **4 mm hex
  key** clockwise in the motor shaft behind the side clip
  ([[C-450 C-625 Owner's Manual (753140 Rev D)]]).
- **Savaria M-Series / PL portable** ([[Savaria-Ceiling-Lifts]]): 4 mm Allen key, power off, many slow
  turns. **If the emergency brake has engaged, don't release it, press Up or
  lower manually: switch off and call the dealer**
  ([[Savaria M-Series Portable Ceiling Lift Owner's Manual (001586)]]).

## Field notes

- [[2026-10-01 P440 batteries no lift]]: won't go up or down; lift light
  red on the charger, charger green; batteries bad, both replaced.

## See also

[[Troubleshooting]], [[P440]], [[C-450-C-625]], [[Savaria-Ceiling-Lifts]], [[C-450 C-625 Technical Manual]],
[[P440 Owner's Manual (2021, Rev 19-Oct)]], [[Overspeed-Safety-Brake]],
[[Mobility-Batteries]], [[Ceiling-Lift-Evaluation]], [[Joint-Commission-DMEPOS]]
