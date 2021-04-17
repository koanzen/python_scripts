# some empty class
class Person:
    pass

# another class with constructor and functions
class Point:

    #Constructor is defined in __init__ function
    def __init__(self, x, y):
        #variables inside __init__ are called instance variable
        self.x = x
        self.y = y


    def move(self):
        print("move")

    
    def draw(self):
        print("draw")





point1 = Point(10,20)
##Can assign objects with value
point1.x = 30
point1.y = 20
print(point1.x)
point1.draw()

#constructor

point2 = Point(20,20)
print(point2.x)


# Set and Get Attributes from a variable to the Class object

person = Person()

first_key = 'first'
first_val = 'Secret'

# setting an attribute inside the class
# using the value of a variable
setattr(person, first_key, first_val)

# check the created attribute
# this will throw some linting problem in python cause first is not existent

#print(person.first)


# to solve the above linting problem we can use the getattr method
first = getattr(person, first_key)

print(first)