def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Фильтрует список операций по значению ключа state."""
    result = []
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result

def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Сортирует список операций по дате."""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)