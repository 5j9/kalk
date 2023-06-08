Kalk
====

installation
------------
Requires Python 3.9+.

``pip install kalk``

Usage
-----
After installation run ``kalk`` from your terminal.

In RPN_ syntax one would first enter the operands and then the operator:

.. code-block:: python

    >>> 1
    1
    >>> 2
    2
    >>> +
    3


You may also enter the operands and the operator in one line, just use space to
separate them:

.. code-block:: python

    >>> 41 1 +
    42

(tip: the space is not needed when the syntax is not ambiguous.)

Kalk tries to follow Python's syntax. Similar to Python, ``**`` is the `power operator`_ and ``^`` is `bitwise XOR`_:

.. code-block:: python

    >>> 3 3 **
    27
    >>> 3 3 ^
    0

Kalk ignores ``,`` (thousands separator) within numbers.

.. code-block:: python

    >>> 1,234 1 +
    1,235

Most of the functions defined in Python's math_ and statistics_ modules are supported.

.. code-block:: python

    >>> 6 lgamma
    4.787491742782047

and many more.


You can even do ``datetime`` and ``timedelta`` calculations:

.. code-block:: python

    >>> "2023-03-22" dt
    2023-03-22 00:00:00
    >>> 2 days 3 hours +
    2 days, 3:00:00
    >>> -
    2023-03-19 21:00:00

Start a substack (a list) with a ``[`` and end it with a ``]``. Some functions require lists as argument. For example to calculate the distance between two points or sum of some numbers:

.. code-block:: python

    >>> [2 -1] [-2 2] dist
    5.0
    >>> [0 0 0] [1 1 1] dist
    1.7320508075688772
    >>> [1 1 1] sum
    3


Handy operators:

* ``<>`` swaps the place of the last two values in the stack.
* ``c`` clears the stack
* ``cp`` copies the last result to clipboard.
* ``del`` deletes the last ``n + 1`` values from from the stack with ``n`` being the last value in the stack.
* ``e`` adds `Euler's number` to the stack
* ``pi`` adds the pi constant to the stack
* ``pst`` pastes the contents of clipboard and evaluates it.
* ``a`` the last answer
* ``s`` prints the stack
* ``sto`` stores the value before the last in storage using the last stack value as the key.
* ``rcl`` recalls the value in storage using the last stack value as the key.
* ``h`` prints a list of all operators. (still needs lots of refinements.)
* ``?`` prints the docstring of the operator given as a string. For example ``"<>" ?`` will print the help string on swap. Note that not all functions have documentation yet.

.. _RPN: https://en.wikipedia.org/wiki/Reverse_Polish_notation
.. _power operator: https://docs.python.org/3/reference/expressions.html#the-power-operator
.. _bitwise XOR: https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
.. _math: https://docs.python.org/3/library/math.html
.. _statistics: https://docs.python.org/3/library/statistics.html
.. _operator: https://docs.python.org/3/library/operator.html
.. _Euler's number: https://en.wikipedia.org/wiki/E_(mathematical_constant)
