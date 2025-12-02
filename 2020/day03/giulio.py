def sledding(stepright, stepdown):
    position = 0
    trees = 0
    with open("input.txt") as f:
        f.readline()
        for line in f:
            for idx in range(stepdown-1):
                line = f.readline()
            position = (position + stepright) % (len(line) -1)
            if line[position] == "#":
                trees += 1
        
    print("We met", trees, "trees")
    return trees

trees_total = 1
for steps in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    trees_total *= sledding(*steps)

print("Total number of trees",trees_total)
