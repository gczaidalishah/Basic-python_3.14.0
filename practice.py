# import random

# secret = random.randint(1, 10)

# guess = int(input("Guess the number (1-10): "))

# if guess == secret:
#     print("Correct! 🎉")
# else:
#     print("Wrong! The number was", secret)
import random

secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Correct! You guessed in", attempts, "attempts")
        break