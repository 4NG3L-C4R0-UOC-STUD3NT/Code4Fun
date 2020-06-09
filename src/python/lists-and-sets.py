a = [1,4,5,3,1,4,3,6,2]
print(a)
print("original list: ", a)
# [1, 4, 5, 3, 1, 4, 3, 6, 2]

print("")

print("[set object] w/o duplicates:")
print(set(a))
# {1, 2, 3, 4, 5, 6}

print("")

print("[list object] w/o duplicates:")
print(list(set(a)))
# [1, 2, 3, 4, 5, 6]