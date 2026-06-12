import random

print("=== Number Guessing Game ===")

secret_number = random.randint(1, 50)
attempts = 0

while True:

    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    if guess == secret_number:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too Low. Try Again.")

    else:
        print("Too High. Try Again.")
