def check_winner(player_hand, computer_hand):
    if len(player_hand) == 0:
        print("Congratulations! You win!")
        return True
    elif len(computer_hand) == 0:
        print("Computer wins! Better luck next time.")
        return True
    elif len(player_hand) >= 10:
        print("You have 10 or more cards. Computer wins!")
        return True
    elif len(computer_hand) >= 10:
        print("Computer has 10 or more cards. You win!")
        return True
    return False