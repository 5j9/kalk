from unittest.mock import patch

from _kalk import STACK, evaluate


def test_add():
    assert evaluate('1 +2 +') == 3


def test_negative():
    assert evaluate('-1 -2 -') == 1


def test_empty():
    del STACK[:]
    assert evaluate('') is None
    STACK.append(1)
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
    assert evaluate('c sin') is None
    mocked_print.assert_called_once_with('Error: not enough arguments')


def test_eulers_number():
    import math

    assert evaluate('e') is math.e


def test_distance():
    assert evaluate('[0 1] [0 0] dist') == 1.0


def test_chr():
    assert evaluate('65 chr') == 'A'


def test_sum_fsum():
    assert evaluate('[[1 2 3]sum') == 6
    assert evaluate('6]fsum') == 12.0


def test_thousand_separator():
    assert evaluate('1,234 5 +') == 1239


def test_swap():
    evaluate('c 1 2 <>')
    assert STACK == [2, 1]


def test_float_without_leading_zero():
    assert evaluate('.9') == 0.9


def test_leading_positive_sign():
    assert evaluate('+1 -1 +') == 0


def test_complex():
    assert evaluate('1+2j 0j -') == 1 + 2j


def test_capital_e():
    assert evaluate('2E-2') == 0.02


@patch('builtins.print')
def test_syntax_error(mocked_print):
    assert evaluate('invalid') is None
    mocked_print.assert_called_once_with('SyntaxError')


@patch('builtins.print')
def test_preserve_stack_on_binary_fail(mocked_print):
    evaluate('c 1 *')
    assert STACK == [1]
    mocked_print.assert_called_once_with('Error: not enough arguments')


def test_ignore_underscore_in_numbers():
    assert evaluate('1_2.3_4e0_6J') == 12340000j


@patch('pyperclip.paste', lambda: '+0j')
@patch('pyperclip.copy')
def test_copy_paste(copy_mock):
    assert evaluate('pst') == 0j
    evaluate('cp')
    copy_mock.assert_called_once_with('0j')


def test_pop():
    assert evaluate('c 7 8 1 del') == 7
    assert STACK == [7]


def test_answer():
    assert evaluate('7 a +') == 14


@patch('builtins.print')
def test_sto_rcl(mocked_print):
    assert evaluate('c 1 2 sto 3 4 + 2 rcl +') == 8
    assert evaluate('1 rcl +') is None
    mocked_print.assert_called_once_with('KeyError')


@patch('builtins.print')
def test_zero_division(mocked_print):
    assert evaluate('1 0 /') is None
    mocked_print.assert_called_once_with('ZeroDivisionError')


def test_notations():
    import _kalk

    v = evaluate('1 3 /')
    assert _kalk.FORMAT(v) == '0.3333333333333333'
    v = evaluate('eng')
    assert _kalk.FORMAT(v) == '333.33e-3'  # default precision is 5
    v = evaluate('sci')
    assert _kalk.FORMAT(v) == '3.33333e-01'
    v = evaluate('gen')
    assert _kalk.FORMAT(v) == '0.33333'
    v = evaluate('nrm')
    assert _kalk.FORMAT(v) == '0.3333333333333333'
    v = evaluate('2 prec')
    assert _kalk.FORMAT(v) == '0.3333333333333333'
    v = evaluate('eng')
    assert _kalk.FORMAT(v) == '333e-3'
    assert _kalk.FORMAT(0) == '0'
    v = evaluate('sci')
    assert _kalk.FORMAT(v) == '3.33e-01'
    v = evaluate('gen')
    assert _kalk.FORMAT(v) == '0.33'


def test_as_integer_ratio_method():
    assert evaluate('.25 .as_integer_ratio') == (1, 4)
    assert evaluate('2 .as_integer_ratio') == (2, 1)


def test_strings():
    assert evaluate('"a" "b" +') == 'ab'
    assert evaluate('.upper') == 'AB'


def test_datetime_timedelta():
    from datetime import timedelta

    assert evaluate('"2023-03-22" dt "2023-02-22" dt -') == timedelta(28)
    assert evaluate('28 days +') == timedelta(56)
    assert evaluate('"1402-01-02" jdt dt "2023-03-22" dt ==') is True


def test_jdatetime():
    assert evaluate('"1402-01-02" jdt "2023-03-22" dt jdt ==') is True


def test_now():
    import datetime

    assert isinstance(evaluate('now'), datetime.datetime)


def test_lt():
    assert evaluate('1 2 <') == 1


def test_gmean():
    assert evaluate('[54 24 36] gmean round') == 36.0


def test_substacks():
    evaluate('c 1 2 [3 4] es 5 ] 6')
    assert STACK == [1, 2, [3, 4, 5], 6]
