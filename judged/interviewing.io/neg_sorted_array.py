"""
Given: sorted array of integers
Return: sorted array of squares of those integers
Ex: [-2,1,5] -> [1,4,25]
"""

from collections import deque
from typing import List


def solution(array: List[int]) -> List[int]:
    return helper(array)


def helper(array: List[int]) -> List[int]:
    neg = deque([])
    pos = []

    for num in array:
        if num < 0:
            neg.appendleft(num**2)
        else:
            pos.append(num**2)

    n = 0
    p = 0
    solution = []

    while n < len(neg) and p < len(pos):
        if neg[n] == pos[p]:
            solution.append(neg[n])
            solution.append(pos[p])
            n += 1
            p += 1
        elif neg[n] < pos[p]:
            solution.append(neg[n])
            n += 1
        else:
            solution.append(pos[p])
            p += 1

    solution.extend(list(neg)[n:])
    solution.extend(pos[p:])

    return solution


