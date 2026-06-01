def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формат XXXX XX** **** XXXX."""
    if len(card_number) != 16:
        return "Некорректный номер карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формат **XXXX."""
    if len(account_number) < 4:
        return "Некорректный номер счета"
    return f"**{account_number[-4:]}"
