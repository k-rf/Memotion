#! /usr/bin/env bash

find memotion -type d | grep -v "__pycache__" | xargs -I {} touch {}/__init__.py
find tests -type d | grep -v "__pycache__" | xargs -I {} touch  {}/__init__.py
