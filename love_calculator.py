name1 = input("What is your name?\n").lower()
name2 =  input("What is their name?\n").lower()
T = name1.count("t")+name2.count("t")
R = name1.count("r")+name2.count("r")
U = name1.count("u")+name2.count("u")
E = name1.count("e")+name2.count("e")

L = name1.count("l")+name2.count("l")
O = name1.count("o")+name2.count("o")
V = name1.count("v")+name2.count("v")
E = name1.count("e")+name2.count("e")

Lpercent = (T+R+U+E)*10 + (L+O+V+E)

if Lpercent<10 and Lpercent>90:
    print(f"Your score is {Lpercent}. You go together like coke and mentos.")
elif Lpercent>40 and Lpercent<50:
    print(f"Your score is {Lpercent}. You are alright together.")
else:
     print(f"Your score is {Lpercent}.")

