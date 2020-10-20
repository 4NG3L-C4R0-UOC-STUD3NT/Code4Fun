#https://github.com/srgnk/HackerRank/blob/master/python/validating-uid.py
import re

inputs = []
for i in range(int(input())):
    inputStr = input()
    inputs.append(inputStr)

for code in inputs: 
    valid = (len(code) == 10 and re.match(r'', code) and 
             re.search(r'[A-Z]{2}', code) and re.search(r'\d\d\d', code) and
             not re.search(r'[^a-zA-Z0-9]', code) and not re.search(r'(.)\1', code))
    if valid: print('Valid')
    else print('Invalid')
