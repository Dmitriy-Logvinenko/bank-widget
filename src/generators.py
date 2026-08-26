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
