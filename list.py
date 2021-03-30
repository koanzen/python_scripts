nums = [1,3,9,8,9,10,0,4]

#print the list
print(nums)

#loop to the list
for n in nums:
    print(n)

# Geting single item in a list using an INDEX
print(nums[0], "First Item") #getting the first item of the list cause it has a index 0
print(nums[-1], "Last Item") #getting the last item of the list cause the index -1 indicates indexing the list backward

# SLICING the List
#list from range of index to end
print(nums[2:])

#list from range of index to index
print(nums[1:3])

#changing value in list
print(nums[5])
nums[5] = 33
print(nums[5])



# METHODS operates in a LIST "In place", rather than returning a new list value
# Examples are .sort() .append() .pop() .insert() .remove() and the keyword "del"

#adding object at the ending of the list
nums.append(20)
print(nums)

#adding object i  a specific index
nums.insert(0,2)
print(nums)
nums.insert(1,5)
print(nums)

#removing a specific value not index in a list
nums.remove(0)
print(nums)

#deleting a value via index not value in the list
del nums[0]
#or del nums[1:] #range of index
print(nums)



#getting and removing the last number in the list
p = nums.pop()
print(nums)
print(p)

#finding the index in the list
print(nums.index(9))

#check if the object is exist in the list
print(9 in nums)

#counting the occurence of the number
print(nums.count(9))

#sorting the numbers
z = sorted(nums)
print(z, "list sorted")

#other sorting methods

strList = ['A','c','a','B','b','C']

#sorting string list happens in ASCII-Betical order where capital leters are priority
strList.sort() #This will sort the string alphabetically but Caps first
print(strList, "String sort")

strList.sort(key=str.lower) #this will sort the list string from Upper to Lower Alphabetically
print(strList, "String sort Alphabetically")

strList.sort(reverse=True) #reverse sort a string list
print(strList, "String sort in reverse")


#copying the list
nums2 = nums.copy()
nums.append(100)
print(nums)
print(nums2)

#reverse the nums
nums.reverse()
print(nums)

#emptying a list
nums.clear()
print(nums)

#concatinating a list
x = [1,2,3] + [4,5,6]

print(x, "concatinated list")

#replicating item list using multiplication operator

x = x * 3

print(x, "Replicated item list")

# Convert a string letters to a List
y = list("Hello")
print(y,"String to list")

#creating a list using a range function

z = list(range(1,10))
print(z,"List using range")