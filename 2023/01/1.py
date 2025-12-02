#!/usr/bin/env python3
"""AoC day 1, 2023: Trebuchet?!"""

import pathlib
import sys

def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    return data


def part2(data):
    """Solve part 2"""
    def extract_digits(string: str):
        digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "zero": "0"
        }
        
        found_digits = []

        for i, s in enumerate(string):
            if s.isdigit():
                found_digits.append(s)
                continue

            for word, digit in digit_map.items():
                if string[i:].startswith(word):
                    found_digits.append(digit)

        if len(found_digits) == 1:
            found_digits.append(found_digits[0])

        return int(found_digits[0] + found_digits[-1])

    return sum(extract_digits(s) for s in data)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
