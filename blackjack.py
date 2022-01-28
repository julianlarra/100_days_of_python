print("Welcome to the game of Blackjack")
# import ###
import random

# variables and list ###
user_cards = []
computer_cards = []
end_user_score = 0
# user_score = 0
computer_score = 0
other_card = ""
new_user_score = 0


# funciones ###

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def first_hard():
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f" Your cards are: {user_cards}")


def calculate_score(lista):
    score = sum(lista)
    return score


def blackjack():
    if calculate_score(user_cards) == 21 and calculate_score(computer_cards) == 21:
        print("Tie")
        exit()
    elif calculate_score(user_cards) == 21:
        print("Blackjack you win!")
        exit()
    elif calculate_score(computer_cards) == 21:
        print(F"The Dealar wins! blackjack, his cards are: {computer_cards}")
        exit()


def new_cards():
    other_card = input("Request other card? Type 'y' or 'n' ")
    if other_card == 'y':
        user_cards.append(deal_card())
        print(calculate_score(user_cards))
        print(f" Your cards are: {user_cards}")
        return True

    if other_card == 'n':
        end_user_score = calculate_score(user_cards)
        print(f"Your end score is: {end_user_score}")
        return False
        #  agregar "Enter a valid option"


def older_tan_21(score):  # calculate_score()

    if score > 21:
        if 11 not in user_cards:
            print('its older than 21 and there is no 11 in the cards. \n GAME OVER')
            exit()
        print("'It's over 21 and they have an As")
        as_for_one(user_cards)
        print("Replace the value 11 of the As by 1")
        print(f"Your cards are: {user_cards}")
        older_tan_21(calculate_score(user_cards))
    if score == 21:
        min_score_dealer()
    if score < 21:
        more_cards = new_cards()
        if more_cards:
            older_tan_21(calculate_score(user_cards))
        else:
            return False
        # print(calculate_score(user_cards))


def as_for_one(list, ):
    # while older_tan_21 is True:
    if 11 in list:
        print('there is an 11')
        list.remove(11)
        list.append(1)
        print(calculate_score(list))

    # croupier###


def min_score_dealer():
    print(f"The dealer have :{calculate_score(computer_cards)} points and his cards are:{computer_cards}")
    if calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
        min_score_dealer()
        # print(calculate_score(computer_cards), computer_cards)
        # min_score_dealer()
    if calculate_score(computer_cards) > 21:

        if 11 not in computer_cards:
            print(f"The dealer has more than 21 points. You wins\n his cards are: {computer_cards}")
            exit()

        as_for_one(computer_cards)
        print("Replace the value 11 of the As by 1")
        print(computer_cards)
        min_score_dealer()
    else:
        return True


######### ejecutar #########################

# dar la primer mano
first_hard()
# Calcular puntaje de jugador
user_score = calculate_score(user_cards)
# calcular puntaje de dealer
computer_score = calculate_score(computer_cards)
# comprobar si alguno de los dos jugadores tienen blackjack
blackjack()

# preguntar al jugador si quiere una nueva carta

# new_cards()

# user_score = calculate_score(user_cards)

# print(calculate_score(user_cards))
older_tan_21(calculate_score(user_cards))

min_score_dealer()

if calculate_score(user_cards) == calculate_score(computer_cards):
    print("Tie")
    exit()
elif calculate_score(user_cards) == 21:
    print("Blackjack you win!")
    exit()
elif calculate_score(computer_cards) == 21:
    print(F"The Dealar wins! blackjack, his cards are: {computer_cards}")
    exit()
elif calculate_score(user_cards) > calculate_score(computer_cards):
    print("Blackjack you win!")
elif calculate_score(user_cards) < calculate_score(computer_cards):
    print(F"The Dealar wins! blackjack, his cards are: {computer_cards}")