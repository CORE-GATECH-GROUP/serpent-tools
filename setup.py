from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "serpentTools = serpentTools.__main__:main",
        ],
    },
)
