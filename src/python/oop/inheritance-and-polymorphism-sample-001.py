# parent class 
class Dog:

    # static attributes
    species = "Canis familiaris"
    
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Printable string representation
    def __str__(self):
        #return 'Mi name is ' + self.name + ' and I am ' + str(self.age) + ' years old'
        #return 'My name is %s and I am %d years old' % (self.name, self.age)
        #return f"My name is {self.name} and I am {self.age} years old"
        return f'My name is {self.name} and I am {self.age} years old'

    # abstract method
    def breed(self):
        pass

    # method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    # method
    def bark(self):
        return 'Woof Woof'

    # method
    def toString(self):
        #return '{ name: \'%s\', age: %d, species: \'%s\' }' % (self.name, self.age, self.species)
        return "[ name: '{}', age: {}, species: '{}' ]".format(self.name, self.age, self.species)

    @classmethod
    def species(cls):
        return cls.species

# child class
class Bulldog(Dog):

    def doSomething(self):
        print('doing something!!!')

# child class
class Dachshund(Dog):

    # Polymorphism
    def breed(self):
        return 'Dachshund'

# child class
class JackRussellTerrier(Dog):

    # Polymorphism
    def breed(self):
        return 'JackRussellTerrier'
    
    # Polymorphism
    def speak(self, sound = 'arf arf'):
        #return f"{self.name} says {sound}"
        return super().speak(sound)


def dogDetails(dog):
    print('name: %s' % dog.name)
    print('breed: %s' % dog.breed())
    print('age: %d' % dog.age)
    print('barking: %s' % dog.bark())


# class instantiations
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print('===========')

print(miles)
print(miles.toString())
print('%s is a %s' % (miles.name, miles.breed()))
print(isinstance(miles, Dog))
print(isinstance(miles, JackRussellTerrier))
print(isinstance(miles, Bulldog))

print('===========')

print(buddy)
print('%s is a %s' % (buddy.name, buddy.breed()))
print(buddy.bark())
#print(buddy.speak())   # !!!Error
print(buddy.speak('grrr'))
#buddy.doSomething()

print('===========')

print(jack)
print('%s is a %s' % (jack.name, jack.breed()))
print(jack.bark())
#print(buddy.speak())   # !!!Error
print(jack.speak('gggrrrrrr!!'))
jack.doSomething()

print('===========')

dogDetails(jim)

print('===========')

dogs = [miles, buddy, jack, jim]

for dog in dogs:
    print('name: %s' % dog.name)
    print('breed: %s' % dog.breed())
    print('age: %d' % dog.age)
    print('barking: %s' % dog.bark())
    print("   ")


# what happend if the abstract method is used
dog = Dog("sasha", 8)
dogDetails(dog);