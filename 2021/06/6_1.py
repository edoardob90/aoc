import sys
from timer.timer import Timer

fishes = [int(x) for x in sys.stdin.readline().strip().split(',')]

# outfile = open('evolution.txt','w')

try:
    days = int(sys.argv[1])
except IndexError:
    days = 80

def update():
    newborn = 0
    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 6
            newborn += 1
        else:
            fishes[i] -= 1
    if newborn:
        fishes.extend([8]*newborn)

@Timer(unit='ms')
def solve():
    for _ in range(days):
        update()
        # outfile.write(f"{d} {len(fishes)}\n")
    print(f"Total fishes after {days} days: {len(fishes)}")

if __name__ == "__main__":
    solve()
    # outfile.close()
