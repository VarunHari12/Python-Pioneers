# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    # this objects expects a duck object to be passed in
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

# this is the expected object to be passed through
person.catch(duck)

# as long as the passed in object has the same methods and trributes as the expected object, it can be used in the method
person.catch(chicken)

# python is essentially saying that the chicken is close enough to the duck since it does the "same things"