import random

def roll_dice():
    return random.randint(1,6)

def player_turn():
    player_score = 0
    while True:
        player1 = input("What would you like to do? roll or hold? ").lower()
        if player1 == "q":
            return player_score, True
        elif player1 == "roll":
            roll = roll_dice()
            print("Dice number is", roll)
            if roll == 1:
                print("You rolled 1. Your score is 0")
                player_score = 0
                break
            else:
                player_score += roll
                print("Player score is", player_score)
        elif player1 == "hold":
            print("Player score is", player_score)
            break
        else:
            print("Invalid input, please enter an option betweeen roll or hold.")
    return player_score, False

def computer_turn():
    computer_score = 0
    while True:
        comp_choice = random.choice(["roll", "hold"])
        print("Computer decides to", comp_choice)
        if comp_choice == "roll":
            computer_roll = roll_dice()
            print("Dice number is", computer_roll)
            if computer_roll == 1:
                print("Computer rolled 1. Computer score is 0")
                computer_score = 0
                break
            else:
                computer_score += computer_roll
                print("Computer score is", computer_score)
        elif comp_choice == "hold":
            print("Computer score is", computer_score)
            break
    return computer_score

def game():
    player_score = 0
    computer_score = 0
    player_turns = True
    
    while True:
        if player_turns:
            print("\nPlayer's turn\n")
            player_result, quit_game = player_turn()
            player_score += player_result
            print("Player total score: is", player_score)
            if player_score >= 50:
                print("Player wins!")
                break
            if quit_game:
                print("\nGame ended by player\n")
                break
            player_turns = False
        else:
            print("\nComputer's turn\n")
            computer_result = computer_turn()
            computer_score += computer_result
            print("Computer total score: is", computer_score)
            if computer_score >= 50:
                print("Computer wins!")
                break
            player_turns = True
        
    print("Final scores: Player: {}, Computer: {}".format(player_score, computer_score))

if __name__ == "__main__":
    game()