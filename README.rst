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

Kalk follows Python syntax for numbers. It even support complex numbers.

.. code-block:: python

    >>> 1-.1e2J
    (1-10j)

Similar to Python, ``**`` is the `power operator`_ and ``^`` is `bitwise XOR`_:

.. code-block:: python

    >>> 3 3 **
    27
    >>> 3 3 ^
    0

Kalk ignores ``,`` (thousands separator) within numbers.

.. code-block:: python

    >>> 1,234 1 +
    1,235

Most of the functions defined in Python's math_ module are supported.

.. code-block:: python

    >>> 6 lgamma
    4.787491742782047

and many more:

.. code-block:: python

    >>> 1 2 3 4 5 sum
    15

Handy operators:

* ``<>`` swaps the place of the last two values in the stack.
* ``c`` clears the stack
* ``cp`` copies the last result to clipboard.
* ``del`` deletes the last ``n + 1`` values from from the stack with ``n`` being the last value in the stack.
* ``e`` adds `Euler's number` to the stack
* ``h`` prints a list of all operators. (still needs lots of refinements.)
* ``pi`` adds the pi constant to the stack
* ``pst`` pastes the contents of clipboard and evaluates it.
* ``a`` the last answer
* ``s`` prints the stack
* ``sto`` stores the value before the last in storage using the last stack value as the key.
* ``rcl`` recalls the value in storage using the last stack value as the key.

.. _RPN: https://en.wikipedia.org/wiki/Reverse_Polish_notation
.. _power operator: https://docs.python.org/3/reference/expressions.html#the-power-operator
.. _bitwise XOR: https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
.. _math: https://docs.python.org/3/library/math.html
.. _operator: https://docs.python.org/3/library/operator.html
.. _Euler's number: https://en.wikipedia.org/wiki/E_(mathematical_constant)
