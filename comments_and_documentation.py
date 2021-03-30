#This is a comment
#used to comment codes
#and some remarks

#documentation docstring is good if you want to document your classes and methods
class ClsNothing(object):
    """This is a documentation for docstring type class""" #This is a docstring documentation in class level

    def nothing(self):
        """This is a documentation for docstring type function""" #This is a docstring documentation in method level
        pass


clx = ClsNothing() #calling this class will show the written docstring for class

clx.nothing() #calling this function will show the written docstring for method