from typing import List
from dataclasses import dataclass

@dataclass
class Card:
    suit: str
    rank: str


@dataclass
class Hand: # a collection of 5 cards
    card_1: Card
    card_2: Card
    card_3: Card
    card_4: Card
    card_5: Card


def poker(hands:List[Hand]):
    return best_hand(hands)


def best_hand(hands:List[Hand]):
    # we want the max hand
    # we nneed to compute a value for each hand
    return hands[0]

