from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions: list[dict], currency: str) -> None:
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]
    assert next(generator) == transactions[3]


def test_transaction_descriptions(transactions: list[dict]) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_card_number_generator() -> None:
    card_generator = card_number_generator(1, 5)
    assert next(card_generator) == "0000 0000 0000 0001"
    assert next(card_generator) == "0000 0000 0000 0002"
    assert next(card_generator) == "0000 0000 0000 0003"
    assert next(card_generator) == "0000 0000 0000 0004"
    assert next(card_generator) == "0000 0000 0000 0005"
