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
    fsum,
    gamma,
    isqrt,
    ldexp,
    lgamma,
    log1p,
    log2,
    log10,
    nextafter,
    prod,
    radians,
    sin,
    sqrt,
    tan,
    trunc,
    ulp,
)
from operator import invert, not_
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


def dt(value):
    """Convert value to datetime using datetime.datetime.fromisoformat."""
    if isinstance(value, str | int):
        import datetime

        return datetime.datetime.fromisoformat(f'{value}')

    import jdatetime

    if isinstance(value, jdatetime.datetime):
        return value.togregorian()

    raise ValueError('unknown format for jdt')


def weeks(val):
    import datetime

    return datetime.timedelta(weeks=val)


def days(val):
    import datetime

    return datetime.timedelta(val)


def hours(val):
    import datetime

    return datetime.timedelta(hours=val)


def minutes(val):
    import datetime

    return datetime.timedelta(minutes=val)


def seconds(val):
    import datetime

    return datetime.timedelta(seconds=val)


def jdt(value):
    """Convert value to jdatetime.datetime."""
    import jdatetime

    if isinstance(value, (str, int)):
        return jdatetime.datetime.fromisoformat(f'{value}')

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
    'days': days,
    'deg': degrees,
    'dt': dt,
    'erf': erf,
    'erfc': erfc,
    'exp': exp,
    'expm1': expm1,
    'fabs': fabs,
    'floor': floor,
    'fmean': fmean,
    'fsum': fsum,
    'gamma': gamma,
    'gmean': geometric_mean,
    'hex': hex,
    'hmean': harmonic_mean,
    'hours': hours,
    'isqrt': isqrt,
    'jdt': jdt,
    'ldexp': ldexp,
    'lgamma': lgamma,
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'max': max,
    'mean': mean,
    'med': median,
    'medg': median_grouped,
    'medh': median_high,
    'medl': median_low,
    'min': min,
    'minutes': minutes,
    'mode': mode,
    'multimode': multimode,
    'nextafter': nextafter,
    'not': not_,
    'oct': oct,
    'prod': prod,
    'pstdev': pstdev,
    'pvar': pvariance,
    'rad': radians,
    'round': round,
    'seconds': seconds,
    'sin': sin,
    'sqrt': sqrt,
    'stdev': stdev,
    'sum': sum,
    'tan': tan,
    'trunc': trunc,
    'ulp': ulp,
    'var': variance,
    'weeks': weeks,
    '~': invert,
}
