a = 9
b = 0

try: #executing a block of code to be checked
    print("Source block execution") 
    print(a/b)

except Exception as e: #this is a basic handling of exception and substituting what exception to e
    print("Can't divided by zero -", e) #printing a message with the "e" exception type

finally: #This will be executed even theres a exception encountered
    print("Exiting block execution")


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

try: #executing a block of code to be checked

    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))

    print("Source block execution") 
    print(x/y)

except ZeroDivisionError as e: #this is a specific handling of exception and substituting what exception to e
    print("Can't divided by zero -", e) #printing a message with the "e" exception type

except ValueError as e: #specific exception checking the a value format
    print("Theres a value error -", e)

finally: #This will be executed even theres a exception encountered
    print("Exiting block execution")


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# define Python user-defined exceptions

class AnythingErr(Exception): #basic custom exception inheriting Exception object
    pass

class ValueTooSmallError(Exception): #Advance custom exception with return message
    def __init__(self, message='Negative Value'): #Constructor for the message
        # Call the base class constructor with the parameters it needs
        #super(ValueTooSmallError, self).__init__(message) #This is the old way of using super on current class
        super().__init__(message) #returning the super class inheritance which is Exception and construct the message var instance


class ValueTooLargeError(Exception): #Advance custom exception with return message
    def __init__(self, message='Positive Value'): #Constructor for the message
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

x = 1

try: #block of code that raises Exceptions
    if x < 0:
        raise ValueTooSmallError #Raise Exception for Negative number
    else:
        raise ValueTooLargeError #Raise Exception for Positive number

except ValueTooSmallError as e: #Exception for Negative number
    print("Lower than zero -", e)

except ValueTooLargeError as e: #Exception for Positive number
    print("Higher than zero -", e)

finally: #This will be executed even theres a exception encountered
    print("Exiting block execution")