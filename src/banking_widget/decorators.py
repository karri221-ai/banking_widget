def log(filename=None):
    """Декоратор для логирования работы функции."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

            except Exception as e:
                message = (
                    f"{func.__name__} error: {e}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise

        return wrapper
    return decorator
