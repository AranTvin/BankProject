import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 01234567890123456789", "Счет **6789"),
    ("Счёт 01234567890123456789", "Счёт **6789"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

def test_get_date(got_date):
    assert get_date("2024-03-11T02:26:18.671407") == got_date