class Mamal: #Called a super class

    #constructor of a super class, all sub class that have inherit this class will have access to this and will be executed
    #if the sub class have no constructor inside
    def __init__(self):
        print("A mamal")

    def walk(self):
        print("walk")

    def spc(self):
        print("Special Mamal")

class Dog(Mamal): #Inherit all the features of Mamal super class, and is called sub class

    #This constructor is the one will be executed after instantiate even the superclass has a constructor
    def __init__(self):
        #Will execute first because of the instance of this class
        print("A dog")
        #if you want to execute the constructor of the inherited super class we need to call a special function super()
        super().__init__() #This will execute the contructor of the super class

    def bark(self):
        print("arf")

class Cat(Dog): #Inherit all the features of Dog and the inherited classes of the Dog class, and is called sub class in multilevel inheritance
    def purr(self):
        print("meow")

class Bird:

    def __init__(self):
        print("A bird")

    def twit(self):
        print('twit')

    def spc(self):
        print("Special Bird")

class Avian(Mamal,Bird): #Inheriting two super classes the Mamal and Bird class, and called multiple inheritance

    def __init__(self):
        print("Aviary")
        #This will execute the constructor of the Inherit Super Class Mamal because of the rule Method Resolution Order
        #It will execute commands from Left to Right, since Mamal ist in the left Inheritance it is the 2nd will be executed
        #After the contructor instance of this sub class
        #and methods or functions follow also this MRO
        super().__init__()
        self.bird = Bird()

    def fly(self):
        print("fly")

print("Dog Class")
print("------------------")
dog1 = Dog()
dog1.walk()
dog1.bark()
print("------------------")

print("Cat Class")
print("------------------")
cat1 = Cat()
cat1.walk()
cat1.purr()
cat1.bark()
print("------------------")

print("Bird Class")
print("------------------")
bird1 = Avian()
bird1.walk()
bird1.twit()
bird1.fly()
bird1.spc() #executes the MRO function of the Leftside Class inheritance which is Mamal
bird1.bird.spc() #executes the instanciated inherited Class Bird

print("------------------")


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Sample Inheritance and super class calls

class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self) #returns Base class print

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__() #returns Base class print

class ChildC(ChildB):
    def __init__(self):
        super().__init__() #returns ChildB class __init__ with superclass __init__ of Base Class

#Will output thesame
ChildA() 
ChildB()
ChildC()