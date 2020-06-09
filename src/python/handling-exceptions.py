# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as error:
        print(error)
        print(type(error))
        print("========================")
        err = sys.exc_info()[0]
        print(err)
        print(type(err))
        print("Next entry.")
        print("========================")

print("The reciprocal of", entry, "is", r)