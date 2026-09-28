---
name: ilcx-h-grade
description: Score and label human contribution in AI-assisted projects using the binary ILCX H-grade 100-point rubric. Use when the user mentions ILCX, H-grade, AI slop, human contribution, asks to grade an AI-assisted project, or finalizes an ILCX project and wants its human-contribution label.
---

# ILCX H-grade

Apply the ILCX H-grade as a human-contribution branding label for AI-assisted projects.

## Core rule

Every category is binary. Never assign partial credit.

For each category:
- If the human substantively performed that category, award the full category weight.
- If the human did not substantively perform that category, award 0.

Scores such as `8/10`, `3/5`, or `4/15` are invalid.

AI assistance does not automatically invalidate a category. Judge whether the human substantively performed the category. Promotion is the special exception below.

| Category | Allowed score |
|---|---:|
| Idea draft | 0 or 10 |
| Concept development | 0 or 10 |
| Implementation skeleton | 0 or 10 |
| Design idea | 0 or 10 |
| Design realization | 0 or 10 |
| Experience realization | 0 or 10 |
| Compatibility check | 0 or 5 |
| Functional testing | 0 or 5 |
| Promotion | 0 or 15 |
| Optimization | 0 or 15 |

Total maximum: 100.

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
- 65 -> `ILCX 6H+ grade`
- 100 -> `ILCX 10H grade`

## Workflow

1. Review the evidence for each category.
2. Make a strict yes/no judgment: did the human substantively perform this category?
3. Award either 0 or the full category weight. Never split the difference.
4. Apply the Promotion special rule exactly.
5. Sum the points.
6. Convert the total to the canonical grade.
7. When useful, show a compact category-by-category reason for each yes/no decision.

If evidence is insufficient to establish that the human substantively performed a category, award 0 for that category. The explanatory text may call the overall result provisional when appropriate.

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
