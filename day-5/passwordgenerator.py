#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# letter_string = ""
# number_string = ""
# symbol_string = ""

# easy_password = ""

# for n in range(nr_letters):
#     rand = random.randint(0, 52)
#     letter_string += letters[rand]
# easy_password += letter_string

# for n in range(nr_numbers):
#     rand = random.randint(0, 9)
#     number_string += numbers[rand]
# easy_password += number_string

# for n in range(nr_symbols):
#     rand = random.randint(0, 9)
#     symbol_string += symbols[rand]
# easy_password += symbol_string

# print(f"The easy password is: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Initialize an empty string for each character list
letter_string = ""
number_string = ""
symbol_string = ""

# Initialize an empty list for all chosen characters
char_list = []

# Initialize an empty string for the final password
hard_password = ""

# Randomly pick the user-specified number of letters
for n in range(nr_letters):
    rand = random.randint(0, len(letters)-1)
    # Add each randomly-picked letter to the char_list
    char_list.append(letters[rand])

# Randomly pick the user-specified number of numbers
for n in range(nr_numbers):
    rand = random.randint(0, len(numbers)-1)
    # Add each randomly-picked number to the char_list
    char_list.append(numbers[rand])

# Randomly pick the user-specified number of symbols
for n in range(nr_symbols):
    rand = random.randint(0, len(symbols)-1)
    # Add each randomly-picked symbol to the char_list
    char_list.append(symbols[rand])

# Empty the characters in char_list into hard_password string, at random
while len(char_list) > 0:
    # For the characters still remaining in the char_list
    for n in range(len(char_list)):
        # Pick a random index of the remaining char_list
        rand = random.randint(0, len(char_list)-1)
        # Add the randomly-picked character to the password string
        hard_password += char_list[rand]
        # Delete the character, preventing repetition and infinite loop
        del char_list[rand]

print(f"The hard password is: {hard_password}")

