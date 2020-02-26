# For Loops
for i in range(5):
    print("I will not chew gum in class.")

for i in range(5):
    print("Please,")
print("Can I go to the mall?")

for i in range(5):
    print("Please,")
    print("Can I go to the mall?")  

repetitions = int(input("How many times should I repeat? "))
for i in range(repetitions):
    print("I will not chew gum in class.")

# Write a function
def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class.")

def main():
    print_about_gum(10)

main()

# Printing numbers in a given range
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10):
    print(i + 1)

# Counting by numbers other than one
for i in range(2,12,2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

for i in range(10, 0, -1):
    print(i)

for i in [2,6,4,2,4,6,7,4]:
    print(i)

# Nesting Loops
for i in range(3):
    print("a")
for j in range(3):
    print("b")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")



# Number Guessing Game
"""
Random Number Guessing Game
"""
import random 

def main():
    print("""Hi! I'm thinking of a random number 
    between 1 and 100.
    """)
    secret_number = random.randrange(1, 101)
    user_attempt_number = 1
    user_guess = 0

    while user_guess != secret_number and user_attempt_number < 8:
        print("--- Attempt", user_attempt_number)
        user_input_text = input("""
        Guess what number I am thinking of: 
        """)
        user_guess = int(user_input_text)
 
        if user_guess > secret_number:
            print("Too high.")
        elif user_guess < secret_number:
            print("Too low.")
        else:
           print("You got it!")
    
        user_attempt_number += 1

    if user_guess != secret_number:
       print("""
       Aw, you ran out of tries. The number was
        " + str(secret_number) + "."
        """)

main()