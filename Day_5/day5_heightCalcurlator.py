# 151 145 179

student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Don't change above
    
# print(student_heights)

# Sum of heights and number of students
sumOfHeights = 0
numberOfStudents = 0
for x in student_heights:
    sumOfHeights += x
    numberOfStudents += 1

# Avarage height
avarageHeight = int(round(sumOfHeights / numberOfStudents, 0))

print(f"total height = {sumOfHeights}")
print(f"number of students = {numberOfStudents}")
print(f"avarage height = {avarageHeight}")

