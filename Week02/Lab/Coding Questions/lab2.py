# Lab Week 2: Periodic Table Guessing Game
import random

# Define the elements array
elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]

# Randomly select an element
randomElement = random.choice(elements)

attempts = 0
isCorrect = False
while(attempts < 3):
    # Prompt the user to guess (to be completed)
    guessElement = input(f"Attempt {attempts + 1}: Guess the element: ")
    guessElement = guessElement.replace(" ", "").lower()

    if(guessElement.isnumeric() or guessElement == ""):
        print("Error: Invalid input. Please enter an element.")
        continue

    # Compare guess to the random element (to be completed)
    if (guessElement == randomElement.lower()):
        print(f"Correct! The element was {randomElement}.")
        if (guessElement == "hydrogen"):
            print("Hydrogen is the lightest element in the universe.")
        elif (guessElement == "helium"):
            print("Helium is commonly used in balloons.")
        elif (guessElement == "lithium"):
            print("Lithium floats on water.")
        elif (guessElement == "beryllium"):
            print("Beryllium is one of the most lightest metals.")
        elif (guessElement == "boron"):
            print("Boron is the second hardest element in its crystal form.")
        elif (guessElement == "carbon"):
            print("Diamonds are made up of carbon.")
        elif (guessElement == "nitrogen"):
            print("Nitrogen is colourless, odorless, and tasteless.")
        elif (guessElement == "oxygen"):
            print("Oxygen is pale blue in its liquid or solid form.")
        elif (guessElement == "fluorine"):
            print("Fluorine is the most chemically reactive element.")
        else:
            print("Neon is used in television sets and lasers.")
        isCorrect = True
        break
    else:
        attempts += 1
        print(f"Try again! The element starts with {randomElement[0].upper()}.")

if(not isCorrect):
    print(f"The correct element was {randomElement}.")