#sample bubble sort

def bsort(list):
    for i in range(len(list)-1,0,-1): #will iterate backward from the len of list to 0
        for j in range(i): #iterate through the index
            if list[j] > list[j+1]: #check the value of index j is greater than the next index
                tmp = list[j] #if yes put the value of index j to temporary variable
                list[j] = list[j+1] #the change the value of index j to the next index value
                list[j+1] = tmp #and the next value index to the index j value

list = [9,3,6,2,7,8,1,4,5]

bsort(list)

print(list)


####
# Sample Selection Sort

def ssort(list):
    for i in range(len(list)-1): #iterate in the range of last index
        minpos = i #make the index iterated as minimum position
        for j in range(i,len(list)): #iterate the range from minimum position to the length of the list
            if list[j] < list[minpos]: #check if the value of index j is less than the value of the index of minimum position
                minpos = j #if yes value of index j is the new minimum position

        tmp = list[i] #make the value of index i as temporary variable
        list[i] = list[minpos] #and change index i value to the value of index minimum
        list[minpos] = tmp #then minpo index value to the value of tmp

list = [9,3,6,2,7,8,1,4,5]

ssort(list)

print(list)