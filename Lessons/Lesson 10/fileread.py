try:
    with open("testRead.txt","r") as file: # since this file is in the project folder, I only need the name. Usually you should use the path. "r" stands for read and is the moade Im opening the file in
        print(file.read())

except FileNotFoundError:
    print("this file does not exist")

# Here I open the file and assign it to the file variable. I then print out the contents of the file

# using a with statement automatically closes the file you are working with after the code segment is run

# file.closed() checks if the file is closed

# using as staement defineds an alias for something. In this case file is assigned to the file of testDoc