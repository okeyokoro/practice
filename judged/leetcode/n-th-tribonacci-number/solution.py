
from functools import cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dp(x):
            if x <= 1:
                return x
            elif x == 2:
                return 1
            return dp(x-1) + dp(x-2) + dp(x-3)
        
        return dp(n)
        

