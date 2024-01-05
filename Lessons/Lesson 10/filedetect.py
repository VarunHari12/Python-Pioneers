import os

path = "C:\\Users\\varun\\Downloads\\text.txt"
# if path has backslashes, use 2 because just using one will make it look like an escape sequence

if os.path.exists(path):
    print("That location exists")
else:
    print("that location does not exist")

# can check if the path exists

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("that location does not exist")

# can check if it is a file


path = "C:\\Users\\varun\\Downloads\\folder"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a folder")
else:
    print("that location does not exist")

# can check for directory/file