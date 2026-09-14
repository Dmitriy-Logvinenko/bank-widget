import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# Функция скрытия номера карты
def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает скрытый номер карты
    :param card_number: Номер карты пользователя
    :type card_number: str
    :return: Скрытый номер карты пользователя
    :rtype: str
    """
    try:
        logger.info("Обрабатываем номер карты пользователя.")

        if card_number.isdigit() and len(card_number) == 16:
            mask_number = card_number[:6] + "******" + card_number[-4:]
            number_chunks = [mask_number[i : i + 4] for i in range(0, len(mask_number), 4)]

            logger.info("Обработка номера карты прошла успешна.")

            return " ".join(number_chunks)
        else:
            logger.info("Обработка номера карты не может быть выполнена.")

            return "Номер карты должен содержать 16 цифр без пробелов."
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        return f"Произошла ошибка {ex}"


# Функция скрытия номера счёта
def get_mask_account(account_number: str) -> str:
    """
    Возвращает скрытый номер счёта.
    :param account_number: Номер счёта пользователя
    :type account_number: str
    :return: Скрытый номер счёта пользователя
    :rtype: str
    """
    try:
        logger.info("Обрабатываем номер счёта пользователя.")

        if not account_number.isdigit():
            logger.info("Не удалось обработать номер счёта из-за неподдерживаемых символов.")
            return "Номер счёта должен содержать только цифры без пробелов."

        elif len(account_number) < 4:
            logger.info("Не удалось обработать номер счёта из-за малой длины.")
            return "Номер счёта не может быть короче четырёх символов."

        else:
            mask_number = "**" + account_number[-4:]
            logger.info("Обработка номера счёта прошла успешно.")
            return mask_number

    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        return f"Произошла ошибка {ex}"
