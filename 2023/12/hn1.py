import pytest

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result

def solve():
    total = 0

    for line in open(0):
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        total += count(cfg, nums)

    print(total)

@pytest.mark.parametrize("line,expected", [
    ("???.### 1,1,3", 1),
    ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
    ("?###???????? 3,2,1", 10),
    ("????.######..#####. 1,6,5", 4),
])
def test_cfgs(line, expected):
    cfg, nums = line.split()
    nums = tuple(int(n) for n in nums.split(","))
    assert count(cfg, nums) == expected

if __name__ == "__main__":
    solve()
