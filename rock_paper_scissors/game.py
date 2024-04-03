import random

def computer_guess():
    choices = ['rock', 'paper', 'scissors']
    computer_guess = random.choice(choices)
    return computer_guess

def game():
    computer_score = 0
    user_score = 0
    while computer_score < 5 and user_score < 5:
        computer_choice = computer_guess()
        user_choice = input("Choose your weapon: ").lower()
        if user_choice == computer_choice:
            print(f"It's a draw! You both picked {user_choice}")
        elif (user_choice == "rock" and computer_choice == "paper" ) or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
            computer_score += 1
            print(f"You lost! {computer_choice} beats {user_choice}. Computer score: {computer_score}. User score: {user_score}.")
        elif (user_choice == "paper" and computer_choice == "rock" ) or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
            user_score += 1
            print(f"You win!, {user_choice} beats {computer_choice}. Computer score: {computer_score}. User score: {user_score}.")
        else:
            print("Invalid input! Please choose between rock, paper or scissors")
            
    if computer_score == 5:
        print("Sorry you lost, Computer wins!")
    else:
        print("Congratulations, you win! You have beat the Computer!")
            

if __name__ == "__main__":
    print("Welcome to rock, paper, scissors! Do you have what it takes to beat the computer?")
    game()
