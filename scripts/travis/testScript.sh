#! /bin/bash

# Script to be called by Travis or CI client
# to test our project. Works for either
# cron builds or pull requests

# Debugging
if [[ $DEBUG ]]; then
    echo ~~~~~DEBUG MODE~~~~~
    # stacktrace
    set -x
else
    # Exit immediately if a simple command fails
    set -e
    # Propagate error codes through pipes
    set -o pipefail
fi
#
# Check if we are on travis
# If so, we also can run our tests with coverage
# If not, run with vanilla python
#

if [ $TRAVIS ]; then
    PY_RUNNER="coverage run -a"
    if [ $TRAVIS_PULL_REQUEST != "false" ]; then
        # Run lint on the whole project later
        FLAKE_DIFF=0
    else
        TARGET=$TRAVIS_BRANCH
    fi
else
    if [[ -z $PY_RUNNER ]]; then
        PY_RUNNER="python"
    fi
fi

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

if [[ $DEBUG ]]; then
    set +x
fi
