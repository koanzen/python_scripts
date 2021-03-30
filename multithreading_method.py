from threading import Thread #threading package is used for multi threading
from time import sleep #time package is used for scheduling or called schedulers

def proc1(name):
    sleep(5) #sleep delay for 5 seconds
    print('proc one -', name)

def proc2(name):
    sleep(5) #sleep delay for 5 seconds
    print('proc two -', name)

t1 = Thread(name='non-daemon', target=proc1,args='1') #create a thread for non_daemon method using argument

t2 = Thread(name='non-daemon', target=proc2,kwargs={"name":"2"}) #create a thread for non_daemon method with a use of keyword arguments

t1.start() #start the Method Thread

t2.start()

#Execution In Main Thread and non_daemon method thread
print('Test one')
t1.join()
print('Test two')
t2.join()

#or try this to see the execution 
#Execution Two
# print('Test one')
# print('Test two')
# t.join()

