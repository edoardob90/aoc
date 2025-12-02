#!/usr/bin/env python3
"""AoC day 7, 2024: Bridge Repair"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> list[tuple[int, list[int]]]:
    """Parse input data"""
    lines = []
    for line in puzzle_input.splitlines():
        result, nums = line.split(": ")
        lines.append((int(result), [int(n) for n in nums.split()]))

    return lines


def part1(data: list[tuple[int, list[int]]]) -> int:
    """Solve part 1"""
    from itertools import product
    from operator import add, mul
    
    def can_make_dumb(target, nums):
        n = len(nums) - 1
        for combo in range(2**n):
            result = nums[0]
            for i in range(n):
                if combo & (1 << i):
                    result *= nums[i+1]
                else:
                    result += nums[i+1]
            if result == target:
                return True
        return False

    def can_make_smart(target, nums):
        for ops in product((add, mul), repeat=len(nums)-1):
            result = nums[0]
            for op, num in zip(ops, nums[1:]):
                result = op(result, num)
            if result == target:
                return True
        return False

    return sum(target for target, nums in data if can_make_smart(target, nums))


def part2(data: list[tuple[int, list[int]]]) -> int:
    """Solve part 2"""


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
