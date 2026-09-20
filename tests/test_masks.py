import pytest
from src.banking_widget.masks import (
    get_mask_card_number,
    get_mask_account,
)


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("123456789012345", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678", "**5678"),
        ("123", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
