import random

target_number = random.randint(1, 100)
guess = 0

while guess != target_number:
    guess = int(input("Enter your guess: "))
    if guess > target_number:
        print("Too high! Try again.")
    elif guess < target_number:
        print("Too low! Try again.")

print("Congratulations! You guessed the correct number.")
