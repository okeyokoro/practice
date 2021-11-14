from collections import defaultdict

"""
    buy and sell k times with max profit
    
    buy/sell/skip 0/1/2 knapsack but the capacity is 2k
    
    ^ don't need to use full capacity, just max profit
"""

def maxProfitWithKTransactions(prices, k):
    # we have to compute at different ks
    
    def profit(chosen):
        result = 0
        for i in range(1, len(chosen), 2):
            result += chosen[i] - chosen[i-1]
        return result
    
    dp = defaultdict(list)

    def solution(k, idx, chosen) -> int:
        
        nonlocal dp
    
        # derranged case
        if idx > len(prices)-1:
            if k % 1:
                dp[(k, idx)].append(0)
                return 0
            else:
                result = profit(chosen)
                dp[(k, idx)].append(result)
                return result
        
        # # base cases
        if k == 0:
            result = profit(chosen)
            dp[(k, idx)].append(result)
            return result
    
        
        if k % 1:
            # pending transaction  ; we can  "skip", "sell"
            # sell
            res1 = solution(k-0.5, idx+1, chosen+(prices[idx],))
            # skip
            res2 = solution(k    , idx+1, chosen)
            
            result = max(res1, res2)
            dp[(k, idx)].append(result)
            return result
        else:
            # no pending transaction; we can "buy", "skip"
            # buy
            res1 = solution(k-0.5, idx+1, chosen+(prices[idx],))
            # skip
            res2 = solution(k    , idx+1, chosen)
            
            result = max(res1, res2)
            dp[(k, idx)].append(result)
            return result
        
    def bottom_up(k, idx):
        """
         dp(k=2, len=6) = max( dp(k=1.5, len=5) , dp(k=2, len=5) )
        """
        return
    
    result = solution(k, 0, tuple())
    return result

