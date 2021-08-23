#rock paper or scissors
player=int(input('''Press:\n 1="Rock"\n 2="paper"\n 3="Scissors"\n '''))


rock = '''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_papper_scissors= [rock, paper, scissors]

print("You:")
user_int= int(player -1)
user=(rock_papper_scissors[user_int])
print(user)
import random
print("Rival:")
computer= int(random.randint(0, 2))
rival=print(rock_papper_scissors[computer])


if user_int == 0:
   if computer == 0:
     print("TIE")
   elif computer ==1:
       print("You lose")
   elif computer == 2 :
     print("You win!!!")
elif user_int == 1 :
    if computer == 0 :
      print("You win!!!")
    elif computer == 1:
      print("TIE")
    elif computer == 2:
      print("You lose")
elif user_int == 2:
    if computer == 0:
      print("You lose")
    elif computer == 1:
      print("You win!!!")
    elif computer == 2:
      print("TIE")