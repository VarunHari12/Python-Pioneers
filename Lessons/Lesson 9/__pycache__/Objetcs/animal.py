class Animal: # this is the parent class
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")



# inheritance

class Rabbit(Animal): # this is the child class. to create one, you just add a pair of paranthese and put in the name of the parent class
    
    def hop(self):

        print("The rabbit is hopping")

class Hawk(Animal): # this is the child class. to create one, you just add a pair of paranthese and put in the name of the parent class
    
    def fly(self):

        print("This hawk is flying")

class Fish(Animal): # this is the child class. to create one, you just add a pair of paranthese and put in the name of the parent class
    
    def swim(self):

        print("This fish is swimming")


# Multi level inheritance


class BabyHawk(Hawk): # this is a child class of a child class which is known as multi level inheritance

    def cry(self):

        print("This baby hawk is crying")



# Multiple inheritance

# Parent classes

class Prey: 

    def flee(self):
        print("This animal flees")

        
class Predator:
    def hunt(self):
        print("This animal hunts")



