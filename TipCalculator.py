print("Welcome to Tip Calculator")
bill = float(input("What was your total bill $ "))
tip = int(input("How much tip would like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
total_bill = tip / 100 + bill + bill
total_bill_rounded = round(total_bill, 2)
print(f"Your total bill is {total_bill_rounded}")