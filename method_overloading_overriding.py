class ClssA:

    def __init__(self):
        pass


    def xum(self,a=None,b=None,c=None): #overloading method workaround

        a = a if a != None else 0
        b = b if b != None else 0
        c = c if c != None else 0

        return a+b+c

    def show(self):
        print("Class A")

class ClssB(ClssA):

    pass

    # def show(self):
    #     print("Class B")


class ClssC(ClssB):

    def show(self):
        print("Class C")


a = ClssA()
b = ClssB()
c = ClssC()


#calling the method overloading xum
print(a.xum(1,2))


#overide method in class inheritance

#Will call its own method show
a.show()

#Will call ClssA method show since no show method inside this class
#ClssA show method will override ClssB
b.show()

#Will call its own method show and override the show method of ClssA
c.show()