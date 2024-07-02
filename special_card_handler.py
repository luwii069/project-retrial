
def handle_special_card(play, computer_hand, player_hand, deck, tablecard):
    rank, suit = play
    
    if rank == "2" and tablecard[-1][0] == "2":
        for _ in range(2):
            if deck:
                card = deck.pop()
                player_hand.append(card)
                print(f"{player_hand} has been awarded 2 cards.")

                if ("A", suit) in player_hand:
                    player_hand.remove(("A", suit))
                    print(f"{player_hand} played an Ace and negated the penalty.")
                    break
            else:
                print("Deck is empty, cannot draw a card.")
    
    elif rank == "3" and tablecard[-1][0] == "3":
        for _ in range(3):
            if deck:
                card = deck.pop()
                player_hand.append(card)
                print(f"{player_hand} has been awarded 3 cards.")

                if ("A", suit) in player_hand:
                    player_hand.remove(("A", suit))
                    print(f"{player_hand} played an Ace and negated the penalty.")
                    break
            else:
                print("Deck is empty, cannot draw a card.")

    
    elif play[0] in ["K", "J", "8", "Q"]:
        pass

