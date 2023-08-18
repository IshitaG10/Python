import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}
print(logo)
while True:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    repeat = input("Are there any other bidders? Type 'yes' or 'no'")
    if repeat == "yes":
        os.system('cls')
    else:
        os.system('cls')
        max_bid = 0
        bid_name = ""
        for key in bidders:
            bid = bidders[key]
            if bid > max_bid:
                max_bid = bidders[key]
                bid_name= key
        print(f"The winner is {bid_name} with a bid of ${max_bid}")
        break