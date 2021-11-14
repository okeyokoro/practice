class Animal(object): # Super class
    pass

class Dod(Animal): # Sub class
    def __init__(self,name): # constructor
        self.name = name

class Car(Animal): # Sub class
    def __init(self,name): # constructor
        self.name = name

class Person(object): # Super Class. Person is-a object.
    def __init__(self,name): #Person has-a name.
        self.name = name

class Employee(Person): # Employee is-a Person
    def __init__(self,name,salary): # An Employee has-a name and salary
        super(Employee, self).__init__(name) # super(Employee, self) --> give the attribute of Employee to its parent/super class (since it is an attribute they share). Which attribute? --> __init__(name)
        self.salary = salary # salary is an attribute unique to class Employee.

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass
