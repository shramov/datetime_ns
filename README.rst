Datetime with nanosecond precision
==================================

This module adds nanosecond precision to python timestamp types: time, datetime and timedelta.
It's a standalone fix of python bug BPO-15443_ and hopefully someday will be merged upstream.

Usage
-----

It can be used as a usual module with separate name

.. code-block:: python

    import datetime_ns as datetime

    datetime.timedelta(nanoseconds=123)

Or patched to ``sys.modules`` as ``datetime`` so third-party code will benefit from it

.. code-block:: python

    import datetime_ns
    datetime_ns.datetime_patch()

Compatibility
-------------

This module is as backward (compared to mainline ``datetime``) as possible.

String formatting of timestamps that have only microseconds precision is done
without using extra digits.

.. code-block:: python

    >>> str(datetime_ns.datetime(2020, 1, 2, microsecond=123))
    '2020-01-02 00:00:00.000123'
    >>> str(datetime_ns.datetime(2020, 1, 2, nanosecond=123456))
    '2020-01-02 00:00:00.000123456'

Unpickle is also compatible with system ``datetime`` module.

.. _BPO-15443: https://bugs.python.org/issue15443
