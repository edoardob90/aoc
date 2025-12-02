#!/usr/bin/env python3
"""AoC day 8, 2024: Resonant Collinearity"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> dict[str, list[tuple]]:
    """Parse input data"""
    antennas = {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(row):
            if char != ".":
                antennas.setdefault(char, []).append((x, y))

    return antennas


def part1(data: list[str]) -> int:
    """Solve part 1"""
    return 0


def part2(data: list[str]) -> int:
    """Solve part 2"""
    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
