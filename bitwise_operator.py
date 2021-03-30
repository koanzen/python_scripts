#Complement operator (~ tilde)
#compliment format makes your binary format to reverse
#it only applies to integral numbers. -(a+1)
#example ~0b1100 is equal to -13 because the binary 1100 is 12. soln. -(12 + 1) = -13 
x = ~12 #The value number will be converted to binary which is 0b1100
print(bin(12))
print(x)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#



#And operator (&)
#the integral numbers must be converted to binary
#12 = 1100
#AND        #Now check the binary "AND" (&) condition
#13 = 1101
#-----------
#     1100  #because in "AND" (&) operators false and true is always equals to false    

print(12 & 13) #the answer is 12 because the bitwise and of 12 and 13 in binary format is 12

#other example
print(25 & 30) #is equals to 24 why the bitwise "AND" of the two is 0b11000
print(bin(0b11001 & 0b11110)) #0b11001 is 25 and 0b11110 is 30, and the answer is 0b11000 (24)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#



#Or operator (|)
#the integral numbers must be converted to binary
#12 = 1100
#OR        #Now check the binary "OR" (|) condition
#13 = 1101
#-----------
#     1101  #because in "OR" (|) operators false and true is always equals to true  

print(12 | 13) #the answer is 13 because the bitwise "OR" of 12 and 13 in binary format is 12

#other example
print(25 | 30) #is equals to 24 why the bitwise "AND" of the two is 0b11000
print(bin(0b11001 | 0b11110)) #0b11001 is 25 and 0b11110 is 30, and the answer is 0b1111 (31)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#



#XOR operator (^)

#the integral numbers must be converted to binary
#12 = 1100
#XOR        #Now check the binary "XOR" (^) condition
#13 = 1101
#-----------
#     0001  #because in "XOR" (^) operators true and true or false and false is always equals to false  
            #and false or true is always equals to true

print(12 ^ 13) #the answer is 1 because the bitwise "XOR" of 12 and 13 in binary format is 1 (0b0001)

#other example
print(25 ^ 30) #is equals to 7 why the bitwise "XOR" of the two is 0b111
print(bin(0b11001 ^ 0b11110)) #0b11001 is 25 and 0b11110 is 30, and the answer is 0b111 (7)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Left Shift operator (<<)

print(10 << 2) #the output is 40
print(bin(10)) #the bin of 10 is 0b1010
print(0b101000)#it will move and add 2 bits to the left the output will be 0b101000 which is equals to 40


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Right Shift operator (>>)

print(10 >> 2) #the output is 2
print(bin(10)) #the bin of 10 is 0b1010
print(0b10)    #it will move and remove 2 bits to the right the output is 2



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#