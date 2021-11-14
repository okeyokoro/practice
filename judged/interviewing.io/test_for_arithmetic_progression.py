"""
    https://start.interviewing.io/interview/YonTaXdr6jNY/replay

    Given an array of numbers arr. A sequence of numbers is called an
    arithmetic progression if the difference between any two consecutive
    elements is the same.

    Return true if the array can be rearranged to form an arithmetic progression,
    otherwise, return false.

    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences

    sum(1 3 5) = 9

    9 = 1 + (2+1)*(n-1) = 1 + 3*

    ========

    question
        + 

    topic
        + sorting
        + math

    twist
        + negative numbers
        + 

    test

    brute-force
        + # 0
        + sort the array, then compare each numbers
        + time-complexity: O(nlogn)

    complexity-ladder
        + # 1
        + exploit math
        + find the smallest and the second smallest => can be done in O(n) time
        + build the arithmetic progression from the above
        + compare the two
        + time complexity: O(n)

    code

    execute
"""


def solution(array:int):
    return

