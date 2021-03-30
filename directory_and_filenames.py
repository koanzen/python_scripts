# os module check and uses your current operating system environment
import os

# directory of windows os are different to mac and linux
# in windows they uses backslash "\" in mac and linux they uses "/" forward slashes

# sample of directory string formatting using join

# windows
w = "\\".join(["folder1","folder2","folder3","filename.file"])
print(w)

# mac and linux
ml = "/".join(["folder1","folder2","folder3","filename.file"])
print(ml)


# using the os module automatically detects what is your os environment.

path = os.path.join("folder1","folder2","folder3","filename.file")
# this will print the mac linux format since am using linux but if you run this scrip to windows
# it will output in windows format
# print(os.sep) # check what seperator used
print(path)


# in checking current path using the os module we will use the getcwd() method
print(os.getcwd())

# changing current directory by using the chdir() of the os method
os.chdir("/home/nexus/makery")
# this will change to the above selected directory
print(os.getcwd())

# this will last only for the entire process of the script
# so if we used any functions or methods to modify files in current directory
# for example a testing method on reading files
# a_fileread("filename.file")



# two types of file path one is absolute filepath the 2nd is relative file path

# absolute file path includes the root directory
# example of absolute directory for windows
print("C:\\dir1\\dir2\\dir3\\filename.file")


# a relative filepath are always relative to the os working current directory
# and doesnt begin with a root folder
# it always assume that the file are in the current working directory
# or in a sub directory of the current working directory

# example

print("filename.file")
# or
# this directories assumed inside the current working directory
print(".\\subdir1\\subdir2\\subdir3\\filename.file")


# the dot and dot-dot dir are special names or char used in relative directory format

# the single dot (.) stands for this directory or this folder
# you can ignore the single dot in relative path if your working already to the current path directory
# examples
print(".\\") # prints this director
print(".\\dir1") # prints this directory and its sub directory dir1
print(".\\dir1\\filename.file") # prints this directory and its sub directory dir1 and the filename

# the two dots (..) stands for the parent directory or folder

print("..\\") # prints the parent director for example the C: directory in windows
# prints the parent directory and the sub directory other_dir inside the parent directory
print("..\\other_dir")
# prints the parent directory and the sub directory other_dir inside the parent directory and the file inside the other_dir
print("..\\other_dir\\filename.file")


# other os.path module functions

# the abspath() function will add the absolute directory to the passed file name
print(os.path.abspath("classes.py")) # this will output absolute directory + filename

# you can specify also jumping out the parent folders
# this will output and jump out 2 folders above the current directory
print(os.path.abspath("../../classes.py"))

# the isabs() function will check if the passed directory is an absolute path
# if absolute path will return True if not False
print(os.path.isabs("../../classes.py")) # returns False
print(os.path.isabs("/home/nexus/makery/sandbox/classes.py")) # returns True

# the relpath() returns the relative path in a absolute path
# example

print(os.path.relpath("/home/nexus/makery/sandbox/classes.py","/home")) # will return nexus/makery/sandbox/classes.py
print(os.path.relpath("/home/nexus/makery/sandbox/classes.py","/home/nexus")) # will return makery/sandbox/classes.py

# the dirname() returns a directory except the last part of it
# example this will output /home/nexus/makery/ and doesnt include classes.py
print(os.path.dirname("/home/nexus/makery/sandbox/classes.py"))
# but if theres no filename only directory it doesnt include the sandbox directory
print(os.path.dirname("/home/nexus/makery/sandbox"))


# the basename() method is the opposite of dirname() method
# this returns only the last part of the path directory after the last slashes
# example this will output classes.py without the directory path
print(os.path.basename("/home/nexus/makery/sandbox/classes.py"))
# but if theres no filename only directory it will return sandbox folder
print(os.path.basename("/home/nexus/makery/sandbox"))


# checking files with path method using exists(), isfile(), and isdir() functions

# checks if the full path exists included filename
print(os.path.exists("/home/nexus/makery/sandbox/classes.py"))

# also works for directory paths only without filename
# checks if the full path exists
print(os.path.exists("/home/nexus/makery/sandbox"))

# we can use isfile to check if its file in the path
print(os.path.isfile("/home/nexus/makery/sandbox/classes.py")) # returns True because its a file
print(os.path.isfile("/home/nexus/makery/sandbox")) # returns False because its a directory


# the opposite of isfile() is isdir()
print(os.path.isdir("/home/nexus/makery/sandbox")) # returns True because its a directory
print(os.path.isdir("/home/nexus/makery/sandbox/classes.py")) # returns False because its a file


# other os functions
# path.getsize() and os.listdir()

# path.getsize() will return the size of the file in bytes
print(os.path.getsize("/home/nexus/makery/sandbox/classes.py")) # will return the size in bytes

# os.listdir() will return all the folder and files inside the path
print(os.listdir("/home/nexus/makery/sandbox"))


# os.makedirs() create a directory or directories inside a specified path
# this will create a sample_directory in the specified path if it not existing
new_dir = 'sample_directory'
if not os.path.isdir(f"/home/nexus/makery/sandbox/{new_dir}"):
    os.makedirs(f"/home/nexus/makery/sandbox/{new_dir}")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# sample program sum of all filesize status inside a folder
allFSize = 0

for filename in os.listdir("/home/nexus/makery/sandbox"):
    if not os.path.isfile(os.path.join("/home/nexus/makery/sandbox",filename)):
        continue
    allFSize += os.path.getsize(os.path.join("/home/nexus/makery/sandbox",filename))

print(allFSize, "bytes")