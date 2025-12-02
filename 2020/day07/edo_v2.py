import fileinput
import re
import sys

def match(content):
    patt = re.compile(r'\s*(\d+)\s+(.*) bags?')
    m = re.search(patt, content)
    return m.groups()[::-1] if m else (None, None)

def process(line):
    bag, what = line.split(' bags contain ')
    content = {k: int(v) for k, v in (match(c) for c in what.split(',')) if k}
    # print(bag, content)
    return {bag: content}

def bag_contains(outer_bag, inner_bag):
    return (inner_bag in bags[outer_bag]) or any(map(lambda x: bag_contains(x, inner_bag), bags[outer_bag].keys()))

if __name__ == '__main__':
    
    bags = dict()
    for line in fileinput.input():
        bags.update(process(line))
    
    print(bags)

    # PART 1
    # How many bags contain at least one shiny gold bag?
    shiny_bags = 0
    for bag in bags:
        if bag_contains(bag, 'shiny gold'):
            shiny_bags += 1
            # print(f"{bag} bags contain at least one shiny gold bag")
    print(f"\nThere are {shiny_bags} bags which contain AT LEAST one shiny gold bag\n")

    # PART 2
    # How many distinct bags are contained in a single shiny gold bag?
