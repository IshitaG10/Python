import random
names = input("Enter everyone's name: ")
name_list = names.split(", ")
index = random.randint(0,len(name_list)-1)
print(f"{name_list[index]} will pay the bill.")