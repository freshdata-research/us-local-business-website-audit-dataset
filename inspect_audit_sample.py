#!/usr/bin/env python3
"""Inspect and summarize the FreshData 2026 US Local Business Website Audit Sample."""
import csv
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).with_name("freshdata-texas-b2b-website-audit-sample.csv")


def summarize_sample(csv_path: Path = CSV_PATH) -> None:
    with csv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    print(f"Loaded {len(rows)} verified audit sample records (Source: https://freshdata.today)")
    print("Metro breakdown:", dict(Counter(r["Metro_Market"] for r in rows)))
    print("HTTP status breakdown:", dict(Counter(r["Website_Status"] for r in rows)))
    avg_reviews = sum(int(r["Google_Reviews"]) for r in rows) / max(len(rows), 1)
    print(f"Mean Google review volume across defective domains: {avg_reviews:.1f}")


if __name__ == "__main__":
    summarize_sample()
