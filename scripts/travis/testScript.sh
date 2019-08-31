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
#

if [ $TRAVIS ]; then
    if [ $TRAVIS_PULL_REQUEST != "false" ]; then
        # Run lint on the whole project later
        FLAKE_DIFF=0
    else
        TARGET=$TRAVIS_BRANCH
    fi
fi

#
# Main test suite
#

echo "----------------------------------------"
echo "Running all unit tests"
echo "----------------------------------------"

pytest -v

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
