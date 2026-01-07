# import random

# def guessing_game():
#     answer = random.randint(0, 100)

#     while True:
#         user_guess = int(input("What is your guess? "))

#         if user_guess == answer:
#             print(f"Right! The answer is {user_guess}")
#             break
#         elif user_guess < answer:
#             print(f"Your guess of {user_guess} is too low!")
#         else:
#             print(f"Your guess of {user_guess} is too high!")

# guessing_game()

#########################
# # Step 1: Choose a secret number
# secret_number = 7  # could also use random.randint(1, 10)

# # Step 2: Ask the player for a guess
# guess = int(input("Guess a number: "))

# # Step 3: Repeat until guess is correct
# while guess != secret_number:
#     if guess < secret_number:
#         print("Too low!")
#     else:
#         print("Too high!")
#     # Ask for another guess
#     guess = int(input("Guess again: "))

# # Step 4: Congratulate the player
# print("Congratulations! You guessed it!")
#########################
# import random
# secret_num  = random.randint(0, 100)
# guess = int(input("enter any number:  "))

# while guess != secret_num:
#     if guess < secret_num:
#         print("too low")
#     else:
#         print("too high")
#     guess = int(input("guess again: "))

# print("ur guess is right: ")
########################
# import random
# def guess_game():
#     secret = random.randint(0,50)

#     while True:
#         guess = int(input("guess secret:   "))
        
#         if guess == secret:
#             print("you win")
#             break
#         elif guess < secret:
#             print("too low")
#         else:
#             print("too high")

# guess_game()

##########################
# import random

# def guess_game():
#     secret = random.randint(0, 50)
#     attempts = 0

#     while True:
#         guess = int(input("enter ur guess:  "))
#         attempts += 1

#         if guess == secret:
#             print("u win")
#             break
#         elif guess < secret:
#             print("too low")
#         else:
#             print("too high")

# guess_game()

#######################

import random

def guess_game():
    secret = random.randint(0, 50)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input("enter ur guess:  "))
        attempts += 1
    
        if guess == secret:
            print(f"u win in {attempts} attempts")
            break
        elif guess < secret:
            print(f"guess too low, u have {max_attempts - attempts} attempts")
        else:
            print(f"guess too high, u have {max_attempts - attempts} attempts")
    else:
        print(f"u lost. the answer is {secret}")


guess_game()