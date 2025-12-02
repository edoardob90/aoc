# Advent of Code 🎅🏻🎄👨🏻‍💻

Solutions for [Advent of Code](https://adventofcode.com/) puzzles, from various years.

## Languages

- **Python** (primary) — runs with PyPy for speed
- **Rust** (2024)
- **Wolfram Language** (occasional, as WolframScript files for portability)

## Usage

```bash
# Run today's solution
mise run aoc

# Run with example data
mise run aot

# Scaffold new day
mise run new
```

Or directly:
```bash
cd 2024/01
pypy 1.py input.txt
```

## Structure

```
YYYY/
  DD/
    N.py          # Python solution
    N.wls         # Wolfram (optional)
    python/       # 2024+ structure
    rust/         # 2024+ structure
    example.txt   # Sample input
```

## Setup

Requires [mise](https://mise.jdx.dev/). Run `mise install` to set up PyPy.

Input files (`input.txt`) are gitignored per AoC copyright policy.
