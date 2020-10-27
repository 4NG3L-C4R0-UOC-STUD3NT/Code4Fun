import numpy as np

n = int(input())
list1 = []
for i in range(n):
    z = [float(elem) for elem in input().split()]
    list1.extend(z)

A = np.array(list1).reshape(n, n)
print(round(np.linalg.det(A), 2))