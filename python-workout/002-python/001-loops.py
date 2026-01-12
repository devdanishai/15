# 1: print 1 to 10
# for i in range(0,11):
#     print(i)

##############################
# 2: Sum of first 5 numbers
# total = 0

# for i in range(0,6):
#     total += i

# print(total)

##############################
# 3: Print only even numbers from 1 to 10

# for i in range(1, 11):
#     if i % 2 == 0:  # check if even
#         print(i)    # print only even numbers

##############################
# 4: print odd numbers till 10
# for i in range(1,11):

#     if i % 2 != 0:
#         print(i)

##############################
# 5: Print each character of a string
# x = "python"

# for i in x:
#     print(i)

##############################
# 6: ask for input and print each character
# x = input("enter word: ")

# for i in x:
#     print(i)

##############################
# 7: Count vowels in a string

# text = input("Enter a word: ")
# vowels = "aeiouAEIOU"
# count = 0

# for char in text:           # use a different variable, like char
#     if char in vowels:      # check if the character is a vowel
#         count += 1          # increase count by 1

# print("Number of vowels:", count)

#################################
# counter = 1
# limit = 5

# while counter <= limit:
#     print("Counter is:", counter)
#     counter += 1



# secret_num = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("guess: "))

#     guess_count += 1
#     if guess == secret_num:
#         print("u win !")
#         break

# counter = 0
# limit = 10

# while counter < limit:
#     counter += 1
#     print(counter)


# c = 10
# l = 0

# while c > l:
#     c -= 1
#     print (c)

# c = 0
# l = 10

# while c < l:
#     if c % 2 == 0:
#         print(c)
#     c += 1


# c = 0
# l = 5
# total = 0

# while c < l:
#      total += c
#      c += 1

# print(total)

#################################
# secret = 7
# counter = 0
# limit = 3

# while counter < limit:
#     guess = int(input("guess num: "))

#     if guess == secret:
#         print("u win")
#         break
#     else:
#         print("try again")

#     counter += 1   # ✅ Must be inside the loop

###############################
# secret = 8
# counter = 0
# limit = 3

# while counter < limit:
#     guess = int(input("guess: "))

#     if guess == secret:
#         print("u won!")
#         break
#     else:
#         remaining_attempts = limit - (counter + 1)
#         print(f"try again, u have {remaining_attempts} attempts")
#     counter += 1

############################
# mosh version
# guess_count = 0
# guess_limit = 3
# secret_number = 9 # Note: Ensure secret_number is defined elsewhere in your code

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')

##############################
# without limit version
# import random

# secret = random.randint(0, 10)

# while True:
#     guess = int(input("guess_num: "))

#     if guess == secret:
#         print("u won!")
#         break
#     elif guess > secret:
#         print("guess is high")
#     else:
#         print("guess is low")


