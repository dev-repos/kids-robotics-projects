# Project 13: Wheelbarrow Walker Robot

**Ages:** 8+ · **Time:** 2–3 hours · Build with a grown-up.

![Printable build card](card.png)

Printable A4 build-steps sheet: [card.png](card.png) · [card.pdf](card.pdf)

**1:1 cut/fold templates (print at 100% / Actual size, do not fit to page):** [templates.pdf](templates.pdf) (preferred) · [sheet 1](template-1.png) barrow tray · [sheet 2](template-2.png) sticks, feet, skewer lengths · [sheet 3](template-3.png) hip plates + crank discs · [sheet 4](template-4.png) torso, pads + 1:1 leg check · [sheet 5](template-5.png) build steps (SVG: `template-N.svg`). Check the 100 mm calibration bar first. Solid = cut, dashed = fold, grey circles = holes, red = size in mm.

## Goal

Build a cardboard and ice-cream-stick worker whose **legs really walk, driven by a motor**, pushing a free-rolling wheelbarrow. A TT gear motor sits upright in his hips. Its shaft sticks out on both sides, and each end turns a little crank. The two cranks point opposite ways (180°), so the legs step left, right, left, right. Learn how a crank and linkage turn round-and-round motion into walking.

## Parts list

- 3 mm corrugated cardboard (sheets 1, 3, 4)
- About 10 ice-cream sticks (114 x 10 mm)
- 2 bottle caps or 65 mm wheels (they roll freely, no motor on them)
- Wooden skewers 3 mm (pins and axles) and a paper straw
- TT gear motor 3–6 V, **double shaft** (body about 70 x 22 x 18 mm, 5.4 mm D-shaft on both sides)
- 2xAA battery holder with batteries, slide switch, about 40 cm of thin wire
- 4 rubber bands (foot grips) or hot glue
- Ping-pong ball (head) and a bottle cap (hat)
- Hot glue (used by a grown-up), kid scissors, pencil

## The leg mechanism (key sizes)

| Part | Size |
|---|---|
| Crank radius (shaft centre to crank pin) | 8 mm, two cranks 180° apart |
| Hip pivot (thigh pivot) | 36 mm behind and 8 mm below the motor shaft |
| Thigh | 45 mm stick, holes 35 mm apart (hip → knee) |
| Leg stick | 90 mm stick, holes at 5 / 45 / 85 mm: crank pin → 40 mm → knee → 40 mm → foot |
| Foot | 30 x 10 mm, rubber-band grip |
| Shaft height above the table | about 77 mm |

The leg stick is driven at the top by the crank pin, and the thigh holds its middle (the knee) on an arc. That makes the foot draw a loop with a flat bottom: it **pushes back about 22 mm** along the table, then **lifts about 9 mm** and swings forward. Two feet half a turn apart give roughly 45–50 mm of walking per turn of the shaft (less if the feet slip). We checked the sizes with a small script ([tools/wheelbarrow_walker_check.py](../../tools/wheelbarrow_walker_check.py)): the crank is the shortest link (8 + 40 ≤ 36.9 + 35), so it turns all the way round and never locks. The knee angle stays between 45° and 73°, and the crank pin never comes closer than 28 mm to the thigh.

## Steps

1. Cut and fold the barrow tray (sheet 1). Fold the base tabs up and glue the side walls, back wall and sloped front flap on.
2. Glue the two axle hangers under the tray. Push the 110 mm skewer axle through a paper straw and through the hangers, add the Ø20 washers, then glue a wheel on each end. The wheels roll freely.
3. Cut the two hip plates (sheet 3, 3 mm cardboard). Cut the Ø30 hole out. Hot-glue one plate on each flat side of the TT motor, with the motor standing upright (gearbox at the bottom) and the shaft in the middle of the Ø30 hole. The second plate is the same shape glued flipped over, so the hip holes are on the same side (the back).
4. Make the cranks: glue the two A discs together, and the two B discs together (6 mm thick each). Push A onto one shaft end and B onto the other (the D-hole fits the flat of the shaft), with a drop of hot glue. Check that the crank pins point **opposite ways**. Glue a 15 mm crank pin into each pin hole.
5. Push the 40 mm hip skewer through both hip holes and glue it to the plates. Slide a thigh onto each end, then glue a short straw ring on the skewer (not the thigh) so the thigh stays on but can swing.
6. Put each leg stick's top hole on a crank pin. Pin its middle hole to the thigh's knee hole with a 12 mm knee pin, then add straw stoppers. Glue a foot across the bottom end. Lay the leg on the 1:1 leg check on sheet 4 to make sure it matches.
7. Glue the torso covers (sheet 4) over the plates, and the head on top. Glue the upper arms to the shoulders and the forearms to the upper arms. With both feet flat on the table and the body upright, glue the hands to the barrow handles. The arms must be stiff: they are what pushes the barrow.
8. Glue the 2xAA holder on its pad under the tray and the slide switch on the switch plate. Run the wires along a handle and an arm to the motor. Switch on and he walks! If he walks backwards, swap the two motor wires.

**Foot grips:** wrap two rubber bands round each foot, or draw zig-zag lines of hot glue under it. A grippy foot pushes, and a slippery foot just slides.

**Tuning:** if the feet drag, glue a thin card shim under the barrow wheels' hangers so the barrow sits a bit higher. If he tips sideways, move the batteries further forward in the tray.

## Safety

- A grown-up uses the hot glue gun and does all craft-knife cutting and hole poking.
- Snip the sharp tips off skewers.
- Keep fingers and hair away from the cranks while the motor is on.
- Batteries: put them in the right way round, never connect the wires directly together, and take them out when you have finished.
- Keep small parts away from little children.

## How it works

The motor shaft turns each crank pin in a circle 8 mm from the centre. The top of each leg rides on its pin, and the thigh is a swinging guide that holds the knee. Together they make a four-bar linkage (like the legs of Theo Jansen's Strandbeest, but much simpler). At the bottom of the loop the foot moves backwards along the table, which pushes the worker forwards. At the top of the loop the foot is lifted and carried forwards. Because the two cranks are 180° apart, one foot is pushing while the other is stepping. The worker's stiff arms are glued to the handles, so he pushes the free-rolling wheelbarrow along in front of him.
