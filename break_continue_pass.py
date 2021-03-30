#samples of "break"

cnt = 10

inp = input("Enter number of candies ")
inp = int(inp)

i = 1

while i < inp:
    if i > cnt:
        print("Out of stock")
        print(f"We only have {cnt} candies in stock")
        break #"break" will stop the process
    else:
        print("candy " , i)
    i += 1



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#Sample of "continue"

for x in range(1,21):
    if x%2!=0 :
        continue #skip the process of the statement and go back to the for loop
        print("Hello") #This will be skipped because of the "continue" keyword
                       #and will execute the next statement which is the print(x)

    print(x, "Sample Continue") #This will only print all even numbers because of the condition above
             #with a command "Continue" it will skip all the numbers that are not even


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#Sample of "pass"
#you can also use pass inside a function or class
#Pass is just "there is no code to execute here"

for x in range(1,21):
    if x%2!=0 :
        pass #"pass" indicates "there is no code to execute here" but if the next line has statements
        print("Hello") #it will be execute the print("Hello")

    print(x) #all in range will be printed because the condition above has no process