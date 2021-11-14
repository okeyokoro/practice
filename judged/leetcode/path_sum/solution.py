# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def hasPathSum(root: TreeNode, sum: int) -> bool:
    sums = {None}

    def DFS(node, acc=0):
        if node is None:
            return

        if (node.right is None) and (node.left is None):
            sums.add(acc + node.val)
            return

        DFS(node.left, acc+node.val)
        DFS(node.right, acc+node.val)

    DFS(root)

    return sum in sums

"""
Runtime: 36 ms, faster than 96.45% of Python3 online submissions for Path Sum.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Path Sum.

Next challenges:
Path Sum II
Binary Tree Maximum Path Sum
Sum Root to Leaf Numbers
Path Sum III
Path Sum IV
"""