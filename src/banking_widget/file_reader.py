import pandas as pd


def get_transactions_from_csv(file_path: str) -> list:
    """Читает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path, sep=";")
        return df.to_dict(orient="records")
    except Exception:
        return []


def get_transactions_from_excel(file_path: str) -> list:
    """Читает финансовые операции из Excel-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []
