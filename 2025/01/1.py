#!/usr/bin/env python3
"""AoC day 1, 2025: Secret Entrance"""

import pathlib
import sys


def parse_data(puzzle_input: str):
    """Parse input"""
    return [
        ((1 if line[0] == "R" else -1), int(line[1:]))
        for line in puzzle_input.splitlines()
    ]


def part1(data):
    """Solve part 1"""
    pos, new, result = 50, 50, 0
    for sign, shift in data:
        r = shift % 100
        new += r * sign
        pos = new % 100
        result += pos == 0
    return result


def part2(data):
    """Solve part 2"""
    pos, result = 50, 0
    for sign, shift in data:
        # Extract full rotations and remainder
        q, r = divmod(shift, 100)

        # Direction-dependent crossing based on current position:
        # - RIGHT (sign=1): cross 0 when pos + movement wraps past 100
        # - LEFT (sign=-1): cross 0 when movement >= pos (and not starting at 0)
        crossing = (pos + r) // 100 if sign == 1 else (r >= pos and pos > 0)

        result += q + crossing
        pos = (pos + r * sign) % 100
    return result


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(s) for s in solutions))
