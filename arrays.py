from array import array

#types of array
# 'b' - signed char - int - 1 byte
# 'B' - unsigned char - int - 1 byte
# 'u' - py unicode - unicode char - 2 byte
# 'h' - signed short - int - 2 byte
# 'H' - unsigned short - int - 2 byte
# 'i' - signed int - int - 2 byte
# 'I' - unsigned int - int - 2 byte
# 'l' - signed long - int - 4 byte
# 'L' - unsigned long - int - 4 byte
# 'f' - float - float - 4 byte
# 'd' - double - float - 8 byte


#simple example of array

x = array('i',[1,2,-3,4,5])
print(x)

#Sample use of array function.
x = array('i',[1,2,-3,4,5])
x.reverse()
print(x)


#use of loop in array
x = array('i',[1,2,-3,4,5])
for i in x:
    print(i)


#advance use of array
x = array('i',[1,2,-3,4,5])
y = array(x.typecode, (a * 2 for a in x))
print(y)


#Creating a blank array and supplying a value inside

z = array('i',[])

n = int(input("Enter range: "))

for i in range(n):
    x = int(input("Enter a number: "))
    z.append(x)

else:
    print("Finished entering numbers in range")
    print(z)


#finding index in array

srch = int(input("Find index of: "))
print(z.index(srch))