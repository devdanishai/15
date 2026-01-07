# # Step 1: Define the function
# def list_sum(a, b, c):
#     answer = a + b + c
#     return answer  # return the value so we can use it outside

# # Step 2: Call the function with values from the list
# numbers = [4, 5, 6]
# result = list_sum(numbers[0], numbers[1], numbers[2])

# # Step 3: Print the result
# print(result)

#_________________________
# def say_hello():
#     print("hello world")


# say_hello()

#_________________________
# def add(a, b):
#     return a + b

# print(add(4, 5))


#_________________________
# def greet(name):
#     return f"hello, {name}, your token is expire"

# message = greet("ali")

# print(message)

#_________________________

# numbers = [10, 20, 30, 40, 50]
# total = 0

# for i in numbers:
#     total += i  # add i to total

# print(total)

#_____________________________
# s = 0.1 + 0.888888888888888888

# print(f'{s:.2f}')

# BOOK SOLUTION
def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output
print(mysum(10, 20, 30, 40))