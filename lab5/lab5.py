def print_intro():
    print("Welcome to Camel!\n")
    print("In your desperation, you have stolen a camel to make your way")
    print("across the great Mobi desert.")
    print("The locals want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the locals.")

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_traveled = -20


def main():
    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        
        user_choice = input("Choice? ")
        if user_choice == "Q":
            done = True


    

    print_intro()

if __name__ == '__main__':
    main()

