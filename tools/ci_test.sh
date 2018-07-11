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
    if [ $TRAVIS_PULL_REQUEST != "false"]; then
        # Run lint on the whole project later
        FLAKE_DIFF=0
    else
        TARGET=$TRAVIS_BRANCH
    fi
else
    if [ -z $PY_RUNNER ]; then
        PY_RUNNER="python"
    fi
    FLAKE_DIFF=1
fi

echo "Python runner" $PY_RUNNER

#
# Main test suite
#

echo "----------------------------------------"
echo "Running all unit tests"
echo "----------------------------------------"

$PY_RUNNER setup.py test

echo "----------------------------------------"
echo "Testing jupyter notebooks"
echo "----------------------------------------"

source tools/testNotebooks.sh

#
# Check for lint
#

echo "----------------------------------------"
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

echo "No lint found"
