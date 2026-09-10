import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def amount_transaction(transaction: dict) -> float:
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
