"""Aggregate capacity estimates; never create or cancel patient appointments."""


def expected_attendance(bookings: int, no_show_rate: float) -> float:
    if bookings < 0 or not 0 <= no_show_rate <= 1:
        raise ValueError("bookings must be non-negative and rate in [0, 1]")
    return bookings * (1 - no_show_rate)


def estimated_clinician_units(
    bookings: int, no_show_rate: float, visits_per_unit: int
) -> int:
    if visits_per_unit < 1:
        raise ValueError("visits_per_unit must be positive")
    attendance = expected_attendance(bookings, no_show_rate)
    return int((attendance + visits_per_unit - 1) // visits_per_unit)
