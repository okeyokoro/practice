## Animal is-a object (yes, sort of confusing) look at the extra credit


class Animal(object):
    pass

## Dod is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute called name
        self.name = name

##  Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute called name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute called name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a attribute called salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## stan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## satan is-a pet of Person: Mary
mary.pet = satan

## frank is-a Employee. frank has-a name: Frank. frank has-a salary: 120000
frank = Employee("Frank", 120000)

## rover is-a pet of Person frank
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut 
harry = Halibut()
