# # TAKE INPUT
# user_input = input("enter numbers and expression then number: ")

# # make parts
# parts = user_input.split(" ")

# # convert string to floats
# num1 = float(parts[0])
# operator = parts[1]
# num2 = float(parts[2])

# # Compute the result
# if operator == "+":
#     results = num1 + num2
# elif operator == "-":
#     results = num1 - num2
# elif operator == "*":
#     results = num1 * num2
# elif operator == "/":
#     results = num1 / num2
# else:
#     results = "invalid operators"

# print(results)

############

# take user input
user_input = input("enter digits and operator like 2 + 2: ")

# split input into parts
parts = user_input.split(" ")

# convert parts into numbers and operator
a = float(parts[0])
op = parts[1]
b = float(parts[2])

# compute result
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("invalid operator")
