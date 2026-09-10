import json


def financial_transaction_data(filename: str) -> list:
    """
    Возвращает данные о финансовых транзакциях.
    :param filename: Имя файла
    :type filename: str
    :return: список с данными о финансовых транзакциях
    :rtype: list
    """
    try:
        with open('data/' + filename, 'r', encoding='utf-8') as f:
            if type(f) != list:
                return []
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
