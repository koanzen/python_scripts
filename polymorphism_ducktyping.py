
class ClassOne:

    def execute(self):
        print("function one")


class ClassTwo:
    def execute(self):
        print("function two")


class ClassThree:
    def execute(self):
        print("function three")


class Execution:
    def check(self,clss):
        clss.execute() #ducktype function function in every class, the only presence we check in every class

clss = ClassThree() #Change what class you are calling
exe = Execution() #Instantiate a execution or caller class for your duck type function
exe.check(clss) #call the method or function for duck typing