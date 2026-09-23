from unittest.mock import patch, mock_open
from src.banking_widget.utils import get_transactions


def test_get_transactions_success():
    """Тест успешного чтения JSON файла."""
    mock_data = '[{"id": 1, "amount": "100"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_transactions("fake_path.json")
        assert result == [{"id": 1, "amount": "100"}]


def test_get_transactions_empty_file():
    """Тест пустого файла."""
    with patch("builtins.open", mock_open(read_data="[]")):
        result = get_transactions("fake_path.json")
        assert result == []


def test_get_transactions_not_list():
    """Тест когда JSON содержит не список."""
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        result = get_transactions("fake_path.json")
        assert result == []


def test_get_transactions_file_not_found():
    """Тест когда файл не найден."""
    result = get_transactions("nonexistent.json")
    assert result == []
