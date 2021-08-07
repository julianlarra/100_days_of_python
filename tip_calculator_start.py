print("Welcome to the tip calculator")
bill = float(input("What was the total bill "))
tip = int(input("What percentage tip would ypu like to give? 10, 12 or 15 "))
how_many_peoples = int(input("How many people to split the bill "))
tip_percentage = (tip / 100) + 1
result = float(bill * tip_percentage / how_many_peoples)

print(f"Each person should pay: {result}")
