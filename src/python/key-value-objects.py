keys = ['a', 'b', 'c', 'd']
values = [2, 5, 1, 9]
print(keys)
print(values)

print(zip(keys, values))
# <zip object at 0x00000298AD6FDC08>

print(dict(zip(keys, values)))
# {'a': 2, 'b': 5, 'c': 1, 'd': 9}

print(list(zip(keys, values)))
# [('a', 2), ('b', 5), ('c', 1), ('d', 9)]