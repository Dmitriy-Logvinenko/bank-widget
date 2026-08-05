import src.masks as masks


def mask_account_card(user_number: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    new_list = user_number.split()

    for i in range(1):
        if new_list[0] == 'Счет':
            new_list[1] = masks.get_mask_account(new_list[1])
        elif new_list[1].isdigit():
            new_list[1] = masks.get_mask_card_number(new_list[1])
        elif new_list[2].isdigit():
            new_list[2] = masks.get_mask_card_number(new_list[2])
        else:
            return 'Некоректно введены данные.'

    return ' '.join(new_list)
