#!/bin/bash
# Install script that depends on $INSTALL variable
# Options:
# setup: install with setup.py
# sdist: create a source distribution and install from that
# bdist_wheel: create a wheel and install from that

set -ev
set -o pipefail

# Run only for CI builds
if [[ $CI != true ]]; then
    echo Install script only meant to be run for CI testing
    exit 1
fi

if [[ -z $ST_INSTALL ]]; then exit 1; fi

case $ST_INSTALL in
    'setup')
        python setup.py install
        ;;
    'sdist')
        python setup.py sdist
        pip install dist/serpentTools-*.tar.gz
        ;;
    *)
        echo No install option $ST_INSTALL
        exit 1
esac
