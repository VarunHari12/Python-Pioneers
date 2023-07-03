# There are lots of things you can do with strings


# String slicing
# extracting a part of the string

# ex.

# syntax for string slicing is (string variable name)[(start):(end):(step)]
# an index is python is the position a certain item is in a sequence
# In python and most other languages, indexes start at a value of 0

# example for a string

#  I love dogs
#  012345678910


word = "Hello"

# if we want one specific letter we can do this

print(word[2]) # this will print l

print(word[0]) # this will print H

# if we want to obtain a part of the word we can do this

print(word[0:2]) # this will print He

# the start. (the first number), is inclusive but the end, (the second number), isnt
# additionaly we can do the same thing we did above by doing this

print(word[:2])

# when you put nothing between the colon, it defaults to choosing the start/end

# these print the same
print(word[2:5])
print(word[2:])

# this is another example of this principle
# it can be useful if you dont know the length of the string you are working with 

# you can also use something called negative indexing
# in this case, and index of -1 is the last character, -2 is the second to last and so on
# this can again be useful if you dont know what index the end of the string is 

print(word[-1]) # last letter
print(word[1:-2]) # ever letter up to the last 2
print(word[-3:]) # the last 3 letters


# now lets talk about the third value, the step
# this determines how much you want to jump by when the program slices your string
# the default value if you put nothing is 1
# ex.

print(word[::2]) # every other letter since it skips one

sentence = "The quick brown fox jumps over the lazy dog"

print(sentence[2:12:2]) # prints eqikb

# we can also print things in reverse by doing this

print(sentence[::-1]) # prints god yzal eht revo spmuj xof nworb kciuq ehT
print(sentence[::-2]) # prints gdya h eosmjxfnobkiqeT





