print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("You are at a crosroad. Where do you want to go? Type 'left' or 'right'")
choice = input()
if choice == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type swim to swim across")
    choice =  input()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which one do you choose?")
        choice = input()
        if choice == "blue":
            print("You entered the room of beasts. GAME OVER")
        elif choice  == "red":
            print("YOU FOUND THE TREASURE!!!")
        else:
            print("You entered the room of ghosts. GAME OVER")
    else:
        print("You were attacked by alligators. GAME OVER")
else:
    print("You fell into a hole. GAME OVER")