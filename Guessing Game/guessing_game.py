from art import logo
import random
print(logo)

def guess(num,attempt):
    while attempt>0:
        print(f"You have {attempt} remaining. Guess the number")
        guess_num = int(input("Make a guess: "))
        attempt-=1
        if attempt>0:
            if guess_num == num:
                print(f"You got it. The answer was {num}")
                break
            
            elif guess_num < num:
                print("Too low.")
                print("Guess again.")
            
            else:
                print("Too high.")
                print("Guess again.")
    
    print("You used all your attempts. You lose")

print("Welcome to the gussing game.")
print("I am thinking of a number between 1 and 100")
num = random.randint(1,100)
print(num)
if input("Choose the level of difficulty. Type 'easy' or 'hard': ") == "easy":
    guess(num,10)

else:
    guess(num,5)