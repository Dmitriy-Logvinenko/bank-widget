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
        if item['state'] == state:
            new_list.append(item)

    return new_list


def sort_by_date(user_list: list[dict[str, Any]], is_sorted: bool = True) -> list[dict[str, Any]]:
    """
    Принимает список словарей  данными о банковских операциях и фильтрует их по указанному направлению.
    :param user_list: список словарей, содержащих данные о банковских операциях.
    :type user_list: list[dict[str, Any]]
    :param is_sorted: направление, по которому фильтруются операции, по умолчанию 'True'.
    :type is_sorted: bool
    :return: список словарей, отфильтрованных по направлению.
    :rtype: list[dict[str, Any]]
    """
    new_list = sorted(user_list, key=lambda k: k['date'], reverse=is_sorted)

    return new_list


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
