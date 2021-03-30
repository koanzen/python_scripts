# common use of opening and reading files
fopen = open('./files/data0.txt')
# we can read the content of the file once so we need to open it again and read it
# so its better to put the read content in a variable
fread = fopen.read()
print(fread)

# closing the file read we need to close it
fopen.close()


## other ways in reading files
f1 = open('./files/data1.txt','r')

# writing or appending to a file
# if the file doesnt exist it will create that file
f2 = open('./files/data2.txt','w') # change the 'w' to append a data on a file

# Note: reading a file consumes the data in the file in 1 pass
# so if you print all and then print per line it will print a blank line
# Print all the content of the file
print(f1.read())

# read the open file and return it as a list
#print(f1.readlines())


# print per line content of the file
#print(f1.readline())
#print(f1.readline())
#print(f1.readline())
#print(f1.readline())


# remember we can read once the file and if is consumed already in output
# will not copy anything because the data is consumed already in print(f1.read())
# or in print(f1.readline())
# copying per line from f1 to be written in f2
for data in f1:
    f2.write(data)


# write data in data2 file
# writing in a file overwrite the content of the file
# if the file open keyword is in 'a' its in append mode so the data will be append to the file

f2.write('\n4\tJohny Saints')

#  closing f1 and f2
f1.close()
f2.close()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Reading image files using open file in binary format

#fimg = open('./files/pic.jpg','rb') #rb mean read binary

#wimg = open('./files/pic_copy.jpg','wb') #wb mean write binary

#print the binary content of the image
# for i in fimg:
#     print(i)

#read and write the binary data from fimg to wimg
# for i in fimg:
#     wimg.write(i)

#close the image file resource
# fimg.close()
# wimg.close()