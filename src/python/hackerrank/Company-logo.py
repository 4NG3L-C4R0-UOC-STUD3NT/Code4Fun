#s = input()
s = 'qwertyuiopasdfghjklzxcvbnm'

counters = {}
for letter in list(s):
    if (counters.get(letter) != None): counters[letter] += 1
    else: counters[letter] = 1
print(counters)
items = sorted(sorted(counters.items(), key=lambda item: item[0]), key=lambda item: item[1], reverse=True);
i = 0
for k, v in items:
    if i < 3:
        print(k,v)
    i += 1

