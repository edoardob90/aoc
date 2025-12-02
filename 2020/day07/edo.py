import fileinput
import re

def match(content):
    patt = re.compile(r'\s*(?P<count>\d+) (?P<color>.*) bag')
    m = re.search(patt, content)
    return m.groups()[::-1] if m else (None, None)

def process(line):
    bag, what = line.split(' bags contain ')
    content = tuple(match(c) for c in what.split(','))
    return bag, {k: v for k, v in content if k}

def bag_contains(outer_bag, inner_bag):
    return (inner_bag in bags[outer_bag]) or any(filter(lambda x: bag_contains(x, inner_bag), bags[outer_bag].keys()))

if __name__ == '__main__':
    bags = {}
    for line in fileinput.input():
        bag, content = process(line)
        bags[bag] = dict(content)

    for bag in bags:
        if bag_contains(bag, 'shiny gold'):
            print(f"{bag} bags contain at least one shiny gold bag")

