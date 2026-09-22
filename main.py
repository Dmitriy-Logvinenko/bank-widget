import src.utils, src.reading


def main():
    print('Программа: Привет! Добро пожаловать в программу работы'
    'с банковскими транзакциями.\n'
    'Выберите необходимый пункт меню:\n'
    '1. Получить информацию о транзакциях из JSON-файла\n'
    '2. Получить информацию о транзакциях из CSV-файла\n'
    '3. Получить информацию о транзакциях из XLSX-файла')

    while True:
        user_option = input('Введите один из вариантов: 1, 2 или 3: ')

        if user_option in '123':
            if user_option == '1':
                print('Для обработки выбран JSON-файл.')
                src.utils.financial_transaction_data('operations.json')
                break
            elif user_option == '2':
                print('Для обработки выбран CSV-файл.')
                src.reading.reading_csv('data/transactions.csv')
                break
            elif user_option == '3':
                print('Для обработки выбран XLSX-файл.')
                src.reading.reading_excel('data/transactions_excel.xlsx')
                break
        elif user_option not in '123':
            print('Такого варианта нет.')
        if not user_option:
            print('Вы ничего не ввели.')


if __name__ == '__main__':
    main()