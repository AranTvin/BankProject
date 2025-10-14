from typing import Generator

from src.generators import card_number_generator, transaction_descriptions


def test_filter_by_currency(filter_by_currency_iterate: Generator[dict | str]) -> None:
    assert next(filter_by_currency_iterate) == {
        "id": 111111,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации № 1",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
         }
    assert next(filter_by_currency_iterate) == {
        "id": 222222,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации № 2",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert next(filter_by_currency_iterate) == "Нет информации о валюте"
    assert next(filter_by_currency_iterate) == "Нет информации о валюте"


def test_transaction_descriptions() -> None:
    description = transaction_descriptions([
        {"id": 111111,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "operationAmount": {
             "amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
         },
         "description": "Перевод организации № 1",
         "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"
         },
        {"id": 222222,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "operationAmount": {
             "amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
         },
         "description": "Перевод организации № 2",
         "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"
         },
        {"id": 333333,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"
         },
        {}
    ])
    assert next(description) == "Перевод организации № 1"
    assert next(description) == "Перевод организации № 2"
    assert next(description) == "Остутствует описание операции"
    assert next(description) == "Остутствует описание операции"


def test_card_number_generator() -> None:
    card_number = card_number_generator(9998, 10002)
    assert next(card_number) == "0000 0000 0000 9998"
    assert next(card_number) == "0000 0000 0000 9999"
    assert next(card_number) == "0000 0000 0001 0000"
    assert next(card_number) == "0000 0000 0001 0001"
    assert next(card_number) == "0000 0000 0001 0002"
