def filter_by_currency(transactions: list, currency: str):
    """Фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> str:
    """Генерирует описания транзакций по одному."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        yield (
            card_number[:4] + " " +
            card_number[4:8] + " " +
            card_number[8:12] + " " +
            card_number[12:16]
        )
