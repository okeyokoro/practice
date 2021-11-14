from collections import deque
from typing import List, Union, Set, FrozenSet


class Node:
    pass


class Edge:
    pass


# represent bi-directionality with two doors
class Door(Edge):
    def __init__(self, unlocked:bool, key:Union[int, bool], next_room:Room):
        self.unlocked  = unlocked
        self.key  = key
        self.next_room = next_room


class Room(Node):
    def __init__(self, key:Union[int, bool], treasure:bool, doors:List[Door]):
        self.key = key
        self.treasure = treasure
        self.doors = []


"""
    My faults:

    - didn't go through the example
    - didn't account for cycles
    - didn't act on the fact that the player could gather keys as he traversed
    - didn't create a test case

    - oh wow there's complexity, you may want to circle back
      to rooms where we couldn't unlock all the doors

    -------------------------

    O(n) // n is number of rooms
"""


def solution(start) -> bool:
    keys = set()
    visited = set()

    # unexplored_doors = {} # Set[FrozenSet[Door]]
    unexplored_rooms = deque([start])

    while unexplored_rooms:
        room = unexplored_rooms.popleft()

        res = find_treasure_or_unexplored_doors(start, keys, visited)
        if res == True:
            return True

        elif res == set(): # or res in unexplored_doors :
            # no unexplored_doors # we've seen everything & we'll never find treasure
            # or
            # we see the same set of unexplored_doors # we can never explore those doors
            return False

        rooms_behind_unexplored_doors = try_to_get_rooms_from_unexplored_doors(res, keys, visited)
        unexplored_rooms.extend(rooms_behind_unexplored_doors)
        # unexplored_doors.append(res)

    return False


def find_treasure_or_unexplored_doors(start, keys, visited,) -> Union[bool, FrozenSet[Door]]:
    unexplored_doors = set()
    q = deque([start])

    while q:
        room = q.popleft()
        keys.add(room.key)

        if room in visited:
            continue

        if room.treasure:
            return True

        for door in room.doors:
            if door.unlocked or door.key in keys:
                q.append(door.next_room)
            elif door not in unexplored_doors:
                unexplored_doors.add(door)

        visited.add(room)

    return frozenset(unexplored_doors)


def try_to_get_rooms_from_unexplored_doors(unexplored_doors, keys, visited) -> List[Room]:
    return [
        door.next_room for door in unexplored_doors
        if door.key in keys and door.next_room not in visited
    ]

