goodPW_part1 = 0
badPW_part1 = 0
goodPW_part2 = 0
badPW_part2 = 0

with open("input.txt") as f:
    for line in f:
        idx = []
        ll = line.split()
        idxs = [int(idx) for idx in ll[0].split("-")]
        letter = ll[1][0]
        pw = ll[2]
        if idxs[0] <= pw.count(letter) <= idxs[1]:
            goodPW_part1 += 1
        else:
            badPW_part1 += 1

        if (pw[idxs[0]-1] == letter) ^ (pw[idxs[1]-1] == letter):
            goodPW_part2 += 1
        else:
            badPW_part2 += 1

print("Part 1 has",goodPW_part1, "good passwords, and", badPW_part1,"bad ones")
print("Part 2 has",goodPW_part2, "good passwords, and", badPW_part2,"bad ones")


