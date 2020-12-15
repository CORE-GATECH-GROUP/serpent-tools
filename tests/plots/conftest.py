""""Utilities for testing plot capabilities

The primary task is to reset the matplotlib configuration to
the default before the entire suite. At each test, a clean
plot should be rendered

"""

import pytest
from matplotlib import pyplot
from matplotlib import rcdefaults
from matplotlib.testing import setup


@pytest.fixture(autouse=True)
def clean_mpl():
    rcdefaults()
    pyplot.close("all")
    setup()
    yield
    pyplot.close("all")
