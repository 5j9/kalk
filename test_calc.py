from unittest.mock import patch

from calc import evaluate, stack, append, e


def test_add():
    assert evaluate('1 2 +') == 3


def test_negative():
    assert evaluate('-1 -2 -') == 1


def test_empty():
    stack.clear()
    assert evaluate('') is None
    append(1)
    assert evaluate('') is 1


def test_percent():
    assert evaluate('1 2 %%') == 100.0


def test_persian_digits():
    assert evaluate('۱ ۲ /') == 0.5


def test_float():
    assert evaluate('1.2 1e2 *') == 120


def test_cos():
    assert evaluate('pi cos') == -1.0


def test_factorial():
    assert evaluate('3!') == 6


@patch('builtins.print')
def test_invalid_op(mocked_print):
    stack.clear()
    assert evaluate('sin') is None
    mocked_print.assert_called_once_with('not enough arguments')


def test_eulers_number():
    assert evaluate('e') is e


def test_distance():
    assert evaluate('0 1 0 0 dist2') == 1.0


@patch('builtins.print')
def test_chr(mocked_print):
    assert evaluate('65.1 chr') == 65.1
    mocked_print.assert_called_once_with('A')


def test_sum_fsum():
    stack.clear()
    assert evaluate('1 2 3sum') == 6
    assert evaluate('6fsum') == 12.0
