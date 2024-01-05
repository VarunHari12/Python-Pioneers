import os

destination = "testMove.txt" 
source = "C:\\Users\\varun\\Desktop\\Python Tests\\testMove.txt"


try:
    if os.path.exists(destination):
        print("There is already a file here")
    else:
        os.replace(source,destination)
        print("The file was moved")
        
except FileNotFoundError:
    print(source + " was not found")


# not anything new, just used to move the file back