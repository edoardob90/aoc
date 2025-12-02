#!/usr/bin/env python
from itertools import combinations

with open("input.txt", "r") as fp:
    numberlist = [int(x) for x in fp.readlines()]
    comblist = combinations(numberlist,2)
    comb = next(comblist)
    while comb[0]+comb[1] != 2020:
        comb = next(comblist)
    print("Oggi ho mangiato ", comb[0]*comb[1], " torte")

