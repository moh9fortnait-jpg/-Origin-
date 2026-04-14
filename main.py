# Day 1: Mastering Input/Output
# A simple script to interact with the user

name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

# Converting input to integer to perform calculation
age = 2026 - int(birth_year)

print(f"Hello {name}, you are {age} years old.")
print("Logic check: Complete.")