import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def amount_transaction(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях.
    :param transaction: Словарь с данными о финансовых транзакциях.
    :type transaction: dict
    :return: Сумма транзакции в рублях.
    :rtype: float
    """
    for _ in transaction:
        amount = transaction['operationAmount']['amount']
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}'

        if transaction['operationAmount']['currency']['code'] != 'RUB':
            response = requests.get(url, headers={'apikey': API_KEY})
            result = response.json()
            result = round(result['result'], 2)
        else:
            result = amount

    return result
