import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    
    if guess.lower() == 'exit':
        print("Thanks for playing. Goodbye!")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Error. Please enter a valid number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break