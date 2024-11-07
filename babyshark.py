def start_game():
    print("Welcome to the Baby Shark Game!")
    print("You will meet the shark family!")
    print("Let's begin!")

    first_choice()

def first_choice():
    print("\nYou're in the ocean! What would you like to do?")
    print("1. Swim forward")
    print("2. Dive deeper")
    
    choice = input("Choose 1 or 2: ")
    
    if choice == '1':
        encounter_baby_shark()
    elif choice == '2':
        encounter_mommy_shark()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def encounter_baby_shark():
    print("\nYou swam forward and encountered Baby Shark!")
    print("Baby Shark starts singing, 'Baby Shark, doo doo doo doo doo doo!'")
    next_step()

def encounter_mommy_shark():
    print("\nYou dove deeper and found Mommy Shark!")
    print("Mommy Shark says, 'Let's find Daddy Shark!'")
    next_step()

def next_step():
    print("\nWhat would you like to do next?")
    print("1. Keep swimming")
    print("2. Go back up")
    
    choice = input("Choose 1 or 2: ")
    
    if choice == '1':
        encounter_daddy_shark()
    elif choice == '2':
        print("You go back up to the surface and see the sun shining.")
        first_choice()
    else:
        print("Invalid choice. Please try again.")
        next_step()

def encounter_daddy_shark():
    print("\nYou found Daddy Shark!")
    print("Daddy Shark says, 'Let's go find Grandma Shark!'")
    final_step()

def final_step():
    print("\nWhat do you want to do now?")
    print("1. Continue the adventure")
    print("2. End the game")
    
    choice = input("Choose 1 or 2: ")
    
    if choice == '1':
        encounter_grandma_shark()
    elif choice == '2':
        print("Thanks for playing the Baby Shark Game!")
    else:
        print("Invalid choice. Please try again.")
        final_step()

def encounter_grandma_shark():
    print("\nYou found Grandma Shark!")
    print("Grandma Shark says, 'You're now part of the shark family!'")
    print("Congratulations! You've completed the Baby Shark adventure!")
    
# Start the game
start_game()
