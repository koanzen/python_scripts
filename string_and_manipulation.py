# Strings are immutable or cannot be change

str = "This is a string"

#getting the character in a string using index
iStr = str[3]
print(iStr, "- Character in a particular index of a string")

#getting the index of a character in a string

strIndex = str.index('a')
print(strIndex, "- index of a character in a string")


#slicing a string
neoStr = str[0:8]

print(neoStr, "- Sliced range of a string")


#check if a character is existing in a string
x = 'a' in str

print(x,"- Checking if a character is in the string")

#or checking a string if exist inside the string

x = 'is a' in str

print(x,"- Checking if a string is in the string")



#multi line strings
#we can use "\" back slash to continue a next line of string


str1 = 'Hello ' \
    'World'

print(str1)

# Or using a ''' triple single quote or """ triple quotes

str2 = """Hello 
World and Mars,

Venus, Jupiter, Saturn and

The Universe"""

print(str2)


#string formatting samples

name = "Alice"

print('Hello %s' % (name), "- Sample string formatting 1")
print('Hello {}'.format(name), "- Sample string formatting 2")
print(f'Hello {name}', "- Sample string formatting 3")


#string functions

msg = "Hello World"

msg1 = msg.lower()
msg2 = msg.upper()
msg3 = msg.swapcase()

print(msg1,"- become all lowercase")
print(msg2,"- become all uppercase")
print(msg3,"- become swapcase or camelcase")

a = msg.islower() #check if string is in lowercase
b = msg.isupper() #check if string is in uppercase
b1 = msg2.isupper()

c = msg.isalpha() #check if string is in alphabet only
c1 = "Hello".isalpha()

d = msg.isalnum() #check if string is in alphanumeric
d1 = "Hello123".isalnum()

e = "123".isdecimal() #check if string is in decimal

f = msg.isspace() #check if string is in all white spaces

g = msg.title()
print(g," All beginning leters of words become capital.")
g1 = g.istitle() #check if string is in title format

h = msg.startswith("He")
h1 = msg.endswith("orld")

print(a,b,b1,c,c1,d,d1,e,f,g1,h,h1,"- Checking the string format case")


# if you make your string to a list you can join them back together using the Join method

lstr = list(msg)


#Joining back the List to string
nstr = ''.join(lstr) #You can change the blank string into any character and the list will be delimetered by that string 

print(lstr,"- to -",nstr)


# The reverse of joining is split() split default to return a string from a string delimetered by white spaces
# sample split
sstr = msg.split() #splitting the string using default white spaces
print(sstr, "Splitted string via spaces") #this will return a list containing ['Hello', 'World']

sstr1 = msg.split('l') #you can also indicate what character you want to use in spliting a string
print(sstr1, "Splitted string via l") #this will return a list containing ['Hello', 'World']


#Justifyin string to a specific length by adding white spacing padding
#we can use rjust and ljust methods to do this

x = "Hello".rjust(10) #padded with white space at the right
y = "Hello".ljust(10) #padded with white spaces at the left
z = "Hello".ljust(10,"x") #you can specify a fill other than white space

print(x,y,"Padded by white spaces so the total lenght of the strings is 10")
print(z,"Padded fill with 'x' character so the total length of the string is 10")


# You can also center your string using a center method
z1 = "Hello".center(11,"*")

print(z1,"The string is in the center of *")



#You can also strip padded white spaces or characters from left and right using the strip methods
print(x,y, "- The x and y value")
print(x.strip(), "- strip the padded left and right white spaces of x")
print(x.lstrip(), "- lstrip the white spaces of x")
print(y.rstrip(), "- rstrip the white spaces of y")

print(z1.strip("*"), "- strip the padded character * of z1")

print("Hello World".strip(), "- to prove it only strip the left and right paddings")



#if you want to change or remove a character or string in a string you can use the replace method

print("Hello World".replace(' ','')) #replace the whitespace with a blank character
print("Hello World".replace(' ','X')) #replace the whitespace with a X character
print("Hello World".replace('World','Earth')) #replace the World with a Earth string