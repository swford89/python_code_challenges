# CodingNomads - Coding Challenge #3: The Perfect Shuffle 
# July 10, 2021
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

def shuffle(deck: list):
    """function for interleaving two halves of a deck of cards"""
    shuffled_deck = []
    interleave_count = 0
    ONE_HALF = deck[:26]
    ANOTHER_HALF = deck[26:]
    while interleave_count < 26:
        shuffled_deck.append(ONE_HALF[interleave_count])
        shuffled_deck.append(ANOTHER_HALF[interleave_count])
        interleave_count += 1 
    return shuffled_deck

def indefinte_shuffle(new_deck: list, shuffled_deck: list):
    """function to determine how many shuffles it will take to reach original new deck state"""
    shuffling = True
    shuffle_count = 1
    while shuffling:
        ONE_HALF = shuffled_deck[:26]
        ANOTHER_HALF = shuffled_deck[26:]
        interleave_count = 0
        transient_deck = []
        while interleave_count < 26:
            transient_deck.append(ONE_HALF[interleave_count])
            transient_deck.append(ANOTHER_HALF[interleave_count])
            interleave_count += 1
        shuffle_count += 1
        shuffled_deck = transient_deck.copy()
        transient_deck.clear()
        if shuffled_deck == new_deck:
            count_string = f"Total shuffles needed to return shuffled deck back to new deck state: {shuffle_count}"
            shuffling = False
    return count_string

# NORMAL NESTED LOOP/CARTESEAN PRODUCT 
# new_deck = []
# for suit_num in range(len(SUITS)):
#     for rank_num in range(len(RANKS)):
#         some_card = Card(suit_num, rank_num)
#         new_deck.append(some_card)

# LIST COMPREHENSION: for creating a deck of cards
new_deck = [Card(suit_num, rank_num) for suit_num in range(len(SUITS)) for rank_num in range(len(RANKS))]
print(f"Brand new deck of cards:\n{new_deck}")

# Shuffle/interleave equal halves of new deck
shuffled_deck = shuffle(new_deck)
print(f"Interleaving two halves of the new deck:\n{shuffled_deck}")

# Shuffle until deck gets back to initial new deck state
count_string = indefinte_shuffle(new_deck, shuffled_deck)
print(count_string)