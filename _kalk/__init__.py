__version__ = '0.10.0'


from math import sin, cos, tan, atan, atan2, atanh, asin, asinh, acos, acosh,\
    factorial, pi, e, ceil, comb, floor, fsum, gcd, lcm, perm, prod, trunc, \
    exp, expm1, log, log10, sqrt, dist, hypot, degrees, radians, erf, erfc,\
    gamma, lgamma, tau, copysign, fabs, fmod, isqrt, ldexp, nextafter,\
    remainder, ulp, log1p, log2, pow as fpow, inf, nan
from operator import add, sub, mul, truediv, floordiv, mod, lshift,\
    rshift, and_, xor, invert, or_, neg
from pprint import pprint

from regex import compile as rc
from pyperclip import copy, paste


STACK = []
APPEND = STACK.append
CLEAR = STACK.clear
POP = STACK.pop


STORAGE = {}


def sum_all():
    s = sum(STACK)
    CLEAR()
    APPEND(s)


def fsum_all():
    s = fsum(STACK)
    CLEAR()
    APPEND(s)


def product():
    p = prod(STACK)
    CLEAR()
    APPEND(p)


def dist2():
    d = dist((STACK[-4], STACK[-3]), (STACK[-2], STACK[-1]))
    del STACK[-3:]
    STACK[-1] = d


def percent(a, b, /):
    return (b - a) / a * 100


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


def print_bin():
    print(bin(STACK[-1]))


def print_min():
    print(min(STACK))


def print_chr():
    print(chr(int(STACK[-1])))


def print_hex():
    print(hex(STACK[-1]))


def print_oct():
    print(oct(STACK[-1]))


def print_max():
    print(max(STACK))


def ans():
    APPEND(STACK[-1])


def swap():
    STACK[-2:] = reversed(STACK[-2:])


def paste_from_clipboard():
    evaluate(paste())


def copy_to_clipboard():
    copy(f'{STACK[-1]}')


def delete():
    del STACK[-STACK[-1] - 1:]


def store():
    k = POP()
    STORAGE[k] = POP()


def recall():
    APPEND(STORAGE[POP()])


PRECISION = 5


def precision(p):
    global PRECISION
    PRECISION = p
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


BINARY_OPERATORS = {
    '%%': percent,
    '٪٪': percent,
    '%': mod,
    '٪': mod,
    '&': and_,
    '*': mul,
    '**': pow,
    '+': add,
    '-': sub,
    'n': neg,
    '/': truediv,
    '//': floordiv,
    '<<': lshift,
    '>>': rshift,
    'C': comb,
    'P': perm,
    '^': xor,
    'cs': copysign,
    'fmod': fmod,
    'fpow': fpow,
    'gcd': gcd,
    'hypot': hypot,
    'lcm': lcm,
    'log': log,
    'rem': remainder,
    '|': or_,
}

UNARY_OPERATORS = {
    '!': factorial,
    'abs': abs,
    'acos': acos,
    'acosh': acosh,
    'asin': asin,
    'asinh': asinh,
    'atan': atan,
    'atan2': atan2,
    'atanh': atanh,
    'ceil': ceil,
    'cos': cos,
    'deg': degrees,
    'erf': erf,
    'erfc': erfc,
    'exp': exp,
    'expm1': expm1,
    'fabs': fabs,
    'floor': floor,
    'gamma': gamma,
    'isqrt': isqrt,
    'ldexp': ldexp,
    'lgamma': lgamma,
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'nextafter': nextafter,
    'prec': precision,
    'rad': radians,
    'round': round,
    'sin': sin,
    'sqrt': sqrt,
    'tan': tan,
    'trunc': trunc,
    'ulp': ulp,
    '~': invert,
}

SPECIAL_OPERATORS = {
    '<>': swap,
    'bin': print_bin,
    'c': CLEAR,
    'chr': print_chr,
    'cp': copy_to_clipboard,
    'del': delete,
    'dist2': dist2,
    'e': loud_eulers_number,
    'eng': set_eng_format,
    'fsum': fsum_all,
    'gen': set_general_format,
    'h': display_help,
    'hex': print_hex,
    'inf': load_inf,
    'max': print_max,
    'min': print_min,
    'nan': load_nan,
    'nrm': set_normal_format,
    'oct': print_oct,
    'pi': load_pi,
    'prod': product,
    'pst': paste_from_clipboard,
    'rcl': recall,
    'a': ans,
    's': print_stack,
    'sci': set_sci_format,
    'SI': toggle_si_format,
    'sto': store,
    'sum': sum_all,
    'tau': load_tau,
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
            r'|\L<operators>'
        r')\s*+'
    r')*+',
    operators=(
        BINARY_OPERATORS.keys()
        | UNARY_OPERATORS.keys()
        | SPECIAL_OPERATORS.keys())).fullmatch


def apply(token):
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
    else:
        return False


def evaluate(i):
    m = fullmatch(i)
    if m is None:
        print('SyntaxError')
        return None
    for token in m.captures(1):
        try:
            if apply(token) is not False:
                continue
        except IndexError:
            print('Error: not enough arguments')
            continue
        except Exception as e:
            print(type(e).__name__)
            return

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
    while True:
        last_result = evaluate(input('>>> '))
        if last_result is not None:
            print(FORMAT(last_result))


if __name__ == '__main__':
    main()
