def get_mask_card_number(card_number: str) -> str:
    """Маскирует введенный пользователем номер банковской карты"""
    if not card_number.isdigit() or len(card_number) != 16:
        return "Некорректный ввод"
    first_part = card_number[:6]
    last_part = card_number[-4:]
    masked_part = "** ****"
    masked_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
    return masked_number


def get_mask_account(account: str) -> str:
    """Маскирует введенный пользователем номер банковского счета"""
    mask_account_list = ["**"]
    if not account.isdigit() or len(account) != 20:
        return "Некорректный ввод"
    for i in account[-4:]:
        mask_account_list.append(i)
    mask_account = "".join(mask_account_list)
    return mask_account
