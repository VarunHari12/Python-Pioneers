import shutil

shutil.copyfile("testCopy.txt","testCopy2.txt") 

# copyfile just copies the contents
# copy is the same as copyfile but it also compies permisission mode and the destination can be a directory
# copy2 is the same as copy but it also copies the files metadata
# they all use the same args

# Args are the source file and destination to copy the file to
# You usually would need to pass in full path names but since both files are in the project folder, I just used the name
