class Module:

	#variable outside __init__ constructors are called class variables
	#this is shared throughout the variable
	vara = 1

	if __name__ == "__main__": #checking if current module is the 1 running or been called by other module
		pass

	def __init__(self,age): #constructor of our class module
		#variables inside __init__ are called instance variable
		self.age = age #instantiate the argument x to instance variable self.x
		self.Etc = self.Others(None) #instantiate the inner class Others with constructor arg value None

	def clean(self,dataset): #method or functions of our class module, in instance level indicated by self argument
		container = []
		for data in dataset:
			if data not in container:
				container.append(data)
		return container
	
	def compare(self,others):
		return True if self.age == others.age else False #This is a ternary operator

	#This are setters ang getter method or accessor and mutator metthods
	def get_vara(self): #accessor instance method, in instance level indicated by self argument
		return self.vara

	def set_vara(self,nvara): #mutator instance method, in instance level indicated by self argument
		self.vara = nvara

	
	@classmethod #this decorator indicates the function or method defined is in the class level
	def cls_getvara(cls): #accessor class method, argument is cls
		return cls.vara

	@classmethod #this decorator indicates the function or method defined is in the class level
	def cls_setvara(cls,nvara): #mutator class method, argument is cls and passing a another argument
		cls.vara = nvara


	@staticmethod #static methods are useful for uninstantiated class objects
	def stat_vara(a,b): #as you can see there is no self argument for instance and we cannot use any instance level objects in this function
		return a + b

	
	class Others: #Inner class that can be used or called in this module

		def __init__(self,name): #constructor of the inner class
			self.name = name

		def get_name(self): #accessor of the inner class
			return self.name