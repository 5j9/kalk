from unittest.mock import patch

from _kalk import evaluate, APPEND, e, CLEAR, STACK


def test_add():
    assert evaluate('1 +2 +') == 3


def test_negative():
    assert evaluate('-1 -2 -') == 1


def test_empty():
    CLEAR()
    assert evaluate('') is None
    APPEND(1)
    assert evaluate('') == 1


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
    CLEAR()
    assert evaluate('sin') is None
    mocked_print.assert_called_once_with('Error: not enough arguments')


def test_eulers_number():
    assert evaluate('e') is e


def test_distance():
    assert evaluate('0 1 0 0 dist2') == 1.0


@patch('builtins.print')
def test_chr(mocked_print):
    assert evaluate('65.1 chr') == 65.1
    mocked_print.assert_called_once_with('A')


def test_sum_fsum():
    CLEAR()
    assert evaluate('1 2 3sum') == 6
    assert evaluate('6fsum') == 12.0


def test_thousand_separator():
    assert evaluate('1,234 5 +') == 1239


def test_swap():
    CLEAR()
    APPEND(1)
    APPEND(2)
    evaluate('<>')
    assert STACK == [2, 1]


def test_float_without_leading_zero():
    assert evaluate('.9') == .9


def test_leading_positive_sign():
    assert evaluate('+1 -1 +') == 0


def test_complex():
    assert evaluate('1+2j 0j -') == 1+2j


def test_capital_e():
    assert evaluate('2E-2') == .02


@patch('builtins.print')
def test_syntax_error(mocked_print):
    assert evaluate('a') is None
    mocked_print.assert_called_once_with('SyntaxError')


@patch('builtins.print')
def test_preserve_stack_on_binary_fail(mocked_print):
    CLEAR()
    APPEND(1)
    evaluate('*')
    assert STACK == [1]
    mocked_print.assert_called_once_with('Error: not enough arguments')


def test_ignore_underscore_in_numbers():
    assert evaluate('1_2.3_4e0_6J') == 12340000j


@patch('_kalk.paste', lambda: '+0j')
@patch('_kalk.copy')
def test_copy_paste(copy_mock):
    assert evaluate('pst') == 0j
    evaluate('cp')
    copy_mock.assert_called_once_with('0j')


def test_pop():
    CLEAR()
    APPEND(7)
    APPEND(8)
    assert evaluate('1 del') == 7
    assert STACK == [7]


def test_repeat():
    APPEND(7)
    assert evaluate('rep +') == 14


@patch('builtins.print')
def test_sto_rcl(mocked_print):
    CLEAR()
    assert evaluate('1 2 sto 3 4 + 2 rcl +') == 8
    assert evaluate('1 rcl +') is None
    mocked_print.assert_called_once_with('KeyError')


@patch('builtins.print')
def test_zero_division(mocked_print):
    assert evaluate('1 0 /') is None
    mocked_print.assert_called_once_with('ZeroDivisionError')
