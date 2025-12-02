"""AoC 8, 2021"""

# Standard library imports
import pathlib
import sys
from collections import defaultdict

digits = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg"
}

# a dictionary mapping how many segments are needed for each digit
digits_len = defaultdict(dict)
for k,v in digits.items():
    digits_len[len(v)][k] = v

print(digits_len)

# [1, 4, 7, 8] are digits that can be rendered with a unique number of segments -> easy digits
# [2, 4, 3, 7] are their lengths

def parse(puzzle_input):
    """Parse input"""
    output = []
    for line in puzzle_input.split('\n'):
        output.append(tuple(tuple(x.split()) for x in line.split(' | ')))
    return output


def part1(data):
    """Solve part 1"""
    easy_digits_len = tuple(k for k in digits_len if len(digits_len[k]) == 1)
    def count_easy_digits(list_):
        total = 0
        for digit in easy_digits_len:
            total += list_.count(digit)
        return total

    result = 0
    for line in data:
        result += count_easy_digits(list(map(len, line[1])))

    return result


def part2(data):
    """Solve part 2"""
    return None


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions if solution))
