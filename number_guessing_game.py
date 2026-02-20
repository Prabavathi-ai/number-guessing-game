import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 50.")

secret_number = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it correctly!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over!")
    print("The correct number was:", secret_number)
