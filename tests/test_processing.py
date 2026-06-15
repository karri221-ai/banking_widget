import pytest

from src.banking_widget.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(operations, state, expected_count):
    result = filter_by_state(operations, state)
    assert len(result) == expected_count
    assert all(op["state"] == state for op in result)


def test_filter_by_state_default(operations):
    result = filter_by_state(operations)
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize(
    "reverse, first_id, last_id",
    [
        (True, 1, 3),
        (False, 3, 1),
    ],
)
def test_sort_by_date(operations, reverse, first_id, last_id):
    result = sort_by_date(operations, reverse)
    assert result[0]["id"] == first_id
    assert result[-1]["id"] == last_id
