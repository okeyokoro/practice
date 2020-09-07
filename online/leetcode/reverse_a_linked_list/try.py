
class ListNode:
    def __init__(self):
        self.data = None
        self.next = None

"""
    1 -> 2 -> 3 -> 4

    4 -> 3 -> 2 -> 1

====
    1 -> 2
    2 <- 1
====
    1 -> 2 -> 3
    3 <- 2 <- 1
====
    # don't lose the pointer you got for free
"""

def solution(node):
    dummy_head = head = ListNode()
    tail = None

    while node:
        head.next = node.next
        head.next.next = tail = node
        node = node.next.next

    return dummy_head.next
