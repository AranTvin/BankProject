from mask import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Обрабатывает информацию о картах и счетах и маскирует их номера"""
    account_type_list = []
    for i in account_card:
        if not i.isdigit():
            account_type_list.append(i)
    account_type = "".join(account_type_list)
    account = account_card.replace(account_type, "", 1)

    if account_type == "Счет " or account_type == "Счёт ":
        masked = get_mask_account(account)
    else:
        masked = get_mask_card_number(account)
    return f"{account_type}{masked}"


def get_date(date_time: str) -> str:
    """Преобразует строку с датой в определенном формате в формат 'ДД.ММ.ГГГГ'"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[0:4]}"
