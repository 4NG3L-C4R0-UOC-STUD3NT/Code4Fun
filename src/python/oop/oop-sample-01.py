class Duck:
    pass

# class
class Dog:

    # attribute
    species = "Canis familiaris"

    # constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Printable string representation
    def __str__(self):
        #return 'Mi name is ' + self.name + ' and I am ' + str(self.age) + ' years old'
        #return 'My name is %s and I am %d years old' % (self.name, self.age)
        #return f"My name is {self.name} and I am {self.age} years old"
        return f'My name is {self.name} and I am {self.age} years old'
    
    # method
    def bark(self):
        return 'Woof Woof'

    # method
    def toString(self):
        return '{ name: \'%s\', breed: \'%s\', age: %d, species: \'%s\' }' % (self.name, self.breed, self.age, self.species)


# class instantiation
a = Duck()
b = Duck()
print(type(a))
print(type(b))
print(a == b)
print(a)
print(b)

# class instantiation
myDog = Dog('sasha', 8, 'labrador')
print(type(myDog))
print(myDog)
print(myDog.toString())
print(myDog.name)
print(myDog.bark())


miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(miles)
print('%s is a %s and he is saying %s' % (miles.name, miles.breed, miles.bark()))
print(buddy)
print('%s is a %s and he is saying %s' % (buddy.name, buddy.breed, buddy.bark()))
print(jack)
print('%s is a %s and he is saying %s' % (jack.name, jack.breed, jack.bark()))
print(jim)
print('%s is a %s and he is saying %s' % (jim.name, jim.breed, jim.bark()))



