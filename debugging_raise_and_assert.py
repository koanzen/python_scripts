import os, traceback

# Sample of raising exception
# raising exception are commonly used to user error but it depends and dabatable
# this is called Traceback
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


# we can log this tracebacks in a file using the traceback module

try:
    boxPrint('$',2,2)
except Exception as e:
    errFile = open('./files/error_log.txt','a') # opening a log file in append mode
    errFile.write(traceback.format_exc()) # getting the exception traceback of the try catch
    errFile.close() # close the log file
    print("Traceback Exception encountered written in error log.")



# Assert is a kind of exception handling commonly used for programmers error but it depends and debatable
# this is used to check some unexpected error in the code
# example

traffic_lights = {"nw":"green", "ew":"red"}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # assertion always check if this conditions is True else it will throw an exception, it is called sanity checks
    # useful in programming debugging purpose and without using the try catch error for fast debugging
    assert 'red' in intersection.values(), f"There is no red in trffic light in {str(intersection)}"

print(traffic_lights)
switchLights(traffic_lights)
print(traffic_lights)
