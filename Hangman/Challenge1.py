import random
words = ["Laptop" , "Rectangle", "Chair" ]
choice = random.choice(words).lower()
guess = input("Guess a letter: ")

for letter in choice:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")