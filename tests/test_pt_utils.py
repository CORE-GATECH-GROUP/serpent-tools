"""Tests for using utility features"""

import pytest
from numpy import random

import serpentTools.utils as sutils


@pytest.mark.parametrize("N", [1, 5, 10])
def test_str2vec(N):
    """Compare the string to vector conversion on a random vector"""
    r = random.random(N)
    s = " ".join(map(str, r))
    v = sutils.str2vec(s)
    assert v == pytest.approx(r, abs=0, rel=0)
