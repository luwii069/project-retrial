import random

# Define ranks and suits for the deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

#new deck to ensure the table card does is'nt a special card
new_ranks= ['4', '5', '6', '7', '9', '10']
new_suits= ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to create and shuffle a deck of cards
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

#function that treates a new deck without the special cards
def new_deck():
    return [(new_rank, new_suit) for new_suit in new_suits for new_rank in new_ranks]

# Function to deal cards to players
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

# Function to display cards
def display_cards(cards, player_name):
    print(f"{player_name}'s cards:")
    for i, card in enumerate(cards):
        print(f"{i + 1}: {card[0]} of {card[1]}")

# Function to check if a card matches the table card
def is_match(card, table_card):
    return card[0] == table_card[0] or card[1] == table_card[1]

# Main function to run the game
def main():
    # Create and shuffle the deck
    deck = create_deck()
    deck2 = new_deck()
    random.shuffle(deck)
    random.shuffle(deck2)

    # Deal cards to players
    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)

    # Place one card from the deck face up on the table
    tablecard = [deck2.pop()]

    while True:
        playermoves(player_hand, computer_hand, tablecard, deck,deck2)
        computer_turn(player_hand, computer_hand, tablecard, deck,deck2)

def playermoves(player_hand, computer_hand, tablecard, deck,deck2):
    print(f"Your hand: {player_hand}")
    print(f"Computer's hand: {computer_hand}")
    print(f"table Card: {tablecard}")

    rank = input("Enter the card rank: ").capitalize().strip()
    suit = input("Enter the card suit: ").capitalize().strip()

    play = (rank, suit)

    if play in player_hand and (play[0] == tablecard[-1][0] or play[1] == tablecard[-1][1]):
        if (tablecard[-1][0] in ['3', '2'] and play[0]!= 'Ace'): 
            for _ in range(int(tablecard[-1][0])): 
                player_hand.append(deck.pop())
            return
        tablecard.append(play)
        player_hand.remove(play)
        if play[0] == "Ace":
            newsuit = input("Enter the new card suit: ").capitalize().strip()
            tablecard[-1] = (tablecard[-1][0], newsuit)
            print(f"The game was changed to {newsuit}")
        if play[0] in ['8', 'King', 'Jack', 'Queen']:
            return playermoves(player_hand, computer_hand, tablecard, deck,deck2)
            
    elif rank == "Pick": 
        player_hand.append(deck.pop())
        print("You picked a card!")
        
    else:
        print(f"Card {play} is not playable. Please try again.")
        playermoves(player_hand, computer_hand, tablecard, deck,deck2)

def computer_turn(player_hand, computer_hand, tablecard, deck, deck2):
    while True:
        # Choose a random card from the computer's hand
        play = random.choice(computer_hand)

        # Check if the card matches the top card on the table
        if is_match(play, tablecard[-1]):
            # If the card has a special effect, apply it
            if play[0] in ['3', '2']:
                for _ in range(int(play[0])):
                    computer_hand.append(deck.pop())
            tablecard.append(play)
            computer_hand.remove(play)
            if play[0] == "Ace":
                newsuit = random.choice(suits)
                tablecard[-1] = (tablecard[-1][0], newsuit)
                print(f"The game was changed to {newsuit}")
            if play[0] in ['8', 'King', 'Jack', 'Queen']:
                return computer_turn(player_hand, computer_hand, tablecard, deck, deck2)
            break
        else:
            # If the card doesn't match, try another card
            continue

    # If the computer has no cards left, it loses the game
    if not computer_hand:
        print("The computer has no cards left. You win!")
        return

    print(f"Computer played: {play}")
    print(f"Computer's hand: {computer_hand}")
    print(f"Table cards: {tablecard}")




if __name__ == "__main__":
    main()