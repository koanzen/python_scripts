#Functions
#all ways use 2 block line after a function

def greet(fname, lname):
    print(f'Hello {fname} {lname}.')


#positional arguments
print("start")
greet("John", "Smith")
print("finish")

#keyword arguments
print("start")
greet(lname="Smith",fname="John")
print("finish")

#Default value arguments
def greetb(fname, lname, age=18): #age argument has a default value 18
    print(f'Hello {fname} {lname} {age}.')
    
print("start")
greetb(lname="Smith",fname="John")
print("finish")


#Variable length argument
def pinfo(name,*data): #data is a variable length argument you can pass any number of random paramters in this variable. the asterix sign indicates its has multiple parameters.
	print(name)
	print(data) #the data returns a tuple
	for x in data:
		print(x)
		
pinfo("Luck",1,2,3,"hello")


#keyword Variable length argument
def pinfob(name,**data): #data is a key variable length argument you can pass any number of random paramters in this variable. the double asterix indicates it has multiple key and parameters.
	print(name)
	print(data) #data returns a dictionary
	for x,y in data.items():
		print(x, y, ' -> keyword vars')
		
pinfob("Luck", id=123, email="email.com")


#Function's return value

def sq(num):
    return num * num


print(sq(3))

#Function's multiple return value

def mv(numa,numb):
    a = numa * numb
    b = numa + numb
    return a, b #this will return the value of a and b

x,y = mv(8,9) #assigning the return value to the inline variables.

print(x,y,' multiple ret')


#Global keyword

i = 10

def samp(num):
	global i #accessing the global var i and use it inside the function. because of the keyword global
	i = num #changing the value of the global var i making this variable not a local variable
	print(i) #expecting 12 value as assigned parameter
	
samp(12) #expecting the var value 12
	
print(i, 'expecting the global var value 10 which is not') #the value is 12 because we change the value of the global var i inside the function using the global keyword.


#sample accessing global var inside a function and also using thesame local var
def sampb(num):
	globals()["i"] = 20 # accessing outside global var using the globals() function and changing its value
	i = num # This is in the local scope not the global scope like the above line
	print(i, 'expecting local var value 12')
	
sampb(12)
print(i, 'expecting global var value 20.') #changed value inside the function using globals() function


#fibonacci sequence pattern
def fib(n):
	a=0
	b=1
	print(a,b,sep=' ',end=' ')
	for _ in range(n):
		c = a + b #incremental of a and b
		a = b #the value of b is shifted to a
		b = c #the value of c is will be supplied to b
		print(c,end=' ')
	print('fibonacci sequence')

fib(5)

#=-=-=-=-==-=-=-=-=-==-=-=-=-=
#sample function 1 odd even

def oddeven(lst):
	
	even=0
	odd=0
	
	for x in lst:
		if x%2==0:
			even += 1
		else:
			odd += 1
		
	return even,odd
		
lst = [1,2,3,4,5]
y = 'etc'

e,o = oddeven(lst)
print(e,o, " even, odd")
print(f"even {e} odd {o}")
print("even {} odd {} note {}".format(e,o,y))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Factorial

def fact(n):
	
	x = 1
	
	for i in range(1,n+1):
		x *= i
	
	return x
	
print(fact(5))


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Recursive Factorial

def rfact1(n):
	
	if n == 0:
		 return 1

	return n * rfact1(n-1)

print(rfact1(5))


#or

def rfact2(n):
	
	x = n
	
	if n != 1:
		x *= rfact2(n-1)
		
	return x
	
print(rfact2(5))
		


#=-=-=-==-=-==-=-=-==-=-=-=-
#SAMPLE Functions 2
def emoji(msg):
	
	words = msg.split(' ')
	
	emojis = {":)":":smile:",":(":":sad:"}
	
	outp = ""
	
	for word in words:
	   	outp += emojis.get(word, word) + " "
	   	
	return outp

msg = input("input emoji code > ")
print(emoji(msg))


