# os module check and uses your current operating system environment
import os


# if we need to walk all throug sirectory and subdirectory of a specific folder
# we will use the os.walk() function
# the value of this function is a iteration and return a 3 arguments
# we can use this to manipulating files and directory for automation.
for parentdir, subdir, filename in os.walk("./backup"):
    print("parent directory:",parentdir) # this returns a a string of the parent directory for each directory iteration
    print("sub directory:",subdir) # this returns a list of subdirectories inside the current parent directory iteration
    print("file names:",filename) # this returns a list of filenames inside the current parent directory iteration