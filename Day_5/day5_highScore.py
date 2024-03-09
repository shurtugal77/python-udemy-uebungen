# 78 65 89 86 55 91 64 89

students_scores = input().split()
for n in range (0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

# print(students_scores)

myHighestScore  = 0
for mahScore in students_scores:
    if mahScore > myHighestScore:
        myHighestScore = mahScore

print(f"The highest score in the class is: {myHighestScore}")