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
        url_usd = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}'
        url_eur = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}'

        if transaction['operationAmount']['currency']['code'] == 'USD':
            response = requests.get(url_usd, headers={'apikey': API_KEY})
            result = response.json()
            result = round(result['result'], 2)
        elif transaction['operationAmount']['currency']['code'] == 'EUR':
            response = requests.get(url_eur, headers={'apikey': API_KEY})
            result = response.json()
            result = round(result['result'], 2)
        else:
            result = amount

    return result
