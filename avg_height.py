heights = input("Enter the height of students: ").split(" ")
size = len(heights)
avg = 0
for height in heights:
    avg+= int(height)

print(round(avg/size,2))