# there are 2 statements that can be useful when using loops
# break
# continue

# Continue
# the continue statement essentially skips the rest of the instructions for that iteration and moves to the next iteration of the loop
# ex.

numbers = [9,11,13,14,17,9,9]
for i in range(0,len(numbers)):
    number = numbers[i]
    if number >= 10:
        continue
    number += 1
    numbers[i] = number

print(numbers)

# in this case, we are adding 1 to all the numbers in the list that are below the value of 10
# by using the continue statement, we are able to only add to the numbers below 10 and skip the numbers that are above or equal to 10

# here is an example with a while loop

# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)

# by using the continue statement we can skip printing all the numbers that are even and only print the odds


# Break
# The break statement completely ends the loop no matter if the condition is satisfied


for i in range(10):
    print(i)
    if i == 2:
        break

# this is a simple non practical case they just showcases the use of the break statement
# here is a more practical one


numbers = []

number = 15

while True:
    guess = input("Guess my number (1-20): ")
    digit = guess.isdigit()

    if digit:
        if int(guess) == number:
            print("You got the number correct! ")
            break
        else:
            print("You got it incorrect! ")
            continue

    print("please input a digit")

# In this case we are actually using a break and a continue
# In this case, if the user guesses the correct number they break out of the "infinite loop"
# if they get the number worng, it uses a continue to ask the guess again
# if they dont input a number, it forces them to guess again           