import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions(file_path: str) -> list:
    """Читает JSON-файл и возвращает список транзакций."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан, загружено {len(data)} транзакций")
                return data
            logger.error(f"Файл {file_path} содержит не список")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {file_path} содержит некорректный JSON")
        return []
