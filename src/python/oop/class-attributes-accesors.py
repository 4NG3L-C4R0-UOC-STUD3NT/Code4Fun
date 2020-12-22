import json 
#from json import JSONEncoder

# class MyEncoder(JSONEncoder):
#
#     def default(self, o):
#         return o.__dict__

class Pet:
    def __init__(self, name, age, bread):
        self.name = name
        self.age = age
        self.bread = bread
    
    def saySomething(self, sound):
        pass

class Dog(Pet):
    
    def __init__(self, name, age, bread, sound):
        super().__init__(name, age, bread)
        self.sound = sound
    
    def saySomething(self, sound = None):
        if sound == None: sound = self.sound
        print(sound)
    
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


billy = Dog('billy', 4, 'labrador', "woof woof")
print(billy)
print(billy["bread"])