# You can use try and except blocks to handle errors in a way that doesnt break your code
# This is especially helpful for handling user input

# Anything you put under a try block will check and catch any errors that occur during that sequence

try:
    print(word)
except:
    print("An error occured")
    
# the excpet block catches the error and executes the following instructions if the error is caught
    
try:
    print(word)
except NameError:
    print("The variable 'x' was never defined")
except:
    print("An error occured")
    
# we can also catch specific errors by specifying the name of the error and make custom instructions

# usually, people will assign the error to the variable e (error) to make many custom outputs for different errors

try:
    num = int(input("What is your numerator: "))
    denom = int(input("What is your denominator: "))
    result = num/denom

except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")

except ValueError as e:
    print(e)
    print("Enter only whole numbers")

except Exception as e:
    print(e)
    print("Something's wrong")
else:
    print(result)
finally:
    print("Done")
    
# you can add an else and run a peice of code only if no errors occur
# Finally is always at the end and runs regardless of if you encounter an error or not

# we can also raise errors based on certain our own requirements
# this can be useful if you want to throw errors to the user that are not actually computational errors
# for example:

x = "hello"

if type(x) is int == False:
  raise TypeError("Only integers are allowed")

# this will basically say the name of the error and a customized message
# (you can also just right excpetion if you want to send a general message)

# Using try and except checks a certain "dangerous" code segment and checks what type of error pops up if any
# you can specify each error by using its name and to catch any error you can use Exception as the name
# adding as e allows you to check which error occured
# you can add an else and run a peice of code only if no errors occur
# Finally is always at the end and runs regardless of if you encounter an error or not
# we can also raise errors based on certain our own requirements
