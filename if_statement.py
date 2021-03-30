x = 4
y = x % 2

#If Else Statement

if y == 0:
    print('Even') #inner statement of if statements must be indented using <tab> or 4 spaces
else:
    print('Odd')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#nested if statement

if y == 0:
    print('Even') #inner statement of if statements must be indented using <tab> or 4 spaces
    if x>5:
        print('Greater then 5')
    else:
        print('Not Greater than 5')
else:
    print('Odd')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#if elif else statement

x = 3
if x == 1:
    print('One')
elif x == 2:
    print('Two')
elif x == 3:
    print('Three')
else:
    print('Lower than One or Higher than Three')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


print('Hello') #this line is not a member of the if statement.


####
# Testing on blank data types
# all data with blank value always return False
a = None
b = []
c = ()
d = {}

if a:
    print("True")

else:
    print("False")
