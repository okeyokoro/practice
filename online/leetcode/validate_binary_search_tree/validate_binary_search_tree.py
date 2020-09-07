"""
https://stackoverflow.com/a/759851/7450570
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def validateBst(node:BST, minimum=float("-inf"), maximum=float("inf")):
    if not node:
        return True

    if (minimum < node.value <= maximum
        and validateBst(node.left, minimum, node.value)
        and validateBst(node.right, node.value, maximum)):
        return True

    return False
