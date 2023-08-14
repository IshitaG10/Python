scores = input("Enter the scores of students: ").split(" ")
max = 0
print(scores)
for score in scores:
    temp = int(score)
    if max < temp:
        max = temp

print(max)