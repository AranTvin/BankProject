from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict | str]:
    """Генератор. Возвращает из списка транзакций транзакцию с заданной ввалютой"""
    no_information_message = "Нет информации о валюте"
    for transaction in transactions:
        if "operationAmount" not in transaction:
            yield no_information_message
        elif transaction["operationAmount"]["currency"]["code"] == currency_code:
            filtered_by_currency = transaction
            yield filtered_by_currency


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Генератор. Возвращает описание транзакции"""
    for transaction in transactions:
        if "description" not in transaction:
            description = "Остутствует описание операции"
        else:
            description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Генератор. Возвращает номера карт в определенном диапазоне в формате XXXX XXXX XXXX XXXX"""
    str_zero = "0"
    for number in range(start, stop + 1):
        str_number = str(number)
        str_card_number = str_zero * (16 - len(str_number)) + str_number
        card_number = f"{str_card_number[0:4]} {str_card_number[4:8]} {str_card_number[8:12]} {str_card_number[12:16]}"
        yield card_number
