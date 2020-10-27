if __name__ == '__main__':
    #s = input()
    s = 'qA2'
    v = [False, False, False, False, False]
    for letter in s:
        if letter.isalpha() or letter.isdigit(): v[0] = v[0] or True
        if letter.isalpha(): v[1] = v[1] or True
        if letter.isdigit(): v[2] = v[2] or True
        if letter.islower(): v[3] = v[3] or True
        if letter.isupper(): v[4] = v[4] or True
    for value in v:
        print(value)
