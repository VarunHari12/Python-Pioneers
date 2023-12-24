class Car:

    color = None


def changeColor(car,color):
    
    car.color = color # we can use the object attributes in the parameter that is passed in the function

car_1 = Car()
car_2 = Car()
car_3 = Car()

#  we can pass objects as arguments in a function
changeColor(car_1,"red")
changeColor(car_2,"Blue")
changeColor(car_3,"green")


print(car_1.color)
print(car_2.color)
print(car_3.color)