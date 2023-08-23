from menu import *

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def payment(cost):
    global profit
    quarters = int(input("How many quarters? : "))*0.25
    dimes = int(input("How many dimes? : "))*0.10
    nickel = int(input("How many nickel? : "))*0.05
    penny = int(input("How many dimes? : "))*0.01
    total = quarters + dimes + nickel + penny
    if total >= cost:
        profit = cost
        print(f"Here is ${round(total-cost,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        print(f"money : ${profit}")
    else:
        type = MENU[choice]
        ingredients = type["ingredients"]
        if check_resources(ingredients):
            print(f'Your bill : ${type["cost"]} ')
            if payment(type["cost"]):
                for item in ingredients:
                   resources[item]-= ingredients[item]
                print(f"Enjoy your {choice}.")
        
