x, y = 0, 0

houses = {(x, y)}

with open('input.txt') as f:
    for c in f.read():
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1

        houses.add((x, y))

print(len(houses))
