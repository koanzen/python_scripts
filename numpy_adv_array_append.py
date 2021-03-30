import numpy as np

x = np.empty((0,3),int) #initializing a blank mutidementional array with a shape of (0,3) 0 rows and 3 columns

#try appending arrays
y = np.array([[1,2,3]]) #the array value to be inserted must be thesame shape
x = np.append(x,y,axis=0) #must have axis because if theres no axis it will be flatten

y1 = np.array([[1,2,3]])
x = np.append(x,y1,axis=0)

y2 = np.array([[1,2,3]])
x = np.append(x,y2,axis=0)

y3 = np.array([[1,2,3]])
x = np.append(x,y3,axis=0)

print(x)