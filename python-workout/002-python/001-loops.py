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

text = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:           # use a different variable, like char
    if char in vowels:      # check if the character is a vowel
        count += 1          # increase count by 1

print("Number of vowels:", count)
