# deck.py
#list of ranks and suits for the main deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

new_ranks = ['4', '5', '6', '7', '9', '10'] #list of ranks and suits for the table card
new_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

#call back functions to be used in the main function 
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def new_deck():
    return [(rank, suit) for suit in new_suits for rank in new_ranks]
#adds cards to players and computer hands and ensure only the number of cards assigned will be displayed 
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]
