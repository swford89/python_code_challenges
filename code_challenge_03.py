# CodingNomads - Coding Challenge #3: The Perfect Shuffle 
# July 3, 2021
# Scott Ford

# Task #1 = split deck into two equal sized halves: 26 cards each, 52 total
# Task #2 = Interleave each half evenly with one another; one card from the left, one card from the right


SUITS = ['♠️', '♥️', '♦️', '♣️']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

SUITS_DICT = {
    '♠️': 1,
    '♥️': 2,
    '♦️': 3, 
    '♣️': 4,
}

RANKS_DICT = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
}

class Card():
    def __init__(self, suit: int, rank: int) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return RANKS[self.rank] + SUITS[self.suit]

    # def shuffle(self, default_deck: list):
    #     one_half = default_deck[:26]
    #     another_half = default_deck[26:]
    #     shuffled_deck = one_half[::2] + another_half[::2]
    #     return shuffled_deck

def shuffle(deck: list):
    one_half = deck[:26]
    another_half = deck[26:]
    shuffled_deck = []
    return shuffled_deck

default_deck = [(suit, rank) for suit in SUITS for rank in RANKS]
one_half = default_deck[:26]
another_half = default_deck[26:]

shuffled_deck = shuffle(default_deck)
print(*default_deck)
print(*shuffled_deck)