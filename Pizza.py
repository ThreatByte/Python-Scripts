print("Welcome to Chris Pizza")
pizza_size = input("What size of pizza do you want S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza Y or N ")
cheese = input("Do you want additional cheese Y or N ")

total_bill = 0
if pizza_size == "S":
    total_bill += 15
    if pepperoni == "Y":
        total_bill += 2
    if cheese == "Y":
        total_bill += 1

if pizza_size == "M":
    total_bill += 20
    if pepperoni == "Y":
        total_bill += 3
    if cheese == "Y":
        total_bill += 1

if pizza_size == "L":
    total_bill += 25
    if pepperoni == "Y":
        total_bill += 3
    if cheese == "Y":
        total_bill += 1

print(f"Your total bill is {total_bill}")