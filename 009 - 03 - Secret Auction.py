# Spyder Editor
# Created on Thu Sep 30 09:35:23 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 009 - 03 - Secret Auction

import os
from art00903 import logo

os.system('clear')
print(logo)
print("Welcome to the Secret Auction program")

bids = {}

def adding_bidder():
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if again == "yes":
        os.system('clear')
        adding_bidder()
        
adding_bidder()
# print(bids)

winner = {}
highest_bid = 0

# Check for the highest bid
for person in bids:
    bid = bids[person]
    if bid > highest_bid:
        highest_bid = bid
        winner = {}
        winner[person] = bid
    elif bid == highest_bid:
        winner[person] = bid
        
# print(winner)

# output
text = ""
if len(winner) > 1:
    text += "No winner!\n"
    value_of_bid = 0
    for person in winner:
        text += person + "\n"
        value_of_bid = winner[person]
    text += f"bid the same amount of ${value_of_bid}."   
else:
    for person in winner:
        text += f"The winner is {person} with ${winner[person]} bid."

print(text)