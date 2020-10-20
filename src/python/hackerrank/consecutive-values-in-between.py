def consecutiveValues(n):
    values = ''
    for i in range(n):
        values += str(i+1)
    return values

n = int(input())
print(consecutiveValues(n))