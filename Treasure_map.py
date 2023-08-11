row1 = ["😑","🫠","👺"]
row2 =["🤓","😹","😈"]
row3 = ["👻","🎃","😴"]
treasure  = [row1,row2,row3]
print(treasure)
position = input("Enter the position : ")
position = position.split(" ")
treasure[int(position[0])][int(position[1])] = "x"
print(treasure)