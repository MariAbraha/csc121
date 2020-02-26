<<<<<<< HEAD
import random

=======
>>>>>>> 4392693b7577cfcfaffcc3fc37df081f94d7dd44
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
<<<<<<< HEAD
drinks_in_canteen = 3


def main():
    print_intro()

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_traveled = -20
    drinks_in_canteen = 3
    done = False

=======


def main():
    done = False
>>>>>>> 4392693b7577cfcfaffcc3fc37df081f94d7dd44
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        
        user_choice = input("Choice? ")
<<<<<<< HEAD
        user_choice = user_choice.lower()
        if user_choice == "q":
            done = True
        
        elif user_choice == "e":
            #status check
            print(f"Miles traveled: {miles_traveled}")
            print(f"Drinks in canteen: {drinks_in_canteen}")
            print("The locals are {} miles behind you.".format(
                -distance_traveled
                )
            )

        elif user_choice == "d":
            #stop for the night
            camel_tiredness = 0
            print("The camel is happy!")
            distance_traveled += random.randrange(7, 15)

        elif user_choice == "c":
            #Full speed
            miles_traveled += random.randrange(10, 21)
            print(f"You've traveled {miles_traveled} miles.")
            thirst += 1
            camel_tiredness += random.randrange(1, 3) 
            distance_traveled += random.randrange(7, 15) 
            if random.randrange(20) == 0:
                oasis = True

        elif user_choice == "b":
            #Moderate speed
            miles_traveled += random.randrange(5, 13)
            print(f"You've traveled {miles_traveled} miles.")
            thirst += 1
            camel_tiredness += 1
            distance_traveled += random.randrange(7, 15)

        elif user_choice == "a":
            #Drink from the canteen
            if drinks_in_canteen >= 1:
                drinks_in_canteen -= 1
                thirst = 0
                print("You drank from the canteen.")

            else:
                print("You don't have any drinks!")

        if thirst > 4:
            print("You are thirsty.")

        elif thirst > 6:
            print("You died of thirst!")
            done = True

        if camel_tiredness > 5:
            print("Your camek is getting tired.")

        elif camel_tiredness > 8:
            print("Your camel is dead.")

        elif miles_traveled <= distance_traveled:
            print("""
            The locals caught you.
            You are dead!
            """)
            done = True
            
        elif distance_traveled < miles_traveled - 15:
            print ("The locals are getting close!")

        if oasis == True:
                print("You've found an oasis!")
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0

        
        elif miles_traveled >= 200:
            print("""
            You won!
            Thank you for playing!
            """)
            done = True
=======
        if user_choice == "Q":
            done = True


    

    print_intro()
>>>>>>> 4392693b7577cfcfaffcc3fc37df081f94d7dd44

if __name__ == '__main__':
    main()

