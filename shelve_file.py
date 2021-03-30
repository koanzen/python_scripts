# import the shelve and os module
import shelve
import os


#print(os.getcwd())

# change directory to save your shelve file
# the directory is in the current directory / files
os.chdir(f"{os.getcwd()}/files")

# open our shelve data file
# if the shelve file doesnt exist it will create the file
# the file format created are diferent for other operating system
fshelf = shelve.open('mydata.dat') # you can specify a extenstion

# here we will create a variable index inside our shelve file named users
# we can save datas like lists, dictionary, text inside our shelves and this will be saved in binary format
#fshelf['users'] = ['user0','user1','user2','user3']

# just like other data we can print out the value of the index
print(fshelf['users'])


# showing the keys inside the shelve
print(list(fshelf.keys()))


# showing the values inside the shelve
print(list(fshelf.values()))


# after reading our shelve file we need to close it
fshelf.close()