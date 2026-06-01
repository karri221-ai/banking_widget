from datetime import datetime
from src.banking_widget.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_or_card: str) -> str:
    parts = account_or_card.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")