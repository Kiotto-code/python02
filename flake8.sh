#!/bin/bash

# find . -name "ex" -type d -exec sh -c 'cd "{}" && flake8' \;
find . -name "ex0*" -exec flake8 {} \;