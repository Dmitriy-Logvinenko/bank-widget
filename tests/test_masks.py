import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1596837868705199", "1596 83** **** 5199"),
    ("6831982476737658", "6831 98** **** 7658")
])
def test_get_mask_card_number(card_number: str, expected: str):
    assert get_mask_card_number(card_number) == expected


def test_get_card_number_len(card_number: str):
    assert get_mask_card_number(card_number + '1') == "Номер карты должен содержать 16 цифр без пробелов."


def test_get_card_number_correct():
    assert get_mask_card_number('Номер карты') == "Номер карты должен содержать 16 цифр без пробелов."
