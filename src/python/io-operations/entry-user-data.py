x = list(map(str, input("Enter a multiple students names: ").split()))
print("List of students: ", x)

y = [entry for entry in input("Enter a multiple students names: ").split()]
print("List of students: ", y)

z = [int(entry) for entry in input("Enter multiple int numbers: ").split()]
print("Number of list is: ", z) 
