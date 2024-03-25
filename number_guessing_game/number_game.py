import random
print("Guess the number game!")

def numbers():
    top_number = input("Enter a number for the maximum guess value: ")
    if not top_number.isdigit() or int(top_number) <= 0:
        print("Incorrect value, please enter a number bigger than 0")
        top_number = input("Enter a number for the maximum guess value: ")
  
    number_to_guess = int(top_number)
    number = random.randrange(1, number_to_guess + 1)
    return number
       
def game():
    user_guess = int(input("Enter a guess: "))
    guess = 0
    while user_guess != number:
        if user_guess > number:
            print("Your number is too high, guess again!")
            user_guess = int(input("Enter a guess: "))
            guess += 1
        elif user_guess < number:
            print("Your number is too low, guess again!")
            user_guess = int(input("Enter a guess: "))
            guess += 1
    if user_guess == number:
            guess += 1
            print("You guessed correct! You guessed in", guess, "guesses!")

number = numbers()
game()


