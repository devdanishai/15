# def main():
#     bill = float(input("Enter the bill amount: "))
#     tip = bill * 0.15
#     print(tip)

# main()
#######

# def main():
#     # Ask the user for the meal amount and convert it to a float
#     dollars = dollars_to_float(input("How much was the meal? "))
    
#     # Ask the user for the tip percentage and convert it to a float
#     percent = percent_to_float(input("What percentage would you like to tip? "))
    
#     # Calculate the tip
#     tip = dollars * percent
    
#     # Print the result formatted to 2 decimal places
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(n):
#     """
#     Convert a string like "$12.34" to a float 12.34
#     """
#     return float(n.replace("$", ""))  # remove the $ sign and convert


# def percent_to_float(n):
#     """
#     Convert a string like "15%" to a float 0.15
#     """
#     return float(n.replace("%", "")) / 100  # remove % and divide by 100


# # Run the program
# main()
################################





def percentage_to_float(p):
    x = float(p.replace("%", ""))
    x = x/100
    return x

def dollar_to_float(d):
    y = float(d.replace("$", ""))
    return y

def main():
    dollar = dollar_to_float(input("what is your bill in dollars? "))
    percent = percentage_to_float(input("what is tip rate?"))

    tip = dollar * percent
    print(f"leave tip of {tip:.2f}")
    # print(f"Leave ${tip:.2f}")

    

main()

# def percentage_to_float(p):
#     # Convert "15%" → 0.15
#     return float(p.replace("%", "")) / 100

# def dollar_to_float(d):
#     # Convert "$42.50" → 42.50
#     return float(d.replace("$", ""))

# def main():
#     dollar = dollar_to_float(input("What is your bill in dollars? "))
#     percent = percentage_to_float(input("What is the tip rate? "))
#     tip = dollar * percent
#     print(f"Leave ${tip:.2f}")

# main()
