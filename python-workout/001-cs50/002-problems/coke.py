


# # solution without loop (just for understanding)
# amount_due = 50

# coin1 = int(input("Insert Coin 1: "))
# if coin1 in [25, 10, 5]:
#     amount_due -= coin1

# coin2 = int(input("Insert Coin 2: "))
# if coin2 in [25, 10, 5]:
#     amount_due -= coin2

# coin3 = int(input("Insert Coin 3: "))
# if coin3 in [25, 10, 5]:
#     amount_due -= coin3

# coin4 = int(input("Insert Coin 4: "))
# if coin4 in [25, 10, 5]:
#     amount_due -= coin4

# coin5 = int(input("Insert Coin 5: "))
# if coin5 in [25, 10, 5]:
#     amount_due -= coin5

# change_owed = abs(amount_due)
# print("Change Owed:", change_owed)
#####################################
# without denominations solution:

# amount_due = 50

# while amount_due > 0:
#     print("Amount Due:", amount_due)
#     coin = int(input("Insert Coin: "))
#     amount_due -= coin

# change_owed = abs(amount_due)
# print("Change Owed:", change_owed)

#####################################

### countdown while loop
# counter = 10
# while counter > 0:
#     print("counter:", counter)
#     counter -= 1  # ← YOU'RE MISSING THIS!

# print("Time's up!")

######################################

### password loop
# password = "python123"
# attempt = 3

# while attempt > 0:
#     user_input = input("Give password: ")  # ← ASK HERE!
    
#     if user_input == password:
#         print("Access granted!")
#         break  # Exit loop if correct
#     else:
#         attempt -= 1
#         print(f"Wrong! {attempt} attempts left")

# if attempt == 0:
#     print("Your account locked")

##########################################

### piggy bank
# goal = 100
# savings = 0

# while savings < goal:
#     deposit = int(input("Enter deposit amount: "))
#     savings += deposit  # ADD to savings
    
#     if savings >= goal:
#         print("Goal achieved!")
#         print(f"Total saved: ${savings}")
#     else:
#         needed = goal - savings
#         print(f"Need ${needed} more")

###########################
### piggy bank (without telling remaining target)
# goal = 100
# savings = 0  # Piggy bank starts empty

# while savings < goal:  # Keep going until we reach goal
#     deposit = int(input("Add money: "))  # How much to add?
#     savings = savings + deposit  # ADD to piggy bank
#     print(f"Piggy bank now has: ${savings}")  # Show current amount

# print("Goal reached!")

############################################


### coke.py solution
amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin

change_owed = abs(amount_due)
print("Change Owed:", change_owed)

