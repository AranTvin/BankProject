import pytest


@pytest.fixture()
def filtered_by_state() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture()
def sorted_by_date() -> list:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '03.07.2019'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '14.10.2018'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '12.09.2018'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'}
    ]


@pytest.fixture()
def got_date() -> str:
    return "11.03.2024"
