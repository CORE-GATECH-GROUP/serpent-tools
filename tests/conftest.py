# Configure the test suite

from tests.plots import config as plotConfig


def pytest_addoption(parser):
    # Add --update command line option
    # https://docs.pytest.org/en/stable/example/simple.html
    parser.addoption("--update", action="store_true", help="Update test data like plots")
    parser.addoption(
        "--plot-tolerance",
        type=int,
        default=10,
        help="Tolerance when comparing generated plots",
    )


# https://docs.pytest.org/en/stable/reference.html#pytest.hookspec.pytest_configure
def pytest_configure(config):
    # Configure test options based on command line
    # Useful for updating plots, rather than comparing
    # against baseline values
    if config.getoption("update") is not None:
        plotConfig["update"] = config.getoption("update")
    if config.getoption("plot_tolerance") is not None:
        plotConfig["plot_tolerance"] = config.getoption("plot_tolerance")
