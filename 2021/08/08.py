#pylint: disable=invalid-name
"""AoC 8, 2021"""

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    output = []
    for line in puzzle_input.split('\n'):
        output.append(tuple(tuple(x.split()) for x in line.split(' | ')))
    return tuple(output)


def part1(data):
    """Solve part 1"""
    # These are the lengths of the easy digits
    # 1 -> 2, 4 -> 4, 7 -> 3, 8 -> 7
    total = 0
    for _, display in data:
        for digit in display:
            if len(digit) in [2, 4, 3, 7]:
                total += 1
    return total


def part2(data):
    """Solve part 2"""
    # The easy digits are those with a unique number of display segments
    # Their lengths are unique as well
    easy_digits = {2: "1", 4: "4", 3: "7", 7: "8"}

    result = 0
    for signal, output in data:
        digits = {len(x): set(x) for x in signal if len(x) in (2, 4)}
        num = ""
        for o in output:
            _len = len(o)
            if _len in easy_digits:
                num += easy_digits[_len]
            elif _len == 5:
                # Could be 2, 3, or 5
                s = set(o)
                if len(s & digits[2]) == 2:
                    num += "3"
                elif len(s & digits[4]) == 2:
                    num += "2"
                else:
                    num += "5"
            else: # l must be 6
                # Could be 0, 6, or 9
                s = set(o)
                if len(s & digits[2]) == 1:
                    num += "6"
                elif len(s & digits[4]) == 4:
                    num += "9"
                else:
                    num += "0"
        result += int(num)
    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text(encoding="utf-8").strip())
        print("\n".join(str(solution) for solution in solutions if solution))
