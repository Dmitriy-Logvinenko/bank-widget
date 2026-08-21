def filter_by_state(user_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и ключ. Возвращает список словарей по ключу"""
    new_list = list()

    for item in user_list:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(user_list: list[dict], is_sorted: bool = True) -> list[dict]:
    """Принимает список словарей и параметр сортировки. Возвращает отсортированный список словарей."""
    new_list = sorted(user_list, key=lambda k: k["date"], reverse=is_sorted)

    return new_list
