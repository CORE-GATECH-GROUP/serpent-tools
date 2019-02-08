#!/bin/bash
# Install script that depends on $INSTALL variable
# Options:
# setup: install with setup.py
# sdist: create a source distribution and install from that
# bdist_wheel: create a wheel and install from that

if [[ -z $ST_INSTALL ]]; then exit; fi

set -ev
set -o pipefail

ST_VERSION=$(python setup.py version | grep Version | cut -d" " -f 2)
echo $ST_VERSION

case $ST_INSTALL in
    'setup')
        python setup.py install
        ;;
    'sdist')
        python setup.py sdist
        pip install dist/serpentTools-${ST_VERSION}.tar.gz
        ;;
    'bdist_wheel')
        python setup.py bdist_wheel
        easy_install dist/serpentTools-${ST_VERSION}*whl
        ;;
    'bdist_egg')
        python setup.py bdist_egg
        easy_install dist/serpentTools-${ST_VERSION}*egg
        ;;
    *)
        echo No install option
        exit 1
esac
                
