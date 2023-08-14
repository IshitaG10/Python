import random


words = ["Laptop" , "Rectangle", "Chair" ]
choice = random.choice(words).lower()
print(f"The word is {choice}")


blanks = []
for i in range(1,len(choice)+1):
    blanks.append('_')

while True:
    guess = input("Guess a letter: ")
    idx = 0
    for letter in choice:
        if letter == guess:
            blanks[idx] = letter
            print(blanks)
        idx+=1
    if '_' not in blanks:
        print("You Win")
        break
