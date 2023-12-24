class Animal:

    def eat(self):
        print("this animal is eating")


class Rabbit(Animal):

    def eat(self): # by usinmg the same name and parameters as a method from the parent class, we are overriding the method to define a more specific implementation of the method
        print("This rabbit is eeating carrots")


# method overriding is used to proviide a more specific implementation of a method for a class
