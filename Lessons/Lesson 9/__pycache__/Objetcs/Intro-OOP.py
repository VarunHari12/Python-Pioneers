from car import Car

make = input("Tell me a make for the car: ")

car_1 = Car(make,"Chorvette",2021,"Blue") # To create a car object, you put the name of the class, and then pass in the argument that are needed in the init method of that class


# Here the attributes of the car object I just created are being printed on screen
print(car_1.make)
print(car_1.model)
print(car_1.color)
print(car_1.wheels)

car_1.drive()
car_1.brake()
