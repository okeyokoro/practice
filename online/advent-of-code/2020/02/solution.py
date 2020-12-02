from collections import Counter

def part1(line):
    policy, password = line.split(":")
    password = password.strip()

    nums, letter = policy.split(" ")
    lo, hi = nums.split("-")
    lo, hi = int(lo), int(hi)

    if lo <= Counter(password)[letter] <= hi:
        return 1

    return 0

def part2(line):
    policy, password = line.split(":")
    password = password.strip()

    nums, letter = policy.split(" ")
    lo, hi = nums.split("-")
    lo, hi = int(lo), int(hi)

    if Counter([password[lo-1], password[hi-1]])[letter] == 1:
        return 1

    return 0

def solution(lines, valid):
    ans = 0
    for line in lines:
        ans += valid(line)
    return ans


if __name__ == "__main__":
    print(
        solution(open("./input.txt"), part2)
    )