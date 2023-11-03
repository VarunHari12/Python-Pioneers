# you can think of a class as a blueprint
# an object is an instance of a class with certain attributes and methods
# a class would be a car but an object would be a 2022 ford f150


class Car:

    # class variablea are variables defined in the class but no in the init method

    wheels = 4 # class var

    # class variables  are the default for each object that is created
    
    def __init__(self,make,model,year,color):

        # the __innit__ method is known as a constructor that essentially creates objects for us using some combinations of attributes
        # The other arguments are arguments that can be passed in to create an object with that set of attributes

        # attributes
        # these variable defined inside of the constructor are called instance variables and each object has their own unique values assigned to each of these variables

        self.make = make # instance var
        self.model = model # instance var
        self.year = year # instance var
        self.color = color # instance var

        # self refers to the object we are currently working on or creating

    # methods

    def drive(self): # self refers to the object that is using this method
        print("This " + self.model + " is driving")

    def brake(self):
        print("This " + self.model + " has stopped")



# An object is an instance of a class
# the class is the general object but an object is the specific thing
# common practice to declare class with uppercase
# Objects can have attributes and methods
# Ex. attributes of a car are the make, model and age
# methods of car could be to drive or brake

# self is replacing the name of the object. self.model is like saying car_1.model