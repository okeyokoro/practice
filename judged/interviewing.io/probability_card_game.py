"""
You're a game designer

# of unique cards for rarity |   (% chance to obtain)
94 Common cards              |   (74%)
81 Rare cards                |   (21%)
37 Epic card                 |   (4%)
33 Legendary cards           |   (1%)

A pack contains 5 random cards.

Part 1: Simulate opening a pack and printing out a sensible result

Part 2: "Catch them all" -- keep calling your openPack method and
        return the number of packs open until you have 2 of every type of card e.g.
        "Common1", "Common1", "Common2", "Common2"
"""


import random
from collections import defaultdict


def helper(common, rare, epic, legendary):
    i = random.randint(1, 100)
    if 1 <= i <= 74:
        k = random.choice(common)
        return f"common card #{k}"
    elif 75 <= i <= 95:
        k = random.choice(rare)
        return f"rare card #{k}"
    elif 96 <= i <= 99:
        k = random.choice(epic)
        return f"epic card #{k}"
    elif i == 100:
        k = random.choice(legendary)
        return f"legendary card #{k}"


def open_pack(common, rare, epic, legendary):
    return [ helper(common, rare, epic, legendary) for i in range(5) ]


def solution1():
    common = [ i for i in range(1, 94+1) ]
    rare = [ i for i in range(1, 81+1) ]
    epic = [ i for i in range(1, 37+1) ]
    legendary = [ i for i in range(1, 33+1) ]

    return open_pack(common, rare, epic, legendary)


def helper2(count, pack, local):
    result = 0
    for card in pack:
        if count[card] < 2:
            count[card] += 1
            result += 1
    return local + result


def solution2():
    common = [ i for i in range(1, 94+1) ]
    rare = [ i for i in range(1, 81+1) ]
    epic = [ i for i in range(1, 37+1) ]
    legendary = [ i for i in range(1, 33+1) ]

    result = 0

    total = (94+81+37+33) * 2
    local = 0
    count = defaultdict(int)

    while local < total:
        result += 1
        pack = open_pack(common, rare, epic, legendary)
        local = helper2(count, pack, local)

    return result


print(solution2())

