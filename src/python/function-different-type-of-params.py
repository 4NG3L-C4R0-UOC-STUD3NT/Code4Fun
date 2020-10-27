from typing import List
def greatings(names: List[str]):
    for name in names:
        print("hello", name)

def Sum(*params):
    result = 0
    for i in params:
        result += i
    return result

print(Sum(2,3,5,500,870))

greatings(["John"])

greatings([100])