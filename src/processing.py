def filter_by_state(operations_list, state="EXECUTED"):
    """Фильтрует операции по статусу"""
    return [i for i in operations_list if i["state"] == state]


def sort_by_date(operations_list, reverse=True):
    """Сортирует операции по дате"""
    return sorted(operations_list, key=lambda x: x['date'], reverse=reverse)
