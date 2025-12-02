#!/usr/bin/env python
# Jonathan Paulson's solution
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2020/15.py

S = [20,9,11,0,1,2]
last_index = {}

for i,n in enumerate(S):
    if i != len(S)-1:
        last_index[n] = i

while len(S) < 30000000:
    prev = S[-1]
    prev_prev = last_index.get(prev, -1)
    last_index[prev] = len(S)-1
    if prev_prev == -1:
        next_ = 0
    else:
        next_ = len(S) - 1 - prev_prev
    S.append(next_)
    if len(S) == 2020:
        print(next_)

print(S[-1])
