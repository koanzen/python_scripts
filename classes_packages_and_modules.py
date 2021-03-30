from packages.module import Module as mod

dataset = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,8,8,8,8,8,8,8,8,9]

#Instantiate a class to represent a new class object
mod1 = mod(25) #instantiate our class object to a new object mod1 and pass a value to our constructor

mod2 = mod(30) #Instantiate a new class object

#use mod1 instance class object to print unique number in dataset list
#instantiated object has a 1 positional argument for "self" pointer
print(mod1.clean(dataset), "dataset with instantiate")

#you can change pointer class variables if it's been instantiated
mod2.age = 25 #Change the mod2 instantiated class object variable age to 25

mod1.vara = 3 #change the class variable vara in instance level mod1
print(mod1.vara, 'print via mod1 class variable in instance level')

#print the vara variable in instantiated mod2
print(mod2.vara, 'print via mod2 class variable in instance level')

#print the original class variable value even we are using a instantited class object mod1
#this is possible if we created a decorated function or method using a class level object
#the method use the @classmethod decorator
#check the module.py
print(mod1.cls_getvara(), 'print via class method, the output is the default value of the vara class variable')
print(mod1.vara, 'check the difference of the class level variable and the instance level variable')

#Lets try to change the value of the class variable vara using a class method mutator
mod1.cls_setvara(9)
print(mod1.cls_getvara(), 'print via class method, showing the changed value of the class variable vara via class method mutator')


#change value of vara in mod2 class instance using a mutator method set_vara
mod2.set_vara(8)
print(mod2.get_vara(), 'print via mod2 class function change by mutator method')



if mod1.compare(mod2) == True: #comparing the 2 instantiated classes constructed age
    print("Age are the same.")
else:
    print("Age are different.")



#sample without instatiating our class using a @staticmethod decorator
#you can't use a instance class because of the positional argument "self" pointer
#this static methods are usefull as ustility methods
print(mod.stat_vara(3,5), "static method without instantiate")


mod3 = mod(99) #Instantiate a new class object
others1 = mod3.Etc #instantiate the innerclass Etc of the main outer class instance
others1.name = "John" #Change the inner class instance variable name
print(others1.get_name()) #calling the inner class accessor method

others2 = mod3.Others("Doe") #Instantiate a new class object for the Inner class of "Module" outer class
print(others2.get_name()) #calling the inner class accessor method