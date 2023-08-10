import random

# the random library can be used get an assortment of random values

number = random.randint(1,5) # this fucntion returns a random integer in the range of the 2 numbers specified
print(number)

number = random.random() # this will return a random decimal from 0-1
print(number)

number = random.randrange(2,10,2) # this function is similar to randint but the endrange is not included
# additionaly there is a final value that is step and it determines the increment you aare choosing from
#ex. an increment of 2 will choose from [2,4,6,8,etc.] since it has an increment of 2
print(number)



