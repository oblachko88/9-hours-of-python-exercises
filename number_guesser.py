import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number that is greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()
    

# int('25') -> 25
# int('Hello') -> Error

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

if guesses == 1:
    print("You tried to guess it", guesses, "time.")
else: 
    print("You tried to guess it", guesses, "times.")
    
    