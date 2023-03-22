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
from operator import invert, not_


def dt(value):
    """Convert value to datetime using datetime.datetime.fromisoformat."""
    if isinstance(value, str):
        import datetime
        return datetime.datetime.fromisoformat(value)

    import jdatetime
    if isinstance(value, jdatetime.datetime):
        return value.togregorian()

    raise ValueError('unknown format for jdt')


def td(days):
    """Convert days to datetime.timedelta."""
    import datetime
    return datetime.timedelta(days)


def jdt(value):
    """Convert value to jdatetime.datetime."""
    import jdatetime
    if isinstance(value, str):
        # todo: use fromisostring when the following issue is resolved
        # https://github.com/slashmili/python-jalali/issues/134
        return jdatetime.datetime.strptime(value, '%Y-%m-%d')

    import datetime
    if isinstance(value, datetime.datetime):
        return jdatetime.datetime.fromgregorian(datetime=value)

    raise ValueError('unknown format for jdt')


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
    'bool': bool,
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
    'jdt': jdt,
    'ldexp': ldexp,
    'lgamma': lgamma,
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'nextafter': nextafter,
    'not': not_,
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
