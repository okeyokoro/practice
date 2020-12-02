
def part1(nums, target=2020):
    """
        lol, it's  just the two sum problem
    """
    visited = set()
    for num in nums:
        if target-num in visited:
            return num * (target-num)
        visited.add(num)


def part2(nums, target=2020):
    def twopointers(left, target):
        p1 = left
        p2 = len(nums)-1

        while p1 < p2:
            candidate = nums[p1] + nums[p2]
            if candidate == target:
                return nums[p1] * nums[p2]
            elif candidate < target:
                p1 += 1
            elif candidate > target:
                p2 -= 1

    nums.sort()

    for i in range(len(nums)):
        two = twopointers(i+1, target-nums[i])
        if two:
            return nums[i]*two
  

if __name__ == "__main__":
    print(
        part2([ int(num) for num in open("./input.txt") ])
    )
