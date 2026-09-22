from unittest.mock import patch
from src.banking_widget.main import main


def test_main_json_executed(capsys):
    """Тест основного потока с JSON файлом."""
    inputs = ["1", "EXECUTED", "Нет", "Нет", "Нет"]
    with patch("builtins.input", side_effect=inputs):
        with patch(
            "src.banking_widget.main.get_transactions",
            return_value=[
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                }
            ],
        ):
            main()
    captured = capsys.readouterr()
    assert "Привет" in captured.out
    assert "EXECUTED" in captured.out


def test_main_invalid_status(capsys):
    """Тест с неверным статусом."""
    inputs = ["1", "INVALID", "EXECUTED", "Нет", "Нет", "Нет"]
    with patch("builtins.input", side_effect=inputs):
        with patch(
            "src.banking_widget.main.get_transactions",
            return_value=[
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                }
            ],
        ):
            main()
    captured = capsys.readouterr()
    assert "недоступен" in captured.out


def test_main_empty_result(capsys):
    """Тест когда нет транзакций по фильтру."""
    inputs = ["1", "PENDING", "Нет", "Нет", "Нет"]
    with patch("builtins.input", side_effect=inputs):
        with patch(
            "src.banking_widget.main.get_transactions",
            return_value=[],
        ):
            main()
    captured = capsys.readouterr()
    assert "Не найдено" in captured.out


def test_main_csv(capsys):
    """Тест с CSV файлом."""
    inputs = ["2", "EXECUTED", "Нет", "Нет", "Нет"]
    with patch("builtins.input", side_effect=inputs):
        with patch(
            "src.banking_widget.main.get_transactions_from_csv",
            return_value=[],
        ):
            main()
    captured = capsys.readouterr()
    assert "CSV" in captured.out


def test_main_invalid_choice(capsys):
    """Тест с неверным выбором файла."""
    inputs = ["5"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert "Неверный выбор" in captured.out
