import json


def financial_transaction_data():
    try:
        with open('data/operations.json', encoding='utf-8') as f:
            return json.load(f) if f else []
    except FileNotFoundError:
        return []
