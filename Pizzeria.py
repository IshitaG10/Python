size = input("What size of pizza do you want?L, M or S ")
if size == "L":
    bill = 25
    add_pepproni =  input("Do you want pepproni? Y or N ")
    if add_pepproni == "Y":
        bill+=3

elif size == "M":
    bill = 20
    add_pepproni =  input("Do you want pepproni? Y or N ")
    if add_pepproni == "Y":
        bill+=3

else:
    bill = 15
    add_pepproni =  input("Do you want pepproni? Y or N ")
    if add_pepproni == "Y":
        bill+=2

extra_cheese =  input("Do you want extra cheese? Y or N ")

if extra_cheese == "Y":
    bill+=1
    print(f"Your final bill is: ${bill}")
else:
    print(f"Your final bill is: ${bill}")
