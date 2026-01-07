

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

for i in camel:
    if i.isupper():
        snake += "_" + i.lower()
    else:
        snake += i

print("snake_case:", snake)