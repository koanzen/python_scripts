import re


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# regular expression commonly uses bakc slashes "\"
# \d indicates numeric digit character 
regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# Or

# numbers in curly brackets example {3} after a pattern is like saying, “Match this pattern three times.”
regex1 = re.compile(r"\d{3}-\d{3}-\d{4}")

# search method - look for the first occurence of the pattern in the string
# this method returns a match object
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match index.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
mo = regex.search(message)
print(mo.group()) #only the first occurence will be returned

#grouping regular expression using a parenthesis
regex2 = re.compile(r"(\d{3})-(\d{3}-\d{4})")
mo = regex2.search(message)

print(mo.group(1), "group by parenthesis geting the first group")
print(mo.group(2), "group by parenthesis geting the second group")


#If the string has a pharentesis you need to add the parenthesis character in the regular expression by using \( and \)
# Example
#phone numbers where area code is inside a parenthesis
message1 = 'Call me at (415)-555-1011 tomorrow. (415)-555-9999 is my office.'
regex3 = re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})") #see regex gouped but inside \( and \) are added
mo1 = regex3.search(message1)
print(mo1.group(), "Full contact number")
print(mo1.group(1),"The area code inside a parenthesis")
print(mo1.group(2),"The phone number")



# pipe character "|" used in regex to match several patterns

msg = "I love kiwi like wine."

sregx = re.compile(r"(apples|banana|orange|grapes)") # several patterns inside a group
#sregx = re.compile(r"apples|banana|orange|grapes") # you can also use patterns not inside a group
mobj = sregx.search(msg)

#checking if theres a match object if there is no match it will return a value None
#ternary operator in checking the Match object
print('Not existing' if mobj == None else mobj.group(1)) 



#conditional or optional regexe uses a question mark character "?"
#The questionmark ? character means matches a group zero or one time
msg = "It's Ironman in the sky."

#the optional character ? will check (wo) will apear zero or one time
sregex = re.compile(r"Iron(wo)?man")
mo = sregex.search(msg)

print('Not existing' if mo == None else mo.group())


#sample using the phone number which we will check if the area code is in the phone number or not
msgphone = 'Call me at 555-1011 tomorrow. 415-555-9999 is my office.' #the first occurence phone number has no area code
sregx = re.compile(r"(\d{3}-)?(\d{3}-\d{4})")
mo = sregx.search(msgphone)
print('Not existing' if mo == None else mo.group()) #this will return even the search number has no area code


#If you want to search a string with a ? character you need to add a \? in the regular expression

smsg = "Is this Batman?"

#the regex is searching if wo apears or not with adding a search for \? questionmasrk character
sregx = re.compile(r"Bat(wo)?man\?")

mo = sregx.search(smsg)
print('Not existing' if mo == None else mo.group())


#The asterix * character means matches a group zero or more times
#if a string has a * charachter you need to add a backslash \* to your regex if you want to add to the search
smsg = "Is this Batwowowowowowowoman?"
sregx = re.compile(r"Bat(wo)*man\?")

mo = sregx.search(smsg)
print('Not existing' if mo == None else mo.group())


#The plus + character means matches a group one or more times.
#this means its not optional needs to apear once in a string
#same if you want to use a + character in regex just escape it with a \+
smsg = "Is this Batman?"
sregx = re.compile(r"Bat(wo)+man\?") # Not existing cause the string contains Batman and not Batwoman

mo = sregx.search(smsg)
print('Not existing' if mo == None else mo.group())


#string repetition in regex is enclosed in curly braces {}
#you can also specify a range where the pattern will repeat {a,b}

msg = "hahahahahahahahaha"
rgx = re.compile(r"(ha){3}") #will return only 3 ha characters
mob = rgx.search(msg)
print('Not existing' if mob == None else mob.group())

rgx = re.compile(r"(ha){3,5}") #will return only 5 ha characters
mob = rgx.search(msg)
print('Not existing' if mob == None else mob.group())

#msg = "hahaha" #Test if string is below 5
rgx = re.compile(r"(ha){5,}") #like slicing this will return range 5 to end of the string, but if below 5 it will not
mob = rgx.search(msg)
print('Not existing' if mob == None else mob.group())


#by default regex in python do a greedy matches
#where it searches the highest posible range of the string

msg = "123456789"
rgx = re.compile(r"(\d){3,5}") #it will return the highest possible string which is 5
mob = rgx.search(msg)
print('Not existing' if mob == None else mob.group())

#to make it in non greedy matches we need to add a ? after a range this pattern is different with a ? after a group
rgx = re.compile(r"(\d){3,5}?") #it will return the lowest possible string which is 3
mob = rgx.search(msg)
print('Not existing' if mob == None else mob.group())



#findall method - look for all occurence of the pattern in the string
#This findall method will return a list of string matches
msg = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# numbers in curly brackets example {3} after a pattern is like saying, “Match this pattern three times.”
rgx = re.compile(r"\d{3}-\d{3}-\d{4}")

print(rgx.findall(msg))

#Takenote if we group a regex the grouped string will become tuples in the list
#consists of object value areacode and phone number which is grouped in the pattern
rgx = re.compile(r"(\d{3})-(\d{3}-\d{4})")
# [(areacode, phone_number)]
print(rgx.findall(msg), "findall grouped")


#if we group the whole pattern it will add that group in the tupple
rgx = re.compile(r"((\d{3})-(\d{3}-\d{4}))")
# [(full_phone_number, areacode, phone_number)]
print(rgx.findall(msg))




# Common character classes
# Shorthand character class

# \d - Any numeric digit from 0 to 9.
# \D - Any character that is not a numeric digit from 0 to 9.
# \w - Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W - Any character that is not a letter, numeric digit, or the underscore character.
# \s - Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S - Any character that is not a space, tab, or newline.


# using shorthand character classes
xmas = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids are milking, 
7 swans are swimming, 6 geese are laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, 1 partridge in a pear tree'''

# This will serach for all number digit 1 or many then a space and a string with 1 or more character
rgx = re.compile(r"\d+\s\w+")

# show a new list of number and string
print(rgx.findall(xmas))


# using your own character classes
msg = "Robocop eats baby food."

rgxVowel = re.compile(r"[aeiouAEIOU]")

print(rgxVowel.findall(msg))


# another sample checking a 2 vowels in a row
# the pattern checks if theres 2 vowels in a row existing in a string
rgxVowel2 = re.compile(r"[aeiouAEIOU]{2}")

print(rgxVowel2.findall(msg))



# negative character classes
# this are character classes that do the opposite
# the character ^ inside the [] is used to do this

#this sample is finding all not vowel letters because of the using the caret ^ inside the []
rgxOtherThanVowel = re.compile(r"[^aeiouAEIOU]")

print(rgxOtherThanVowel.findall(msg))


# Begining and end of a string
# to search a particular string in the begining we will use the Caret sign again ^

str = "Hello world"
# This will check if the begining string has this string
rgx = re.compile(r"^Hello")

print(rgx.search(str)) # returns a match



# searching at the end string we will use the dollar sign $
# This will check if the ending string has this string
rgx2 = re.compile(r"world$")

print(rgx2.search(str)) # returns a match


# we can use both caret and dollar sign in a regexpr

samp = "123456789"

# this will check the begining and end pattern must be all numeric digit
rgx3 = re.compile(r"^\d+$")

print(rgx3.search(samp)) # returns a match since the samp is all numerical digit



# dot/period in regexp stands for any beginning single character except the new line
# the "at" in the beginning will not be included since it only contain a 2 character
# and flat because it has 2 starting chatracters
samp1 = "at the cat in the hat sat on the flat mat."

rgx4 = re.compile(r".at")

print(rgx4.findall(samp1))


#we can also specify a range of the beginning characters for the dot character
rgx5 = re.compile(r".{1,2}at") #range character for the dot sign

print(rgx5.findall(samp1))


# the dot and asterix combination means anything or any pattern
samp2 = "First name: John Last name: Doe"

#This will search the pattern and return the grouped patterns
# This is useful in some hard to find string
# this pattern in default is a greedy match
rgxp1 = re.compile(r"First name: (.*) Last name: (.*)")

print(rgxp1.findall(samp2))


# non greedy pattern .* uses a ? at the end
samp3 = "<To serve human> for dinner.>"

# non greedy pattern
rgxp2 = re.compile(r"<(.*?)>")

print(rgxp2.findall(samp3))


# the difference with greedy pattern
# this will get all the string until it satisfy the > ending character as shown in the value
rgxp3 = re.compile(r"<(.*)>")

print(rgxp3.findall(samp3))


# proving that the dot character only searches a character except a new line \n even using * and a greedy pattern
msg = "Hello Earthlings.\nHello Aliens."

regx = re.compile(r".*")

mo = regx.search(msg)

#it will stop searching in the first occurence of the new line \n
print(mo.group())


# Options or Second argument in re.compile using some regexp methods
# to include the new line in using dot character we need to add a option in the compile method re.DOTALL
regx1 = re.compile(r".*", re.DOTALL) #DOTALL method ignores the \n newline character

# this will get all characters as possible since we have a greedy pattern
print(regx1.search(msg))


# example for not case insensitive
msg1 = "Al, why all messages are about robocop"
regx2 = regx1 = re.compile(r"[aeiou]", re.IGNORECASE) # or you can make it short by using -> re.I

#this will find all vowel even there is no capital inside the [] because of the option re.IGNORECASE
print(regx2.findall(msg1))




# using sub method in replacing the search pattern to a new string
secret = "Agent Alice gave the secret document to Agent Bob"

srgx = re.compile(r"Agent \w+")

# check what the pattern gets
print(srgx.findall(secret))

# substitute the searched pattern to another string
# The 2 agents will be substituted with REDUCTED
outp = srgx.sub("REDUCTED", secret)

print(outp)


# other sample of substitution using a part of the string

# this pattern is looking for a first character and grouping it followed by character zero to any length of character
srgx = re.compile(r"Agent (\w)\w*")

# check what the pattern gets
# since in default if the pattern has groupings it will return only the groups
# in list format if theres only a single group, tuples in multiple groups
print(srgx.findall(secret))


# substitute the searched pattern to another string using the index of the group of the pattern
# the \1 means using the group 1 of the pattern
# format the string to raw to avoid the terminating symbol for backslashes and we only have the literal backslash of the string
outp = srgx.sub(r"Agent \1****", secret)

print(outp)



# verbose -> in verbose moe whitespace in string will not reflect on the actual pattern
# so this means we can use triple quotes for multiline strings
# and even new lines will not bw part of the pattern.
# we can use comments inside the string using the verbose mode
# Note: adding multiple 2nd argument for regexp compile method the bitwise operator "|" or vertical pipe is used
# to add the options for example adding re.DOTALL | re.IGNORECASE | re.VERBOSE
# this is only for compile method and only in python a older fashion way
xreg = re.compile(r'''
(\d\d\d-|    # area code (no parens, with dash)
\(\d\d\d\)\s)? # or area code inside parenthesis with space and no dash
(\d\d\d        # first 3 digit number
-
\d\d\d\d)      # last 4 digit number
\s(x\d{2,4})    # extension like x0000
''', re.VERBOSE)

print(xreg.findall("My number is (123) 123-1234 x000, ok?"))