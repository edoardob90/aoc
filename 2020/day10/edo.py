#!/usr/bin/env python
import fileinput

xs = [int(y) for y in fileinput.input()]
xs.append(0)
xs.sort()
xs.append(max(xs)+3)

DP = {}

def dp(i):
    if i == len(xs)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    next_i = i+1
    while next_i < len(xs) and xs[next_i]-xs[i] <= 3:
        ans += dp(next_i)
        next_i += 1
    DP[i] = ans
    return ans

print(dp(0))
