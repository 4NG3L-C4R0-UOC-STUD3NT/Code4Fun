import numpy

P = map(float, input().split())
val = float(input())
print (numpy.polyval(list(P), val))