from hangman_art import *
from hangma_words import *

import random
print(logo)
print("\n")

choice = random.choice(words).lower()



blanks = []
for i in range(1,len(choice)+1):
    blanks.append('_')
lives = len(stages)
print(blanks)
while True:
    guess = input("Guess a letter: ")
    idx = 0
    for letter in choice:
        if letter == guess:
            blanks[idx] = letter
            print(blanks)
        idx+=1
    if guess not in blanks:
        lives-=1
        print(stages[lives])
    if '_' not in blanks:
        print("You Win")
        break
    if lives == 0:
        print("You Lose")
        break
print(f"The word was {choice}")