from mypy.types import Any


def filter_by_currency(transactions: list[dict], currency: str) -> Any:
    """
    Принимает транзакции и валюту.
    Возвращает итератор, поочерёдно выдающий транзакции по заданной валюте
    :param transactions: Список словарей, представляющих транзакции
    :type transactions: list[dict]
    :param currency: значение, по которому возвращаются транзакции
    :type currency: str
    :return: транзакции по валюте
    :rtype: Any
    """
    while True:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Any:
    """
    Принимает транзакции и возвращает их описание.
    :param transactions: Список словарей, представляющих транзакции
    :type transactions: list[dict]
    :return: Описание транзакций
    :rtype: Any
    """
    while True:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start: int, final: int) -> Any:
    """
    Генерирует номера карт по диапазону номеров
    :param start: Начальное значение диапазона
    :type start: int
    :param final: Конечное значение диапазона
    :type final: int
    :return: Номера карт по диапазону
    :rtype: Any
    """
    for i in range(start, final + 1):
        new_card_number = f"{i:016}"
        yield " ".join([new_card_number[i: i + 4] for i in range(0, 16, 4)])
        if new_card_number == "9999 9999 9999 9999":
            break
