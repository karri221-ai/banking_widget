# Banking Widget

Виджет банковских операций клиента.

## Описание

Проект содержит функции для маскировки банковских данных и обработки списка операций.

## Функции

### masks.py
- `get_mask_card_number(card_number)` — маскирует номер карты: `7000 79** **** 6361`
- `get_mask_account(account_number)` — маскирует номер счета: `**4305`

### widget.py
- `mask_account_card(account_or_card)` — принимает строку с типом и номером карты или счета, возвращает маску
- `get_date(date_string)` — конвертирует дату из ISO-формата в `ДД.ММ.ГГГГ`

### processing.py
- `filter_by_state(operations, state='EXECUTED')` — фильтрует список операций по статусу
- `sort_by_date(operations, reverse=True)` — сортирует список операций по дате

## Примеры

```python
from src.banking_widget.widget import mask_account_card
mask_account_card('Visa Platinum 7000792289606361')  # 'Visa Platinum 7000 79** **** 6361'

from src.banking_widget.processing import filter_by_state
filter_by_state(operations, 'CANCELED')  # только отменённые операции
```

## Установка

Проект использует Poetry. Для установки зависимостей:
```
poetry install
```

## Тестирование

Проект покрыт тестами с использованием `pytest`.

Запуск тестов:
```
poetry run pytest
```

Запуск тестов с отчётом о покрытии:
```
poetry run pytest --cov=src --cov-report=html
```

HTML-отчёт о покрытии находится в папке `htmlcov/` (откройте `htmlcov/index.html` в браузере).

Текущее покрытие кода тестами: 100%

### generators.py
- `filter_by_currency(transactions, currency)` — фильтрует транзакции по коду валюты, возвращает итератор
- `transaction_descriptions(transactions)` — генерирует описания транзакций по одному
- `card_number_generator(start, stop)` — генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне

### Пример использования generators.py
```python
from src.banking_widget.generators import card_number_generator, filter_by_currency

for card in card_number_generator(1, 3):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003

usd = filter_by_currency(transactions, "USD")
print(next(usd))  # первая USD транзакция
```

### decorators.py
- `log(filename=None)` — декоратор для логирования работы функции. Если `filename` задан — пишет в файл, иначе в консоль.

### Пример использования decorators.py
```python
from src.banking_widget.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)  # запишет "my_function ok" в mylog.txt
```
### utils.py
- `get_transactions(file_path)` — читает JSON-файл и возвращает список транзакций. При ошибке возвращает пустой список.

### external_api.py
- `get_transaction_amount_in_rub(transaction)` — конвертирует сумму транзакции в рубли. Использует Exchange Rates Data API для USD и EUR.

## Переменные окружения
Создайте файл `.env` на основе `.env.example` и добавьте ваш API ключ:
```
API_KEY=ваш_ключ
```