#!/bin/bash

# Script that looks for lint in the project

# If FLAKE_DIFF==0, then look for lint
# across the whole project (just flake8)
# If FLAKE_DIFF==1, then look at the
# lint in the diff between this branch
# and TARGET.
# If TARGET is not set, then use develop

# If FLAKE_DIFF is not set, then attempt to
# infer the best route. If the current branch
# is master or develop, then diff the whole
# project. Otherwise, assume this is a feature branch
# and lint against the difference between
# develop and this branch.

# Exit in any simple command fails
set -e

LINTER="flake8"

# get config file
if [ -f "setup.cfg" ]; then
    LINT_OPTS="--config=setup.cfg"
else
    LINT_OPTS=""
fi

echo "----------------------------------------"
echo "Checking for lint with" $LINTER
echo "Additional arguments:" $LINT_OPTS
echo "----------------------------------------"

if [ ! -z $FLAKE_DIFF ]; then
    # lint the whole project from right here
    $LINTER $LINT_OPTS
    echo "No lint found"
    exit
fi

# Determine against what branch to diff

CURRENT=$(git rev-parse --abbrev-ref HEAD) 

if [ $TARGET ]; then
    if [ $CURRENT=="develop" ] || [ $CURRENT=="master" ]; then
        # Assume on one of our "production" branches
        # run linter on the whole thing
        $LINTER $LINT_OPTS
        echo "No lint found"
        exit
    fi
else
    # Not on production/release branch
    # Determine the "upstream" or
    # reference branch against which to diff and then
    # apply linter
    TARGET="develop"
fi

# Check lint introduced by the diff of this branch vs the target branch
echo Linting ${CURRENT} vs. ${TARGET}
git diff --unified=0 $TARGET | $LINTER --diff $LINT_OPTS
echo "No lint found"

