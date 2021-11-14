
from collections import defaultdict
from functools import lru_cache


"""
    dp:

    1 0/1 knapsack
    2 unbounded knapsack
    3 fibonacci numbers
    4 palindromic substring 
    5 longest common substring

    no. 4
        
    -----

    questions

    topic =
    dp

    twist =

    test

    brute-force = 
    - try every substring;  <return every substring recusively>
    - filter out substring without duplicates;
    - return the max

    complexity-ladder
    - 2(n) = brute-force
    - n^2 = top-down, bottom-up

    code

    execute
"""


def longestSubstringWithoutDuplication(string) -> str:
    """ tuple -> ( length, start, end ) """
    
    def without_duplication(start, end):
        bag = defaultdict(int)
        for s in string[start:end+1]:
            bag[s] += 1
            if bag[s] > 1:
                return False
            
        return True

    @lru_cache
    def solution(start, end) -> tuple:
        if start == end:
            result = [1, start, end]
            print(result)
            return result
        
        if start > end:
            result = [0, start, end]
            print(result)
            return result
        
        if without_duplication(start, end):
            result = [end-start+1, start, end]
            print(result)
            return result
        else:
            option1 = solution(start+1, end)
            option2 = solution(start, end-1)
            result = max(option1, option2, key=lambda x: x[0])
            print(result)
            return result
    
    result = solution(0, len(string)-1)
    return string[result[1]:result[2]+1]


if __name__ == "__main__":
    print(
        longestSubstringWithoutDuplication("clementisacap")
    )
