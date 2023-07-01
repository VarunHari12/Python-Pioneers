# A conditional is a statement is a statement that can allow program to choose between multiple options based off a certain value

# this is how you write an if statement:
# if (whatever you are checking):
# (do this)

# ex.

rainy = True

if rainy == True:
    print("it is rainy")

# what is the difference between == and =?
# = assigns that value to a variable
# == checks if that value is equal to the varible
# when instructions are contained within an if statement, there has to be a indent that distinguishes which "block" of code it is in

# there is also something called an else statement

sunny = False
if sunny == True:
    print("It is sunny")
else:
    print("It is not sunny")



# And the final conditional statement is the elif statement whoch stands for else if

mood = "Sad"

if mood == "Happy":
    print("You are happy")
elif mood == "Sad":
    print("You are sad")
else:
    print("You are not happy or sad")

# the else is the final thing that is run if every other if statement fails
# if an elif statement succeds, it skips the rest of the if statements


# there are infinite number of things you can use if's to check

number = 5

if number == 5:
    print(number)

word = "hi"

if word.islower() == True:
    print(word)

# there is something that should be noted when you are working with if statements and booleans
# you dont have to add the == True and here is example that explains why

if True:
    print("hi")

# the if statement is only passed if the follwing statement evaluates to a value of true
# for example you could do this instead

if rainy:
    print(rainy)

# since rainy = True, this would be the same as saying if True
# same idea applies for word.islower(), you dont need the == True


# here are some other things you can do with if statemts

# you can use >, <, <=, >=, != on numbers to check certain things

integer = 13

if integer > 10:
    print(integer)

if integer <= 20:
    print(integer)

if integer != 22: # != means not equal to so it checks to see if integer is not equal to 22
    print(integer)

# going back to operators, we can also use logical operators with if statements

# the and statement says that both expression must be true for the if statement to be considered true
# the or statement says that al least one of the expressions must be true for the expression to be considered true
# the not statement switches the value of the boolean for that expression
# remember the entire expression has to evaluate to True for an if statement to pass
# when using logical operators, it is good practice to use parentheses to organize the if statement


# this uses an and statement which means both expressions have to be true

number = 5
word = "hello"

if (number == 5) and (word == "hello"):
    print("success")


# this uses an or statement which means at least one of the statements must evauluate to true

number = 10
word = "awesome"

if (number == 10) or (word == "cool"):
    print("success")


# this uses a not statement which switches switches the value of False to True and vice versa

if (number == 10) and (not(word == "hello")):
    print("success")


# you can also write more complex if statements by combining logical operators

weather = "sunny"
day = "monday"

# the or has to evaluate to true and the and has to evalute to true
if ((weather == "sunny") or (weather == "rainy")) and (day == "monday"):

    print("Today is is monday and the weather is " + weather)

# lets talk about nested conditionals
# nested conditionals are if statements inside if statements
# ex.


weight = 105
height = "5 feet"

if height == "5 feet":

    if weight == 105:
        print("You are normal weight and height")
    else:
        print("You are normal height but not height")

else:
    print("You are not normal weight or height")

# nested conditionals can be useful when you want to want to check 2 connected conditionals seperately and customize the output
# always remeber that there has to be an indent. this is a "block" of code inside a "block" of code so it needs 2 indents

# One question you might have is what is the difference between a sequence of if's and a sequence of elif's
# Here it is

age = 7

if age < 5:
    print("You are less than 5")
if age < 10:
    print("You are less than 10")
if age < 15:
    print("You are less than 15")
if age < 20:
    print("You are less than 20")


if age < 5:
    print("You are less than 5")
elif age < 10:
    print("You are less than 10 and greater than 5")
elif age < 15:
    print("You are less than 15 and greater than 10")
elif age < 20:
    print("You are less than 20 and greater than 15")


# the difference is that with elifs, it skips the rest of the if's if one of them is satisfied
# it allows for more customization and conveniece
# alternative technically you could use a bunch of nested conditionals but it is very tedious and a waste of time
# the aim of a programmer is to be lazy and to make things as easy as possible



    