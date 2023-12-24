from car import Car

car_1 = Car("Chevy","corvette",2021,"blue") # To create a car object, you put the name of the class, and then pass in the argument that are needed in the init method of that class
car_2 = Car("Ford", "Mustang", 2010, "red") # another instance of the Car class


# Without assigning them, they default to 4 wheels since wheels is a class variable

print(car_1.wheels)
print(car_2.wheels)

# You can still change the class var for each object ex:

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

# You can also change the class variable for all instances of the object. This would set the new default class varable for every new instanc of the class ex:

Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

# A class varuable is essentially a variable that is set to a certain value by default when an object is created but can be changed