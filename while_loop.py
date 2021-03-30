i = 1
x = 5

#while loop increment sample

while i <= 5:
    print(i)
    i = i + 1

print('End Increment')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#while loop increment sample

while x >= 1:
    print(x)
    x = x - 1

print('End Decrement')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#nested while sample
#the output is
#Head Body Body Body Body
#Head Body Body Body Body
#Head Body Body Body Body
#Head Body Body Body Body
#Head Body Body Body Body

x = 1

while x <= 5:
    y = 1
    print('Head ', end="") # the (end="") will print the output inline
    while y <= 4:
        print('Body ', end="")
        y = y+1
    x = x+1
    print() # This will print only a new line


#while else statement it will finish iterating the range loop and output after finishing it with else

z = 1

while z <= 5:
    if z % 2 == 0:
        print(z)
    z += 1
else:
    print('Finished Iterating')