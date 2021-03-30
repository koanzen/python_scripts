class Person:


    #Constructor is defined in __init__ function
    def __init__(self,name):
        #variables inside __init__ are called instance variable
        self.name = name


    def talk(self):
        print(f"Hi I'm {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()