import functools

list1 = [1,2,3,4]
print(list1)

func = lambda x,y:x*y
varf = functools.reduce(func,list1)
print(varf)
