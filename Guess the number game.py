import random 

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Press Q for Quit: ")
    if userChoice == "Q":
        break
    
    userChoice = int(userChoice)
    if userChoice == target:
        print("Congratulations! You guessed the correct number.")
        break
    elif userChoice < target:
        print("Too small. Take a bigger guess.")
    else:
        print("Too large. Take a smaller guess.")

print("Game over!")

input("\nPress Enter to exit...")
