"""
    https://start.interviewing.io/interview/YonTaXdr6jNY/replay

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    minimum depth = 2

        3 
    / \
    9  20
        /  \
    15   7
"""

from collections import deque

def solution(tree) -> int:
    q = deque([(tree, 1)])

    while q:
        node, level = q.popleft()

        if not node.left and not node.right:
            return level

        if node.left:
            q.append((node.left, level+1))

        if node.right:
            q.append((node.right, level+1))
