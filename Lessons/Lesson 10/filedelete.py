import os
import shutil

path = "testDelete.txt" # since the file in in my project folder, I can just use the file name. Usally you should use the entire path

try:
    os.remove(path)
except FileNotFoundError:
    print("this file does not exist")


# os.remove can be used to delete a file at a given path
# to delete an empty folder, you can do os.rmdir(path)
# to delete a folder with files in it, use shutil.rmtree(path)
# some other erros you can encouter are OSErros or PermissionErrors