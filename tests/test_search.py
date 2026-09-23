import pytest
from src.banking_widget.search import process_bank_search, process_bank_operations


@pytest.fixture
def transactions():
    return [
        {"id": 1, "description": "Перевод организации", "state": "EXECUTED"},
        {"id": 2, "description": "Перевод со счета на счет", "state": "EXECUTED"},
        {"id": 3, "description": "Открытие вклада", "state": "CANCELED"},
    ]


def test_process_bank_search_found(transactions):
    """Тест поиска по строке — найдено."""
    result = process_bank_search(transactions, "Перевод")
    assert len(result) == 2


def test_process_bank_search_not_found(transactions):
    """Тест поиска по строке — не найдено."""
    result = process_bank_search(transactions, "Зарплата")
    assert result == []


def test_process_bank_search_case_insensitive(transactions):
    """Тест поиска без учёта регистра."""
    result = process_bank_search(transactions, "перевод")
    assert len(result) == 2


def test_process_bank_operations(transactions):
    """Тест подсчёта категорий."""
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations(transactions, categories)
    assert result["Перевод организации"] == 1
    assert result["Открытие вклада"] == 1


def test_process_bank_operations_empty(transactions):
    """Тест подсчёта с пустыми категориями."""
    result = process_bank_operations(transactions, [])
    assert result == {}
