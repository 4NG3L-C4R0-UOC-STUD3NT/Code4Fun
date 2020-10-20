# students = []
# n = int(input())
# for i in range(n):
#     name = input()
#     score = float(input())
#     students.append([name, score])

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

grades = []
temp = [grades.append(student[1]) for student in students if student[1] not in grades]
grades.sort()
secondLowestGrade = grades[1]
studentsWithLG = [student[0] for student in students if student[1] == secondLowestGrade]
studentsWithLG.sort()
for student in studentsWithLG:
    print(student)


