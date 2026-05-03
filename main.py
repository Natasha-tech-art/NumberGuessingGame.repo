import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100.")
    
    # This variable will store how many guesses the user gets
    attempts = 0
    
    # Choose difficulty
    level = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower()
    
    if level == 'easy':
        attempts = 10
    elif level == 'medium':
        attempts = 7
    else:
        attempts = 5
        
    guess = 0
    while guess != secret_number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        # Take the user's input
        guess = int(input("Make a guess: "))

        # Check the guess
        if guess > secret_number:
            print("Too high.")
            attempts -= 1
        elif guess < secret_number:
            print("Too low.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {secret_number}.")

    if attempts == 0:
        print("You've run out of guesses, you lose.")

# Start the game
play_game()  