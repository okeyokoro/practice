
def hasPathSum(root: TreeNode, sum: int) -> bool:
    if root is None:
        return False

    nodes = [root]
    sums = [0]

    while nodes:
        currnode = nodes.pop()
        currsum = sums.pop()

        if not currnode.left and not currnode.right: #this is a leaf
            if currsum + currnode.val == sum:
                return True

        if currnode.left:
            nodes.append(currnode.left)
            sums.append(currsum+currnode.val)

        if currnode.right:
            nodes.append(currnode.right)
            sums.append(currsum+currnode.val)

    return False

"""
https://leetcode.com/problems/path-sum/discuss/456046/Python-DFS-Iterative%3A-99.7-100

Python DFS Iterative: 99.7%, 100%
"""