"""Aggregate no-show rate interval using a Wilson binomial confidence interval."""

from statsmodels.stats.proportion import proportion_confint


def no_show_rate_interval(no_shows: int, appointments: int, *, alpha: float = 0.05) -> tuple[float, float]:
    if appointments < 1 or not 0 <= no_shows <= appointments:
        raise ValueError("require 0 <= no_shows <= appointments and appointments > 0")
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    low, high = proportion_confint(no_shows, appointments, alpha=alpha, method="wilson")
    return float(low), float(high)
