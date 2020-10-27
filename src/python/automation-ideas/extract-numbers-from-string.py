import re

test_string = input("Enter string: ")

print("The original string: {} ".format(test_string))

temp = re.findall(r'\d+', test_string)

res = list(map(int, temp))

print("The numbers list is: {} ".format(str(res)))
