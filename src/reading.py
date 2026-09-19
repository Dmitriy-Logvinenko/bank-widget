import csv
import pandas as pd


def reading_csv(file_path: str) -> list[dict]:
    """
    Считывает данные из csv-файла и возвращает их как список словарей
    :param file_path: Путь до csv-файла
    :type file_path: str
    :return: данные о финансовых операциях
    :rtype: list[dict]
    """
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        csv_list = []

        for row in reader:
            csv_list.append(row)

        return csv_list


def reading_xlsx(file_path: str) -> list[dict]:
    """
    Считывает данные из excel-файла и возвращает их как список словарей
    :param file_path: Путь до xlsx-файла
    :type file_path: str
    :return: данные из таблицы с финансовыми операциями
    :rtype: list[dict]
    """
    excel_data = pd.read_excel(file_path)

    return excel_data.to_dict(orient="records")
