import random

def slot_choices():
    choice1 = random.choice(["seven", "gold bar", "cherry"])
    choice2 = random.choice(["gold bar", "cherry", "seven"])
    choice3 = random.choice(["cherry", "seven", "gold bar"])
    return f"{choice1} {choice2} {choice3}"

def slot_game():
    print("Welcome to the slot machine game! It costs only £10 to play for each go!")
    print("Here are the prizes: \n 3 cherry's: £500 \n 3 seven's: £1,000 \n 3 gold bars: £10,000")
    user_money = input("Enter how much you want to play with: ")
    
    score = int(user_money)
    
    playing = True
    while playing:
        play = slot_choices()
        print(play)
        
        if play == "cherry cherry cherry":
            score += 500
            print(f"Congratulations you win £500! Your total amount is £{score}")
            playing = False
            break
        elif play == "seven seven seven":
            score += 1000
            print(f"Congratulations you win £1,000! Your total amount is £{score}")
            playing = False
            break
        elif play == "gold bar gold bar gold bar":
            score += 10000
            print(f"Congratulations you win £10,000! Your total amount is £{score}")
            playing = False
            break
        else:
            score -= 10
            print(f"Sorry no wins this time! Your score is £{score}")
            
        if score <= 0:
            print("You have run out of money. Game over!")
            break
        
        continue_or_quit_game = input("Do you want to continue or quit the game? ").lower()
        if continue_or_quit_game == "continue":
            continue
        elif continue_or_quit_game == "quit":
            playing = False
            print(f"Your remaining withdrawn funds are £{score}")
        else:
            print("Invalid response, enter continue or quit")
            
slot_game()        
