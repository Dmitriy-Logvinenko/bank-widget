import src.masks as masks


# Функция обработки данных
def mask_account_card(user_number: str) -> str:
    """Возвращает скрытую информацию о картах и счетах"""
    new_list = user_number.split()

    if user_number:
        for i in range(1):
            if new_list[0] == "Счет":
                new_list[1] = masks.get_mask_account(new_list[1])
            elif new_list[1].isdigit():
                new_list[1] = masks.get_mask_card_number(new_list[1])
            elif new_list[2].isdigit():
                new_list[2] = masks.get_mask_card_number(new_list[2])
            else:
                return "Некоректно введены данные."
    else:
        return "Вы ничего не ввели."
    return " ".join(new_list)


# Функция обработки дат
def get_date(user_date: str) -> str:
    new_date = user_date[:10].split("-")
    reversed_date = new_date[::-1]
    return ".".join(reversed_date)


if __name__ == "__main__":
    print(mask_account_card(input()))
    print(get_date(input()))
