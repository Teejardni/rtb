import random

# Card representation and deck setup
suits = ['♥', '♦', '♣', '♠']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
rank_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

def create_deck():
    return [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck