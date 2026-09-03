import pytest
from src.decorators import log


def test_log(capsys):
    @log(filename=None)
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add: ok - 3" in captured.out


def test_zero_log(capsys):
    @log(filename=None)
    def division(x, y):
        return x / y
    division(1, 0)
    captured = capsys.readouterr()
    assert "division ZeroDivisionError: division by zero. Inputs: (1, 0), {}" in captured.out


def test_log_incorrect(capsys):
    @log(filename=None)
    def add(x, y):
        return x + y
    add("1", 2)
    captured = capsys.readouterr()
    assert 'add TypeError: can only concatenate str (not "int") to str. Inputs: (\'1\', 2), {}\n' in captured.out
