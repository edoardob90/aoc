#!/usr/bin/env python3
"""AoC day 2, 2025: Gift Shop"""

import pathlib
import sys
import re


def parse_data(puzzle_input: str):
    """Parse input"""
    return [r.split("-") for r in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    invalid = 0
    for start, end in data:
        for num in range(int(start), int(end) + 1):
            if re.search(r"^(\d+)\1$", str(num)):
                invalid += num
    return invalid


def part2(data):
    """Solve part 2"""
    invalid = 0
    for start, end in data:
        for num in range(int(start), int(end) + 1):
            if re.search(r"^(\d+)\1+$", str(num)):
                invalid += num
    return invalid


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(s) for s in solutions))
