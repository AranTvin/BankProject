from src.mask import get_mask_card_number, get_mask_account


def test_get_mask_account():
    assert get_mask_account ("01234567891234567890") == "**7890"


def test_get_mask_card_number():
    assert get_mask_card_number("0123456789123456") == "0123 45** **** 3456"
