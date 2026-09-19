import csv


def reading_csv(file_path: str) -> list[dict]:
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        csv_list = []

        for row in reader:
            csv_list.append(row)

        return csv_list
