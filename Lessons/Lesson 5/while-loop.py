# While loop is a loop that continues to iterates as long a certain condition is true
# think of it as an if statement that constantly keeps replaying itself

# ex.
x = 0

while x < 10:
    x += 1 # this is called an assignment operator (it is the same as saying x = x+1) it just adds whatever value you put to the varible
    print(x)

# this while loop prints out all the numbers from 1-10

# lets break down the anatomy of a while loop

# while (condition) == True:
#   instructions

# just like if statements, you have to add an indent

# one thing that is important is to prevent something called an infinite loop
# an infinite loop is when a loop never stops
# the way to prevent this is to make sure that there is always a way to stop the loop
# in the case above, I incremented x to print all the varibles but also to eventualy make the loop stop
# to stop an infinite loop do Ctrl C

# lets look at an example of a infinite loop

# x = 1
# while x != 10:
#   x += 2
#   print(x)

# if we ran this the result would be 3,5,7,9,11,13,15,17 etc.
# since it x would never = 10, the loop would run infinitely

# here is another while loop for you to look at

names = ["Jim","John","Michael","Bob"]

index = 0

while index < len(names):
    print(names[index])
    index += 1

# this is a little more complicated so let me walk you through it
# this would be easier to write with a for loop which we will cover later in this lesson

# with while loops, just like if statements, you can use logical operators for more complex statements

# x = 0
# while (x < 10) or (x != 5): 
    # x += 1 
    # print(x)

# why does this produce an infinite loop?

# remeber you have to be carfeul especially when you are using logical operators
# this is why it is important for you to have  fundamental understanding of logical operators
# the correct way to write this is

x = 0
while (x < 10) and (x != 5): 
    x += 1 
    print(x)

# why does this work and the other doesn't?

# In conlcusion, while loops 