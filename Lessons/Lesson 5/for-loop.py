# For loop is a loop that iterates through a sequence
# lets look at a basic for loop

fruits = ["apple", "orange", "blueberry", "grape"]

for i in fruits:
    print(i)

# lets break the for loop
# first of all I is just a varible and although the common term for a variable in a for loop is i, the varible i can be named anything
# to make this simpler we will just write it this way

for fruit in fruits:
    print(fruit)

# Essentially this means, for every "fruit" in the list "fruits". Print that fruit  
# The in keyword is a membership operator which means it iterates through every "member" of the fruits list
# next the instructions will occur and then it will move to the next member
# In this case it starts with apple, then it goes to orange and so on.
# remeber what we did we for loops using lists
# this is an easier and simpler way of doing that
# lets look at another example

for i in range(1,11): 
    print(i)

# range is a function that returns a sequence of numbers from the first argument to the second argument -->  range((start, inclusive),(end,not inclusive),(step, default is 1 if not specified))
# in this case, we are iterating though each value from 1-10 and printing the result
# we can iterate through any type of sequence
# we can even use a for loop on a string

word = "Hello"

for letter in word:
    print(letter)

# this will iterate though each letter of the word "Hello" and print it

# we can use for loops on sets, dictionaries, lists, tuples, and string
