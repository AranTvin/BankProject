import pytest

import datetime

from src.decorators import log


def test_log_error(capsys):
    @log
    def my_function():
        result = 1 / 0
        captured = capsys.readouterr()
        assert ("Функция: my_function\n"
                "Тип ошибки: ZeroDivisionError\n"
                "Входные параметры:1, 0, {}") in captured.out


def test_log_success(capsys):
    @log
    def my_function():
        result = 1 / 1
        captured = capsys.readouterr()
        assert (f"Функция: my_function\n"
                f"Время запуска: {datetime.datetime.now()}\n"
                f"Время окончания: {datetime.datetime.now()}\n"
                f"Статус: OK") in captured.out