from typing import Any


def filter_by_state(user_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """
    Принимает список словарей с данными о банковских операциях и фильтрует их по указанному состоянию.

    :param user_list: список словарей, содержащих данные о банковских операциях.
    :type user_list: list[dict[str, Any]]
    :param state: состояние, по которому фильтруются операции, по умолчанию 'EXECUTED'.
    :type state: str
    :return: список словарей, отфильтрованных по состоянию.
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
    :param user_list: список словарей, содержащих данные о банковских операциях.
    :type user_list: list[dict[str, Any]]
    :param is_sorted: направление, по которому фильтруются операции, по умолчанию 'True'.
    :type is_sorted: bool
    :return: список словарей, отфильтрованных по направлению.
    :rtype: list[dict[str, Any]]
    """
    new_list = sorted(user_list, key=lambda k: k['date'], reverse=is_sorted)

    return new_list
