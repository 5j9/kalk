Kalk
====

installation
------------
Requires Python 3.9+.

``pip install kalk``

Usage
-----
After installation run ``kalk`` from your terminal.

Kalk follows Python syntax for numbers. It even support complex numbers:

..

    >>> 1-.1e2J
    (1-10j)

In RPN_ syntax one would first enter the operands and then the operator:

..

    >>> 1
    1
    >>> 2
    2
    >>> +
    3


You may also enter the operands and the operator in one line, just use space to separate them:

    >>> 41 1 +
    42

(tip: the space is not needed when the syntax is not ambiguous.)

As mentioned before, Kalk follows Python's syntax, so ``**`` is the `power operator`_ and ``^`` is `bitwise and`_.

    >>> 3 3 **
    27
    >>> 3 3 ^
    0

Most of the functions defined in Python's math_ modules are supported.

    >>> 6 lgamma
    4.787491742782047

and many more:

    >>> 1 2 3 4 5 sum
    15

A few handy functions:

* ``c`` clears the stack
* ``s`` prints the stack
* ``pi`` adds the pi constant to the stack
* ``e`` adds `Euler's number` to the stack
* ``<>`` swaps the place of the last two values in the stack.
* ``h`` prints a list of all operators. (still needs lots refinements.)



.. _RPN: https://en.wikipedia.org/wiki/Reverse_Polish_notation
.. _power operator: https://docs.python.org/3/reference/expressions.html#the-power-operator
.. _bitwise and: https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
.. _math: https://docs.python.org/3/library/math.html
.. _operator: https://docs.python.org/3/library/operator.html
.. _Euler's number: https://en.wikipedia.org/wiki/E_(mathematical_constant)
