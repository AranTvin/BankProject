from widget import get_date


def filter_by_state(transactions: list[dict], status: str = "EXECUTED") -> list[dict]:
    """Фильтрует операции по статусу"""
    return [transaction for transaction in transactions if transaction["state"] == status]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате"""
    transactions_sorted = sorted(transactions, key=lambda x: x["date"], reverse=reverse)
    for transaction in transactions_sorted:
        transaction["date"] = get_date(transaction["date"])
    return transactions_sorted
