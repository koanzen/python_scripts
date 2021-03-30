import csv #import the csv module


adata = open('./files/data1.txt','a') #open the file for append data

#we will append a new data to our delimetered file
#\n -> "is a new line" and \t -> "is a tab"
adata.write('\n{}\t{}'.format('4','Johny Saints'))

adata.close() #Close the file to release resources


#rdata = open('./files/data1.txt','r') #open the file
#or you can use a with block in python for more readability for file streams
#with blocks is a good practice for file streams because of its resource handling
with open('./files/data1.txt','r') as rdata:

#read the content of the open file using the csv module with a delimeter of type
#example of delimeters: ';' or '\t' -> tab
    data_read = csv.reader(rdata,delimiter='\t')
    for data in data_read:
        print(data)

    #rdata.close() #using the with block statement we dont have to use a .close() method