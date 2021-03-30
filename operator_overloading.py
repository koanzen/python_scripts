# x = 1
# y = 2

# z = int.__add__(x,y) #builtin function __add__ in a int data type

# print(z)

#we will use the __add__ function inside a function

class Claxx:

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other): #will be called if a two class instance is added "+"
        n1 = self.n1 + self.n2
        n2 = other.n1 + other.n2
        n3 = Claxx(n1,n2)
        return n3

    def __gt__(self,other): #will be called if a two class instance uses a conditional operator > "greater than"
        g1 = self.n1 + self.n2
        g2 = other.n1 + other.n2
        return True if g1 > g2 else False

    def __str__(self):
        return f'{self.n1}, {self.n2}'



a = Claxx(1,2) #instantiate a new object a
b = Claxx(3,4) #instantiate a new object b

#This will represent the Claxx.__add__(a,b), in the class because it will look the + sign as __add__ inside the class
#Claxx.__add__(a,b) the "a" is self "b" is other
c = a + b
print(c.n1 + c.n2)

#This will represent the Claxx.__gt__(a,b), in the class because it will look the > sign as __gt__ inside the class
#Claxx.__gt__(a,b) the "a" is self "b" is other
if a > b:
    print("True")
else:
    print("False")

#call the __str__ function
print(a)
