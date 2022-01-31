import random

numbrer_computer = random.randint(1, 100)
# print(numbrer_computer)

difficulty = input(
    "Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.\n Choose a difficulty. Type 'easy' or 'hard': ")
user_number = 0

if difficulty == "easy":
    tries = 10
    print("You have 10 attempts remaining to guess the number.")
if difficulty == "hard":
    tries = 5
    print("You have 5 attempts remaining to guess the number.")


def start_game(tries):
    for user in range(tries):
        user_number = int(input("Make a guess: "))
        if user_number == numbrer_computer:
            print("you win")
            return
        elif user_number < numbrer_computer:
            print(f"Too low.")

        elif user_number > numbrer_computer:
            print(f"Too high.")

        tries -= 1
        if tries >= 1:
            print(f" Guess again.\n You have {tries} attempts remaining to guess the number.")
    print("You've run out of guesses, you lose.")


start_game(tries)

