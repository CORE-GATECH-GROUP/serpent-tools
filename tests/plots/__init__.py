from functools import wraps
import pathlib
from os import remove

import pytest
from matplotlib import pyplot
from matplotlib.testing.compare import compare_images

# Configuration options for plot tests
config = {
    "update": False,
    "plot_tolerance": 10,
}

FIG_RESULT_BASE = pathlib.Path(__file__).parent / "result_images"
if not FIG_RESULT_BASE.exists():
    FIG_RESULT_BASE.mkdir(exist_ok=False, parents=True)
elif not FIG_RESULT_BASE.is_dir():
    raise NotADirectoryError(FIG_RESULT_BASE)


def compare_or_update_plot(f):
    """Build a decorator that wraps a plot test

    The test function must produce a single figure that will be
    compared to the expected figure during the test. If the --update
    command line option is given, then the newly generated figure
    will be save in place of the expected figure
    """
    update = config["update"]
    baseline = (FIG_RESULT_BASE / f.__name__).with_suffix(".png")
    testFile = baseline.with_name("{}-test.png".format(f.__name__))
    # TODO Don't convert to str - needed because MPL for python 3.5
    # doesn't support saving as pathlib.Path instances
    baseline = str(baseline)
    testFile = str(testFile)

    @wraps(f)
    def wrapped(*args, **kwargs):
        f(*args, **kwargs)
        fig = pyplot.gcf()
        if update:
            fig.savefig(baseline)
            return
        fig.savefig(testFile)
        res = compare_images(baseline, testFile, tol=config["plot_tolerance"])
        assert res is None, res
        remove(testFile)

    # If a test is tagged with this decorator, mark is with the
    # plot mark automatically
    pytest.mark.plot(wrapped)

    return wrapped
