import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формат XXXX XX** **** XXXX."""
    if len(card_number) != 16:
        logger.error(f"Некорректный номер карты: длина {len(card_number)} символов")
        return "Некорректный номер карты"
    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info("Номер карты успешно замаскирован")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формат **XXXX."""
    if len(account_number) < 4:
        logger.error(f"Некорректный номер счета: длина {len(account_number)} символов")
        return "Некорректный номер счета"
    result = f"**{account_number[-4:]}"
    logger.info("Номер счета успешно замаскирован")
    return result
