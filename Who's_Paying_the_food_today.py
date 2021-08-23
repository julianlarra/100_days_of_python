#Who's Paying the food today?
names_string = input("Give me everybody's names, separated by a comma.\n insert name: ")
names = names_string.split(", ")


import random


num= random.randint(0, len(names)-1 )

pay_name= names[num]
print(f"{pay_name} is going to buy the meal today!")