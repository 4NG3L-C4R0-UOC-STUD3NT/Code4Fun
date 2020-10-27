import re

#text = input()
#text = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
text = "match a single character not present in the list below"
#text = "abaabaabaabaae"
#text = "abaabaabaabaaei"
matches = re.findall(r'(?<=[^aeiouAEIOU ])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU ])', text)
groups = [group for group in matches]
print(groups)
printed = 0
for group in groups:
    if len(group) >= 2:
        print(group)
        printed = 1
else: 
    if  printed == 0: print(-1)
