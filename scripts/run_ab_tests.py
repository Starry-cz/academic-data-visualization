#!/usr/bin/env python3
"""Explain why the former hard-coded A/B score is no longer treated as evidence."""

from __future__ import annotations

import json


def main() -> None:
    report = {
        "status": "retired",
        "reason": "The former baseline scores were hard-coded and did not invoke a model or render outputs.",
        "replacement": {
            "trigger": "Use fresh-context host evaluations outside this deterministic repository test.",
            "routing": "python scripts/eval_runner.py",
            "execution_and_quality": "python scripts/eval_runner.py --execute",
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
