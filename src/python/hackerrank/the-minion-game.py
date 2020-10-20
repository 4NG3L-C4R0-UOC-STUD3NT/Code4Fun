def minionGame(string):
    vowelsList = list('aeiou')
    consonants = 0
    vowels = 0
    string = string.lower()
 
    n = len(string)
    for i, l in enumerate(string):
        if l in vowelsList: vowels += n-i
        else: consonants += n-i
 
    winner = 'Draw' 
    score = 0
    if vowels > consonants:
        winner = 'Kevin'
        score = vowels
    elif vowels < consonants: 
        winner = 'Stuart'
        score = consonants
    
    if winner != 'Draw': print(winner, score)
    else: print(winner)

minionGame('BANANA')
minionGame('BANANANAAAS')
minionGame('BANAASA')