import re
text = "Life is beautiful"
pattern = r"\b(?=[a-z]*[aeiou])[a-z]+\b"
result = re.findall(pattern, text, re.I)
print(result)



non_flat = [ [1,2,3], [4,5,6], [7,8] ]

#list1 = [y for y in x for x in non_flat]
#print(list1)

list2 = [y for x in non_flat for y in x]
print(list2)

list3 = [ y for x in non_flat if len(x) > 2 for y in x ]
print(list3)


strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'], ['ts', 'h'] ]
list4 = [ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>2 for letter in word]
list5 = [ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>=2 for letter in word]
print(list4)
print(list5)

tags = [u'man', u'you', u'are', u'awesome']
entries = [[u'man', u'thats'],[ u'right',u'awesome']]
list6 = [entry for tag in tags for entry in entries if tag in entry]
print(list6)

matrix = [[j for j in range(5)] for i in range(5)] 
print(matrix) 

seq_x = [1, 2, 3, 4]
seq_y = 'abc'
list7 = [(x,y) for x in seq_x for y in seq_y]
print(list7)

print("============================================")

x = 1
y = 1
z = 1
n = 2

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != n:
                print('i = ', i, ', j = ', j, ', z = ', z)

list8 = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if i+j+k != n ]
print(list8)


