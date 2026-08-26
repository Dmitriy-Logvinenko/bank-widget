import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("user_number, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(user_number: str, expected: str) -> None:
    assert mask_account_card(user_number) == expected


def test_mask_account_card_empty() -> None:
    assert mask_account_card("") == "Вы ничего не ввели."


def test_mask_account_card_correct() -> None:
    assert mask_account_card("1596837868705199") == "Некорректно введены данные."


def test_get_date(user_date: str) -> None:
    assert get_date(user_date) == "11.03.2024"
