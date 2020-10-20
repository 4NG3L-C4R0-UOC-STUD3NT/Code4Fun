#Given an integer, , perform the following conditional actions:
#
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird


n = 0
while n < 1 or n > 100:
    n = int(input())

print('n = ', n)

if n % 2 != 0: print('Weird')
elif n >= 2 and n <= 5: print('Not Weird')
elif n >= 6 and n <= 20: print('Weird')
elif n > 20: print('Not Weird')

