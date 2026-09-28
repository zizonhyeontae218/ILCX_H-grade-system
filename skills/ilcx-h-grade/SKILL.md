---
name: ilcx-h-grade
description: Score and label human contribution in AI-assisted projects using the ILCX H-grade 100-point rubric. Use when the user mentions ILCX, H-grade, AI slop, human contribution, asks to grade an AI-assisted project, or finalizes an ILCX project and wants its human-contribution label.
---

# ILCX H-grade

Apply the ILCX H-grade as a human-contribution label for AI-assisted projects.

## Core rule

Score only substantive work attributable to humans. Do not treat the grade as a quality score.

Use integer points within each category maximum:

| Category | Max |
|---|---:|
| Idea draft | 10 |
| Concept development | 10 |
| Implementation skeleton | 10 |
| Design idea | 10 |
| Design realization | 10 |
| Experience realization | 10 |
| Compatibility check | 5 |
| Functional testing | 5 |
| Promotion | 15 |
| Optimization | 15 |

Total maximum: 100.

Partial credit is allowed for genuinely mixed human/AI work. Base it on substantive authorship, decisions, execution, checking, and revision rather than time spent.

## Promotion special rule

Award Promotion = 15 only if AI did not intervene at all in promotional image, video, audio, or hologram media.

If the project had no promotion, Promotion = 15 is allowed.

If AI intervened in any covered promotional medium, Promotion = 0.

## Grade conversion

For total `S`:

- `H = floor(S / 10)`
- append `+` if `S mod 10 >= 5`
- `100` is `ILCX 10H grade`

Canonical output:

`ILCX {H}H{+ if applicable} grade`

Examples:

- 40 -> `ILCX 4H grade`
- 45 -> `ILCX 4H+ grade`
- 95 -> `ILCX 9H+ grade`
- 100 -> `ILCX 10H grade`

## Workflow

1. Identify what the human actually contributed in each category.
2. Assign 0..maximum integer points to each category.
3. Apply the Promotion special rule exactly.
4. Sum the points.
5. Convert the total to the canonical grade.
6. When useful, show a compact breakdown followed by the canonical label.

Do not invent human contribution that is not established. If evidence is incomplete but a best-effort score is still useful, score only documented contribution and call the result provisional in explanatory text.

## Known example

ILCX - CometDust:
- Idea draft 10
- Design idea 10
- Compatibility check 5
- Functional testing 5
- Promotion 15 because no promotion was performed
- all other categories 0

Total 45 -> **ILCX 4H+ grade**

For the normative wording, read `references/ILCX_H_GRADE_SPEC.md`.
