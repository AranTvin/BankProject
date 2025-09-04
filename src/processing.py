from widget import get_date


def filter_by_state(transactions: list, status: str = "EXECUTED") -> list:
    """Фильтрует операции по статусу"""
    return [i for i in transactions if i["state"] == status]


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    """Сортирует операции по дате"""
    for i in transactions:
        i["date"] = get_date(i["date"])
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
