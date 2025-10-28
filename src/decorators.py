import datetime


def log(filename):
    """Декоратор. Отображает имя функции и статус при успешном выполнении;
    отображает имя, тип ошибки и введенные данные при ошибке"""
    def inner_log(func):
        def wrapper(*args, **kwargs):
            try:
                function_result = func(*args, **kwargs)
                log_message = (f"Функция: {func.__name__}\n"
                               f"Время запуска: {datetime.datetime.now()}\n"
                               f"Время окончания: {datetime.datetime.now()}\n"
                               f"Статус: OK")
                if filename:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return function_result
            except Exception as e:
                error_message = (f"Функция: {func.__name__}\n"
                                 f"Тип ошибки: {e}\n"
                                 f"Входные параметры:{args}, {kwargs}")
                if filename:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
        return wrapper
    return inner_log

@log(filename="")
def myfunc(a, b):
    return a + b

myfunc(2, 1)