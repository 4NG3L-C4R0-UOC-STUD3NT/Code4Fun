if __name__ == '__main__':
    N = int(input())
    L = list()
    commands = list()
    counter = 0
    while counter < N:
        command = input()
        commands.append(command)
        counter += 1
    
    #print(commands)
    for command in commands:
        commandArgs = command.split()
        #print(commandArgs)
        if commandArgs[0].lower() == 'print':
            print(L)
        elif commandArgs[0].lower() == 'insert':
            idx = int(commandArgs[1])
            value = int(commandArgs[2])
            if len(L) < idx + 1:
                L.append(value)
            else:
                L.insert(idx, value)
        elif commandArgs[0].lower() == 'append':
            value = int(commandArgs[1])
            L.append(value)
        elif commandArgs[0].lower() == 'pop':
            L.pop()
        elif commandArgs[0].lower() == 'remove':
            value = int(commandArgs[1])
            if value in L:
                L.remove(value)
        elif commandArgs[0].lower() == 'sort':
            L.sort()
        elif commandArgs[0].lower() == 'reverse':
            L = L[::-1]
    
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print