# Use Case: Continuous Eval Suites

**Author fingerprint:** `DBHATT-Debashis2007-SystemDesignPOC-2026` — Debashis Bhattacharjee ([@Debashis2007](https://github.com/Debashis2007))

**YouTube walkthrough:** [Continuous Eval Suites — System Design #Shorts](https://youtu.be/37Odvhpq8G4)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](https://github.com/Debashis2007/continuous-eval-suites/blob/main/08-finetuning-eval-data-pipelines.md)  
**Also references:** [05 — Monitoring](https://github.com/Debashis2007/continuous-eval-suites/blob/main/05-model-monitoring-observability.md)

## Users & problem

Every candidate model must pass versioned golden suites before promote. Suites themselves must not leak into training data.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Suites | Content-addressed versions |
| Gate | Blocking in CI/release |
| Leakage | Train publish blocked if near-dup to eval |
| Reporting | Scores by slice/category |

## Design (from parent)

```
Eval authors → suite registry (immutable)
  → sweep runner ([03](https://github.com/Debashis2007/offline-eval-sweeps/blob/main/README.md))
  → results DB → pass/fail gate
  → firewall checks on all train publishes
```

## Specializations

| Concern | Continuous eval choice |
|---------|------------------------|
| Ownership | Quality/T&S own suite SLAs |
| Freshness | Rotate items; keep frozen release sets |
| Automation | Nightly + pre-promote |
| Pairing | Always compare to prod control |

## Failure modes

- Silent suite edit → immutability; new version id.
- Train contamination → MinHash firewall.
- Flaky items → quarantine list without deleting history.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Continuous Eval Suites — System Design #Shorts](https://youtu.be/37Odvhpq8G4)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd continuous-eval-suites
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/gate -H 'Content-Type: application/json' -d '{"suite":"suite@v1","score":0.88}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

