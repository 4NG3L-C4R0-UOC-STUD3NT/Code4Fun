# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

#line = list('1234567890')
#print(list(map(float, line)))

student_marks = {}
student_marks['Krishna'] = [67, 68, 69]
student_marks['Arjun'] = [70, 98, 63]
student_marks['Malika'] = [52, 56, 60]
query_name = 'Malika'

values = student_marks.get(query_name)
print("%0.2f" % (sum(values)/len(values)))
