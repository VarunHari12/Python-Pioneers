# By using the input function, we can get text based user input from a user
# ex.

name = input("What is your name? ") # the varible will store whatever the user puts and the rest pof the program wont run until the user inputs something

print("Hello " + name) # this is a string operator

# here we are essentialy combining the strings of "Hello " and the string variable name into one string
# the reason this is useful is because we are able to have an customizeable message instead of hardcoding a message in

# lets see another example

age = input("How old are you? ") # this results in a string not an int

# age = age + 5 this wont work and here is why:
# think about it this way, you can combine an int and a string
# instead you have to use something called casting
# casting is essentialy when you convert a value into a different type
# ex.

age = int(age) # this string casting which turns 5 into "5"

# you can do other types of casting such as str(value), float(value), bool(value) etc.

# now we can use this value for math

age = age + 5

# now we have to convert age back to a string so tha it can be printed with other strings

age  = str(age) # age is a str now

print("Your age plus five is " + age)

# optionally you can also do this print("Your age plus five is " + str(age)) instead if you want to temporarily chnage the variable




