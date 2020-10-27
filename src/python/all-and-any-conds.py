subs = 2400
likes = 200
comments = 56

conditions = [
    subs > 150,
    likes > 150,
    comments > 50
]

if subs > 150 and likes > 150 and comments > 50: 
    print('awesome')
if all(conditions):
    print('awesome')


if subs > 150 or likes > 150 or comments > 50: 
    print('awesome')
if any(conditions):
    print('awesome')

