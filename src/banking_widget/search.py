import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет транзакции по строке в описании используя регулярные выражения."""
    return [
        transaction for transaction in data
        if re.search(search, transaction.get("description", ""), re.IGNORECASE)
    ]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций по категориям из поля description."""
    descriptions = [
        transaction.get("description", "")
        for transaction in data
        if transaction.get("description", "") in categories
    ]
    return dict(Counter(descriptions))
