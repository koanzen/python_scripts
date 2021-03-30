from threading import Thread #threading package is used for multi threading
from time import sleep #time package is used for scheduling or called schedulers

#Executions normally executes in the Main Thread
#to separate the execution of code blocks we need to seperate them in threads
#the execution of multi threads in a main threads is paralleled they are executed in the same time

class ClsOne(Thread): #Inherit the Thread class for multithreading, this will run separately in another thread not in the main thread

    def run(self): #run is invoked if we call the thread method start()
        for i in range(5):
            print('Class One', i)
            sleep(1) #sleep is used for delaying/scheduling the execution of this block of code


class ClsTwo(Thread): #Inherit the Thread class for multithreading, this will run separately in another thread not in the main thread

    def run(self): #run is invoked if we call the thread method start()
        for i in range(5):
            print('Class Two', i)
            sleep(1) #sleep is used for delaying/scheduling the execution of this block of code


#instantiate the classes
t1 = ClsOne()
t2 = ClsTwo()

#start invoking the run method of thread ClsOne
t1.start()

#the sleep here delays the start of t1 thread and after 0.2 seconds t2 thread will be executed
#so there will be a gap between execution
sleep(0.2)

#start invoking the run method of thread ClsTwo
t2.start()

t1.join() #waits the Thread One to finish and join the Main Thread
t2.join() #waits the Thread Two to finish and join the Main Thread

#Waits the two Threads to Join the Main Thread as shown above code block and executes the code below.
print('End') #This line will be executed in the Main thread since its not separately threaded