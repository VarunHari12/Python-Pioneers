import math

# Mathematical expressions


# Just like we can store numbers in variables, we can also store Mathematical expressions in a variable
# ex.





result = 5+6 # addition
print(result) # prints "11" not "5+6"

result = 5-3 # subtraction
print(result)

result = 5*3 # multiplication
print(result)

result = 6/3 # division
print(result)

result = 3**2 # 3 to the power of 2 (** is power symbol)
print(result)

result = 5//2 # keeps the part of the quotient without the remainder (2)
print(result)

result = 5%2 # keeps the remainder part of the division (1)
print(result)

# you can also perform math on variables
x = 1
y = 2
result = x+y # x + y = 1 + 2
print(result)

# Order of operations
# follows simple order of operations PEMDAS

print(3+2*2) # will result in 7
print((3+2)*2) # will result in 10


# math library


power = math.pow(3,2) # this function takes the first number and puts it to a power of the second number
print(power) 

sqrt = math.sqrt(4) # this functions takes the square root of a number provided
print(sqrt)

pi = math.pi # This gives you the value of pi
print(pi)

floor = math.floor(5.6) # this function takes the number an rounds down no matter what the number is
print(floor)

rounded = round(5.5463,2) # this function is not a part of the math library but it rounds the first number to the amount of decimal the second number specifies
print(rounded)

# there are so many more functions in the math library and you can veiw them all by typing math. and viewing all the options

