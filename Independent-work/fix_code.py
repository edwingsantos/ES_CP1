#ES 1 fix game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0 # logic error, it will run an error if its 0. attempts += 1 is the better answer
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")  #This is not an interger so it will brake at line 19, becuase it shows as a string not an int, this is a runtime error. Fix by putting int()
        if attempts >= max_attempts:   #Logic error, how can something be grader than zero, correct is   if attempts <= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue # you dont need it, so just deleat it
    print("Game Over. Thanks for playing!")
start_game()
