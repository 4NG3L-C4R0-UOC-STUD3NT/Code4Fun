import os

print('Enter file:')
name = input()
handle = open(name, 'r')
text = handle.read()
print(text)