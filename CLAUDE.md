# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Personal Advent of Code solutions repository covering years 2015, 2018-2024. Solutions are written in multiple languages: Python (primary), Rust (2024), and Wolfram Language.

## Directory Structure

Each year has its own folder with day subfolders:
- **2015-2023**: Mixed structure with `dayNN/` or `NN/` folders containing solution files directly
- **2024**: Organized structure with `DD/python/solution.py` and `DD/rust/src/main.rs`

Day folders use **2-digit padding** (e.g., `01`, `09`, `15`).

## Running Solutions

### Python
```bash
# 2024 structure
python 2024/01/python/solution.py input.txt

# Older years (varies by year)
python day01/edo.py < input.txt
# or
python 01/1.py input.txt
```

Uses PyPy (pypy3.10) for performance. Fish shell aliases in `aoc.fish` provide shortcuts.

### Rust (2024 only)
```bash
cd 2024/01/rust
cargo run -- input.txt
```

### Wolfram Language
```bash
chmod +x script.wls
./script.wls < input.txt
```
Requires [WolframScript interpreter](https://www.wolfram.com/wolframscript/).

### Tests
```bash
pytest test_solution.py  # in day folder with tests
```

## Solution Pattern (2024 Python)

Standard structure:
- `parse_data(puzzle_input: str)` - parse raw input
- `part1(data)` / `part2(data)` - solve each part
- `solve(puzzle_input)` - returns tuple of both solutions
- CLI accepts multiple input files as arguments

## Utility Modules

- `2024/utils.py`: `partition()`, `ilist()` helpers
- `tools/aoc_tools.py`: `adjacent_pairs`, `all_pairs`, `rolling_window`, `nums` (extract integers from string), and aliases (`adjp`, `ap`, `rw`, `rsum`, `dd`, `ctr`)

## Input Files

- `input.txt` - actual puzzle input (gitignored)
- `example.txt` / `sample.txt` - test data from puzzle description
- `prompt.md` - puzzle text (2024)
