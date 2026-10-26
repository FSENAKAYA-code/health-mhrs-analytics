"""Run synthetic no-show classification or analyze an authorized local CSV."""

import argparse

from sklearn.datasets import make_classification

from health.data_checks import validate_aggregate_input
from health.experiment import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-csv", help="authorized, de-identified local appointment CSV")
    parser.add_argument("--target", default="no_show")
    args = parser.parse_args()
    if args.data_csv:
        import pandas as pd

        frame = pd.read_csv(args.data_csv)
        validate_aggregate_input(frame.columns)
        if args.target not in frame:
            raise ValueError(f"target column {args.target!r} is missing")
        y = frame.pop(args.target)
        X = frame.select_dtypes(include="number")
    else:
        X, y = make_classification(
            n_samples=500, n_features=12, n_informative=8, random_state=42
        )
    print(run_experiment(X, y, random_state=42))


if __name__ == "__main__":
    main()
