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