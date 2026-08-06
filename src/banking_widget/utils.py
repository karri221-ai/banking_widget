import json


def get_transactions(file_path: str) -> list:
    """Читает JSON-файл и возвращает список транзакций."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
