#!/usr/bin/env pypy3
import fileinput
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])

FOODS = []

for l in L:
    f, r = l.split('(contains ')
    I = set( f.split() )
    A = set( r[:-1].split(', ') )
    FOODS.append((I,A))

# build a list of unique ingredients and allergens
all_I = set()
all_A = set()
for i,a in FOODS:
    all_I |= i # |= is the in-place union operation between sets
    all_A |= a

COULD_BE = {i: set( all_A ) for i in all_I}
C = defaultdict(int)

for I,A in FOODS:
    for i in I:
        C[i] += 1 # count how many occurences of ingredient i there are
    for a in A:
        for i in all_I:
            if i not in I:
                COULD_BE[i].discard(a)

#for i,j in COULD_BE.items():
#    print(i, C[i], j)

# part 1
p1 = 0
for i in all_I:
    if not COULD_BE[i]:
        p1 += C[i]

print(p1)

# part 2
MAPPING = {}
USED = set()

while len(MAPPING) < len(all_A):
    for i in all_I:
        poss = [a for a in COULD_BE[i] if a not in USED]
        if len(poss)==1:
            MAPPING[i] = poss[0]
            USED.add(poss[0])
sorted_i = ','.join([k for k,v in sorted(MAPPING.items(), key=lambda kv:kv[1])])

print(sorted_i)

