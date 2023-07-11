import random

# Data structures are the fundamental constructs around which you build your programs. Each data structure provides a particular way of organizing data so it can be accessed efficiently, depending on your use case. 
# there are 4 basic types of data structures in python



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

# we can also change an element in a list buy doing as follows

names[2] = "Julia"

# elements of a list can be anything even other lists

people = [["John",35],["Jeff",17],["Bob",23]]

# when you have a list of lists, it is called a multidimesional list

print(people[1])

# to index into a specific element of a multidimensional list you can do this

print(people[0][1])

# this is essentialy the same as saying taking the second element of the first list


# there are also many methods that can be run on lists
# here are a few useful ones

ages = [12,34,11,67,49,35]

print(ages)

ages.append(17) # adds the element to the end of the list
print(ages)

ages.insert(4,42) # inserts the second parameter as an element in the first parameter's position in the list
print(ages)

ages.remove(34) # removes the first instance of the element in the list
print(ages)

age = ages.pop(3) # pop is similar to remove excpet it actually stores the removed item and also instead of using the element, it uses the index of the element. If no parameter is passed, pop just removes the last element of the list
print(age)

# You can find the length of a list by using the len function

length = len(age)
print(length)

choice = random.choice(ages) # using this function from the random library allows you to make a random choice from a list or othr data structure
print(choice)

shuffle = random.shuffle(ages) # this function will completely randomize the order of whatever list you pass through
print(shuffle)


# to learn more list functions you can go to https://docs.python.org/3/tutorial/datastructures.html



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

# We access a value of the dictionary susing its key

print(grades["English"]) # this is how we acces a value using its key
print(grades["History"])

# keys have to be unique because each key can only access one value
# just like a list, we can change a value like this

grades["English"] = "C"
print(grades["English"])

# here are some useful methods you can use with dictionaries

print(grades.get("Math")) # this essentialy does the same thing as grades["Math"] but instead of returning an error if the key is not found, it returns None

print(grades.keys()) # returns a list containing all the keys in the dictionary

print(grades.values()) # returns a list containing all the values in the dictionary

print(grades.clear()) # clears the dictionary

# again there are many more methods to explore and you can see them here https://www.w3schools.com/python/python_ref_dictionary.asp


# Tuples
# a Tuple is very similar to list except it is not mutable and in some ways faster to access efficiently
# there are many other costs  and benefits to using tuples and they are listed here https://www.upgrad.com/blog/list-vs-tuple/
# the syntax is the name except instead of [] you use () and you cant perform many of functions above

# Set
# A set is a collection which is unordered, unchangeable, and unindexed.
# even though I said unchangeble, you can still remove and insert items you just cant change the value of those items
# with unordered data structures, there can be no duplicates


# you can also use casting on data structures by using th same methods we were using in the past


names = ("Bob","John","Max")

print(names)

names = list(names)

print(names)

