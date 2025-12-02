bags = {
    "gold": {
        "red": 2,
        "blue": 3,
    },
    "red": {
        "orange": 2,
    },
    "orange": {
        "yellow": 2,
    },
    "yellow": {},
    "blue": {},
    # "yellow": {
    #     "green": 2,
    # },
    # "green": {
    #     "blue": 2,
    # },
    # "blue": {
    #     "violet": 2,
    # },
    # "violet": {},
}

def count_bags(outer_bag: str) -> int:
    if not bags[outer_bag]:
        print(f"'{outer_bag}' bag contains no other bags")
        return 0
    count = 0
    for bag in bags[outer_bag]:
        inner_content = bags[outer_bag][bag]
        print(f"'{outer_bag}' bag contains {inner_content} '{bag}' bags")
        count += inner_content * (1 + count_bags(bag)) # CORRECT ;-)
        # count += inner_content * count_bags(bag) # WRONG!
    return count

if __name__ == "__main__":
    print("bags: ", bags, "\n")
    count = count_bags("gold")
    print(f"\n\nBag 'gold' must contain {count} other bags\n\n")
