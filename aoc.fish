#!/usr/bin/env fish
# Quick navigation aliases (tasks are in mise.toml)
set -gx AOC_DIR "$HOME/git/aoc"

alias aocd="cd $AOC_DIR/(date +%Y)"
alias aoct="cd $AOC_DIR/(date +%Y)/(date +%d)"
