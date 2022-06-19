import os
import sys
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
bot_position = random.randint(0, 2)
bot_choice = choices[bot_position]

print("Let's start a new game of Rock, Paper, Scissors!")
user_input = input("Choose rock, paper, or scissors: ")

# Print respective ASCII art for user input
first_char = user_input[0].lower()
user_choice = ""
if first_char == "r":
    user_choice = rock
elif first_char == "p":
    user_choice = paper
elif first_char == "s":
    user_choice = scissors
else:
    print("That isn't a valid choice. Let's start over.")
    os.execl(sys.executable, sys.executable, *sys.argv)

print(user_input)
print(user_choice)
print(bot_choice)

if user_choice == bot_choice:
    print("It's a tie! Play again.")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif user_choice == rock and bot_choice == scissors:
    print("Rock beats Scissors, you win!")
elif user_choice == rock and bot_choice == paper:
    print("Paper covers Rock, you lose!")
elif user_choice == paper and bot_choice == rock:
    print("Paper covers Rock, you win!")
elif user_choice == paper and bot_choice == scissors:
    print("Scissors cuts Paper, you lose!")
elif user_choice == scissors and bot_choice == paper:
    print("Scissors cuts Paper, you win!")
elif user_choice == scissors and bot_choice == rock:
    print("Rock beats Scissors, you lose!")

replay = input("Do you want to play again? Type 'Y' for yes, any other key for no. ")
if replay.lower() == 'y':
    os.execl(sys.executable, sys.executable, *sys.argv)

