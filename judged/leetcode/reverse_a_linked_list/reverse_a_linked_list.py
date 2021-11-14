
"""
                  ** head.next = X **
                        |
                        |
    5 -> 4 -> 3 -> 2 -> 1 -> X
                   |___________ ** head.next.next = head **
    1 -> 2 -> 3 -> 4 -> 5 -> X
    |    |    |
  head   |    |
    head.next |
         head.next.next
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val} -> {self.next}"

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(head)

# 1 -> 2 -> 3 -> 4 -> 5 -> None

def reverse_linked_list(head: Node):
    print(head)

    if head is None or head.next is None: # nothing to reverse
        print("="*29)
        return head # 5 -> None

    # p is for pointer
    # ^^ this is key
    p = reverse_linked_list(head.next) # really I'm just saying; `p = head.next`
    # ^ realize that all variables are pointers in python

    print(f"before `head.next.next = head`; head: {head}")
    print(f"before `head.next.next = head`; p   : {p}")
    print("")

    head.next.next = head    # here, I'm actually modifying `p`
    # since `head.next.next = p.next` i.e `p = head.next`
    # so i'm saying 5   ->    4 ->  5 -> None
    # it's self-referential, loop, cycle,
    # ^^ that's why i'm getting a recursion error
    print(f"before `head.next = None`;      head: { head.next.val} -> { head.val } -> {head.next.val} -> {head.next.next.val}")
    print("")

    head.next = None
    # stop making it self-referential, loopy, cyclic
    # let 4 -> None

    # We modified `p` by modifying what it points to

    print(f"head:  {head}")  # 5 -> None
    print(f"p   :  {p}")
    print("")
    print("")
    return p

reverse_linked_list(head)