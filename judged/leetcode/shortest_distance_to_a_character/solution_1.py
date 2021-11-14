from collections import deque

class Solution:
    def shortestToChar(self, string, char):
        lst = [deque([])]

        for i, c in enumerate(string):
            if c == char:
                if len(lst[-1]) < 2 or len(lst) == 1:
                    if not lst[-1] and i == len(string)-1:
                        continue
                    lst.append(deque([]))
                    if lst[-2] and i < len(string)-1:
                        lst.append(deque([]))
                else:
                    tmp = deque()
                    for _ in range(len(lst[-1])//2):
                        tmp.append(lst[-1].popleft())
                    lst.append(tuple(tmp))
                    lst.append(deque([]))
                    if i < len(string)-1:
                        lst.append(deque([]))
            else:
                lst[-1].appendleft(c)

        ans = []
        for i, l in enumerate(lst):
            if not l:
                ans.append(0)
                continue
            if i == 0 or isinstance(l, tuple):
                ans.extend(list( range(len(l),0,-1) ))
                continue
            ans.extend(list(range(1,len(l)+1)))
        return ans
