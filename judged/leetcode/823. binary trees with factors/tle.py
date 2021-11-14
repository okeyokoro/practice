"""
TLEs
but will print out the trees for you :)
"""


from copy import copy
from collections import deque
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        trees = [ deque([None, a]) for a in arr ]
        ans = len(arr)
            
        def can_make_tree(a, i, j):
            # print("======")
            # print(a, i, j)
            
            store = { 'i': i, 'j': j }
            idx = {}

            tree = deque([None, a])
            i.popleft()
            j.popleft()
            
            def addfrom(s):
                idx[len(tree)] = s
                try:
                    tree.append(store[s].popleft())
                except:
                    tree.append(None)
            
            addfrom('i')
            addfrom('j')

            x = 2
            while i or j:
                addfrom(idx[x])
                addfrom(idx[x])
                x += 1
                
            def isvalid(tree):
                for i in range(1, len(tree)//2):
                    if tree[2*i] == tree[(2*i) + 1] == None:
                        continue
                    if tree[i] != tree[2*i] * tree[(2*i) + 1]:
                        return False
                return True
            
            # print(tree)
            # print("======")
            
            if isvalid(tree):
                return tree
            else:
                return None
        

        # print(trees)
        keepgoing = True
        while keepgoing:
            temp = []
            for a in arr:
                for i in trees:
                    for j in trees:
                        tree = can_make_tree(a, copy(i), copy(j))
                        if tree and tree not in trees:
                            temp.append(tree)
                            print(tree)
                            ans += 1
            
            if not temp:
                keepgoing = False

            trees.extend(temp)

        print(ans)
        return ans


# Solution().numFactoredBinaryTrees([18,3,6,2])
# Solution().numFactoredBinaryTrees([2,4])
# Solution().numFactoredBinaryTrees([2,4,5,10])
Solution().numFactoredBinaryTrees([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48])
 



