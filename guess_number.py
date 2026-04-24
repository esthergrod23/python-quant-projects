import random

number = random.randint(1, 10)

attempts = 3

print("Guess a number between 1 and 10")

for i in range(attempts):
    guess = int(input("Your guess: "))

    if guess == number:
        print("Correct! You guessed it!")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

if guess != number:
    print("You lost. The number was", number)
