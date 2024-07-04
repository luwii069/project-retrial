import random
from deck import create_deck, new_deck, deal_cards
from special_card_handler import *
from winner import *

joker = ('Joker', 'Joker')

def main():
    deck = create_deck()
    deck2 = new_deck()
    deck.append(joker)
    random.shuffle(deck) #shuffle main deck randomly
    random.shuffle(deck2)#suddles deck 2 randomly

    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)

    tablecard = [deck2.pop()]

    current_player = "player"  # Start with player's turn
# controls game flow until winner is determined
    while True:
        try:
            player_moves(player_hand, computer_hand, tablecard, deck, current_player)
            if check_winner(player_hand, computer_hand):
                break
            computer_turn(player_hand, computer_hand, tablecard, deck, current_player)
            if check_winner(player_hand, computer_hand):
                break
        except Exception as e:
            print("Error occurred:", e)

def player_moves(player_hand, computer_hand, tablecard, deck, current_player):
    print(f"Your hand: {player_hand}")
    print(f"Computer's hand: {computer_hand}")
    print(f"Table Cards: {tablecard}")
    #inputing the rank and the suit to start playing or quiting 
    rank = input("Enter the card rank (or type 'quit' to exit): ").capitalize().strip()
    if rank.lower() == 'quit':
        print("You have exited the game...Goodbye!")
        exit()

    suit = input("Enter the card suit: ").capitalize().strip()
    if suit.lower() == 'quit':
        print("You have exited the game...Goodbye!")
        exit()
#player game loop
    play = (rank, suit)

    if play in player_hand and (play[0] == tablecard[-1][0] or play[1] == tablecard[-1][1]): 
        tablecard.append(play)
        player_hand.remove(play)

        if play[0] == "A":
            newsuit = input("Enter the new card suit: ").capitalize().strip()
            tablecard[-1] = (tablecard[-1][0], newsuit)
            print(f"The game was changed to {newsuit}")

        if play[0] in ["2", "3", "K", "J", "8", "Q"]:
            handle_special_card(play, computer_hand, player_hand, deck, tablecard, current_player)

        if play[0] == "Joker" or play[1] == "Joker":
            for _ in range(5):
                if deck:
                    computer_hand.append(deck.pop())
   

    elif rank.lower() == "pick": 
        player_hand.append(deck.pop())
        print("You picked a card!")

    else:
        print(f"Card {play} is not playable. Please try again.")
        player_moves(player_hand, computer_hand, tablecard, deck, current_player)

#computer turn
def computer_turn(player_hand, computer_hand, tablecard, deck, current_player):
    playable_cards = [card for card in computer_hand if card[0] == tablecard[-1][0] or card[1] == tablecard[-1][1] or card[1] == "joker"]
    #list comp..filters to check only legal cards are available
    if playable_cards:
        play = random.choice(playable_cards)
    else:
        if deck:
            computer_hand.append(deck.pop())
            print("Computer picked a card!")
        return

    tablecard.append(play)
    computer_hand.remove(play)

    if play[0] in ["2", "3", "K", "J", "8", "Q"]:
        handle_special_card(play, computer_hand, player_hand, deck, tablecard, current_player)
      
    if play[0] == "Joker" or play[1] == "Joker":
        for _ in range(5):
            if deck:
                player_hand.append(deck.pop())

    print(f"Computer's hand: {computer_hand}")
    print(f"Table Cards: {tablecard}")

if __name__ == "__main__":
    main()
