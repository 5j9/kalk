from math import sin, cos, tan, atan, atan2, atanh, asin, asinh, acos, acosh,\
    factorial, pi, e, ceil, comb, floor, fsum, gcd, lcm, perm, prod, trunc, \
    exp, expm1, log, log10, sqrt, dist, hypot, degrees, radians, erf, erfc,\
    gamma, lgamma, tau, copysign, fabs, fmod, isqrt, ldexp, nextafter,\
    remainder, ulp, log1p, log2, pow as fpow, inf, nan
from operator import add, sub, mul, truediv, floordiv, mod, lshift,\
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
    '%%': percent,
    '%': mod,
    '&': and_,
    '*': mul,
    '**': pow,
    '+': add,
    '-': sub,
    '/': truediv,
    '//': floordiv,
    '<<': lshift,
    '>>': rshift,
    'C': comb,
    'P': perm,
    '^': xor,
    'copysign': copysign,
    'fmod': fmod,
    'fpow': fpow,
    'gcd': gcd,
    'hypot': hypot,
    'lcm': lcm,
    'log': log,
    'remainder': remainder,
    '|': or_,
}
unary_operators = {
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
    '~': invert,
}


special_operators = {
    'bin': print_bin,
    'c': clear,
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
    'tau': load_tau,
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
