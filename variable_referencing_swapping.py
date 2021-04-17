#Checking address of the variable in the memmory.
#Variables with thesame value in the memmory will also use thesame address
#cause addresses pertains to the actual value that is referenced by the id
#if the value is not used it will be retain in the memory for garbage collection
a = 10
b = a
c = 10
a = 9

# _ (underscore symbol) is called a throw away variable which commonly used to for loop for indexes

#you can also assign values in multiple variables inline
x,y,z = 1,2,3

print(id(a))
print(id(b))
print(id(10))
print(id(c))
print(id(a))


#and you can also swap the variable values via inline variable swapping
x,y,z = z,y,x

print(f"{x} {y} {z}","These variables are swapped") #list value in a variable
a,b,c = ['cat','dog','bird']

print(a,b,c)


#if the value is a List it will be referened as a whole with the same address
#it will output thesame ID or Address even the value of the list is changed
#mutable value like List have this a somekind of bug if you dont remember
#immutable values like string and tuples have no problems in ID because its not editable and can allow only 1 value

lst = [1,2,3]

print(lst)
print(id(lst),"- ID of the list")

#change and add objects in the list
lst[0] = 'Hello'
lst.append(8)
print(lst)

print(id(lst),"- ID of the list after changing same as above id")


#manipulating list value using a function scoping
#here we can see the somekind of bug where value of our Global var lxt is changed
#even if we changed it inside the local scope of the function change
#remember in function scoping we only have access on the global scope variable but we cannot
#edit or change its value directly if we dont use the keyword "global"
#remember List values if referenced it will retain its ID.
#This is in refence with the memory allocation and not duplicating the data everytime we supply it in a variable

def change(neolst): #neolst pertains to a new variable reference
    neolst.append('Hello')

lxt = [1,2,3]
print(lxt, 'unchanged lxt')
print(id(lxt), 'id of unchanged lxt')

change(lxt)

print(lxt, 'Changed lxt in the local scope of function')
print(id(lxt), 'id of changed lxt')