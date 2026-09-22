import src.processing
import src.reading
import src.utils


def main() -> None:
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
        user_status = src.processing.filter_by_state(user_data, user_filter_status.upper())
    else:
        print(f'Статус операции "{user_filter_status}" недоступен.')

    print('Отсортировать операции по дате? Да/Нет')

    is_user_sort_status = input()
    if is_user_sort_status.lower() == 'да':
        print('Отсортировать по возрастанию или по убыванию?')
        user_sort_status = input()

        if user_sort_status.lower() in ['по возрастанию', 'по убыванию']:
            if user_sort_status.lower() == 'по возрастанию':
                user_sorted = src.processing.sort_by_date(user_status, False)
            elif user_sort_status.lower() == 'по убыванию':
                user_sorted = src.processing.sort_by_date(user_status)
        else:
            user_sorted = user_status
            print('Статус введён некорректно. Сортировка отменена.')
    else:
        user_sorted = user_status

    print('Выводить только рублевые транзакции? Да/Нет')

    is_rub_status = input()
    if is_rub_status.lower() == 'да':
        rub_sorted = list()

        for item in user_sorted:
            if 'operationAmount' in item:
                if item["operationAmount"]["currency"]["code"] == 'RUB':
                    rub_sorted.append(item)
    else:
        rub_sorted = user_sorted

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

    is_search_status = input()
    if is_search_status.lower() == 'да':
        user_search_word = input('Введите слово для фильтрации: ')
        user_search = src.processing.process_bank_search(rub_sorted, user_search_word)
    else:
        user_search = rub_sorted

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(user_search)}')
    print(user_search)

    if not user_search or user_search == []:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.')


if __name__ == '__main__':
    main()
