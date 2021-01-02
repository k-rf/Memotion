#! /bin/bash

git ls-files | xargs git update-index --no-skip-worktree
