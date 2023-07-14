
# just like with conditionals, nested loops are loops within loops

# lets make a rectangle that is 3 wide and 4 long

for column in range(1,4):
    for row in range(1,5):
        print("0",end = "")    
    print("\n",end = "")

# so how does this run?
# the second loop actually runs a total of 12 times
# essentially it prints 4 consectuive 0's
# next is starts a new line
# it repeats this process 3 times


i = 1
while i <= 4 :
    j = 0
    while  j <= 3 :
        print(i*j, end=" ")
        j += 1
    print()
    i += 1

# this prints out the first 3 mutliples of the numbers 1-4
# lets walk throught this
# when working with break and continue statements, if the break/continue is performed on the inner loop, it only performs that operation on the inner loop. If it is on the outer loop, it applies to both

# ****
# ****
# ****