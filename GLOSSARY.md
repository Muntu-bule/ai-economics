# AEI Glossary — the shared language of the series

*One term, one meaning, in every post. AEI v0.3 (Oct 2026). The formula's weights and the verification-cost operationalization stay in the private vault and are not in this file. Nothing here is a recipe — it is the vocabulary the posts are written in.*

## The index and its components

- **AEI — Agentic Exposure Index.** A per-task index estimating the share of a task an AI agent can execute end-to-end, without a human in the loop, by 2030. Occupation scores are hours-weighted averages of task scores. The published headline is always the occupation-level 2030 autonomy share (A).
- **C — LLM capability.** The share of a task's steps that current frontier models can perform to professional standard. Theoretical capability — what the model *can* do.
- **U — Observed copilot use.** How much AI assistance is actually observed on the task in the real economy today. Observed, not assumed.
- **A — Agent autonomy, 2030.** The share of a task an agent can plan, execute with tools, and complete multi-step by 2030, without a human initiating each step. The published headline.
- **V — Verification cost.** How cheaply the correctness of a task's output can be checked automatically. Low V — code compiles, numbers reconcile — agents deploy fast. High V — advice quality, empathy, thesis calls — deployment lags capability. The principle is public; the operationalization is vault-only.

## The distinctions the series stands on

- **Exposure vs adoption.** Exposure is what the AEI measures: how much of a task is agent-executable. Adoption is deployment: copilots rolled out firm-wide. Adoption is not exposure.
- **Agent-executable vs copilot-touched.** Agent-executable (A): an agent can run the task end-to-end by 2030. Copilot-touched (U): a copilot already assists with the task today. A task can be copilot-touched without being agent-executable.
- **Human-core.** The share of an occupation's task content that remains human — judgment, relationships, empathy under pressure. Analyst ~35%, contact centre ~30%, developer ~28% (100 − A, hours-weighted).
- **AI value vs return.** AI value is a reported figure — realised or projected value, a numerator. A return is value relative to spend — it needs a denominator. No return is printed anywhere in this series, because no bank discloses the spend underneath its value figure.
- **Descriptive, not causal.** The series describes what is disclosed and what is exposed. It does not claim AI caused any wage or hiring change. Wage comparisons are industry-level, nominal dollars, descriptive.
- **Evident-audited.** A figure is printed as Evident's only when it comes from Evident's own text. Figures from secondary reporting are attributed as such.
- **Hours-weighted.** Occupation scores weight each task by the hours it takes in a real shift — a task that takes 2 hours counts four times a task that takes 30 minutes.

## Headline figures (frozen, v0.1–v0.3)

| Occupation | Agent-executable by 2030 (A) | Copilot-touched today (U) | Day mapped |
|---|---|---|---|
| Junior analyst | 64.8% | 64.9% | 10 tasks, 10.0 h |
| Contact-centre agent | 69.8% | 65.5% | 9 tasks, 7.5 h |
| Junior developer | 71.9% | — | 10 tasks, 8.0 h |

*Sources: task scores in `data/junior_tasks_aei.csv`, `data/contact_centre_tasks_aei.csv`, `data/junior_dev_tasks_aei.csv`; capability and use grounded in the Anthropic Economic Index and Felten AIOE; bank deployment facts from bank disclosures and earnings calls. Method: `~/workspace/aei-core-scaffold/FORMULA.md` (vault).*
