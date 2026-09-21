import re

from typing import Any


def filter_by_state(user_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """
    Принимает список словарей с данными о банковских операциях и фильтрует их по указанному состоянию.
    :param user_list: Данные о банковских операциях
    :type user_list: list[dict[str, Any]]
    :param state: Состояние, по которому фильтруются операции, по умолчанию 'EXECUTED'
    :type state: str
    :return: список словарей, отфильтрованных по состоянию
    :rtype: list[dict[str, Any]]
    """
    new_list = list()

    for item in user_list:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(user_list: list[dict[str, Any]], is_sorted: bool = True) -> list[dict[str, Any]]:
    """
    Принимает список словарей данными о банковских операциях и фильтрует их по указанному направлению.
    :param user_list: Данные о банковских операциях
    :type user_list: list[dict[str, Any]]
    :param is_sorted: направление, по которому фильтруются операции, по умолчанию 'True'
    :type is_sorted: bool
    :return: список словарей, отфильтрованных по направлению
    :rtype: list[dict[str, Any]]
    """
    new_list = sorted(user_list, key=lambda k: k['date'], reverse=is_sorted)

    return new_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Обрабатывает банковские запросы.
    :param data: Данные о банковских операциях
    :type data: list[dict]
    :param search: Строка запроса
    :type search: str
    :return: Данные, в которых присутствует строка запроса
    :rtype: list[dict]
    """
    search_list = []

    try:
        for item in data:
            # Проверка на наличие ключа
            if 'description' in item:
                # Поиск запроса по ключу
                operation = re.findall(search, item['description'])
                if operation:
                    # Добавление операции в список
                    search_list.append(item)
    # Вывод в случае ошибки
    except Exception as e:
        print(e)

    return search_list
