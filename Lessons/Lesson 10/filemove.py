import os

source = "testMove.txt" # source location of og file
destination = "C:\\Users\\varun\\Desktop\\Python Tests\\testMove.txt" # destination of moved file (you can change the name)


try:
    if os.path.exists(destination):
        print("There is already a file here")
        # Checks if a file with that name is already in that location
    else:
        os.replace(source,destination)
        print("The file was moved")
        # moves the file 
        
except FileNotFoundError:
    print(source + " was not found")
    # makes sure a file exists


# the replace method can be used to move a file or directory from its source to a destination
