#Sample of a linear search

pos = -1

def search(list,n):

    for i,x in enumerate(list):

        if x == n:
            globals()["pos"] = i
            return True
    
    return False

list = [9,3,6,2,7,8,1,4,5]
n = 8

if search(list,n):
    print("Found in index", pos)
else:
    print("Not Found")


# or
# Simple search using "in"

a = n in list #This will return True if in the List else False

if a:
    print("Found")
else:
    print("Not Found")

# or

#Find the index of the value
#if the value has 2 occurence only the index of the first match will be returned
#if the value is not existing it will return a ValueError saying the value is not in the list
k = list.index(n)

print(k)

# or
# This will return a list which returns the value of y which is the index enumerated in the list
# z is the value of the enumerated list and n is the value we want to search

y = [y for y,z in enumerate(list) if z == n] #output is in list format

print("Found in index",y)



#################################
# Sample of Binary Search

def bsearch(list, n):

# must determine the lower and upper bound index of the list

    l = 0 # lower bound index
    u = len(list)-1 # upper bound index

    while l <= u:

        # get the mid value of the list
        # the formula is lower + upper devided by 2 the quotient must be in integer or floor number
        mid = (l+u) // 2 # Get the floor value of the lower bound and upper bound to get the mid

        if list[mid] == n: # check if the value of the mid index is the same of the search object
            #if yes return the index to global variable pos and return True
            globals()['pos'] = mid
            return True
        
        else:
            # if the condition above not met chack if the value of mid index is lower than the search object
            if list[mid] < n:
                l = mid + 1 # if yes make the mid index the lower bound index
            else:
                u = mid + 1 # else make mid index the upper bound index

    return False #return false if not found

# always sort the list ascending, else it will loop infinitely
# always the first match index will be returned
slist = sorted(list)
n = 9

print(slist)

if bsearch(slist,n):
    print("B Found in index", pos)
else:
    print("Not Found")