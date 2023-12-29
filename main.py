import random
from art import logo
import os
def deal_card():
    """ Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # balckjack --> 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return " You lost :-( "
    if user_score == computer_score:
        return "Draw" # نه برنده نه بازنده
    elif computer_score == 0:
        return " You Lost, Computer has a blackjack"
    elif user_score == 0:
        return "You Won with a blackjack"
    elif user_score > 21:
        return "You Lost (more than 21 )"
    elif computer_score > 21:
        return "You won (computer score is more than 21)"
    elif user_score > computer_score:
        return "You Won :-)"
    else:
        return "You lost :-("
def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"your cards:{user_cards}, current score: {user_score}")
            print(f"computer first card :{computer_cards[0]}")
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

    while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score= calculate_score(computer_cards)
    print(f"Computer's final hand:{computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))
    print("--------------------------------------")

while input("Do you want to play black jack game? Type 'y' or 'n' ") == 'y':
    os.system('cls') # clear
    play_game()