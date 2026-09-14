import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transaction_data(filename: str) -> list:
    """
    Возвращает данные о финансовых транзакциях.
    :param filename: Имя файла
    :type filename: str
    :return: список с данными о финансовых транзакциях
    :rtype: list
    """
    try:
        logger.info("Выполняется чтение файла.")
        with open('data/' + filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if not isinstance(data, list):
                logger.info("Файл пуст.")
                data = []

            logger.info("Чтение файла завершено.")
            return data

    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []
