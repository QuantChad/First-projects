print("Welcome to the hardest game in the world!")

input("What is your name? ")
age = input("How old are you? ")

if int(age) < 16:
    print(" You are way too young to play, go back to roblox buddy! ")
else:
    cont = input(" Would you like to continue? (yes/no) ")
    if cont.lower() == "yes":
        print("Okay, Let's start the game!")
        choice = input("You are stranded on a deserted island. You have two choices: (1) search for food or (2) build a shelter. What do you choose? (1/2) ")
        if choice == "1":
            print("You found some berries, but they were poisonous! You died HAHA LOSER!")
        elif choice == "2":
            print("You built a shelter, and you survived the night! you are starving though, what do you do? (1) search for food or (2) wait for a rescue team. (1/2) ")
            choice = input()
            if choice == "1":
                print(" You found some rare slurpfish, you ate them and it tasted lowkey fire! You survived!")
            elif choice == "2":
                print(" You waited for a rescue team, but they never came. You died of starvation! HAHAH LOSER!")
            print("It's day 3 and you are still stranded on the island. Do you (1) try to find buried treasure or (2) try to signal for help? (1/2)")
            choice = input()
        if choice == "1":
            print(" You lowkey found some treasure, it was a flair gun! Lucky bastard!")
        elif choice == "2":
                print(" You signaled for help, but after hours and hours of waiting, no one came for you, you died of dehydration! lock bro")
        choice = print(" Where do you shoot the flair gun? (1) into the sky or (2) into the ocean? (1/2)")
        choice = input()
        if choice == "1":
                print(" you shot the flair gun into the sky, and it hit the heilicopter that was coming to rescue you! You died after the helicopter crashed into you!")
        elif choice == "2":
                print(" You shot the flair gun into the ocean, and it attracted the attention of the united states navy! They rescued you and forced you to join the navy! you are now a sailor!")
                print("Congratulations! You survived the hardest game in the world!")

