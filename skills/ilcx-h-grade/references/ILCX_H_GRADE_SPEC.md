# ILCX H-grade Specification v1.0

## 1. Purpose

ILCX H-grade expresses the weighted amount of substantive human contribution in an AI-assisted project.

It does not measure artistic quality, technical quality, originality, commercial value, or moral value.

## 2. Scoring model

Each category may receive an integer score from `0` through its category maximum.

Partial credit is allowed when work was genuinely mixed between human and AI contribution. Credit should reflect **substantive authorship, decision-making, execution, checking, and revision**, not merely elapsed time.

| ID | Category | Maximum |
|---|---|---:|
| A | Idea draft | 10 |
| B | Concept development | 10 |
| C | Implementation skeleton | 10 |
| D | Design idea | 10 |
| E | Design realization | 10 |
| F | Experience realization | 10 |
| G | Compatibility check | 5 |
| H | Functional testing | 5 |
| I | Promotion | 15 |
| J | Optimization | 15 |

Total maximum: **100**.

## 3. Promotion special rule

Category I receives 15 points only when promotional **image, video, audio, and hologram media** contain no AI intervention.

If no promotion exists, the category may receive the full 15 points because no AI intervention occurred in promotional media.

If AI intervention exists in any covered promotional medium, Category I receives 0 points.

## 4. Conversion

For total score `S`, where `0 <= S <= 100`:

1. `H = floor(S / 10)`
2. `R = S mod 10`
3. Append `+` if `R >= 5`
4. If `S = 100`, emit `10H` with no plus

Canonical form:

`ILCX {H}H{optional +} grade`

Examples:

- 44 -> `ILCX 4H grade`
- 45 -> `ILCX 4H+ grade`
- 99 -> `ILCX 9H+ grade`
- 100 -> `ILCX 10H grade`

## 5. Evidence and uncertainty

A score should not credit human contribution that is not documented or reasonably established.

When the available history is incomplete, the label may be marked **provisional** in explanatory text, while the canonical grade string itself remains unchanged.

## 6. Interpretation

The score is a weighted contribution index. It is not a literal percentage of pixels, tokens, code lines, or labor hours made by humans.

## 7. Recommended disclosure

When space allows, publish both:

- the canonical grade, and
- a short category breakdown.

This makes the label auditable without turning it into a long certification report.
