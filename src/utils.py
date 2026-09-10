import json

from mypy.types import Any


def financial_transaction_data(filename: str) -> Any:
    """Возвращает данные о финансовых транзакциях"""
    try:
        with open('data/' + filename, encoding='utf-8') as f:
            return json.load(f) if f else []
    except FileNotFoundError, json.decoder.JSONDecodeError:
        return []
