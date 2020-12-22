import json 

class Person:
    
    def __init__(self, firstName, lastName, age, address):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address

    def __str__(self):
        return json.dumps(self.__dict__)
    
    def __getitem__(self, key):
        objectAttrs = self.__dict__
        if key in objectAttrs.keys():
            return objectAttrs.get(key)
        return None

    def __setitem__(self, key, value):
        objectAttrs = self.__dict__
        if key in objectAttrs.keys():
            objectAttrs[key] = value
        else: setattr(self, key, value)

if __name__ == "__main__":
    person = Person('john', 'doe', 40, 'unknow')
    print(person)
    setattr(person, 'email', 'johndoe@gmail.com')
    print(person)
    person["mobile"] = "99999999999"
    print(person)
    print('first name: ', getattr(person, 'firstName'))


