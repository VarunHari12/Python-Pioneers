# Prevents the user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract clas = a class which contains one ore more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod 

# abc stands for abstract base class
# this will help us make the vehicle class bastract


class Vehicle(ABC): # to make the class abstract, add parantheses and make it inherit from the ABC class

    @abstractmethod # above any method in the abstract class, you have to add this statement to make it an abstract method
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("The car is driving") # to create a child class of an abstract class, we must override all abstract methods of the abstract parent class

    def stop(self):
        print("The car has stopped") # to create a child class of an abstract class, we must override all abstract methods of the abstract parent class

class Motorcycle(Vehicle):

    def go(self):
        print("the motorcycle is driving") # to create a child class of an abstract class, we must override all abstract methods of the abstract parent class
    
    def stop(self):
        print("The motorcycle has stopped") # to create a child class of an abstract class, we must override all abstract methods of the abstract parent class



# vehicle = Vehicle()  this will no longer work since it has been made an abstract class
car = Car()
motorcycle = Motorcycle()


# vehicle.go() This will no longer work because it is a part of that abstract class
# vehicle.stop() This will no longer work because it is a part of that abstract class

motorcycle.go()
car.go()

motorcycle.stop()
car.stop()


# The use of an abstract class is to prevent a use from using that class to create an object
# ex. if we want the uset to make a car in the game from the car or motorcycle class and instead they use the Vehicle class, the object could be missing a lot of the features we want it to have
# we want to prevent this ^

# an example of why the abstract class is useful is because in our game we dont want the vehicle to just go
# we would want the vehicle to go depening on the vehicle type and attributes so we make it an abstract method to prevent that