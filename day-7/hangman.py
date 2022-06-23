import random
from hangman_art import *
from hangman_words import *

# Toggle print debugging, set to False in production!
test = False

# Initialize the game until stopped
end_of_game = False

# List of secret words
word_list = word_list
if test:
    word_list = ["aardvark", "baboon", "camel"]

# Secret word chosen randomly from word_list
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

# Get the length of the word to create the display list
word_length = len(chosen_word)

# Set number of 'lives' - wrong guesses allowed
lives = 6

# Print the logo at the start of the game
print(logo + "\n")

# Create a list that holds blanks for secret word.
# This will be displayed to the console during gameplay.
display = []
for _ in range(word_length):
    display += "_"
print(display)

# Print secret word
if test:
    print(f'Pssst, the solution is {chosen_word}.')

# While there are un-guessed letters in display
while not end_of_game:
    # User guesses a letter
    guess = input("Guess a letter: ").lower()

    # Replace every blank in display with matching letter 
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Make the user try again if input is too long
    while len(guess) > 1:
        print("You can only guess one letter at a time. Try again.")
        guess = input("Guess a letter: ").lower()

    # Make the user try again if input not a letter
    while ord(guess) not in range(97, 123):
        print("Your guess must be a valid letter. Try again.")
        guess = input("Guess a letter: ").lower()

    # Print success message if guess is correct, else decrement lives by one
    if guess in chosen_word:
        print(f"There is at least one \"{guess}\".")
    else:
        print(f"Sorry, there is no \"{guess}\".")
        lives -= 1
        print(f"You have {lives} remaining attempts.")
        # If lives are gone, end the game and print Game Over
        if lives == 0:
            end_of_game = True
            print("You lose. Game Over.")

    # Print the current state of display as a string
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the ASCII hangman art for lives state
    print(stages[lives])