import pandas as pd
import pytest
from unittest.mock import patch

from src.banking_widget.file_reader import get_transactions_from_csv, get_transactions_from_excel


@pytest.fixture
def sample_data():
    return pd.DataFrame([
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-09-05",
            "amount": 1000.0,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 123",
            "to": "Счет 456",
            "description": "Перевод"
        }
    ])


def test_get_transactions_from_csv(sample_data):
    """Тест чтения CSV файла."""
    with patch("pandas.read_csv", return_value=sample_data):
        result = get_transactions_from_csv("fake.csv")
        assert len(result) == 1
        assert result[0]["state"] == "EXECUTED"


def test_get_transactions_from_csv_error():
    """Тест обработки ошибки при чтении CSV."""
    with patch("pandas.read_csv", side_effect=Exception("File not found")):
        result = get_transactions_from_csv("fake.csv")
        assert result == []


def test_get_transactions_from_excel(sample_data):
    """Тест чтения Excel файла."""
    with patch("pandas.read_excel", return_value=sample_data):
        result = get_transactions_from_excel("fake.xlsx")
        assert len(result) == 1
        assert result[0]["state"] == "EXECUTED"


def test_get_transactions_from_excel_error():
    """Тест обработки ошибки при чтении Excel."""
    with patch("pandas.read_excel", side_effect=Exception("File not found")):
        result = get_transactions_from_excel("fake.xlsx")
        assert result == []
