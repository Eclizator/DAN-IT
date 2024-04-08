import random


def guess_number():

    secret_number = random.randint(1, 100)
    max_attempts = 5

    print("Welcome to the Guessing Game! Can you guess the secret number between 1 and 100?")

    for attempt in range(max_attempts):
        guess = int(input("Enter your guess: "))


        if guess == secret_number:
            print("Congratulations! You guessed the right number.")
            return


        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")



guess_number()