import random

try:
    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())
except FileNotFoundError:
    #If the file is not found, set the hiscore to a default value
    hiscore = float('inf') #inf = infinity

randNumber = random.randint(1,100)

userGuess = None
guesses = 0

while userGuess != randNumber:
    try:
        userGuess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    guesses += 1

    if userGuess == randNumber:
        print("You guessed it right!")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a larger number.")

print(f"You guessed the number in {guesses} guessed")

if guesses<hiscore:
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))