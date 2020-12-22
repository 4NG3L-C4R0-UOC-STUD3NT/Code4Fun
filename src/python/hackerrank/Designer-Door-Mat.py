if __name__ == '__main__':
    N, M = input().split()
    N = int(N)
    M = int(M)
    welcome = 'WELCOME'.center(M, '-')
    lines = (N // 2) - (1 if N % 2 == 0 else 0)
    middle = 2 if N % 2 == 0 else 1
    #print('Size: %d x %d' % (N, M))
    for i in range(N):
        idx = i+1
        if idx <= lines:
            midpattern = '.|.' * (idx + i)
            print(midpattern.center(M, '-'))
        if idx > lines and idx <= lines + middle:
            print(welcome)
        if idx > lines + middle:
            factor = (2 * (N - idx)) + 1
            midpattern = '.|.' * factor
            print(midpattern.center(M, '-'))

#Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------