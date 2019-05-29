# flake8: noqa
"""
Minor compatibility between python 2 and python 3 outside of six

Provided objects:
    - ``Iterable``, ``Callable`: ``collections.x`` or ``collections.abc.x``
"""
import six

if six.PY2:
    from collections import Iterable, Callable
else:
    from collections.abc import Iterable, Callable
