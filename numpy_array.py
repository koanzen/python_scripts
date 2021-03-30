import numpy as np


#creating array using numpy
#types of array in numpy
#array()
#linspace()
#logspace()
#arange()
#zeros()
#ones()


#sample array()
x = np.array([1,2,3,4,5]) #will show a array and what type

print(x)
print(type(x))
print(x.dtype)

#sample array() specifying type

x = np.array([1,2,3,4,5],float) #all the arrays will be a float

print(x)
print(type(x))
print(x.dtype)


#sample linspace()
#creating a array range from start to stop at specific number
#default number range if leved is 50
#but you can specify how many parts/objects of the array taht will be created
#for the start and stop number range

y = np.linspace(0,9,num=10) #this will create 10 parts/objects for the range 1 to 9
print(y)
print(type(y))


#sample of arange()
#create a array from start to stop range number by increments of steps
z = np.arange(1,15,step=2) #will output a array from 1 to 15 in increments of 2
print(z)


#sample of logspace()
#It creates an array by using the numbers that are evenly separated on a log scale.
x = np.logspace(1,20,num=5) #create an array from 1 to 20 range with 5 parts/objects
print(x)

print('%.2f' %x[2]) #show in decimal format




#sample of zeros() and ones()
#this will create how many parts/objects filled with zeros or ones

print(np.zeros(5)) #will create a array with a shape of 5 zeros
print(np.ones(5)) #will create a array with a shape of 5 ones



#Arithmetic operation inside numpy array

d = np.array([1,2,3,4,5])
d1 = d * 2 #this will multiply 2 in every element of the array you can use other arithmetic operator
print(d1)


#adding two arrays
a1 = np.array([1,3,3])
a2 = np.array([1,2,3])

a3 = a1 + a2 #this will add the two arrays per their specific index.
#the shape of the two array must be thesame.

print(a3, 'add array')


#numpy have numerical functions
#examples
a1 = np.array([1,2,3])
print(np.sum(a1)) #print the sum of the array
print(np.sqrt(a1)) #print the square root of every object of the array
print(np.average(a1)) #print the average of the array
print(np.min(a1)) #print the min of the array
print(np.max(a1)) #print the max of the array


#concatenate two array
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

a3 = np.concatenate([a1,a2]) #combined two array

print(a3)



#copying array to a new variable

a1 = np.array([1,2,3])
a2 = a1

print(a1)
print(id(a1))
print(a2)
print(id(a2))

#shallow copying
#it change the id of the array value
#but if you change the value of the main array it will inherit its value to the
#new variable
a2 = a1.view() #shallow copied the data in the variable as new id

a1[1] = 8 #changed the value of the index 1 of the array

print(a1) #print the changed array
print(id(a1)) #print its original id
print(a2) #print and inherited the changed main array
print(id(a2)) #print the new id


#deep copying
a2 = a1.copy() #deep copied the data in the variable as new id

a1[1] = 2 #changed the value of the index 1 of the array

print(a1) #print the changed array
print(id(a1)) #print its original id
print(a2) #print the unchanged coppied array
print(id(a2)) #print the new id


#Numpy multi dimentional array

arr1 = np.array([
    [1,2,3,5,8,4],
    [1,2,3,5,9,9]
    ])

print(arr1)
print(arr1.shape) #print the shape of the array
print(arr1.size) #print the size of the array

arr2 = arr1.flatten() #flatten the multidimensional array

print(arr2)

# reshaping a numpy array
# rule is the shape must be proportional to the objects
# uneven shapes will result to error
arr3 = arr2.reshape(3,4) #create a 3 rows 4 column/object array. Still 2D

print(arr3) #print the 3 rows 4 column/object array. Still 2D

#3D array

arr4 = arr2.reshape(2,2,3) #print 2 row array with 2 rows objects with 3 column object. 3D

print(arr4)



#numpy matrix
#Returns a matrix from an array-like object, or from a string of data. A matrix is a specialized 2-D array
#will be deprecated
m = np.matrix('1 2 3;1 5 3;1 2 9') #create a 2D array with 3 rows and 3 columns
m1 = np.matrix('1 2 3;1 5 3;1 2 9')

print(m) #print the matrix array
print(np.diagonal(m)) #print a diagonal array of the matrix which is [1,5,9]

m3 = m * m1 #this will do the multiplication of matrices
#     A       B
#   1 2 3	1 2 3
#   1 5 3	1 5 3
#   1 2 9	1 2 9
#this will multiply per row of A to per column of B and add the results
#sample A(B)
#1(1) + 2(1) + 3(1) , 1(2) + 2(5) + 3(2) , 1(3) + 2(3) + 3(9)
# 1+2+3 , 2+10+6 , 3+6+27
# 6,18,36 -> first row of the matrix

print(m3, ' m array') #look at the first row of the 2d array printed the same as the above output [6,18,36]


#programmatically
#multiplication of matrices

ar1 = np.array([[1, 2, 3],[1, 5, 3],[1, 2, 9]])
ar2 = np.array([[1, 2, 3],[1, 5, 3],[1, 2, 9]])

nr1,nc1 = ar1.shape
nr2,nc2 = ar2.shape

y = np.empty((0,nc2),int)

for a in range(nr1):
    
    x = np.empty(0,int)
    
    for b in range(nc2):
        
        dda = 0
        
        for c in range(nr2):
            
            dda += ar1[a][c] * ar2[c][b]
            
        x = np.append(x,dda)
        
    y=np.append(y,[x],axis=0)
    
print(y)

        