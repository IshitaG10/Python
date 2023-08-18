student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score>=91 and score<=100:
        student_grades[key] = "Outstanding"
    elif score>= 81 and score <=90:
        student_grades[key] = "Exceeds Expectations"
    elif score>= 71 and score <=80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)