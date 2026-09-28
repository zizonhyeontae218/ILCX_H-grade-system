# ILCX H-grade Specification v1.0

# ILCX H-grade 규격 v1.0

## 1. Purpose

ILCX H-grade expresses the weighted amount of substantive human contribution in an AI-assisted project.

ILCX H-grade는 AI 보조 프로젝트에서 인간이 실질적으로 관여한 정도를 가중치 기반으로 표현합니다.

It does not measure artistic quality, technical quality, originality, commercial value, or moral value.

예술성, 기술적 품질, 독창성, 상업적 가치, 도덕적 가치를 측정하는 지표는 아닙니다.

## 2. Scoring model

## 2. 점수 체계

Each category may receive an integer score from `0` through its category maximum.

각 항목은 `0`점부터 해당 항목의 최대 점수까지 정수 점수를 부여할 수 있습니다.

Partial credit is allowed when work was genuinely mixed between human and AI contribution. Credit should reflect **substantive authorship, decision-making, execution, checking, and revision**, not merely elapsed time.

사람과 AI의 기여가 실제로 혼합된 경우 부분 점수를 줄 수 있습니다. 점수는 단순 작업 시간이 아니라 **실질적인 작성, 판단, 실행, 검토, 수정**의 정도를 기준으로 합니다.

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

| ID | 항목 | 최대 점수 |
|---|---|---:|
| A | 아이디어 초안 | 10 |
| B | 콘셉트 구체화 | 10 |
| C | 구현 뼈대 | 10 |
| D | 디자인 아이디어 | 10 |
| E | 디자인 작성(실현) | 10 |
| F | 경험 작성(실현) | 10 |
| G | 호환성 점검 | 5 |
| H | 작동 테스트 | 5 |
| I | 홍보 | 15 |
| J | 최적화 | 15 |

Total maximum: **100**.

총점의 최대값은 **100점**입니다.

## 3. Promotion special rule

## 3. 홍보 항목 특별 규칙

Category I receives 15 points only when promotional **image, video, audio, and hologram media** contain no AI intervention.

I 항목인 홍보는 홍보용 **이미지, 비디오, 오디오, 홀로그램 미디어에 AI 개입이 전혀 없는 경우에만 15점**을 받습니다.

If no promotion exists, the category may receive the full 15 points because no AI intervention occurred in promotional media.

홍보 자체가 존재하지 않는 경우에도 홍보 미디어에 AI가 개입하지 않은 것으로 간주하여 15점을 부여할 수 있습니다.

If AI intervention exists in any covered promotional medium, Category I receives 0 points.

위에 포함된 홍보 미디어 중 어느 하나라도 AI가 개입했다면 I 항목은 0점입니다.

## 4. Conversion

## 4. 등급 변환

For total score `S`, where `0 <= S <= 100`:

총점 `S`가 `0 <= S <= 100`일 때:

1. `H = floor(S / 10)`
2. `R = S mod 10`
3. Append `+` if `R >= 5`
4. If `S = 100`, emit `10H` with no plus

1. `H = floor(S / 10)`
2. `R = S mod 10`
3. `R >= 5`이면 `+`를 추가
4. `S = 100`이면 `+` 없이 `10H`로 표기

Canonical form:

표준 표기:

`ILCX {H}H{optional +} grade`

Examples:

예시:

- 44 -> `ILCX 4H grade`
- 45 -> `ILCX 4H+ grade`
- 99 -> `ILCX 9H+ grade`
- 100 -> `ILCX 10H grade`

## 5. Evidence and uncertainty

## 5. 근거와 불확실성

A score should not credit human contribution that is not documented or reasonably established.

기록되거나 합리적으로 확인되지 않은 인간 기여도를 임의로 인정해서는 안 됩니다.

When the available history is incomplete, the label may be marked **provisional** in explanatory text, while the canonical grade string itself remains unchanged.

작업 이력이 불완전하다면 설명문에서 해당 등급을 **provisional(잠정)**이라고 표시할 수 있습니다. 단, 표준 등급 문자열 자체는 변경하지 않습니다.

## 6. Interpretation

## 6. 해석

The score is a weighted contribution index. It is not a literal percentage of pixels, tokens, code lines, or labor hours made by humans.

이 점수는 가중치 기반 기여도 지표입니다. 사람이 만든 픽셀, 토큰, 코드 줄 수, 작업 시간의 실제 비율을 뜻하지 않습니다.

## 7. Recommended disclosure

## 7. 권장 표기 방식

When space allows, publish both:

가능하면 다음 두 가지를 함께 표시하는 것을 권장합니다.

- the canonical grade, and
- a short category breakdown.

- 표준 등급
- 간단한 항목별 점수 내역

This makes the label auditable without turning it into a long certification report.

이를 통해 지나치게 긴 인증 보고서 없이도 라벨의 근거를 확인할 수 있습니다.
