#!/usr/bin/env python3
"""AoC day 10, 2024: Hoof It"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> list[str]:
    """Parse input data"""
    return puzzle_input.splitlines()


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