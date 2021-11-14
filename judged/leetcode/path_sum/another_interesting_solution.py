
def hasPathSum(root: TreeNode, sum: int) -> bool:
    stack_s = []

    if root is not None:
        stack_s.append((root,root.val))

    ret = False

    while(stack_s):
        left,right = False, False

        current_s,path_sum = stack_s.pop()

        if current_s.left is not None:
            stack_s.append((current_s.left,current_s.left.val + path_sum))
        else:
            left = True

        if current_s.right is not None:
            stack_s.append((current_s.right,current_s.right.val + path_sum))
        else:
            right = True

        if left and right and path_sum == sum:
            ret = True
            break

    return ret

"""
faster than 99%.
"""