def mutate_string(string, position, character):
    l = list(string)
    l.insert(position, character)
    l.pop(position + 1)
    return ''.join(l)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)