# https://www.math.ubc.ca/~pwalls/math-python/linear-algebra/linear-algebra-scipy/

import numpy as np
import scipy.linalg as la
from numpy.linalg import matrix_power as mpow
from numpy import linalg as npLA

a = np.array([1,3,-2,1])
print(a)

numOfRows = a.ndim
print('num of rows: ', numOfRows)

print(a.shape)

numOfCols = a.size
print('num of columns: ', numOfCols)

M = np.array([[1,2],[3,7],[-1,5]])
print(M)

numOfRows = M.ndim
print('num of rows: ', numOfRows)

print(M.shape)

numOfCols = M.size
print('num of columns: ', numOfCols)

# Select a row or column from a 2D NumPy array and we get a 1D array:
col = M[:,1] 
print(col)
#Verify the number of dimensions of the slice:
print(col.ndim)
#Verify the shape and size of the slice:
print(col.shape)
print(col.size)

# For example, create a 2D column vector from the 1D slice selected 
# from the matrix M above:
column = np.array([2,7,5]).reshape(3,1)
print(column)
# Verify the dimensions, shape and size of the array:
print('Dimensions:', column.ndim)
print('Shape:', column.shape)
print('Size:', column.size)
# The variables col and column are different types of objects even though 
# they have the "same" data.
print(col)
print('Dimensions:',col.ndim)
print('Shape:',col.shape)
print('Size:',col.size)


test = [[1,0],[0,2]]
f = lambda i, j: sum(test[i])
matrix = np.fromfunction(np.vectorize(f), (len(test), len(test)), dtype=int)
print(matrix)

# Matrix Operations and Functions
# Arithmetic Operations
# Recall that arithmetic array operations +, -, /, * and ** are performed elementwise
# on NumPy arrays. Let's create a NumPy array and do some computations:

M = np.array([[3,4],[-1,5]])
print(M)
print(M * M)

# Matrix Multiplication
# We use the @ operator to do matrix multiplication with NumPy arrays:
print(M @ M)

# Let's compute  for
A = np.array([[1,3],[-1,7]])
print(A)
B = np.array([[5,2],[1,2]])
print(B)
# and  is the identity matrix of size 2:
I = np.eye(2)
print(I)
print(2*I + 3*A - A@B)


# Matrix Powers
# There's no symbol for matrix powers and so we must import the function matrix_power from the subpackage numpy.linalg.
M = np.array([[3,4],[-1,5]])
print(M)

print(mpow(M,2))

print(mpow(M,5))

# Compare with the matrix multiplcation operator:
print(M @ M @ M @ M @ M)

print(mpow(M,3))
print(M @ M @ M)


# Tranpose
# We can take the transpose with .T attribute:
print(M)

print(M.T)

# Notice that MM^T is a symmetric matrix:
print(M @ M.T)


# Inverse
# We can find the inverse using the function scipy.linalg.inv:
A = np.array([[1,2],[3,4]])
print(A)

print(la.inv(A))

# Trace
# We can find the trace of a matrix using the function numpy.trace:
print(np.trace(A))

# Determinant
# We find the determinant using the function scipy.linalg.det:
A = np.array([[1,2],[3,4]])
print(A)

print(la.det(A))


# https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm
a = np.arange(9) - 4
b = a.reshape((3, 3))
print('a: ', a)
print('b: ', b)
print('norm(a): ', npLA.norm(a))
print('norm(b): ', npLA.norm(b))
print('norm(b "fro"): ', npLA.norm(b, 'fro'))
npLA.norm(a, np.inf)
npLA.norm(a, -np.inf)
npLA.norm(b, np.inf)
npLA.norm(b, -np.inf)


# https://www.geeksforgeeks.org/calculate-the-average-variance-and-standard-deviation-in-python-using-numpy/
# Taking a list of elements 
list1 = [2, 4, 4, 4, 5, 5, 7, 9] 
# Calculating average using average() 
print(np.average(list1))
# Calculating variance using var() 
print(np.var(list1))
# Calculating standard deviation using var() 
print(np.std(list1))

# Taking a list of elements 
list2 = [2, 40, 2, 502, 177, 7, 9] 
# Calculating average using average() 
print(np.average(list2))
# Calculating variance using var() 
print(np.var(list2))
# Calculating standard deviation using var() 
print(np.std(list2))

# Taking a list of elements 
list3 = [290, 124, 127, 899] 
# Calculating average using average() 
print(np.average(list3))
# Calculating variance using var() 
print(np.var(list3))
# Calculating standard deviation using var() 
print(np.std(list3))


a = np.random.rand(1000)
print(a)
print('mean(a): ', a.mean())
print('var(a): ', a.var())
# 10000 loops, best of 3: 80.6 µs per loop

m = a.mean()
print('mean((a-m)**2: ', np.mean((a-m)**2))
# 10000 loops, best of 3: 60.9 µs per loop

# If you really are trying to speed things up, try np.dot
# to do the squaring and summing (since that's what a dot-product is):
c = a-m
print('a-m: ', c)
print('np.dot(c,c)/a.size: ', np.dot(c,c)/a.size)
# 10000 loops, best of 3: 38.2 µs per loop


# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
my_array = np.array([ [1, 2], [3, 4] ])
print(np.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(np.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print(np.mean(my_array, axis = None))     #Output : 2.5
print(np.mean(my_array))                  #Output : 2.5

print(np.var(my_array, axis = 0))         #Output : [ 1.  1.]
print(np.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
print(np.var(my_array, axis = None))      #Output : 1.25
print(np.var(my_array))                   #Output : 1.25

print(np.std(my_array, axis = 0))         #Output : [ 1.  1.]
print(np.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
print(np.std(my_array, axis = None))      #Output : 1.11803398875
print(np.std(my_array))                   #Output : 1.11803398875



# other resources:
# https://python.quantecon.org/linear_algebra.html
# http://web.stanford.edu/class/cs231a/section/section1.pdf
# https://numpy.org/doc/stable/reference/routines.linalg.html
# https://numpy.org/doc/stable/reference/routines.linalg.html
# https://rlhick.people.wm.edu/stories/linear-algebra-python-basics.html
# https://plotly.com/python/v3/linear-algebra/
# https://www.twilio.com/blog/2018/06/data-science-linear-algebra-python-scipy-numpy.html

