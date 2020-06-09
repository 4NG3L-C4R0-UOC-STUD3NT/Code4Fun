import random

print("Step 1")
print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

print("Step 2")
# Get random choice
print(random.choice(x))

print("Step 3")
# Shuffle x
random.shuffle(x)

print("Step 4")
# Print the shuffled x
print(x)

print("Step 5")
# Print random element
print(random.random())