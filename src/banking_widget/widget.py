from datetime import datetime
from src.banking_widget.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_or_card: str) -> str:
    """Маскирует номер карты или счета из строки с типом и номером."""
    parts = account_or_card.split()
    if len(parts) < 2:
        return "Ошибка. Перепроверьте правильность написания данных"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Конвертирует дату из ISO-формата в формат ДД.ММ.ГГГГ."""
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")