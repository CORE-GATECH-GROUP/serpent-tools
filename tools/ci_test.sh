#! /bin/bash

# Script to be called by Travis or CI client
# to test our project. Works for either
# cron builds or pull requests

# Exit immediately if a simple command fails
set -e
# Propagate error codes through pipes
set -o pipefail

#
# Check if we are on travis
# If so, we also can run our tests with coverage
# If not, run with vanilla python
#

if [ -z "TRAVIS" ]; then
    PY_RUNNER="coverage run"
else
    PY_RUNNER="python"
fi
#
# Main test suite
#

echo "Running all unit tests"
echo "----------------------------------------"

$PY_RUNNER setup.py test

echo "Testing jupyter notebooks"
echo "----------------------------------------"

source tools/testNotebooks.sh

#
# Check for lint
#

echo "Checking for lint"
echo "----------------------------------------"

if [ $TRAVIS_PULL_REQUEST != "false" ]; then
    # not a pull request
    # and we don't build pushes so it is either a tag
    # or a cron build
    # check the whole project for lint
    flake8
else
    # pull request
    # check lint of proposed code to be introduced
    git diff --unified=0 $TRAVIS_BRANCH | flake8 --diff

fi
