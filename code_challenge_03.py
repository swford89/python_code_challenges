# CodingNomads - Coding Challenge #3: The Perfect Shuffle 
# July 3, 2021
# Scott Ford

# Task #1 = split deck into two equal sized halves: 26 cards each, 52 total
# Task #2 = Interleave each half evenly with one another; one card from the left, one card from the right
# Task #3 = How many shuffles does it take to get back to the default deck state?


SUITS = ['♠️', '♥️', '♦️', '♣️']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card():
    def __init__(self, suit: int, rank: int) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return RANKS[self.rank] + SUITS[self.suit]

    def shuffle(self):
        """class method for interleaving two halves of a deck of cards"""
        return shuffled_deck

def shuffle(deck: list):
    """function for interleaving two halves of a deck of cards"""
    shuffled_deck = []
    count = 0
    while count < 26:
        one_half = deck[:26]
        another_half = deck[26:]
        shuffled_deck.append(one_half[count])
        shuffled_deck.append(another_half[count])
        count += 1 
    return shuffled_deck

def indefinte_shuffle(deck: list):
    shuffled_deck = []
    shuffle_count = 0
    while shuffled_deck != deck:
        one_half = deck[:26]
        another_half = deck[26:]
        shuffled_deck.append(one_half[shuffle_count])
        shuffled_deck.append(another_half[shuffle_count])
        shuffle_count += 1 
    return shuffle_count

# NORMAL NESTED LOOP 
# new_deck = []
# for suit_num in range(len(SUITS)):
#     for rank_num in range(len(RANKS)):
#         some_card = Card(suit_num, rank_num)
#         new_deck.append(some_card)

# LIST COMPREHENSION
new_deck = [Card(suit_num, rank_num) for suit_num in range(len(SUITS)) for rank_num in range(len(RANKS))]

# Shuffle/interleave equal halves of new deck
shuffled_deck = shuffle(new_deck)

# Shuffle until deck gets back to initial new deck state
shuffle_count = indefinte_shuffle(new_deck)
print(shuffle_count)