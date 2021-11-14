import itertools
from pprint import pprint
from typing import List
from copy import copy


"""
    pushed = [1,2,3,4,5], popped = [4,5,3,2,1]

    choices = pushed + popped

    generate all permutations of choices

    see which permutations would actually be a valid stack operation
"""




class Choice:
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def __repr__(self):
        return f"<{self.op} {self.arg}>"




class Solution:

    def valid_sequence(self, ops: List[Choice]):
        stack = []
        for op in ops:
            try:
                if op.op == "append":
                    stack.append(op.arg)
                if op.op == "pop":
                    assert stack.pop() == op.arg
            except:
                return False

        return True


    def permute_in_order(self, arrays, ans=[], candidate=[]):

        if (not arrays[0]) and (not arrays[1]):
            ans.append(copy(candidate))
            return

        for bit in [0,1]:
            try:
                candidate.append( arrays[bit][0] )
            except:
                continue

            array_0_slice = 0 if bit == 1 else 1
            array_1_slice = 1 if bit == 1 else 0

            array_0 = arrays[0][array_0_slice:]
            array_1 = arrays[1][array_1_slice:]

            self.permute_in_order([ array_0, array_1 ], ans, candidate)

            candidate.pop()

        return ans


    def validateStackSequences(self, pushed, popped) -> bool:
        choices = [ ]
        pushed = [ Choice("append", num) for num in pushed ]
        popped = [ Choice("pop", num) for num in popped ]


        permutations = self.permute_in_order([pushed, popped])
        pprint(permutations)


        if not permutations:
            return True

        for permutation in permutations:
            if self.valid_sequence(permutation):
                return True

        return False





# assert Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) == True

Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])

