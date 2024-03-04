#!/bin/bash

# Generate a random number between 1 and 100
correct_number=$(( (RANDOM % 100) + 1 ))

# Maximum number of attempts allowed
max_attempts=5

echo "Welcome to the Number Guessing Game!"
echo "Try to guess the number between 1 and 100. You have $max_attempts attempts."

# Loop for user attempts
for (( attempt=1; attempt<=$max_attempts; attempt++ )); do
    read -p "Enter your guess: " user_guess

    # Check if the guess is correct
    if (( user_guess == correct_number )); then
        echo "Congratulations! You guessed the right number ($correct_number)."
        exit 0
    else
        # Provide feedback and allow the user to guess again
        if (( user_guess > correct_number )); then
            echo "Too high! Try again."
        else
            echo "Too low! Try again."
        fi
    fi
done

# If all attempts are used without a correct guess
echo "Sorry, you've run out of attempts. The correct number was $correct_number."
exit 0
