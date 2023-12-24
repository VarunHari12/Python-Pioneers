class Prey: 
    def flee(self):
        print("This animal flees")

        
class Predator:
    def hunt(self):
        print("This animal hunts")


class Hawk(Predator): # This inherits one parent class
    pass

class Fish(Predator, Prey): # with multiple inheritance, you can inherit the methods and attributed from multiple classes by specifying all the classes you want that class to inherit from
    pass

class Rabbit(Prey): # This inherits one parent class
    pass


# hawk only inheritd from the predator class

hawk = Hawk()

hawk.hunt()


# rabbit only inherits from the prey class

rabbit = Rabbit()

rabbit.flee()



# Fish inherits from both classes

fish = Fish()

fish.flee()
fish.hunt()

