rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer = random.randint(0, 2)

if computer == 0:
    print(f"the machine chooses:\n  {rock}\n Rock")
elif computer == 1:
    print(f"the machine chooses:\n  {paper}\nPaper")
elif computer == 2:
    print(f"the machine chooses:\n{scissors}\nScissors")

else:
    print("error")

if user == 0:
    print(f"you choose:\n{rock}\n Rock")
elif user == 1:
    print(f"you choose:\n{paper}\nPaper")
elif user == 2:
    print(f"you choose:\n{scissors}\nScissors")

if user == 0 and computer == 2:
    print("you win!")
elif user == 0 and computer == 1:
    print("You lose!")
elif user == 1 and computer == 0:
    print("You win!")
elif user == 1 and computer == 2:
    print("You lose!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user == 2 and computer == 1:
    print("You win!")
elif user == computer:
    print("They have tied, repeat the game. Please!")
elif user != 0 or 1 or 2:
    print("invalid option!")