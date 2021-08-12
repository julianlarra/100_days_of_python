# Leap year
# verifique si un año determinado  es bisiesto
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("it's a leap year ")

else:
    print("It's not a leap year")
