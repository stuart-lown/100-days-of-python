import os
from auction_art import *
#HINT: You can call clear() to clear the output in the console.

bid_record = {}

more_users = "y"
while more_users == "y":
  print(logo)
  name = input("What is your name? ")
  bid_price = input("What is your bid price? $")
  bid_record[name] = int(bid_price)
  more_users = input("Would you like to add another bidder? Type y/n ").lower()
  os.system('clear')

highest_bid = 0
winner = ""
for k, v in bid_record.items():
  if v > highest_bid:
    highest_bid = v
    winner = k

print(f"The winning bidder is {winner} with a bid of ${highest_bid}.")