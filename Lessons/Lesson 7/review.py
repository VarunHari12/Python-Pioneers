# lets do some review before we get started with he complicated stuff


# Conditionals: Statements that can allow the porgram to choose between different operations based on a value

mood = "Sad"

if mood == "Happy":
    print("You are happy")
elif mood == "Sad":
    print("You are sad")
elif mood == "Angry":
    print("Angry")
else:
    print("You are not happy or sad")
    
# Remember that we can also use logical operators to make our conditionals more complex

# this uses an and statement which means both expressions have to be true

number = 5
word = "hello"

if (number == 5) and (word == "hello"): # TT 
    print("success")


# this uses an or statement which means at least one of the statements must evauluate to true

number = 10
word = "awesome"

if (number == 10) or (word == "cool"): # TT TF FT
    print("success")


# this uses a not statement which switches the value of False to True and vice versa

if (number == 10) and (not(word == "hello")): # TT
    print("success")



# Loops: Statements that can be used to reiterate a certain set of code based off a condition

# this is a for loop, it iterates through a sequence of values

fruits = ["apple", "orange", "blueberry", "grape"]

for fruit in fruits:
    print(fruit)


# This is a while loop, it keeps iterating until a certain condition is false
    
x = 0
while (x < 10) and (x != 5): 
    x += 1 
    print(x)
    
    
# We can also use break and continue statements to change up the flow of our loop

number = 15

while True:
    guess = input("Guess my number (1-20): ")
    digit = guess.isdigit()

    if digit == True:
        if int(guess) == number:
            print("You got the number correct! ")
            break
        else:
            print("You got it incorrect! ")
            continue

    print("please input a digit")


# Remember this example?
# In this case we are actually using a break and a continue
# In this case, if the user guesses the correct number they break out of the "infinite loop"
# if they get the number worng, it uses a continue to ask the guess again
# if they dont input a number, it forces them to guess again             


# Data Structures

# Lists
# a list is an ordered and mutable collection of data that can be indexed to
# ex.

names = ["John", "Bob", "Jimmy", "Emily"]

print(names)

# Remember string slicing? We can do the same thing with lists
# we can acess an element by using its index
# remeber the first element is considered to be at index 0

print(names[0])
print(names[3])
print(names[-1])
print(names[0:2])


# we can also change an element in a list buy doing as follows

names[2] = "Julia"
print(names)


# Dictionaries
# A dictionary is a data structure that maps keys to values
# Each key must be unique but the values can be duplicates
# A dictionary is also ordered as of python 3.7
# they have different names in different languages but they have similar uses

grades = {"Math": "A-", "English" : "B+", "Science" : "B", "History": "A+"} # this is the syntax for a dictionary

# Each key, value pair is seperates by a :
# the value on the left of the : is the key
# the value on the right is the value
# the comma, as always, seperates the elements
# to make it easier for you to comprehend you can do this instead

grades = {"Math": "A-", 
          "English" : "B+", 
          "Science" : "B", 
          "History": "A+"}


# We access a value of the dictionary using its key

print(grades["English"]) # this is how we acces a value using its key
print(grades["History"])

# keys have to be unique because each key can only access one value
# just like a list, we can change a value like this

grades["English"] = "C"
print(grades["English"])


# Functions: Prebuilt sets of code that we can use with customized inputs as tools 

def Hello_extra(name,age,gender):
    print("Hello " + name + " you are " + str(age) + " years old and you are a " + gender) 

Hello_extra("Varun",15,"male")


Hello_extra(gender = "male", name = "Varun", age = 15)

# We can use return statements to output a value

def add(x,y):
    result = x+y
    return result

result = add(3,6) # just like saying result = 9 (remember you can store operation in varible even if they arent mathematical)
print(result)