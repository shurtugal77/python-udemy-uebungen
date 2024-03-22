student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

def getGrade(grade):
    if (grade >= 91 and grade <= 100):
        result = 'Outstanding'
    elif (grade >= 81 and grade <= 90):
        result = 'Exceeds Expectations'
    elif (grade >= 71 and grade <= 80):
        result = 'Acceptable'
    elif (grade <= 70):
        result = 'Fail'
    return result
    

for studentName in student_scores: 
    studentPoints = student_scores[studentName]
    textGrade = getGrade(studentPoints)
    student_grades[studentName] = textGrade

print('\n')
# 🚨 Don't change the code below 👇
print(student_grades)

#'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
