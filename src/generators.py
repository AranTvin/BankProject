def filter_by_currency(transactions: list[dict], currency_code: str) -> GeneratorExit(None):
    """Генератор. Возвращает из списка транзакций транзакцию с нужной ввалютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> GeneratorExit(None):
    """Генератор. Возвращает описание транзакции"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> GeneratorExit(None):
    """Генератор. Возвращает номера карт в определенном диапазоне в формате XXXX XXXX XXXX XXXX"""

    str_zero = "0"
    for number in range(start, end + 1):
        str_number = str(number)
        str_card_number = str_zero * (16 - len(str_number)) + str_number
        card_number = f"{str_card_number[0:4]} {str_card_number[4:8]} {str_card_number[8:12]} {str_card_number[12:16]}"
        yield card_number
