# Проект "Банковский виджет"

## Описание:

Проект "Банковские виджет" - это веб-приложение на Python помогающее пользователю удобнее следить и управлять своими финансами.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:Dmitriy-Logvinenko/bank-widget.git
```

## Использование:

1. Откройте свой терминал.
2. Запустите проект с помощью команды:
```
python src/processing.py
```

## Изменения:

1. Добавлены зависимости в requirements.txt.
2. Добавлены тесты для функций:
    - get_mask_card_number
    - get_mask_account
    - mask_account_card
    - get_date
    - filter_by_state
    - sort_by_date
3. В функции `mask_account_card` добавлена проверка
на ошибку *IndexError*