from math import (
    comb,
    copysign,
    fmod,
    gcd,
    hypot,
    lcm,
    log,
    perm,
    pow as fpow,
    remainder,
)
from operator import (
    add,
    and_,
    floordiv,
    lshift,
    mod,
    mul,
    neg,
    or_,
    rshift,
    sub,
    truediv,
    xor,
)


def percent(a, b, /):
    return (b - a) / a * 100


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

