import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("value, expected", [
    ("0123456789123456", "0123 45** **** 3456"),
    ("0000000000000000000", "Некорректный ввод"),
    ("11111111аа111111", "Некорректный ввод"),
    ("342342", "Некорректный ввод")
])
def test_get_mask_card_number(value: str, expected: list) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("01234567891234567890", "**7890"),
    ("56874956568890009598899", "Некорректный ввод"),
    ("111111111111111", "Некорректный ввод"),
    ("43635635635ggg", "Некорректный ввод")
])
def test_get_mask_account(value: str, expected: list) -> None:
    assert get_mask_account(value) == expected
