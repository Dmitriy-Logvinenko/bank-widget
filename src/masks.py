# Функция скрытия номера карты
def get_mask_card_number(card_number: str) -> str:
    """Возвращает скрытый номер карты."""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number[:6] + "******" + card_number[-4:]
        number_chunks = [mask_number[i : i + 4] for i in range(0, len(mask_number), 4)]
        return " ".join(number_chunks)
    else:
        return "Номер карты должен содержать 16 цифр без пробелов."


# Функция скрытия номера счёта
def get_mask_account(account_number: str) -> str:
    """Возвращает скрытый номер счёта."""
    if not account_number.isdigit():
        return "Номер счёта должен содержать только цифры без пробелов."
    elif len(account_number) < 4:
        return "Номер счёта не может быть короче четырёх символов."
    else:
        mask_number = "**" + account_number[-4:]
        return mask_number
