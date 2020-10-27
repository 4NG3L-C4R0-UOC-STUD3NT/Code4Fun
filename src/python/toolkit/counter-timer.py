import time

def countDown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        #print('mins: ', mins, 'secs: ', secs)
        print("%2d:%02d" % (int(mins), secs))
        t -= 1
    
    print('times up!!!')

t = int(input("Enter push up time in seconds: "))
countDown(t)
