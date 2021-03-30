lst = [1,2,3]

def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq #yield is a keyword for a generator and a iterator is generated
        n +=1


vals = topten() #vals is a new iterator from a method yielded data

vals2 = iter(lst) #vals2 is a new iterator from a list data

print(vals2.__next__()) #beginning iterate the iteration data of the vals2
print(next(vals2)) #second iterate the iteration data of the vals2, using a next() method they are thesame as __next__

print("----------------------------------------------------------------")

#use for loop to iterate through data yielded vals
for i in vals:
    print(i)
