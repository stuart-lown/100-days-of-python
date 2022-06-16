# Simple Python program to split a restaurant bill (including tip)

# Print a program greeting
print("Welcome to the tip calculator.")

# Request user input for total bill amount, tip percent, number of people splitting the bill
total_bill = input("What was the total bill? $")
tip_pct = input("What percent would you like to give? 10, 12 or 15? ")
split_people_count = input("How many people to split the bill? ")

# Input data type conversion, from string to numerical types
total_bill = float(total_bill)
tip_pct = float(tip_pct)
split_people_count = int(split_people_count)

# Calculate the total per person: total * (1 + tip_pct / 100) / people
total_per_person = round(total_bill * (1.0 + tip_pct / 100) / split_people_count, 2)

# Print a descriptive message with the total per person
print(f"Each person should pay: ${total_per_person}")
