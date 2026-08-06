from unittest.mock import patch
from src.banking_widget.external_api import get_transaction_amount_in_rub


def test_rub_transaction():
    """Тест транзакции в рублях — API не вызывается."""
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "RUB"}
        }
    }
    result = get_transaction_amount_in_rub(transaction)
    assert result == 1000.0


def test_usd_transaction():
    """Тест конвертации USD через mock API."""
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 8000.0}
        result = get_transaction_amount_in_rub(transaction)
        assert result == 8000.0


def test_eur_transaction():
    """Тест конвертации EUR через mock API."""
    transaction = {
        "operationAmount": {
            "amount": "50.00",
            "currency": {"code": "EUR"}
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 5000.0}
        result = get_transaction_amount_in_rub(transaction)
        assert result == 5000.0
