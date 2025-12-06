#!/usr/bin/env python3
"""AoC day 6, 2025: Trash Compactor"""

import pathlib
import sys
from functools import reduce
from operator import add, mul


def parse_data(puzzle_input: str):
    """Parse input"""
    *grid, ops = puzzle_input.splitlines()
    return grid, [{"*": mul, "+": add}[o] for o in ops.split()]


def part1(data):
    """Solve part 1"""
    grid, ops = data
    grid = zip(*(line.strip().split() for line in grid))

    result = 0
    for nums, op in zip(grid, ops):
        result += reduce(op, map(int, nums))
    return result


def _part2(data):
    """
    Solve part 2

    This was my first attempt, a bit more verbose.
    I forgot about `itertools.groupby` and the magic of iterators.

    Other than that, there's a negligible speedup between this and the final solution.
    """
    from collections import deque

    grid, ops = data
    ops = deque(ops)

    total = 0
    op = ops.popleft()
    result = 0 if op is add else 1
    for digits in zip(*grid):
        if all(d == " " for d in digits):
            total += result
            op = ops.popleft()
            result = 0 if op is add else 1
            continue
        result = op(result, int("".join(digits).strip()))
    return total + result


def part2(data):
    """Solve part 2"""
    from itertools import groupby

    grid, ops = data
    ops_iter = iter(ops)
    total = 0

    for is_sep, group in groupby(
        zip(*grid), key=lambda col: all(c == " " for c in col)
    ):
        if is_sep:
            continue
        op = next(ops_iter)
        nums = (int("".join(col).strip()) for col in group)
        result = reduce(op, nums)
        total += result
    return total


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(s) for s in solutions))
