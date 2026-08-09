# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Continuous Eval Suites — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload, AUTHOR_NAME, AUTHOR_FINGERPRINT, AUTHOR_GITHUB
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Continuous Eval Suites"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(
        USE_CASE,
        {
            "author": AUTHOR_NAME,
            "author_github": AUTHOR_GITHUB,
            "fingerprint": AUTHOR_FINGERPRINT,
        },
    )

@app.get("/author")
def author():
    return {
        "author": AUTHOR_NAME,
        "github": AUTHOR_GITHUB,
        "fingerprint": AUTHOR_FINGERPRINT,
        "notice": "Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.",
    }


suites = {"suite@v1": {"immutable": True, "threshold": 0.85}}

class GateIn(BaseModel):
    suite: str
    score: float
    train_overlap: bool = False

@app.post("/gate")
def gate(body: GateIn):
    if body.train_overlap:
        raise HTTPException(400, detail="eval leakage firewall")
    meta = suites.get(body.suite)
    if not meta:
        raise HTTPException(404, detail="unknown suite version")
    return {"pass": body.score >= meta["threshold"], "suite": body.suite, "immutable": True}
