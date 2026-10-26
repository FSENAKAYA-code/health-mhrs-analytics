"""Basic privacy-oriented checks for appointment analytics inputs."""

from collections.abc import Iterable

SENSITIVE_COLUMN_NAMES = {"name", "full_name", "email", "phone", "patient_id", "national_id"}


def validate_aggregate_input(columns: Iterable[str]) -> None:
    normalized = {column.strip().lower() for column in columns}
    found = normalized & SENSITIVE_COLUMN_NAMES
    if found:
        raise ValueError(f"remove direct identifiers before analysis: {sorted(found)}")
