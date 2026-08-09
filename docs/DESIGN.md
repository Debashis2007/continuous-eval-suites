# Design: Continuous Eval Suites

**Project:** `continuous-eval-suites`  
**Parent system design:** `08-finetuning-eval-data-pipelines.md / 05`

## 1. What this POC demonstrates

Immutable suite versions and leakage firewall before promote gate.

## 2. Architecture (POC)

```text
POST /gate → reject train_overlap → pass/fail vs threshold
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Immutable suite ids | Silent suite edits invalidate history. | `immutable: True`. |
| Eval leakage firewall | Train/test contamination lies. | `train_overlap` reject. |
| Threshold gate | Automate release quality bar. | `pass` boolean. |

## 4. Key endpoints

`GET /health`, `POST /gate`

## 5. Tradeoffs / POC limits

No MinHash near-dup implementation — boolean flag demo.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

Narrated with **ElevenLabs Debpro voice** and Debpro still image (via [GitaProject](/Users/deb/Development/GenAI/GitaProject)):

- Video: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Script: [`video/narration.txt`](./video/narration.txt)

