__version__ = '0.13.1.dev0'


from math import dist, e, floor, fsum, inf, log10, nan, pi, prod, tau
from pprint import pprint
from statistics import (
    fmean,
    geometric_mean,
    harmonic_mean,
    mean,
    median,
    median_grouped,
    median_high,
    median_low,
    mode,
    multimode,
    pstdev,
    pvariance,
    stdev,
    variance,
)

from regex import compile as rc

from _kalk.binary_ops import BINARY_OPERATORS
from _kalk.unary_ops import UNARY_OPERATORS

STACK = []
APPEND = STACK.append
CLEAR = STACK.clear
POP = STACK.pop


STORAGE = {}


def dist2():
    d = dist((STACK[-4], STACK[-3]), (STACK[-2], STACK[-1]))
    del STACK[-3:]
    STACK[-1] = d


def print_stack():
    for i, n in enumerate(STACK):
        print(f'{i}: {n:,}')


def display_help():
    pprint(BINARY_OPERATORS)
    pprint(UNARY_OPERATORS)
    pprint(SPECIAL_OPERATORS)


def loud_eulers_number():
    APPEND(e)


def load_pi():
    APPEND(pi)


def load_tau():
    APPEND(tau)


def load_nan():
    APPEND(nan)


def load_inf():
    APPEND(inf)


def print_min():
    print(min(STACK))


def print_max():
    print(max(STACK))


def ans():
    APPEND(STACK[-1])


def swap():
    STACK[-2:] = reversed(STACK[-2:])


def paste_from_clipboard():
    from pyperclip import paste
    evaluate(paste())


def copy_to_clipboard():
    from pyperclip import copy
    copy(f'{STACK[-1]}')


def delete():
    del STACK[-STACK[-1] - 1:]


def store():
    k = POP()
    STORAGE[k] = POP()


def recall():
    APPEND(STORAGE[POP()])


PRECISION = 5


def precision():
    global PRECISION
    PRECISION = POP()
    try:
        return STACK[-1]
    except IndexError:
        return None


FORMAT = '{:,}'.format


def set_normal_format():
    global FORMAT
    FORMAT = '{:,}'.format


SI = 0


def toggle_si_format():
    global SI
    SI = not SI


def set_eng_format():
    global FORMAT

    # from https://stackoverflow.com/a/19270863/2705757 with some modifications
    def eng_string(x):
        """
        Returns float/int value <x> formatted in a simplified engineering format -
        using an exponent that is a multiple of 3.

        format: printf-style string used to format the value before the exponent.

        si: if true, use SI suffix for exponent, e.g. k instead of e3, n instead of
        e-9 etc.

        E.g. with format='%.2f':
            1.23e-08 => 12.30e-9
                 123 => 123.00
              1230.0 => 1.23e3
          -1230000.0 => -1.23e6

        and with si=True:
              1230.0 => 1.23k
          -1230000.0 => -1.23M
        """
        if x < 0:
            x = -x
            sign = '-'
        elif x > 0:
            sign = ''
        else:
            return '0'

        exp = int(floor(log10(x)))
        exp3 = exp - (exp % 3)
        x3 = x / (10 ** exp3)

        if SI is True and -24 <= exp3 <= 24 and exp3 != 0:
            exp3_text = 'yzafpnum kMGTPEZY'[(exp3 + 24) // 3]
        elif exp3 == 0:
            exp3_text = ''
        else:
            exp3_text = f'e{exp3}'

        return f'{sign}{x3:.{max(PRECISION, 3)}g}{exp3_text}'

    FORMAT = eng_string


def set_sci_format():
    global FORMAT

    def sci_string(n):
        return f'{n:.{PRECISION}e}'

    FORMAT = sci_string


def set_general_format():
    global FORMAT

    def sci_string(n):
        return f'{n:.{PRECISION}g}'

    FORMAT = sci_string


def call_method(identifier: str):
    APPEND(getattr(POP(), identifier)())


def now():
    import datetime
    APPEND(datetime.datetime.now())


def _whole_stack(func):
    def f():
        m = func(STACK)
        CLEAR()
        APPEND(m)
    f.__name__ = func.__name__
    f.__doc__ = func.__doc__
    return f


SPECIAL_OPERATORS = {
    '<>': swap,
    'SI': toggle_si_format,
    'a': ans,
    'c': CLEAR,
    'cp': copy_to_clipboard,
    'del': delete,
    'dist2': dist2,
    'e': loud_eulers_number,
    'eng': set_eng_format,
    'fmean': _whole_stack(fmean),
    'fsum': _whole_stack(fsum),
    'gen': set_general_format,
    'gmean': _whole_stack(geometric_mean),
    'h': display_help,
    'hmean': _whole_stack(harmonic_mean),
    'inf': load_inf,
    'max': print_max,
    'mean': _whole_stack(mean),
    'med': _whole_stack(median),
    'medg': _whole_stack(median_grouped),
    'medh': _whole_stack(median_high),
    'medl': _whole_stack(median_low),
    'min': print_min,
    'mode': _whole_stack(mode),
    'multimode': _whole_stack(multimode),
    'nan': load_nan,
    'now': now,
    'nrm': set_normal_format,
    'pi': load_pi,
    'prec': precision,
    'prod': _whole_stack(prod),
    'pst': paste_from_clipboard,
    'pstdev': _whole_stack(pstdev),
    'pvar': _whole_stack(pvariance),
    'rcl': recall,
    's': print_stack,
    'sci': set_sci_format,
    'stdev': _whole_stack(stdev),
    'sto': store,
    'sum': _whole_stack(sum),
    'tau': load_tau,
    'var': _whole_stack(variance),
}

N = ( # noqa
    r'(?>'
        r'[\d۰-۹][\d۰-۹,_]*+(?:\.[\d۰-۹_]*+)?+'
        r'|\.[\d۰-۹_]++'
    r')(?:[Ee][+-]?+[\d۰-۹_]++)?+')
fullmatch = rc(  # noqa
    r'\s*+'
    r'(?:'
        r'('  # each token is either a number or an operator
            rf'[+-]?+{N}(?:[Jj]|[-+]{N}[Jj])?+'  # complex part
            r'|"[^"]*"'
            r'|\L<operators>'
            r'|\.[^\d\W]\w*'
        r')\s*+'
    r')*+',
    operators=(
        BINARY_OPERATORS.keys()
        | UNARY_OPERATORS.keys()
        | SPECIAL_OPERATORS.keys())).fullmatch


def operate(token):
    if (op := BINARY_OPERATORS.get(token)) is not None:
        last = POP()
        try:
            APPEND(op(POP(), last))
        except IndexError:
            APPEND(last)
            raise
    elif (op := UNARY_OPERATORS.get(token)) is not None:
        APPEND(op(POP()))
    elif (op := SPECIAL_OPERATORS.get(token)) is not None:
        op()
    elif token[0] == '.' and (identifier := token[1:]).isidentifier():
        call_method(identifier)
    else:
        return False


def evaluate(i):
    m = fullmatch(i)
    if m is None:
        print('SyntaxError')
        return None
    for token in m.captures(1):
        try:
            if operate(token) is not False:
                continue  # the token was an operator
        except IndexError:
            print('Error: not enough arguments')
            continue
        except Exception as e:
            print(type(e).__name__)
            return

        if token[0] == '"':
            APPEND(eval(token))
            continue

        token = token.replace(',', '').replace('_', '')
        try:
            try:
                result = int(token)
            except ValueError:
                result = float(token)
        except ValueError:
            result = complex(token)

        APPEND(result)

    try:
        return STACK[-1]
    except IndexError:
        return None


def main():
    print(f'Kalk v{__version__}')
    while True:
        last_result = evaluate(input('>>> '))
        if isinstance(last_result, (int, float)):
            print(FORMAT(last_result))
        elif last_result is not None:
            print(last_result)


if __name__ == '__main__':
    main()
