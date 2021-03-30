#Function decorators
#You can modify the flow of a existing function by using a decorator function without modifying the main function


#decorator function you can use to change the logic process use of the main function
def smart_div(func): #created function accepting a parameter value of a function

    def inner(a,b): #inner function acting as a wrapper for our logic for the main function
        if a<b:
            a,b = b,a #swapping variables
        
        #returning our main function with modified parameters logic of a and be which if a is less than b they will swap
        return func(a,b)
    
    return inner #return the inner wrapper function to be used to istantiate and substitute to a variable object

#Main function that you want to modify using a decorator
#@smart_div #@ symbol and the name of the decorator method is a syntactic sugar to implement decorators.
def div(a,b):
    return a/b

#Reassign/Instantiate the variable div and passing the main function div(a,b) to the decorator function smart_div(func)
div = smart_div(div)

print(div(2,4), '- Output of decorator function') #using the instantiated variable div as a function

