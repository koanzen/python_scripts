from functools import reduce

#lambdas are anonymous function only in single line
#it was indicated with lambda keyword and next
#with arguments and the expression after the : symbol
#lambdas must be initiated in a object.

x = lambda a,b : a+b

print(x(4,5))


#other samples

#The filter() function in Python takes in a function and a list as arguments.
#The function is called with all the items in the list
#and a new list is returned which contains items for which the function evaluates to True.

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list,' filter output')


#The map() function in Python takes in a function and a list or dictionary.
#The function is called with all the items in the list or dictionary
#and a new list is returned which contains items returned by that function for each item.
new_list = list(map(lambda x : x * 2 , my_list))

print(new_list,'- Map output list 1')

# Or

y = [*map(lambda x : x * 2 , my_list)]

print(y,'- Map output list 2')




#Sample for dictionary
iter_Dict = {"Python":0, "CSharp":0, "Java":0}
print(iter_Dict, "- Sample Dictionary")

map_result =  dict(map(lambda x: (x[0],x[1]+1), iter_Dict.items()))

print(map_result,"- New dictionary")



#The reduce() function in Python takes in a function and a list.
#The function is called with by 2 items sequence in the list
#and the return value will became a first parameter and traverse through out the end of the list.

new_list = reduce(lambda x,y: x + y , my_list)

print(new_list,' reduce output')


#Creating a function returning a lambda function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #instantiate the returned lambda function based on its arguments which is 2
mytripler = myfunc(3) #instantiate the returned lambda function based on its arguments which is 3

print(mydoubler(11),' mydoubler output') #Use the instatiated labda functions
print(mytripler(11),' mytripler output') #Use the instatiated labda functions