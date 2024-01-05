text1 = "My\nName\nIs\nVarun"
text2 = "\nAnd\nI\nAm\10"
created = False

try:
    with open("testWrite.txt","w") as file: # since this file is in the project folder, I only need the name. Usually you should use the path. "w" stands for write and is the moade Im opening the file in
        file.write(text1)

except FileNotFoundError:
    print("this file does not exist")
else:
    created = True


with open("testWrite.txt","a") as file: # since this file is in the project folder, I only need the name. Usually you should use the path. "a" stands for append and is the moade Im opening the file in
        print(file.write(text2))