import random


words = ["Laptop" , "Rectangle", "Chair" ]
choice = random.choice(words).lower()
print(f"The word is {choice}")
guess = input("Guess a letter: ")

blanks = []
for i in range(1,len(choice)+1):
    blanks.append('_')

print(blanks)   
idx = 0
for letter in choice:
    if letter == guess:
        blanks[idx] = letter
    idx+=1
print(blanks)