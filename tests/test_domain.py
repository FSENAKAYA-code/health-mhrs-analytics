import pytest

from health.data_checks import validate_aggregate_input


def test_rejects_direct_identifiers():
    with pytest.raises(ValueError, match="direct identifiers"):
        validate_aggregate_input(["week", "patient_id", "outcome"])

def test_accepts_aggregate_fields():
    validate_aggregate_input(["week", "department_group", "outcome"])
