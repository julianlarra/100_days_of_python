print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choise1= input('''You're at a cross road. Where do you want to go? Type "left" or "right" ''').lower()
if choise1 == "right":
  print("Fall into a hole...Game over. ")
elif choise1 == "left":
    choise2= input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ''').lower()
    if choise2 == "swim":
      print("Attaked by trout... Game over.")
    elif choise2 == "wait":
     choise3= input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
     if choise3 == "blue":
       print("You enter a room of beasts... Game over. ")
     if choise3 == "red":
        print("You got attacked by a angry trout ... Game over.")
     elif choise3 == "yellow":
        print("You found the treasure!\n You win")
     else:
       print("Game over.")
    else:
      print("Game over.")
else:
  print("Game over")