import json

from mypy.types import Any


def financial_transaction_data() -> Any:
    """Возвращает данные о финансовых транзакциях"""
    try:
        with open('data/operations.json', encoding='utf-8') as f:
            return json.load(f) if f else []
    except FileNotFoundError:
        return []
