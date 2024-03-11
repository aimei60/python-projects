import random

print("Guess the number!")

top_number = input("Enter a number for the maximum guess value: ")
    
if int(top_number) <= 0:
        print("Value entered is too small. Enter a value bigger than 0.")
        top_number = input("Enter a number for the maximum guess value: ")
        
if top_number.isdigit():
    number_to_guess = int(top_number)
    
number = random.randrange(1, number_to_guess)

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


