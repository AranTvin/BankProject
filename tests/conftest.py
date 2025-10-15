from typing import Generator

import pytest

from src.generators import filter_by_currency


@pytest.fixture()
def filtered_by_state() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture()
def sorted_by_date() -> list[dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '03.07.2019'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '14.10.2018'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '12.09.2018'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'}
    ]


@pytest.fixture()
def got_date() -> str:
    return "11.03.2024"


@pytest.fixture()
def filter_by_currency_iterate() -> Generator[dict | str]:
    filter_by_currency_list = [
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
    ]
    return filter_by_currency(filter_by_currency_list, "USD")
