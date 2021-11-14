"""
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""


from copy import copy
from typing import List
from collections import defaultdict, deque

# one person can bribe at most 2 others = you can only move forward 2 positons
# a person can only bribe the person directly in front of them
# we could build a game tree
# we stop when every-one has bribed twice


def minimumBribes(final:List[int]):
    answers = []
    swap_table = [ 0 for i in final ]
    memo = set()

    bfs(sorted(final), final, answers, swap_table)

    if not answers:
        print("Too chaotic")
    else:
        print(min(answers))



def move_forward(i, node, swap_table):
    swap_table[ node[i]-1 ] += 1

    if swap_table[ node[i]-1 ] > 2:
        raise

    if node[i-1] > node[i]:
        raise

    node[i-1], node[i] = node[i], node[i-1]
    return node, swap_table



def bfs(start, final, answers, table):
    q = deque([ (0, start, table,) ])

    while q:
        level, node, swap_table = q.popleft()

        if level >= len(start):
            return

        if node == final:
            answers.append(level)
            return

        for i in range(1, len(node)):
            try:
                new_node, new_swap_table = move_forward(i, copy(node), copy(swap_table))
                q.append( (level+1, new_node, new_swap_table) )
            except:
                continue



if __name__ == "__main__":
    minimumBribes([2, 1, 5, 3, 4]) # 3
    minimumBribes([2, 5, 1, 3, 4]) # too chaotic # works,
    minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) # too chaotic # works, but still slow
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) # 7  # works, but still slow
    minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]) # 4  #  works, but still slow

