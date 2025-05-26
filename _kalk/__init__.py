__version__ = '0.18.0'
import math
from math import floor, log10
from pprint import pprint
from statistics import correlation, covariance, linear_regression

try:
    # required for activating hist navigation on windows
    import readline  # noqa: F401
except ImportError:
    pass

from regex import compile as rc

from _kalk.binary_ops import BINARY_OPERATORS
from _kalk.unary_ops import UNARY_OPERATORS

stack = []
STACKS = [stack]


STORAGE = {}


def two_arg_factory(func):
    def f():
        d = func(stack[-1], stack[-2])
        del stack[-1]
        stack[-1] = d

    f.__doc__ = func.__doc__
    f.__name__ = func.__name__
    return f


def print_stack():
    for i, n in enumerate(stack):
        print(f'{i}: {n}')


def display_help():
    pprint(BINARY_OPERATORS)
    pprint(UNARY_OPERATORS)
    pprint(SPECIAL_OPERATORS)


def load_constant_factory(name):
    val = getattr(math, name)

    def load_constant():
        stack.append(val)

    load_constant.__doc__ = f"""Load {name} = {val} into the stack."""
    return load_constant


def ans():
    stack.append(stack[-1])


def swap():
    """Swap the place of last two results on the stack"""
    stack[-2:] = reversed(stack[-2:])


def paste_from_clipboard():
    from pyperclip import paste

    evaluate(paste())


def copy_to_clipboard():
    from pyperclip import copy

    copy(f'{stack[-1]}')


def delete():
    del stack[-stack[-1] - 1 :]


def store():
    k = stack.pop()
    STORAGE[k] = stack.pop()


def recall():
    stack.append(STORAGE[stack.pop()])


_precision = 5


def precision():
    global _precision
    _precision = stack.pop()
    try:
        return stack[-1]
    except IndexError:
        return None


fmt = '{:,}'.format


def set_normal_format():
    global fmt
    fmt = '{:,}'.format


si = 0


def toggle_si_format():
    global si
    si = not si


def set_eng_format():
    global fmt

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

        exp = floor(log10(x))
        exp3 = exp - (exp % 3)
        x3 = x / (10**exp3)

        if si is True and -24 <= exp3 <= 24 and exp3 != 0:
            exp3_text = 'yzafpnum kMGTPEZY'[(exp3 + 24) // 3]
        elif exp3 == 0:
            exp3_text = ''
        else:
            exp3_text = f'e{exp3}'

        return f'{sign}{x3:.{max(_precision, 3)}g}{exp3_text}'

    fmt = eng_string


def set_sci_format():
    global fmt

    def sci_string(n):
        return f'{n:.{_precision}e}'

    fmt = sci_string


def set_general_format():
    global fmt

    def sci_string(n):
        return f'{n:.{_precision}g}'

    fmt = sci_string


def call_method(identifier: str):
    stack.append(getattr(stack.pop(), identifier)())


def now():
    import datetime

    stack.append(datetime.datetime.now())


def utcnow():
    import datetime

    stack.append(datetime.datetime.utcnow())


def today():
    import datetime

    stack.append(datetime.date.today())


def str_help():
    string = stack.pop()
    op = (
        UNARY_OPERATORS.get(string)
        or SPECIAL_OPERATORS.get(string)
        or UNARY_OPERATORS.get(string)
    )
    help(op)


def clear_stack():
    del stack[:]


def start_substack():
    global stack
    new_stack = []
    stack.append(new_stack)
    stack = new_stack
    STACKS.append(new_stack)


def end_substack():
    global stack
    STACKS.pop()
    stack = STACKS[-1]


def enter_substack():
    global stack
    stack = stack[-1]
    STACKS.append(stack)


def exit_():
    raise SystemExit


SPECIAL_OPERATORS = {
    '<>': swap,
    '?': str_help,
    'SI': toggle_si_format,
    '[': start_substack,
    ']': end_substack,
    'a': ans,
    'c': clear_stack,
    'corr': two_arg_factory(correlation),
    'covar': two_arg_factory(covariance),
    'cp': copy_to_clipboard,
    'del': delete,
    'dist': two_arg_factory(math.dist),
    'eng': set_eng_format,
    'es': enter_substack,
    'exit': exit_,
    'gen': set_general_format,
    'h': display_help,
    'linreg': two_arg_factory(linear_regression),
    'now': now,
    'nrm': set_normal_format,
    'prec': precision,
    'pst': paste_from_clipboard,
    'rcl': recall,
    's': print_stack,
    'sci': set_sci_format,
    'sto': store,
    'today': today,
    'utcnow': utcnow,
}

for const in 'tau', 'pi', 'e', 'nan', 'inf':
    SPECIAL_OPERATORS[const] = load_constant_factory(const)


N = (
    r'(?>'
    r'[\d][\d,_]*+(?:\.[\d_]*+)?+'
    r'|\.[\d_]++'
    r')(?:[Ee][+-]?+[\d_]++)?+'
)
fullmatch = rc(
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
        | SPECIAL_OPERATORS.keys()
    ),
).fullmatch


def operate(token):
    if (op := BINARY_OPERATORS.get(token)) is not None:
        last = stack.pop()
        try:
            stack.append(op(stack.pop(), last))
        except IndexError:
            stack.append(last)
            raise
    elif (op := UNARY_OPERATORS.get(token)) is not None:
        stack.append(op(stack.pop()))
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
            stack.append(eval(token))
            continue

        token = token.replace(',', '').replace('_', '')
        try:
            try:
                result = int(token)
            except ValueError:
                result = float(token)
        except ValueError:
            result = complex(token)

        stack.append(result)

    try:
        return stack[-1]
    except IndexError:
        return None


def main():
    print(f'Kalk v{__version__}')

    while True:
        try:
            last_result = evaluate(input('>>> '))
        except KeyboardInterrupt:
            print()
            continue

        if isinstance(last_result, (int, float)):
            print(fmt(last_result))
        elif last_result is not None:
            print(last_result)


if __name__ == '__main__':
    main()
