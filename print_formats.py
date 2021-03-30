#print types and format

#print simple string using single and double quotes
print('string') #print a simple string inside single quotes

print('"string"') #print a simple string enclosed in double quotes you cannot use double quotes if you want to enclose the string in those characters

print("string") #print a simple string inside double quotes

print("string's") #print a simple string with apostrope s using double quotes cause theres a conflict between single quotes in a string

#print formats
other = 'string2'
another='string3'
print(f"string {other}") #format string using the variable name

print(r"string {other}") #this will print what's in the print function because this is a raw string

print("string {} {}".format(other,another)) #format string using the variable index

#using print seperator and end
print('string1',other,another,sep=',') #print the concatinated strings and value of variables seperated by comma

#connect/concat the succeeding prints at the end
#output is string1 string2 string3
print('string1',end=' ')
print(other,end=' ')
print(another)
