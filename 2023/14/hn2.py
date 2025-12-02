grid = tuple(open(0).read().splitlines())

def cycle(grid):
    for _ in range(4):
        grid = map("".join, zip(*grid))
        grid = ("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

    return grid

seen = {grid}
array = [grid]

iter = 0

while True:
    iter += 1
    grid = cycle(grid)
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

print(iter)

first = array.index(grid)

print(first)

index = (1_000_000_000 - first) % (iter - first) + first

print(index)

grid = array[index]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
