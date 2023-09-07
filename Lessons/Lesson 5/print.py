sum = 0

for number in range(1,11):
    sum += number
    
print(sum)

integer = int(input("Give me a number: "))

increment = 1
sum = 0

while increment <= integer:
    sum += increment
    increment += 1
    
print(sum)