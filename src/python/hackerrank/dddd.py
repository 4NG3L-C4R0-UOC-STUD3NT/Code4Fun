import random
def arrayKthGreatestQuick(inputArray, k):

    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []
    #inputArray.sort()
    #print(inputArray)
    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        #print(pos)
        print(inputArray[i], inputArray[k])
        if inputArray[i] <= inputArray[k]:
            left.append(inputArray[i])
        else:
            right.append(inputArray[i])
    print(left)
    print(right)
    return (left + right)
print(arrayKthGreatestQuick([19, 32, 11, 23], 3))