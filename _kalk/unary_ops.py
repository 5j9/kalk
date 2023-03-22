from math import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atan2,
    atanh,
    ceil,
    cos,
    degrees,
    erf,
    erfc,
    exp,
    expm1,
    fabs,
    factorial,
    floor,
    gamma,
    isqrt,
    ldexp,
    lgamma,
    log1p,
    log2,
    log10,
    nextafter,
    radians,
    sin,
    sqrt,
    tan,
    trunc,
    ulp,
)
from operator import invert


def dt(string):
    """datetime.datetime.fromisoformat"""
    from datetime import datetime
    return datetime.fromisoformat(string)


def td(days):
    """datetime.timedelta"""
    from datetime import timedelta
    return timedelta(days)


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
    'bin': bin,
    'ceil': ceil,
    'chr': chr,
    'cos': cos,
    'deg': degrees,
    'dt': dt,
    'erf': erf,
    'erfc': erfc,
    'exp': exp,
    'expm1': expm1,
    'fabs': fabs,
    'floor': floor,
    'gamma': gamma,
    'hex': hex,
    'isqrt': isqrt,
    'ldexp': ldexp,
    'lgamma': lgamma,
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'nextafter': nextafter,
    'oct': oct,
    'rad': radians,
    'round': round,
    'sin': sin,
    'sqrt': sqrt,
    'tan': tan,
    'td': td,
    'trunc': trunc,
    'ulp': ulp,
    '~': invert,
}
