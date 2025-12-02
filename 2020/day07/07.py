"""AoC 07, 2020: Handy Haversacks"""

# Standard library imports
import pathlib
import sys
import re


# def parse(puzzle_input):
#     """Parse input"""
#     def match(content):
#         patt = re.compile(r'\s*(\d+)\s+(.*) bags?')
#         match = re.search(patt, content)
#         return match.groups()[::-1] if match else (None, None)

#     bags = {}

#     for line in puzzle_input.split("\n"):
#         bag, what = line.split(' bags contain ')
#         # bags = [tuple(y for y in x.strip().split()) for x in what.split(',')]
#         content = {k: int(v) for k, v in (match(c) for c in what.split(',')) if k}
#         bags.update({bag: content})

#     return bags


def parse(puzzle_input):
    """Parse input"""

    def parse_bags(line):
        """Parse a single line of input"""
        bag_color, contents_str = line.split(" bags contain ")
        contents = contents_str.split(", ")
        contents_dict = {}
        for content in contents:
            if content == "no other bags.":
                continue
            count, adj, color, _ = content.split(" ")
            contents_dict[f"{adj} {color}"] = int(count)
        return bag_color, contents_dict

    # return dict(tuple(parse_bags(line) for line in puzzle_input.splitlines()))

    bags = []
    for line in puzzle_input.splitlines():
        bags.append(parse_bags(line))

    return dict(bags)


def part1(bags):
    """Solve part 1"""
    shiny_bags = 0

    # Pythonic way
    # def bag_contains(outer_bag, inner_bag):
    #     return (inner_bag in bags[outer_bag]) or any(
    #         # map(lambda x: bag_contains(x, inner_bag), bags[outer_bag].keys())  # functional programming
    #         bag_contains(x, inner_bag) for x in bags[outer_bag].keys()  # no map/lambda
    #     )

    # Dumb way
    def bag_contains(outer_bag, inner_bag):
        if inner_bag in bags[outer_bag]:
            return True

        for bag in bags[outer_bag].keys():
            if bag_contains(bag, inner_bag):
                return True

        return False

    for bag in bags:
        if bag_contains(bag, "shiny gold"):
            shiny_bags += 1

    return f"There are {shiny_bags} bags which contain AT LEAST one shiny gold bag\n"


def part2(bags):
    """Solve part 2"""
    bag = "shiny gold"

    def count_bags_in(outer_bag):
        # If a bag is empty, just count the bag itself
        if not bags[outer_bag]:
            # print(f"'{outer_bag}' bag contains no other bags")
            return 0
        count = 0
        for inner_bag in bags[outer_bag]:
            inner_content = bags[outer_bag][inner_bag]
            count += inner_content * (1 + count_bags_in(inner_bag))
            # print(f"'{outer_bag}' bag contains {inner_content} '{inner_bag}' bags")

        return count

    return f"A '{bag}' bag must contain {count_bags_in(bag)} other bags\n"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    print(data)
    solution1 =  part1(data)
    solution2 =  part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
