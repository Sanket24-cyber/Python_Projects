
# Number Guessing game

number = 54
print("Welcome to the Number Guessing Game!")
print("* You have chosen a number between 1 and 100. *")
print("* You have 5 guesses to find the correct number. *")
#
for i in range(1, 6):
    print("\nGuess #", i)
    guess = int(input("Enter your guess: "))

    if 50 < guess < 54 or 55 < guess < 60:
        print("Too close!")
    elif guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!!")
    else:
        print(f"Congratulations! You guessed the correct number that is {number} in your {i}th guess!")
        break
else:
    print("\nGame over! You have used all your guesses.")
    print("The correct number was", number)
    