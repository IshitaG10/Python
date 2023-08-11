import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
generate = [rock,paper,scissors]

print("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors ")
choice = input()

if choice == '0':
    print(rock)
elif choice == '1':
    print(paper)
else:
    print(scissors)

print("Computer chose")
Comp_choice = str(random.randint(0,2))
if Comp_choice == '0':
    print(rock)
elif Comp_choice == '1':
    print(paper)
else:
    print(scissors)



if (choice == "0" and Comp_choice == "0") or (choice == "1" and Comp_choice == "1") or (choice == "2" and Comp_choice == "2"):
    print("It's a draw")

else:
    if choice == "0" and Comp_choice == "1":
        print("You Lose")
    
    elif choice == "0" and Comp_choice == "2":
        print("You Win")
    
    elif choice  == "1" and Comp_choice =="2":
        print("You Lose")
    
    elif choice == "1" and Comp_choice == "0":
        print("You Win")

    elif choice == "2" and Comp_choice == "0":
        print("You Lose")

    else:
        print("YOu Lose")




