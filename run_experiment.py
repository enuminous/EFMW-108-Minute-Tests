#!/usr/bin/env python3
import argparse, json, csv
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data import load_confirmatory_dataset
from src.models import NaiveRateBaseline, EFMWCandidate, EFMWAblation
from src.metrics import binary_log_loss

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--output", default="results/confirmatory_results.csv")
    args = ap.parse_args()

    cfg = json.load(open(args.config))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for condition in cfg["conditions"]:
        for h in cfg["horizons_minutes"]:
            ds = load_confirmatory_dataset(h, condition)
            models = [NaiveRateBaseline(), EFMWCandidate(), EFMWAblation()]
            for model in models:
                model.fit(ds.X_train, ds.y_train)
                p = model.predict_proba(ds.X_test)
                rows.append({
                    "condition": condition,
                    "horizon_minutes": h,
                    "model": model.name,
                    "n_test": len(ds.y_test),
                    "binary_log_loss": binary_log_loss(ds.y_test, p)
                })

    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
