import pytest

from health.calibration import no_show_rate_interval
from health.capacity import estimated_clinician_units
from health.data_checks import validate_aggregate_input


def test_rejects_direct_identifiers():
    with pytest.raises(ValueError, match="direct identifiers"):
        validate_aggregate_input(["week", "patient_id", "outcome"])

def test_accepts_aggregate_fields():
    validate_aggregate_input(["week", "department_group", "outcome"])


def test_no_show_rate_interval_is_bounded():
    low, high = no_show_rate_interval(5, 20)
    assert 0 <= low < high <= 1


def test_capacity_estimate_uses_aggregate_attendance_only():
    assert estimated_clinician_units(20, 0.25, 5) == 3
