from typing import Any

from src.generators import filter_by_currency


def test_filter_by_currency(transactions, currency):
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[0]
