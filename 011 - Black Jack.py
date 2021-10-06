# Spyder Editor
# Created on Mon Oct  4 21:29:01 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 011 - Black Jack

from art011 import logo
import random

print(logo)

# Deck cards' values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_for_ace(cards):
    i = 0
    for card in cards:
        if card == 11 and sum(cards) > 21:
            cards[i] = 1
        i += 1
    return cards

def blackjack():
    your_cards = []
    dealer_cards = []
    
    # Add the first card
    your_cards.append(cards[random.randint(0, 12)])
    dealer_cards.append(cards[random.randint(0, 12)])
    # Add the second card for dealer
    dealer_cards.append(cards[random.randint(0, 12)])

    continue_adding = True
    bust = False
    black_jack = False
    
    # It adds next card to your cards untill it sums over 21 or the player says pass
    while continue_adding:
        # Adding next card
        your_cards.append(cards[random.randint(0, 12)])
        your_cards = check_for_ace(your_cards)
        your_score = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {your_score}\nComputer's first card: {dealer_cards[0]}")
        
        # over 21 or player stops deal
        if your_score > 20:
            continue_adding = False
            if your_score > 21:
                bust = True
            if your_score == 21:
                black_jack = True
        elif input("Type 'y' to get another card, type 'n' to pass: ") == 'n':
            continue_adding =  False
            
    # Adding dealer cards
    while sum(dealer_cards) < 17 and not bust and not black_jack:
        dealer_cards.append(cards[random.randint(0, 12)])
        dealer_cards = check_for_ace(dealer_cards)
    
    # Judgment
    result = ""
    y_score = sum(your_cards)
    d_score = sum(dealer_cards)
    if bust:
        result = "Bust! You lose :("
    elif y_score == d_score:
        result = "Push! No winner."
    elif y_score > d_score or d_score > 21:
        result = "You Win! :)"
    else:
        result = "You lose! :("
    
    # Result
    print(f"Your final hand: {your_cards}, final score: {y_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {d_score}")
    print(result)
    
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()

blackjack()