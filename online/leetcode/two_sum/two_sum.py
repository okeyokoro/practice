from typing import List
improt string



def twoSum(nums: List[int], target: int) -> List[int]:
    bag = {}

    for i, num in enumerate(nums):
        if target-num in bag:
            return [i, bag[target-num]]
        bag[num] = i


print(twoSum([3,2,4], 6))
print(twoSum([2, 7, 11, 15], 9))
