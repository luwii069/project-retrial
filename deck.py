# deck.py
import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
new_ranks = ['4', '5', '6', '7', '9', '10']
new_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
joker = [('Joker', 'Joker')]

def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def new_deck():
    return [(rank, suit) for suit in new_suits for rank in new_ranks]

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]
