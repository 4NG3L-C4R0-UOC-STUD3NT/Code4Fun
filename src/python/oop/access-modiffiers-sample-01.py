# class
class Employee:

    # public attribute
    name = None
    # protected attribute
    _age = None
    # private attribute
    __salary = None
    # protected attribute
    _sex = None

    __onVacation = False

    # constructor 
    def __init__(self, name, age, sex, sal):
        self.name = name  # public attribute 
        self._age = age
        self.__salary = sal # private attribute
        self._sex = sex # protected attribute

    # Printable string representation
    def __str__(self):
        return f'My name is {self.name}, I am a {self._sex} of {self._age} years old. My salary is about {self.__salary} soles'
    
    # private method
    def __doingSomething(self, action):
        if not self.__onVacation:
            print(action)
        else:
            print("on vacation!!!")

    # protected method
    def _working(self):
        self.__doingSomething('working!!!')

    # public method
    def onVacation(self):
        self.__doingSomething('on vacation!!!')

    def showFile(self):
        print("")
        print("name: %s" % self.name)
        print("age: %d" % self._age)
        print("gender: %s" % self._sex)
        print("salary: %s" % self.__salary)
        if (self.__onVacation):
            print("status: on vacation")
        else:
            print("status: active")
        print("")

    def startVacations(self):
        self.__onVacation = True

    def backToWork(self):
        self.__onVacation = False

    # public method
    # attribute accesor method
    def getSalary(self):
        return self.__salary
    
    # public method
    # attribute mutator method
    def setSalary(self, salary):
        self.__salary = salary


class Manager(Employee):

    __team = []

    def addTeamMember(self, employee):
        self.__team.append(employee)

    def showTeam(self):
        print("")
        print("%s's team:" % self.name)
        for employee in self.__team:
            #print(employee)
            employee.showFile()
        print("-------- end of team member list")
        print("")


pedro = Employee('Pedro', 30, 'Male', 2000)
samanta = Employee('Samanta', 25, 'Female', 2000)
manuel = Manager('Manuel', 40, 'Male', 5000)
manuel.addTeamMember(pedro)
manuel.addTeamMember(samanta)

print(pedro)
print(pedro.name)
# protected attributes does not prevent instance 
# from accessing or modifying the value
print(pedro._age)
# the attribue cannot be accessed because was declared as private
#print(pedro.__salary)  # !!!ERROR
print(pedro.getSalary())

print(samanta)
print(samanta.name)
print(samanta._age)
#print(samanta.__salary)  # !!!ERROR
print(samanta.getSalary())

#pedro.__doingSomething()  # !!!ERROR
pedro._working()


print(manuel)
print(manuel.name)
# protected attributes does not prevent instance 
# from accessing or modifying the value
print(manuel._age)
# the attribue cannot be accessed because was declared as private
#print(manuel.__salary)  # !!!ERROR
print(manuel.getSalary())

manuel.showTeam()

print("")
manuel.startVacations()
manuel.showFile()