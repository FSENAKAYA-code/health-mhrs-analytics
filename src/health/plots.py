"""Optional aggregate-only plotting helpers; never plots row-level patient data."""

from pathlib import Path

from matplotlib.figure import Figure


def save_no_show_rates(rates: dict[str, float], destination: Path) -> None:
    if not rates or any(not 0 <= rate <= 1 for rate in rates.values()):
        raise ValueError("provide aggregate rates between zero and one")
    from matplotlib import pyplot as plt

    figure: Figure
    figure, axis = plt.subplots(figsize=(8, 4))
    axis.bar(list(rates), list(rates.values()), color="#3973ac")
    axis.set_ylabel("No-show rate")
    axis.set_ylim(0, 1)
    axis.set_title("Aggregate appointment no-show rates")
    figure.tight_layout()
    destination.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(destination, dpi=150)
    plt.close(figure)
