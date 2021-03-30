#binary

x = bin(25)
print(x)

#output is 0b11001
#calculating the binary

#2 / 25
#2 / 12 - rem - 1
#2 / 6  - rem - 0
#2 / 3  - rem - 0
#    1  - rem - 1

#binary = 11001
#the 0b in the output of bin() function in python represents that the output is binary format

#print it in reverse
x = 0b11001 #because 0b represents this value is in binary format
print(x)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#octal

x = oct(25)
print(x) # 0o represents this value is in octal format

#hexadecimal

x = hex(25)
print(x) # 0x represents this value is in hexadecimal format

x = hex(10)
print(x)

print(0xf) # in reverse output is 15


#decimal
#process to determine a binary to decimal format

x = '110011010'
l,i,y = len(x),1,0

while l >= i:
    v = int(x[-i])

    if v == 0:
        pass
        #print(i-1)

    else:
        #pass
        #print(i-1)
        #print(2 ** (i-1))
        y += 2 ** (i-1)
        
    i += 1

print(y) #output is 410

print(bin(410))
