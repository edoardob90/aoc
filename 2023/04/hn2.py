lines = open(0).read().splitlines()

m = {i: 1 for i in range(len(lines))}

for i, x in enumerate(lines):

    x = x.split(":")[1].strip()
    a, b = [set(map(int, k.split())) for k in x.split(" | ")]
    j = len(a & b)
    print(f"Card #{i+1}: {j}")

    for n in range(i + 1, i + j + 1):
        m[n] += m[i]

print(sum(m.values()))

