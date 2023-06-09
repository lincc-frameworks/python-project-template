#!/usr/bin/env bash

echo "Initializing local git repository"
git init .
git branch -m master main 2>/dev/null

echo "Installing package and runtime dependencies in local environment"
pip install -e . > /dev/null

echo "Installing developer dependencies in local environment"
pip install -e .'[dev]' > /dev/null

echo "Installing pre-commit"
pre-commit install > /dev/null
