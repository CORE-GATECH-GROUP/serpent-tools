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

source scripts/travis/testNotebooks.sh

#
# Check for lint
#
source scripts/travis/checkLint.sh
