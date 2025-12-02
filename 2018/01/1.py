from collections import deque

freqs = deque([int(x) for x in open(0).read().splitlines()])

total = step = 0
results = set((0,))

while True:
    step += 1
    total += freqs[0]
    if total in results:
        print(f"{total} (after {step} steps)")
        break
    results.add(total)
    freqs.rotate(-1)
