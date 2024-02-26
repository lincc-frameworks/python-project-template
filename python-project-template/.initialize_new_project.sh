#!/usr/bin/env bash

echo "Checking virtual environment"
if [ -z "${VIRTUAL_ENV}" ] && [ -z "${CONDA_PREFIX}" ]; then
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
pipversion=( $(python -m pip --version | awk '{print $2}' | sed 's/\./ /g') )
if let "${pipversion[0]}<${MINIMUM_PIP_VERSION}"; then
    echo "Insufficient version of pip found. Requires at least version ${MINIMUM_PIP_VERSION}."
    echo "See https://lincc-ppt.readthedocs.io/ for details."
    exit 1
fi

echo "Initializing local git repository"
{
    gitversion=( $(git version | git version | awk '{print $3}' | sed 's/\./ /g') )
    if let "${gitversion[0]}<2"; then
	# manipulate directly
	git init . && echo 'ref: refs/heads/main' >.git/HEAD
    elif let "${gitversion[0]}==2 & ${gitversion[1]}<34"; then
	# rename master to main
	git init . && { git branch -m master main 2>/dev/null || true; };
    else
	# set the initial branch name to main
	git init --initial-branch=main >/dev/null
    fi
} > /dev/null

echo "Installing package and runtime dependencies in local environment"
python -m pip install -e . > /dev/null

echo "Installing developer dependencies in local environment"
python -m pip install -e .'[dev]' > /dev/null
if [ -f docs/requirements.txt ]; then python -m pip install -r docs/requirements.txt; fi

echo "Installing pre-commit"
pre-commit install > /dev/null

echo "Committing initial files"
git add . && SKIP="no-commit-to-branch" git commit -m "Initial commit"
