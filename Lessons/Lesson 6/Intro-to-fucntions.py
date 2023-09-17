# a function is a peice of code that can be used by a programmer to complete small customized tasks 
# you can write your own functions (we will cover this later in the course)

# lets learn the anatomy of a function

# def [function name]([parameter],[parameter],etc.):
#       [instructions]

# lets make our first function

def Hello(name):
    number = 3
    print("Hello " + name)


# print(name)
# print(number)



# this is a function
# in the parentheses is something tcalled a parameter. It is essentialy input the programming uses to create their desired output
# when we write a function, we write all the parameter we want associated to a "varible name"
# in this case, name will store whatever string the user passes into this function
# this varible can then be used inside the function to create the customized output

# lets call this function
# a call to a function is essentially just using a function

Hello("Tejas")

# we must say the name of the function then in the parentheses, list a value for every argument (parameter and argument are interchangle terms) the function needs in the same exact order

# Variable Scope
# now that we are dealing with writing our own function we should know what variable scope is
# essentially it scope of a variable is its lifetime in the program. This means that the scope of a variable is the block of code in the entire program where the variable is declared, used, and can be modified.
# the parameters we use in functions can only be used modified and declared inside of that function
# if we tried to same print(name) outside of that function, it would cause an error because that is not within the scope of the name variable
# this also goes for any varible you declare inside a function

# lets try writing another function with more parameters

def Hello_extra(name,age,gender):
    Hello("hi")
    print("Hello " + name + " you are " + str(age) + " years old and you are a " + gender) 

Hello_extra("Varun",15,"male")


Hello_extra(gender = "male", name = "Varun", age = 15)

# remember you have to stay consistent with the order of the parameters in the fucntion declaration and call
# you cant forget to pass the neccesary arguments
# we can pass any type of varible as an argument
# we can also make a function with no arguments


def Hello_World():
    print("Hello World")



# when you want to use something as a placeholder you can do this

def add():
    pass


# this just acts as placeholder text so that you dont get an error, this works with conditionals and loops too

# Return
# the return statement is a statement that allows you get a certain output value from your function

def add(x,y):
    result = x+y

print(add(3,6))

import math

print(math.pow(2,3))


# this doesnt actually do anything since the fucntion never RETURNS a value back to the user
# instead it should be written like this


def add(x,y):
    result = x+y
    return result

result = add(3,6) # just like saying result = 9 (remember you can stroe operation in varible even if they arent mathematical)
print(result)

# think of the return statement as giving a value to the function
# usually you would want to store the "function call" in a varible but you can only properly do that if you have a return statement
# this also a good example of scope because remeber the result we have in the function is not the same as the one we have outside


# Why write a function?
# if you are going to use the same operation over and over again, instead of re writing it everytime, you can use a function to decrease the length of your program

