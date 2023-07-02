# What is a varible?
# a variable is a named contanier that stores a certain type of data 
# there are many different types of variables, here are a few:



# Strings (str)

# A string is essentialy just text ex.

word = "hello" # we can name our variables anything we want and can store data in it by writing (variable name) = (value) 'hello' "hello"

# here we are a storing a string that says hello in the word variable
# here is another example

phrase = "hi"
greeting = "hello how was your day"


print(greeting) # print("hello how was your day")



# just like in math, one variable can't store 2 different values so if you want to store multiple values you have to use multiple variables



# Integers (int)

# integers are whole numbers ex.

number = 5
number2 = 6

# What is the difference between a string and an integer?

integer = 5
string = "5"
apples = 3

print(apples)

# although these appear to have the same value, the integer version has a numerical value that can be used to perfrom mathamtical equations whereas the string is just text and doesnt have a numerical value




# Floating points (float)

# floats are decimal numbers ex.

decimal = 2.5
decimal2 = 3.3
money = 1.50

print(money)

# floats and ints are not the same since an int is a whole number whereas a float is a decimal value





# Booleans

# booleans are true/false Value

boolean1 = True
boolean2 = False

# is it raining?

rainy = True # yes
rainy =  False # no

print(rainy)


# the value of true/false has to have a capital first letter ex. True, False




# None

# A varible assigned to a none type has no value

oranges = None # doesnt have a value
print(oranges)

# more common practice to use when trying to reset a varible




# Overriding variables

# you can set a varible to a different value by restating the variable declaration

number = 1

number = 2

print(number)

# after overriding the first iteration of the number varible, we cant access it's previous value since we overrided it with the value of 2

# we can also override it with a different type of variable (this is something that is not common across other programming languages and is not good practice)

number = 1.5 # float

print(number)

number = "hi" # string

print(number)


# these are some data types that we see in python but there are many others and other languages have more datatypes that differ based on precision and speed