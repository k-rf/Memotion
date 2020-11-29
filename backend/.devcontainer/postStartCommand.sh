#! /bin/bash

git ls-files | xargs git update-index --no-skip-worktree

git update-index --skip-worktree .commit_template
git update-index --skip-worktree .gitignore
git update-index --skip-worktree docker-compose.yaml

git ls-files | grep script | xargs git update-index --skip-worktree
git ls-files | grep frontend | xargs git update-index --skip-worktree
