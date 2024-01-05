# Method chaining = calling multiple methods sequentially. each call prefroms an action of the same object and return self


class Car:

    def on(self):
        print("you turned on the engine")
        return self # You need to put this to do method chaining

    def drive(self):
        print("You are driving the car")
        return self

    def brake(self):
        print("you pressed the brakes")
        return self

    def off(self):
        print("you turned off the engine")
        return self
    
   


car = Car()


# This is one option if you want to do 2 methods sequentially

car.on() 
car.drive()


# you can also do this

car.on().drive()

# Remeber, if you want to do mehtod chaining, each mehtod that you are chaining needs to return self since a method cant be operated on a NoneType

car.on().drive().brake().off()

# You can chain any amount of methods you want

# You can also do this

car.on()\
.drive()\
.brake()\
.off()

# the backslash is a line continuation