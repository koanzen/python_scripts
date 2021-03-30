#None (If a variable is not assigned equivalent of null)

x = None
print(x)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Numeric (float, int, complex, bool)

#float (are with decimal numbers)
x = 3.9
print(type(x))

#int (are absolute number)
x = 9
print(type(x))

#converting float to int
a = 3.9
b = int(a)
print(b)
print(type(b))

#convert int to float
k = float(b)
print(k)
print(type(k))

#complex (value which have a number and mathematicaly partnered with a imaginary number)
#the indicator for complex number is j
x = 9 + 3j
print(type(x))

#convert numbers to complex
z = complex(b,k)
print(z)
print(type(z))

#bool or boolean for decision conditions
y = 9 < 3 #will output False
print(y)
print(int(True)) #will return numerical representation of True
print(int(False)) #will return numerical representation of False

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#String

str1 = "This is a string"
str2 = 'This is a String'

print(type(str1))
print(type(str2))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#List

lst = [1,2,3,4,5]
print(type(lst))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Tuple

tup = (1,2,3,4,5)
print(type(tup))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Set

s = {1,2,3,4,5}
print(type(s))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Range (only found in python)

print(type(range(10)))
print(list(range(10)))
print(list(range(2,10,2)))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Dictionary

d = {
    "1":"user1",
    "2":"user2",
    "3":"user3"
}

print(d.keys())
print(d.values())
print(d["3"])
print(type(d))