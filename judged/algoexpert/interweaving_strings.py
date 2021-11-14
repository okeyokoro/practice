import functools

"""
    https://leetcode.com/problems/interleaving-string/
"""


def interweavingStrings(one, two, three) -> bool:
    if len(one) + len(two) != len(three):
        return False

    result = False

    @functools.lru_cache
    def helper(l1, l2, l3, p1, p2, p3):
        nonlocal result

        if p1 == len(l1) and p2 == len(l2):
            if p3 == len(l3):
                result = True
            return
        
        if p3 == len(l3):
            return

        if p1 < len(l1):
            if l1[p1] == l3[p3]:
                helper(l1, l2, l3, p1+1, p2, p3+1 )
        
        if p2 < len(l2):
            if l2[p2] == l3[p3]:
                helper(l1, l2, l3, p1, p2+1, p3+1 )
        
        
    helper(one, two, three, 0, 0, 0)
    
    return result


