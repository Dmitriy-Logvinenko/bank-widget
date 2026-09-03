import time
from functools import wraps
from typing import Optional

from mypy.types import Any


def log(filename: Optional[str]=None) -> Any:
    """
    Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    :param filename: Аргумент, который определяет, куда будут записываться логи (по умолчанию в консоль)
    :type filename: str
    :return: Время работы функции, а также её результат в случае успешного выполнения,
    или информацию о возникшей ошибке в консоль или указанный файл.
    :rtype: None
    """
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            error = None
            result = None
            text_error = None

            try:
                result = func(*args, **kwargs)
                status = "ok"
            except Exception as e:
                status = "error"
                error = e
                text_error = str(error)

            end = time.perf_counter()
            time_work = end - start

            if filename:
                with open(filename, 'a', encoding="UTF-8") as f:
                    f.write(f'Time work: {time_work}\n')

                    if status == "ok":
                        f.write(f"{func.__name__}: {status} - {result}\n")
                    else:
                        f.write(f"{func.__name__} {type(error).__name__}: {text_error}. Inputs: {args}, {kwargs}")
            else:
                print(f'Time work: {time_work}\n')

                if status == "ok":
                    print(f"{func.__name__}: {status} - {result}\n")
                else:
                    print(f"{func.__name__} {type(error).__name__}: {text_error}. Inputs: {args}, {kwargs}")

            return result

        return inner

    return wrapper
