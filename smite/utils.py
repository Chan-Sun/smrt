# -*- coding: utf-8 -*-
#
# Author: Taylor Smith <taylor.smith@alkaline-ml.com>
#
# Utils for SMITE

from __future__ import absolute_import, division, print_function
from numpy.random import RandomState
import sys

__all__ = [
    'get_random_state'
]

if sys.version_info[0] >= 3:
    long = int


def get_random_state(random_state):
    """Get a ``numpy.random.RandomState`` PRNG given a seed or
    an existing ``RandomState``.

    Parameters
    ----------
    random_state : ``RandomState``, int or None
        The seed or PRNG.
    """
    if random_state is None:
        return RandomState()
    elif isinstance(random_state, RandomState):
        return random_state
    elif isinstance(random_state, (int, long)):
        return RandomState(random_state)
    else:
        raise ValueError('Cannot seed RandomState given class=%s' % type(random_state))
