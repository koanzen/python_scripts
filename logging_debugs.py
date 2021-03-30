import logging

# this is our logging format
# this will be saved in a specific directory and with a filename programlog.txt
# but if we removed the key argument filename the logging message will show into our screen
logging.basicConfig(filename='./files/programlog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# this option disables the logging from what we indicated in the argument
# this will disable logging from CRITICAL to lowest level
# so if we run again this program it will not show any logging messages
# types of loggin disable DEBUG, INFO, WARNING, ERROR, CRITICAL
#logging.disable(logging.CRITICAL)

# There are logging levels we can use in our program
# logging.debug() -> this is the lowest level
# logging.info()
# logging.warning()
# logging.error()
# logging.critical() -> This is the highest level of logging

#Factorial Sample
logging.debug('Start of program')

def fact(n):
    logging.debug(f'Start of factorial {n}')
    x = 1
    
    for i in range(1,n+1):
        x *= i
        logging.debug(f'i is {i}, total is {x}')
        
    logging.debug(f'Returning value is {x}')
    return x
	
print(fact(5))

logging.debug('End of program')