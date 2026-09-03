from typing import Any

from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log(capsys:CaptureFixture[str]) -> None:
    @log(filename=None)
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add: ok - 3" in captured.out


def test_zero_log(capsys:CaptureFixture[str]) -> None:
    @log(filename=None)
    def division(x: int, y: int) -> float| int:
        return x / y
    division(1, 0)
    captured = capsys.readouterr()
    assert "division ZeroDivisionError: division by zero. Inputs: (1, 0), {}" in captured.out


def test_log_incorrect(capsys: CaptureFixture[str]) -> None:
    @log(filename=None)
    def add(x: str, y: str) -> Any:
        return x + y
    add("1", 2)
    captured = capsys.readouterr()
    assert 'add TypeError: can only concatenate str (not "int") to str. Inputs: (\'1\', 2), {}\n' in captured.out
