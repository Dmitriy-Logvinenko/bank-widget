import src.masks as masks


def mask_account_card(user_number: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    new_list = user_number.split()
    for i in range(1):
        if new_list[0] == 'Cчет':
            new_list[1] = masks.get_mask_account(new_list[1])

    return ' '.join(new_list)


print(mask_account_card('Cчет 765849673576389'))
