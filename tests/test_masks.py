import pytest

from src.masks import get_mask_card_number, get_mask_account


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


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("64686473678894779589", "**9589"),
    ("35383033474447895560", "**5560")
])
def test_get_mask_account(account_number: str, expected: str):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_no_isdigit(account_number):
    assert get_mask_account("Номер счёта") == "Номер счёта должен содержать только цифры без пробелов."


def test_get_mask_account_len():
    assert get_mask_account("345") == "Номер счёта не может быть короче четырёх символов."
