def handle_special_card(play, computer_hand, player_hand, deck, tablecard, current_player):
    rank, suit = play
    
    if rank == "2" and tablecard[-1][0] == "2":
        for _ in range(2):
            if deck:
                card = deck.pop()
                if current_player == "player":
                    computer_hand.append(card)  
                    print(f"Computer's hand: {computer_hand} has been awarded 2 cards.")
                elif current_player == "computer":
                    player_hand.append(card)  
                    print(f"Player's hand: {player_hand} has been awarded 2 cards.")
                
                # Check if there's an Ace to negate the penalty
                if ("A", suit) in player_hand:
                    player_hand.remove(("A", suit))
                    print(f"Player played an Ace and negated the penalty.")
                    break
                elif ("A", suit) in computer_hand:
                    computer_hand.remove(("A", suit))
                    print(f"Computer played an Ace and negated the penalty.")
                    break
            else:
                print("Deck is empty, cannot draw a card.")
    
    elif rank == "3" and tablecard[-1][0] == "3":
        for _ in range(3):
            if deck:
                card = deck.pop()
                if current_player == "player":
                    computer_hand.append(card) 
                    print(f"Computer's hand: {computer_hand} has been awarded 3 cards.")
                elif current_player == "computer":
                    player_hand.append(card) 
                    print(f"Player's hand: {player_hand} has been awarded 3 cards.")
                
                # Check if there's an Ace to negate the penalty
                if ("A", suit) in player_hand:
                    player_hand.remove(("A", suit))
                    print(f"Player played an Ace and negated the penalty.")
                    break
                elif ("A", suit) in computer_hand:
                    computer_hand.remove(("A", suit))
                    print(f"Computer played an Ace and negated the penalty.")
                    break
            else:
                print("Deck is empty, cannot draw a card.")
    
    elif rank in ["K", "J", "8", "Q"]:
        pass

