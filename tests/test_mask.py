import pytest

from src.mask import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("value, expected", [
    ("01234567891234567890", "**7890"),
    ("56874956568899598899", "**8899"),
    ("11111111111111111111", "**1111")
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("0123456789123456", "0123 45** **** 3456"),
    ("0000000000000000", "0000 00** **** 0000"),
    ("1111111111111111", "1111 11** **** 1111")
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected
