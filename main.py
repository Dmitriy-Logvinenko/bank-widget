import src.utils, src.reading, src.processing


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
                user_data = src.utils.financial_transaction_data('operations.json')
                break
            elif user_option == '2':
                print('Для обработки выбран CSV-файл.')
                user_data = src.reading.reading_csv('data/transactions.csv')
                break
            elif user_option == '3':
                print('Для обработки выбран XLSX-файл.')
                user_data = src.reading.reading_excel('data/transactions_excel.xlsx')
                break
        elif user_option not in '123':
            print('Такого варианта нет.')
        if not user_option:
            print('Вы ничего не ввели.')


    print('\nВведите статус, по которому необходимо выполнить фильтрацию.\n'
    'Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING')

    user_filter_status = input()

    if user_filter_status.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Операции отфильтрованы по статусу {user_filter_status.upper()}.')
        user_state = src.processing.filter_by_state(user_data, user_filter_status.upper())
    else:
        print(f'Статус операции "{user_filter_status}" недоступен.')


if __name__ == '__main__':
    main()
