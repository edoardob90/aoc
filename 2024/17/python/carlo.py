def solve(prog: list[int], a: int, b: int, c: int) -> list[int]:
    ip, out = 0, []
    while ip < len(prog):
        instr, operand = prog[ip], prog[ip + 1]
        combo = operand, operand, operand, operand, a, b, c
        a = a // (2 ** combo[operand]) if instr == 0 else a
        b = b ^ operand if instr == 1 else b
        b = combo[operand] % 8 if instr == 2 else b
        ip = operand - 2 if instr == 3 and a != 0 else ip
        b = b ^ c if instr == 4 else b
        if instr == 5:
            out.append(combo[operand] % 8)
        b = a // (2 ** combo[operand]) if instr == 6 else b
        c = a // (2 ** combo[operand]) if instr == 7 else c
        ip += 2
    return out


def part2(n: int, a: int) -> int:
    if n == -1:
        return a
    a <<= 3
    for x in range(8):
        if solve(prog, a + x, 0, 0) == prog[n:]:
            s = part2(n - 1, a + x)
            if s != -1:
                return s
    return -1


data = open("../example.txt" if __debug__ else "../input.txt").read().replace("\n", " ")
ints = lambda x: [int(i) for i in __import__("re").findall(r"-?\d+", x)]  # noqa: E731
a, b, c, *prog = ints(data)
print(prog)
p1, p2 = ",".join(map(str, solve(prog, a, b, c))), part2(len(prog) - 1, 0)
print(p1, p2, sep="\n")
assert p1 == "4,6,3,5,6,3,5,2,1,0" and p2 == -1
