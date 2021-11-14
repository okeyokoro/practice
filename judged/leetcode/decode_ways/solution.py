import functools

class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache
        def dp(s):
            if s == "":
                return 1
            
            if s[0] == "0":
                return 0

            if len(s) == 1:
                return 1

            dp1 = dp(s[1:])
            dp2 = 0

            if 1 <= int(s[:2]) <= 26:
                try:
                    dp2 = dp(s[2:])
                except:
                    pass
                
            return dp1 + dp2

        
        return dp(s)
            
  