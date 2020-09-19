__version__ = '0.2'


from math import sin, cos, tan, atan, atan2, atanh, asin, asinh, acos, acosh,\
    factorial, pi, e, ceil, comb, floor, fsum, gcd, lcm, perm, prod, trunc, \
    exp, expm1, log, log10, sqrt, dist, hypot, degrees, radians, erf, erfc,\
    gamma, lgamma, tau, copysign, fabs, fmod, isqrt, ldexp, nextafter,\
    remainder, ulp, log1p, log2, pow as fpow, inf, nan
from operator import add, sub, mul, truediv, floordiv, mod, lshift,\
    rshift, and_, xor, invert, or_, neg
from pprint import pprint

from regex import compile as rc


STACK = []
APPEND = STACK.append
CLEAR = STACK.clear
POP = STACK.pop


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


def swap():
    STACK[-2:] = reversed(STACK[-2:])


BINARY_OPERATORS = {
    '%%': percent,
    '%': mod,
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
    '|': or_}
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
    'rad': radians,
    'round': round,
    'sin': sin,
    'sqrt': sqrt,
    'tan': tan,
    'trunc': trunc,
    'ulp': ulp,
    '~': invert}
SPECIAL_OPERATORS = {
    'bin': print_bin,
    'c': CLEAR,
    'chr': print_chr,
    'dist2': dist2,
    'e': loud_eulers_number,
    'fsum': fsum_all,
    'h': display_help,
    'hex': print_hex,
    'inf': load_inf,
    'max': print_max,
    'min': print_min,
    'nan': load_nan,
    'oct': print_oct,
    'pi': load_pi,
    'prod': product,
    's': print_stack,
    'sum': sum_all,
    '<>': swap,
    'tau': load_tau,
}

N = ( # noqa
    r'(?>'
        r'[\d۰-۹][\d۰-۹,]*+(?:\.[\d۰-۹]*+)?+'
        r'|\.[\d۰-۹]++'
    r')(?:[Ee][+-]?+[\d۰-۹]++)?+')
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
        APPEND(op(POP(), last))
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

        token = token.replace(',', '')
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
            print(f'{last_result:,}')


if __name__ == '__main__':
    main()
