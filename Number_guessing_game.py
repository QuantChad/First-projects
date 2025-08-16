import numpy

print(" Welcome to the *best* number guessing game in the world!")

input("What is your name? ")

age = input(" How old are you? ") 
if int(age) < 16:
    print(" You are too young to play")
else:
    cont = input(" Would you like to continue? (yes/no) ")
    if cont.lower() == "yes":
        print("Okay, buckle up, it's time for the number game!")
        print("You have 3 chances to guess the number I'm thinking of between 1 and 20. Guessing wrong will not blow up your new car, I hope.")
        number = numpy.random.randint(1, 21)
        attempts = 0
        while attempts < 3:
            while True:
                choice = input("Enter your guess (1-20): ")
                if not choice.isdigit():
                    print("Please enter a valid number!")
                    continue
                guess = int(choice)
                if guess < 1 or guess > 20:
                    print("You have to guess a number between 1 and 20, try again!")
                else:
                    break  # Valid guess, exit inner loop
            if guess == number:
                print("Perfect, you just barely avoided a car explosion!")
                break
            else:
                attempts += 1
                if attempts < 3:
                    print(f"You guessed wrong, you have {3 - attempts} attempts left.")
                else:
                    print("You have used all your chances, your car has blown up!!! BOOOM BOOM!")
                    print("The number was", number)
    elif cont.lower() == "no":
        print("Bruh, why did you even start the game then?")








