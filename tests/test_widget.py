from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

def test_get_date(got_date):
    assert get_date("2024-03-11T02:26:18.671407") == got_date