import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy-password as a list
# password = ""
# for n in range(0,nr_letters):
#     index = random.randint(1,len(letters)-1)
#     password += letters[index]

# for n in range(0,nr_symbols):
#     index = random.randint(1,len(symbols)-1)
#     password += symbols[index]

# for n in range(0,nr_numbers):
#     index = random.randint(1,len(numbers)-1)
#     password+=numbers[index]

# print(password)

#hard-password as a list
password = []
for n in range(1,nr_letters+1):
   password += random.choice(letters)

for n in range(1,nr_symbols+1):
    password += random.choice(symbols)

for n in range(1,nr_numbers+1):
    password += random.choice(numbers)
random.shuffle(password)
new_password = ""
for n in range(0,len(password)):
    new_password+=password[n]

print(new_password)
