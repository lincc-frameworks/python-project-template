#!/usr/bin/env bash

# Bash Unofficial strict mode (http://redsymbol.net/articles/unofficial-bash-strict-mode/) 
# and (https://disconnected.systems/blog/another-bash-strict-mode/)
set -o nounset # Any uninitialized variable is an error
set -o errexit # Exit the script on the failure of any command to execute without error
set -o pipefail # Fail command pipelines on the failure of any individual step
IFS=$'\n\t' #set internal field separator to avoid iteration errors
# Trap all exits and output something helpful
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

# This script should be run by new developers to install this package in
# editable mode and configure their local environment

echo "Checking virtual environment"
if [ "${VIRTUAL_ENV:-missing}" = "missing" ] && [ "${CONDA_PREFIX:-missing}" = "missing" ]; then
    echo 'No virtual environment detected: none of $VIRTUAL_ENV or $CONDA_PREFIX is set.'
    echo
    echo "=== This script is going to install the project in the system python environment ==="
    echo "Proceed? [y/N]"
    read -r RESPONCE
    if [ "${RESPONCE}" != "y" ]; then
        echo "See https://lincc-ppt.readthedocs.io/ for details."
        echo "Exiting."
        exit 1
    fi

fi

echo "Checking pip version"
MINIMUM_PIP_VERSION=22
pipversion=( $(python -m pip --version | awk '{print $2}' | sed 's/\./\n\t/g') )
if let "${pipversion[0]}<${MINIMUM_PIP_VERSION}"; then
    echo "Insufficient version of pip found. Requires at least version ${MINIMUM_PIP_VERSION}."
    echo "See https://lincc-ppt.readthedocs.io/ for details."
    exit 1
fi

echo "Installing package and runtime dependencies in local environment"
python -m pip install -e . > /dev/null

echo "Installing developer dependencies in local environment"
python -m pip install -e .'[dev]' > /dev/null
if [ -f docs/requirements.txt ]; then python -m pip install -r docs/requirements.txt > /dev/null; fi

echo "Installing pre-commit"
pre-commit install > /dev/null

#######################################################
# Include any additional configurations below this line
#######################################################
