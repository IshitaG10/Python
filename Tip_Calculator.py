bill = float(input("What is your total bill?"))
percent = int(input("What percentage tip would you like to give? 10 or 12 or 15 "))/100
split = int(input("How many people to split the bill?"))
tip = (percent * bill)/split
payment =  round((bill/split) + tip,2)
print(f"Each person should pay: {payment}")