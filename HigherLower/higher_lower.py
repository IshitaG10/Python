from art import *
from game_data import data
import random
import os


def choose_celebrity():
    return random.choice(data)


def compare(A,B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'


def game_play(A,B): 
    print(logo)
    score = 0
    while True:
        if score > 0:
            print(f"You're right! Current Score : {score}")
            B = choose_celebrity()
            if A==B:
                B = choose_celebrity()
        ans = compare(A,B)
        print(f"Compare A : {A['name']}, {A['description']}, {A['country']}")
        print(vs)
        print(f"Against B : {B['name']}, {B['description']}, {B['country']}")
        
        if input("Who has more followers? Type 'A' or 'B' : ").upper() == ans:
            score+=1
            A=B
            os.system('cls')
            os.system('cls')
            print(logo)
        else:
            print(f"Sorry, that's wrong. Final Score : {score}")
            break

A = choose_celebrity()
B = choose_celebrity()
game_play(A,B)