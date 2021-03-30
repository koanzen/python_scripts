#Arithmetic Operators
#but used in assignment operation

x = 10
y = 3
z = x + y #Addition
a = x - y #Subtraction
b = x * y #Multiplication
c = x / y #Division
d = x % y #Modulus
e = x ** y #Exponent (or power)
f = x // y #Floor Division (Will get the Floor of the quotient)

print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Assignment Operators

g = e + 2 

#augmented assignment arithmetic opertor
g += 2 #equals to 12
g *= 3 #equals to 36
g -= 2 #equals to 34
g /= 2 #equals to 17.0 since division quotient is a float

print(g)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Unary Operator (arithmetic operator that will multiply to the value of the variable)

h = 8
print(h)
h = -h
print(h)
h = -h
print(h)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Relational Operators

i = 3
j = 9

k = i<=j
print(k)

k = i>=j
print(k)

k = i != j
print(k)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Logical Operators (AND or OR)


i = 3
j = 9


k = i < 8 and b < 5
print(k)

k = i < 8 and b > 5
print(k)

k = i < 8 or b < 5
print(k)

k = i > 8 or b < 5
print(k)

k = True
print(k)
k = not k #(not logical operator reverses the boolean value)
print(k)


# The IN operator
lst = [1,2,3]
if 3 in lst:
    print("True")
else:
    print("False")