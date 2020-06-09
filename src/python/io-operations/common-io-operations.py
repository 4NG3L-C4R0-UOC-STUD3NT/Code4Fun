import os
import sys
import hashlib 
import random

cwd = os.getcwd()
directories = print(os.listdir(cwd))
print(directories)

print("************")
print("To find the absolute path to a file, you can use os.path.abspath:")
print(os.path.abspath('README.md'))

print("************")

print("Checks whether a file or directory exists:")
print("** README.md **")
print(os.path.exists('README.md'))
print("** README.py **")
print(os.path.exists('data'))

print("************")

print("If it exists, checks whether it's a directory or a file:")
print("** README.md **")
print("It's a file: {}".format(os.path.isfile('README.md')))
print("It's a directory: {}".format(os.path.isdir('README.md')))
print("** data **")
print("It's a file: {}".format(os.path.isfile('data')))
print("It's a directory: {}".format(os.path.isdir('data')))

print("************")

print("list of the files (and other directories) in the given directory:")
os.listdir(cwd)

print("************")
print("Count how many txt file are in the current directory:")
count = 0
for (dirname, dirs, files) in os.walk('.'):    
    for filename in files:
        print("{}\\{}".format(dirname, filename))
        if filename.endswith('.md'):
            count = count + 1
print('number of txt files: {}'.format(count))

print("************")
print("list all the md files in the current directory:")
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.md'):
            thefile = os.path.join(dirname,filename)
            print("size: {}    file: {}".format(os.path.getsize(thefile), thefile))