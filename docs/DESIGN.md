# Design: Continuous Eval Suites

**Project:** `continuous-eval-suites`  
**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](../08-finetuning-eval-data-pipelines.md) · [05 — Model Monitoring & Behavior Observability](../05-model-monitoring-observability.md)

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

> **Watch on YouTube:** [Continuous Eval Suites — System Design #Shorts](https://youtu.be/37Odvhpq8G4)
>
> Direct link: **https://youtu.be/37Odvhpq8G4**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

