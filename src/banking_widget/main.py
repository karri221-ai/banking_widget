from src.banking_widget.file_reader import get_transactions_from_csv, get_transactions_from_excel
from src.banking_widget.processing import filter_by_state, sort_by_date
from src.banking_widget.search import process_bank_search
from src.banking_widget.utils import get_transactions
from src.banking_widget.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = get_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = get_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Пользователь: ").upper()
        if state in valid_states:
            print(f'Операции отфильтрованы по статусу "{state}"')
            transactions = filter_by_state(transactions, state)
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    # Сортировка по дате
    sort_answer = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if sort_answer == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse=reverse)

    # Фильтрация по валюте
    currency_answer = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if currency_answer == "да":
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            or t.get("currency_code") == "RUB"
        ]

    # Поиск по описанию
    search_answer = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).lower()
    if search_answer == "да":
        search_query = input("Введите слово для поиска:\nПользователь: ")
        transactions = process_bank_search(transactions, search_query)

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        date = get_date(t.get("date", ""))
        description = t.get("description", "")
        from_account = t.get("from", "")
        to_account = t.get("to", "")

        if from_account:
            from_masked = mask_account_card(from_account)
        else:
            from_masked = ""

        to_masked = mask_account_card(to_account) if to_account else ""

        amount = t.get("operationAmount", {}).get("amount") or t.get("amount", "")
        currency = t.get("operationAmount", {}).get("currency", {}).get("name") or t.get("currency_name", "")

        print(f"{date} {description}")
        if from_masked:
            print(f"{from_masked} -> {to_masked}")
        else:
            print(f"{to_masked}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
