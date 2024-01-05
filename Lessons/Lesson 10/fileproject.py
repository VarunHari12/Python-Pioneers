import shutil
import os

print("Lets mess around with some files")

# mode and source path
mode = input("What mode would you like to enter (w,a,r,d,m,c): ")
path = input("Please enter the path for your file: ")


# Variable that checks to see if a file already exists
exists = True

try:

    # Checks to see if the given path exists
    if mode == "r" or mode == "d" or mode == "m" or mode == "a":
        if not(os.path.exists(path) and os.path.isfile(path)):
            exists = False
        
        # read mode
        if mode == "r" and exists == True:
            with open(path,"r") as file:
                print("This is the contents of the file you have provided: ")
                print(file.read())
        
        # delete mode
        elif mode == "d" and exists == True:
            os.remove(path)
            print("The file " + path + " has been deleted")
        
        # move mode
        elif mode == "m" and exists == True:
            destination = input("Please input the path in which you want to move your file to: ")
            os.replace(path,destination)
            print("Your file has been moved to " + destination)
        
        # append mode
        elif mode == "a" and exists == True:
            with open(path,"a") as file:
                text = input("What text would you like to add to the file: ")
                text = "\n" + text
                file.write(text)
        
        # if the file does not exist, it tells the user that the file does not exist
        elif exists == False:
            print("This file path does not exist")
        
        # if the mode is not one of the options, it tells the user that the mode is not elligible
        else:
            print("This is not an elligible mode")

    else:
        
        # write mode
        if mode == "w":
            with open(path,"w") as file:
                text = input("What would you like your text file to say: ")
                file.write(text)
        # copy mode
        if mode == "c":
            destination = input("Where would you like to copy your file to: ")
            shutil.copy2(path,destination)

# Error catchers

except FileNotFoundError as  e:
    print("The file does not exist")

except PermissionError as e:
    print("You do not have permission to edit this file")
  

# example of using a combination of file extraction techniques