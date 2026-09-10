import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY", "default_value")


def amount_transaction(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях.
    :param transaction: Словарь с данными о финансовых транзакциях.
    :type transaction: dict
    :return: Сумма транзакции в рублях.
    :rtype: float
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    for _ in transaction:
        if currency != "RUB":
            response = requests.get(url, headers={"apikey": API_KEY})
            return round(response.json()["result"], 2)

    return amount
