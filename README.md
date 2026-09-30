# ILCX™ H-grade

**ILCX™ H-grade** is a human-contribution branding label for AI-assisted works.

**ILCX™ H-grade**는 AI 보조 결과물에서 인간의 개입 영역을 표현하기 위한 브랜딩 라벨입니다.

It uses a weighted 100-point rubric, but every category is judged strictly as **yes or no**: if the human substantively performed that category, the full weight is awarded; otherwise it receives 0.

100점 가중치 체계를 사용하지만 각 항목은 철저히 **예 또는 아니오**로만 판정합니다. 사람이 그 영역을 실질적으로 수행했다면 전체 점수를 받고, 아니라면 0점입니다.

There is **no partial credit**. Scores such as `8/10`, `3/5`, or `4/15` are invalid.

**부분 점수는 없습니다.** `8/10`, `3/5`, `4/15` 같은 표기는 규격 위반입니다.

Example:

예시:

> **ILCX™ 4H+ grade**

This is a branding/contribution label, **not a quality score**, scientific measurement, anti-AI score, or claim that a work is fully human-made.

이 표기는 품질 점수, 과학적 측정치, 반(反)AI 지표, 또는 완전한 인간 제작물임을 주장하는 인증이 아닙니다. AI-assisted work에 사람이 어떤 영역까지 직접 관여했는지를 보여주는 **브랜딩/기여 라벨**입니다.

## Rubric

## 평가 항목

| Area | Allowed score |
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
| **Total** | **0–100** |

| 영역 | 허용 점수 |
|---|---:|
| 아이디어 초안 | 0 또는 10 |
| 콘셉트 구체화 | 0 또는 10 |
| 구현 뼈대 | 0 또는 10 |
| 디자인 아이디어 | 0 또는 10 |
| 디자인 작성(실현) | 0 또는 10 |
| 경험 작성(실현) | 0 또는 10 |
| 호환성 점검 | 0 또는 5 |
| 작동 테스트 | 0 또는 5 |
| 홍보 | 0 또는 15 |
| 최적화 | 0 또는 15 |
| **총점** | **0–100** |

### Promotion rule

### 홍보 점수 규칙

Promotion receives **15 points only when AI has not intervened at all in promotional image, video, audio, or hologram media**.

홍보 점수는 홍보용 **이미지, 비디오, 오디오, 홀로그램 제작에 AI가 전혀 개입하지 않은 경우에만 15점**을 부여합니다.

If the project was **not promoted at all**, this is treated as no AI intervention in promotion and the 15 points may still be awarded.

프로젝트를 **아예 홍보하지 않은 경우**에도 홍보 과정에서 AI 개입이 없었던 것으로 간주하여 15점을 부여할 수 있습니다.

## Grade conversion

## 등급 변환

Let `S` be the total score from 0 to 100.

총점 `S`는 0점부터 100점까지입니다.

- Base grade: `floor(S / 10)H`
- Add `+` when `S mod 10 >= 5`
- `100` is written as `10H`, not `10H+`

- 기본 등급: `floor(S / 10)H`
- 일의 자리 점수가 5 이상이면 `+` 추가
- `100`점은 `10H+`가 아니라 `10H`로 표기

## Example: ILCX™ - CometDust

## 예시: ILCX™ - CometDust

Human-performed categories:

사람이 직접 수행한 것으로 인정되는 영역:

- Idea draft: 10
- Design idea: 10
- Compatibility check: 5
- Functional testing: 5
- Promotion: 15 — no promotion was performed

- 아이디어 초안: 10
- 디자인 아이디어: 10
- 호환성 점검: 5
- 작동 테스트: 5
- 홍보: 15 — 홍보 자체를 하지 않음

All other categories receive 0.

나머지 항목은 모두 0점입니다.

Total: **45 / 100**

총점: **45 / 100**

Result: **ILCX™ 4H+ grade**

결과: **ILCX™ 4H+ grade**

## Repository contents

## 저장소 구성

- `SPEC.md` — normative specification
- `skills/ilcx-h-grade/` — reusable ChatGPT/OpenAI Agent Skill
- `plugin.json` — portable skills-only plugin manifest

- `SPEC.md` — 규격 본문
- `skills/ilcx-h-grade/` — 재사용 가능한 ChatGPT/OpenAI Agent Skill
- `plugin.json` — 이식 가능한 skills-only 플러그인 매니페스트

## Status

## 상태

Version: **1.1.0**

버전: **1.1.0**

“ILCX™ H-grade” is used here as a project labeling mark. The ™ symbol denotes branding use and does not by itself assert or prove legal trademark registration.

“ILCX™ H-grade”는 프로젝트 브랜딩 및 표기를 위한 라벨로 사용됩니다. ™ 기호는 브랜딩 표기이며, 이 저장소의 존재 자체가 법적 상표 등록이나 공식 인증을 의미하지는 않습니다.
