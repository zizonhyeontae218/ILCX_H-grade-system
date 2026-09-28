# ILCX H-grade

**ILCX H-grade** is a human-contribution label for AI-assisted works.

It is intentionally simple: score how much of a project was substantively performed by humans across a weighted 100-point rubric, then compress the result into an `H` grade.

Example:

> **ILCX 4H+ grade**

This is a contribution label, **not a quality score**, an anti-AI score, or a claim that a work is fully human-made.

## Rubric

| Area | Max |
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
| **Total** | **100** |

### Promotion rule

Promotion receives **15 points only when AI has not intervened at all in promotional image, video, audio, or hologram media**.

If the project was **not promoted at all**, this is treated as no AI intervention in promotion and the 15 points may still be awarded.

## Grade conversion

Let `S` be the total human-contribution score from 0 to 100.

- Base grade: `floor(S / 10)H`
- Add `+` when `S mod 10 >= 5`
- `100` is written as `10H`, not `10H+`

Examples:

| Score | Label |
|---:|---|
| 0 | ILCX 0H grade |
| 5 | ILCX 0H+ grade |
| 40 | ILCX 4H grade |
| 45 | ILCX 4H+ grade |
| 95 | ILCX 9H+ grade |
| 100 | ILCX 10H grade |

## Example: ILCX - CometDust

Human contribution credited for:

- Idea draft: 10
- Design idea: 10
- Compatibility check: 5
- Functional testing: 5
- Promotion: 15 — no promotion was performed

Total: **45 / 100**

Result: **ILCX 4H+ grade**

## Repository contents

- `SPEC.md` — normative specification
- `skills/ilcx-h-grade/` — reusable ChatGPT/OpenAI Agent Skill
- `plugin.json` — portable skills-only plugin manifest

## Status

Version: **1.0.0**

“ILCX H-grade” is used here as a project labeling mark. This repository does not by itself assert or prove legal trademark registration.
