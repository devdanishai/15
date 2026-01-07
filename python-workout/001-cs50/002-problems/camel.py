

##########################

# for i in range(0,8):
#     print(i)

##########################

# word = "hello"

# for letter in word:
#     print(letter)

#########################
# total = 0
# for i in range(1,11):
#     total += i
    
# print(total)

########################

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

########################

camel = input("camelCase: ")
snake = ""

for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char

print("snake_case:", snake)