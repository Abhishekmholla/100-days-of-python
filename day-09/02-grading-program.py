print("Welcome to the grading program")

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 75,
    "Neville": 62
}

student_grades = {}

for key, value in student_scores.items():
    grade = ""
    if value > 90:
        grade = "Outstanding"
    elif value > 80:
        grade = "Exceeds Expectations"
    elif value > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key] = grade

print(student_grades)
