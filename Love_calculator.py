# Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1.lower()
name2.lower()
partner = name1.lower() + name2.lower()
true= partner.count("t" ) + partner.count("r") + partner.count("u") + partner.count("e")
love= partner.count("l") + partner.count("o") + partner.count("v") + partner.count("e")

true_love= int(str(true) +str(love))

if true_love < 10 or true_love > 90:
   print(f"Your score is {true_love} , you go together like coke and mentos.")
elif true_love >= 40 and true <=50:
  print(f"Your score is {true_love}, you are alright together.")
else :
  print(f"Your score is {true_love}.")