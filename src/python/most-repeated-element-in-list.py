a = [1,3,4,6,7,8,3,2,12,2,2,5,6,7,1,1,2,4]
print(a.count(2))
mostRepeated = max(set(a), key=a.count)
print(mostRepeated)
