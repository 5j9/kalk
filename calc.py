from math import sin, cos, tan, atan, atan2, atanh, asin, asinh, acos, acosh,\
    factorial, pi, e, ceil, comb, floor, fsum, gcd, lcm, perm, prod, trunc, \
    exp, expm1, log, log10, sqrt, dist, hypot, degrees, radians, erf, erfc,\
    gamma, lgamma, tau, copysign, fabs, fmod, isqrt, ldexp, nextafter,\
    remainder, ulp, log1p, log2, pow as fpow, inf, nan
from operator import add, sub, mul, pow, truediv, floordiv, mod, lshift,\
    rshift, and_, xor, invert, or_
from pprint import pprint

from regex import compile as rc


stack = []
append = stack.append
clear = stack.clear
pop = stack.pop


def sum_all():
    s = sum(stack)
    clear()
    append(s)


def fsum_all():
    s = fsum(stack)
    clear()
    append(s)


def product():
    p = prod(stack)
    clear()
    append(p)


def dist2():
    d = dist((stack[-4], stack[-3]), (stack[-2], stack[-1]))
    del stack[-3:]
    stack[-1] = d


def percent(a, b, /):
    return (b - a) / a * 100


def print_stack():
    for i, n in enumerate(stack):
        print(f'{i}: {n:,}')


def display_help():
    pprint(binary_operators)
    pprint(unary_operators)
    pprint(special_operators)


def loud_eulers_number():
    append(e)


def load_pi():
    append(pi)


def load_tau():
    append(tau)


def load_nan():
    append(nan)


def load_inf():
    append(inf)


def print_bin():
    print(bin(stack[-1]))


def print_min():
    print(min(stack))


def print_chr():
    print(chr(int(stack[-1])))


def print_hex():
    print(hex(stack[-1]))


def print_oct():
    print(oct(stack[-1]))


def print_max():
    print(max(stack))


binary_operators = {
    '%': mod,
    'fmod': fmod,
    'remainder': remainder,
    'copysign': copysign,
    '%%': percent,
    '*': mul,
    '**': pow,
    'fpow': fpow,
    '+': add,
    '-': sub,
    '&': and_,
    '|': or_,
    '^': xor,
    '/': truediv,
    '//': floordiv,
    '<<': lshift,
    '>>': rshift,
    'gcd': gcd,
    'lcm': lcm,
    'P': perm,
    'C': comb,
    'log': log,
    'hypot': hypot,
}
unary_operators = {
    'ulp': ulp,
    '~': invert,
    'abs': abs,
    'fabs': fabs,
    'round': round,
    'erf': erf,
    'erfc': erfc,
    'gamma': gamma,
    'lgamma': lgamma,
    '!': factorial,
    'acos': acos,
    'acosh': acosh,
    'asin': asin,
    'asinh': asinh,
    'atan': atan,
    'atan2': atan2,
    'atanh': atanh,
    'cos': cos,
    'sin': sin,
    'tan': tan,
    'ceil': ceil,
    'floor': floor,
    'trunc': trunc,
    'exp': exp,
    'expm1': expm1,
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'sqrt': sqrt,
    'ldexp': ldexp,
    'isqrt': isqrt,
    'deg': degrees,
    'rad': radians,
    'nextafter': nextafter,
}


special_operators = {
    'bin': print_bin,
    'hex': print_hex,
    'oct': print_oct,
    'min': print_min,
    'max': print_max,
    'chr': print_chr,
    'c': clear,
    'e': loud_eulers_number,
    'h': display_help,
    'pi': load_pi,
    'tau': load_tau,
    'inf': load_inf,
    'nan': load_nan,
    's': print_stack,
    'prod': product,
    'dist2': dist2,
    'fsum': fsum_all,
    'sum': sum_all,
}


fullmatch = rc(  # noqa
    r'\s*+'
    r'(?:('
        r'-?[\d۰-۹][\d۰-۹,.]*+(?:e[\d۰-۹]++)?'
        fr'|\L<operators>'
    r')\s*+)*+', operators=binary_operators.keys()
                           | unary_operators.keys()
                           | special_operators.keys()).fullmatch


def apply(token):
    if (op := binary_operators.get(token)) is not None:
        last = pop()
        append(op(pop(), last))
    elif (op := unary_operators.get(token)) is not None:
        append(op(pop()))
    elif (op := special_operators.get(token)) is not None:
        op()
    else:
        return False


def evaluate(i):
    tokens = fullmatch(i).captures(1)
    # print(tokens)
    for token in tokens:
        try:
            if apply(token) is not False:
                continue
        except IndexError:
            print('not enough arguments')
            continue

        # treat it as number
        token.replace(',', '')
        try:
            token = int(token)
        except ValueError:
            token = float(token)
        append(token)

    try:
        return stack[-1]
    except IndexError:
        return None


def run():
    while True:
        last_result = evaluate(input('>>> '))
        if last_result is not None:
            print(f'{last_result:,}')


if __name__ == '__main__':
    run()
