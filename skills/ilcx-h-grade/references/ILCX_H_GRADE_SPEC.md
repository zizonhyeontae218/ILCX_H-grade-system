# ILCX H-grade Specification v1.1

# ILCX H-grade 규격 v1.1

## 1. Purpose

ILCX H-grade is a branding label that discloses which weighted parts of an AI-assisted project were substantively performed by humans.

ILCX H-grade는 AI 보조 프로젝트에서 어떤 가중치 영역을 사람이 실질적으로 수행했는지 표시하는 브랜딩 라벨입니다.

It is not a quality score, scientific measurement, percentage estimate, or artistic ranking.

품질 점수, 과학적 측정치, 실제 비율 추정치, 작품성 등급이 아닙니다.

## 2. Binary scoring model

## 2. 이진 점수 체계

Every category is binary. A category receives either its full weight or zero.

모든 항목은 이진 판정합니다. 각 항목은 정해진 전체 점수 또는 0점만 받을 수 있습니다.

- If the human substantively performed the category: award the full category weight.
- If the human did not substantively perform the category: award 0.
- Partial scores are forbidden.

- 사람이 해당 영역을 실질적으로 수행했다면: 해당 항목의 전체 점수를 부여합니다.
- 사람이 해당 영역을 실질적으로 수행하지 않았다면: 0점을 부여합니다.
- 부분 점수는 금지합니다.

Scores such as `8/10`, `3/5`, or `4/15` are invalid under this specification.

`8/10`, `3/5`, `4/15` 같은 점수는 이 규격에서 유효하지 않습니다.

AI assistance does not automatically invalidate a category. The question is whether the human substantively performed that category. Promotion is the special exception defined below.

AI의 보조가 있었다는 이유만으로 해당 항목이 자동으로 0점이 되지는 않습니다. 핵심 질문은 사람이 그 영역을 실질적으로 수행했는가입니다. 단, 홍보 항목은 아래 특별 규칙을 따릅니다.

| ID | Category | Allowed scores |
|---|---|---:|
| A | Idea draft | 0 or 10 |
| B | Concept development | 0 or 10 |
| C | Implementation skeleton | 0 or 10 |
| D | Design idea | 0 or 10 |
| E | Design realization | 0 or 10 |
| F | Experience realization | 0 or 10 |
| G | Compatibility check | 0 or 5 |
| H | Functional testing | 0 or 5 |
| I | Promotion | 0 or 15 |
| J | Optimization | 0 or 15 |

| ID | 항목 | 허용 점수 |
|---|---|---:|
| A | 아이디어 초안 | 0 또는 10 |
| B | 콘셉트 구체화 | 0 또는 10 |
| C | 구현 뼈대 | 0 또는 10 |
| D | 디자인 아이디어 | 0 또는 10 |
| E | 디자인 작성(실현) | 0 또는 10 |
| F | 경험 작성(실현) | 0 또는 10 |
| G | 호환성 점검 | 0 또는 5 |
| H | 작동 테스트 | 0 또는 5 |
| I | 홍보 | 0 또는 15 |
| J | 최적화 | 0 또는 15 |

Total maximum: **100**.

총점의 최대값은 **100점**입니다.

## 3. Promotion special rule

## 3. 홍보 항목 특별 규칙

Promotion receives 15 points only when promotional **image, video, audio, and hologram media** contain no AI intervention.

홍보는 홍보용 **이미지, 비디오, 오디오, 홀로그램 미디어에 AI 개입이 전혀 없는 경우에만 15점**을 받습니다.

If no promotion exists, Promotion may still receive 15 points because no AI intervention occurred in promotional media.

홍보 자체가 존재하지 않는 경우에도 홍보 미디어에 AI가 개입하지 않은 것으로 간주하여 15점을 부여할 수 있습니다.

If AI intervention exists in any covered promotional medium, Promotion receives 0 points.

위 홍보 미디어 중 어느 하나라도 AI가 개입했다면 홍보 항목은 0점입니다.

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

## 5. Evidence and uncertainty

## 5. 근거와 불확실성

Do not split the difference when evidence is ambiguous. Decide the category as yes or no from the available evidence.

근거가 애매하다고 중간 점수를 주지 않습니다. 확인 가능한 근거를 바탕으로 해당 항목을 예 또는 아니오로 판정합니다.

If there is not enough evidence to establish that the human substantively performed a category, award 0 for that category and the explanatory text may mark the overall result as provisional.

사람이 해당 영역을 실질적으로 수행했다고 확인할 근거가 부족하다면 그 항목은 0점으로 처리하고, 필요하면 전체 결과를 설명문에서 잠정 등급으로 표시할 수 있습니다.

## 6. Interpretation

## 6. 해석

The final score is the sum of fixed category weights that passed a binary human-performance check. It is not a literal percentage of pixels, tokens, code lines, labor hours, or authorship.

최종 점수는 사람 수행 여부를 이진 판정해 통과한 항목의 고정 가중치를 합산한 값입니다. 사람이 만든 픽셀, 토큰, 코드 줄, 작업 시간, 저작 비율의 실제 퍼센트가 아닙니다.
