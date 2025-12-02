import sys
from timer import Timer

X = [int(x) for x in sys.stdin.readline().strip().split(',')]

days = int(sys.argv[1]) if len(sys.argv) > 1 else 80

def update(X):
    fishes = []
    for x in X:
        if x == 0:
            fishes.append(6)
            fishes.append(8)
        else:
            fishes.append(x-1)
    return fishes

@Timer(unit='ms')
def solve(X):
    for _ in range(days):
        X = update(X)
    print(len(X))

if __name__ == "__main__":
    solve(X)
