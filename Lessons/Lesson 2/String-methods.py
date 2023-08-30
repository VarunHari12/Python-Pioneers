# lets look at a couple things you can do to strings

phrase = "Hello, how are you?"
numbers = "3452"

# here are a couple useful string methods

print(phrase.isalpha()) # Returns the boolean True if all characters in the string are in the alphabet
print(numbers.isdigit()) # Returns the boolean True if all characters in the string numbers
print(phrase.lower()) # Makes the enitre string lower case
print(phrase.upper()) # Makes the entire string upper case
print(phrase.islower()) # Returns the boolean True if all characters in the string are lowercase
print(phrase.isupper()) # Returns the boolean True if all characters in the string are uppercase
print(len(phrase)) # you can use this len function to find the length of a sequence. In this case we are using it on a string

# there are tons more methods you can use and to check them out, you can head to https://www.w3schools.com/python/python_ref_string.asp