def filter_by_state(operations_list: str, state: str="EXECUTED") -> list:
    """Фильтрует операции по статусу"""
    return [i for i in operations_list if i["state"] == state]


def sort_by_date(operations_list: list, reverse: bool=True) -> list:
    """Сортирует операции по дате"""
    return sorted(operations_list, key=lambda x: x["date"], reverse=reverse)
