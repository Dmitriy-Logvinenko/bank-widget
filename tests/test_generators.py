from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, currency):
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]
    assert next(generator) == transactions[3]


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
