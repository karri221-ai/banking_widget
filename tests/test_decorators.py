from src.banking_widget.decorators import log


def test_log_to_console(capsys):
    """Тест логирования в консоль при успешном выполнении."""
    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_error_to_console(capsys):
    """Тест логирования ошибки в консоль."""
    @log()
    def bad_func(x):
        raise ValueError("что-то пошло не так")

    try:
        bad_func(1)
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert "bad_func error" in captured.out
    assert "Inputs" in captured.out


def test_log_to_file(tmp_path):
    """Тест логирования в файл при успешном выполнении."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    multiply(2, 3)
    content = log_file.read_text()
    assert "multiply ok" in content


def test_log_error_to_file(tmp_path):
    """Тест логирования ошибки в файл."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def bad_func(x):
        raise TypeError("неверный тип")

    try:
        bad_func("hello")
    except TypeError:
        pass

    content = log_file.read_text()
    assert "bad_func error" in content
    assert "Inputs" in content
