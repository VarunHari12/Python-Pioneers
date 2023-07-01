# lets look at a couple things you can do to strings

phrase = "Hello, how are you?"
numbers = "3452"

# here are a couple useful string methods

print(phrase.isalpha()) # Returns the boolean True if all characters in the string are in the alphabet
print(numbers.isdigit()) # Returns the boolean True if all characters in the string numbers
print(phrase.lower()) # Makes the enitre string lower case
print(phrase.upper()) # Makes the entire string upper case
print(phrase.replace("o", "a")) # Replaces all instances of the first string with the second string
print(phrase.islower())  # Returns the boolean True if all characters in the string are lowercase
print(phrase.isupper()) # Returns the boolean True if all characters in the string are uppercase

# there are tons more methods you can use and to check them out, you can head to https://www.w3schools.com/python/python_ref_string.asp