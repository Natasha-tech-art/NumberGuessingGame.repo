import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100.")
    
    # This variable will store how many guesses the user gets
    attempts = 0