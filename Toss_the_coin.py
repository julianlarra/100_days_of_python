throw = input('''Hi, count up to three and push "P"\n THROW YOUR COIN ''').lower()
import random

if throw == "p":
    coin = random.randint(0, 1)

    if coin == 0:
        print("Head")

    elif coin == 1:
        print("Tails")
    print(coin)
    # elif coin == 1:
    # print("Tails")
else:
    input("Push P ")
