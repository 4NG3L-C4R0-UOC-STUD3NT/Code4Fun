#year = 0
#while year >= 1900 and year <= 10 ** 5:
#    year = int(input())

n = [2000, 2400, 1800, 1900, 2100, 2200, 2300, 2500]

for year in n:
    if (year % 4 == 0) and (year % 100 == 0 and year % 400 == 0): print(year, True)
    else: print(year, False)