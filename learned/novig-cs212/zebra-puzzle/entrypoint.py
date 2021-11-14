import itertools

"""
    1 There are five houses.
    2 The Englishman lives in the red house.
    3 The Spaniard owns the dog.
    4 Coffee is drunk in the green house.
    5 The Ukrainian drinks tea.
    6 The green house is immediately to the right of the ivory house.
    7 The Old Gold smoker owns snails.
    8 Kools are smoked in the yellow house.
    9 Milk is drunk in the middle house.
    10 The Norwegian lives in the first house.
    11 The man who smokes Chesterfields lives in the house next to the man with the fox.
    12 Kools are smoked in a house next to the house where the horse is kept.
    13 The Lucky Strike smoker drinks orange juice.
    14 The Japanese smokes Parliaments.
    15 The Norwegian lives next to the blue house.

    Who drinks water? 
    Who owns the zebra?

    Each house is painted a different color,
    and their inhabitants are of different nationalities,
    own different pets,
    drink different beverages
    and smoke different brands of American cigarettes.
"""

def solution():
    print("working...")

    colors = [ "red", "green", "ivory", "blue", "yellow" ]
    nationalities = [ "spaniard", "englishman", "ukrainian", "norwegian", "japanese" ]
    cigarettes = [ "Kools", "Chesterfields", "Old Gold", "Lucky Strike", "Parliaments" ]
    pets = [ "dog", "snails", "zebra", "fox", "horse" ]
    drinks = [ "coffee", "tea", "milk", "orange juice", "water" ]

    def green_right_of_ivory(k):
        return k.index("green") == k.index("ivory") + 1

    def milk_in_middle(d):
        return d[2] == "milk"

    def norwegian_first(n):
        return n[0] == "norwegian"

    for k in filter(green_right_of_ivory, itertools.permutations(colors)):
        for d in filter(milk_in_middle, itertools.permutations(drinks)):
            for n in filter(norwegian_first, itertools.permutations(nationalities)):
                for c in itertools.permutations(cigarettes):
                    for p in itertools.permutations(pets):

                        if k.index("red") != n.index("englishman"):
                            continue

                        if p.index("dog") != n.index("spaniard"):
                            continue

                        if d.index("coffee") != k.index("green"):
                            continue

                        if n.index("ukrainian") != d.index("tea"):
                            continue

                        if c.index("Old Gold") != p.index("snails"):
                            continue

                        if c.index("Kools") != k.index("yellow"):
                            continue

                        if abs(p.index("fox") - c.index("Chesterfields")) != 1:
                            continue
                        
                        if abs(p.index("horse") - c.index("Kools")) != 1:
                            continue
                        
                        if d.index("orange juice") != c.index("Lucky Strike"):
                            continue

                        if n.index("japanese") != c.index("Parliaments"):
                            continue
                        
                        if abs(n.index("norwegian") - k.index("blue")) != 1:
                            continue

                        print(f"Who drinks water? {n[d.index('water')]}")
                        print(f"Who owns the zebra? {n[p.index('zebra')]}")
                        return

if __name__ == "__main__":
    print(solution())


