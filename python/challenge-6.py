## Random number guessing
import random # import random library

secret_number = random.randint(1 , 100)

# Initialize guess count
guess_count = 0

print("Welcome to the Number Guessing Game!")
print("I've picked a random number between 1 and 100. Can you guess it?")

flag = True

while flag: # looping until true
    guess = input("Enter your guess (between 1 and 100): ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    guess_count += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")
        print(f"It took you {guess_count} guesses.")
        flag =False